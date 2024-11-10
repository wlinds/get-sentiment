import pandas as pd
import re
from typing import Dict, List, Union, Set, Optional
from dataclasses import dataclass
from enum import Enum, auto

class ColumnType(Enum):
    """Types of columns that can be processed."""
    SINGLE = auto()    # Single category output
    MULTIPLE = auto()  # Multiple categories possible
    YES_NO = auto()    # Binary classification
    NUMBER = auto()    # Numeric data
    STRING = auto()    # Plain text, no processing

@dataclass
class ColumnConfig:
    """Configuration for a column to be processed in the DataCleaner pipeline.
    
    Attributes:
        original_col: Original column name in the input dataframe
        new_col: New column name for the processed data
        mapping_key: Key to lookup mapping rules in the maps dictionary. Empty string if no mapping needed
        column_type: Enum specifying how the column should be processed (SINGLE, MULTIPLE, YES_NO, or NUMBER)
    """
    original_col: str
    new_col: str
    mapping_key: str
    column_type: ColumnType

@dataclass
class ProcessingContext:
    """Context for text processing with metadata."""
    text: str
    negation_regions: List[tuple[int, int]]
    contrast_splits: List[int]
    debug: bool = False

class DataCleaner:    
    def __init__(self, configs: List[ColumnConfig], mapping_rules: Dict):
        self.configs = configs
        self.maps = mapping_rules
        
        self.negation_markers = {
            'inte': 4, 'ej': 4, 'aldrig': 5, 'ingen': 3,
            'inget': 3, 'inga': 3, 'sällan': 4
        }
        self.contrast_markers = ['utan', 'men', 'däremot', 'istället']
        
        # Init processing functions map with bindings
        self.processors = {
            ColumnType.NUMBER: self._process_numeric,
            ColumnType.SINGLE: lambda x, k: self._process_text(x, k, False),
            ColumnType.MULTIPLE: lambda x, k: self._process_text(x, k, True),
            ColumnType.YES_NO: lambda x, k: self._process_text(x, k, False),
            ColumnType.STRING: lambda x, _: x
        }

    def process_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Process all cols in the dataframe."""
        df_processed = df.copy()
        
        for config in self.configs:
            process_func = self.processors[config.column_type]
            df_processed[config.new_col] = process_func(
                df_processed[config.original_col],
                config.mapping_key
            )
            
        return df_processed[self._get_column_order(df_processed)]

    def _process_numeric(self, series: pd.Series, _: str) -> pd.Series:
        """Process numeric values, handling string inputs and missing values."""
        def extract_number(x: str) -> Optional[float]:
            if pd.isna(x):
                return None
            numbers = re.findall(r'-?\d*\.?\d+', str(x))
            return float(numbers[0]) if numbers else None

        cleaned = series.apply(extract_number)
        cleaned = pd.to_numeric(cleaned, errors='coerce')
        
        # Fill missing values with mean
        mean_value = cleaned.mean()
        cleaned = cleaned.fillna(mean_value)
        
        # Convert to int if all values are whole numbers
        if all(cleaned.round() == cleaned):
            cleaned = cleaned.astype(int)
            
        return cleaned

    def _process_text(self, series: pd.Series, mapping_key: str, return_multiple: bool) -> pd.Series:
        """Process text data using pattern matching and context analysis."""
        def process_text_value(text: str) -> Union[str, List[str]]:
            if pd.isna(text) or not str(text).strip():
                return ['Ej angiven'] if return_multiple else 'Ej angiven'

            context = self._create_processing_context(str(text).lower().strip())
            
            # Special handling for yes/no answers
            if mapping_key == 'ja_nej_svar':
                return self._classify_yes_no(context)
            
            # Process text using pattern matching and context
            categories = self._find_categories(context, mapping_key)
            
            if not categories:
                return ['Övrigt'] if return_multiple else 'Övrigt'
                
            return categories if return_multiple else categories[0]

        return series.apply(process_text_value)

    def _create_processing_context(self, text: str) -> ProcessingContext:
        """Create processing context with negation and contrast information."""
        negation_regions = []
        
        # Find negation regions
        for marker, length in self.negation_markers.items():
            for match in re.finditer(r'\b' + marker + r'\b', text):
                start = match.start()
                end = start + length + 20  # Approximate scope of negation
                negation_regions.append((start, min(end, len(text))))
                
        # Find contrast markers
        contrast_splits = []
        for marker in self.contrast_markers:
            for match in re.finditer(r'\b' + marker + r'\b', text):
                contrast_splits.append(match.start())
                
        return ProcessingContext(text, negation_regions, sorted(contrast_splits))

    def _find_categories(self, context: ProcessingContext, mapping_key: str) -> List[str]:
        """Find matching categories considering context."""
        categories: Dict[str, float] = {}
        
        for pattern, category in self.maps[mapping_key].items():
            for match in re.finditer(pattern, context.text):
                # Check if match is in a negated region
                is_negated = any(start <= match.start() <= end 
                               for start, end in context.negation_regions)
                
                # Find relevant contrast split
                relevant_split = next((pos for pos in context.contrast_splits 
                                    if pos > match.start()), None)
                
                score = -1.0 if is_negated else 1.0
                
                # Adjust score based on contrast position
                if relevant_split and any(pos < relevant_split 
                                        for pos in context.contrast_splits):
                    score *= -1
                    
                if category in categories:
                    categories[category] = max(categories[category], score)
                else:
                    categories[category] = score
        
        return [cat for cat, score in categories.items() if score > 0]

    def _classify_yes_no(self, context: ProcessingContext) -> str:
        """Classify yes/no responses using pattern matching."""
        text = context.text
        
        # Strong negatives
        if (re.search(r'(?:^|\s|,)(absolut\s+inte|tyvärr\s+inte|såklart\s+inte)(?:\s|\.|,|$)', text) or
            re.search(r'(?:^|\s)(nej|nope|näe)(?:\s|\.|,|$)', text)):
            return 'Nej'
            
        # Strong positives
        if (re.search(r'(?:^|\s|,)(japp|yes)(?:\s|\.|,|!|$)', text) or
            re.search(r'(?:idag|nu)\s+gör\s+(?:jag|det)', text)):
            return 'Ja'
            
        # Uncertainty
        if re.search(r'(?:^|\s)vet\s+(?:inte|ej)(?:\s|\.|,|$)', text):
            return 'Vet ej'
            
        # Default response based on general sentiment
        positive_indicators = len(re.findall(r'\b(ja|bra|nöjd|tillräckligt)\b', text))
        negative_indicators = len(re.findall(r'\b(nej|inte|aldrig|sällan)\b', text))
        
        if positive_indicators > negative_indicators:
            return 'Ja'
        elif negative_indicators > positive_indicators:
            return 'Nej'
        
        return 'Vet ej'

    def _get_column_order(self, df: pd.DataFrame) -> List[str]:
        """Get the column order keeping original and processed columns together."""
        ordered_cols = []
        for config in self.configs:
            ordered_cols.extend([config.original_col, config.new_col])
            
        remaining = [col for col in df.columns if col not in ordered_cols]
        return ordered_cols + remaining

    @staticmethod
    def analyze_categories(df: pd.DataFrame, config: List[ColumnConfig]) -> Dict[str, pd.Series]:
        """Analyze category distributions for all processed cols."""
        results = {}
        
        for col_config in config:
            if col_config.column_type == ColumnType.MULTIPLE:
                # Flatten lists and count all categories
                all_cats = [cat for cats in df[col_config.new_col] for cat in cats]
                results[col_config.new_col] = pd.Series(all_cats).value_counts()
            else:
                results[col_config.new_col] = df[col_config.new_col].value_counts()
                
        return results

    @staticmethod
    def save_results(df: pd.DataFrame, filename: str = 'cleaned.xlsx') -> None:
        """Save results to Excel, convert lists to strings."""
        df_excel = df.copy()
        list_cols = df_excel.select_dtypes(include=['object']).columns
        
        for col in list_cols:
            if isinstance(df_excel[col].iloc[0], list):
                df_excel[col] = df_excel[col].apply(lambda x: ', '.join(x) if isinstance(x, list) else x)
        
        df_excel.to_excel("data/"+filename, index=False)
        print(f"\nResults saved to {filename}")