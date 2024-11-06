import pandas as pd
import re
from typing import Dict, List, Union, Callable
from dataclasses import dataclass
from enum import Enum, auto
from maps import maps

class ColumnType(Enum):
    SINGLE = auto()
    MULTIPLE = auto()
    YES_NO = auto()
    NUMBER = auto()

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

class DataCleaner:
    def __init__(self, column_configs: List[ColumnConfig]):
        self.column_configs = column_configs
        self.cleaners: Dict[ColumnType, Callable] = {
            ColumnType.NUMBER: lambda s, _: self._clean_numeric(s),
            ColumnType.SINGLE: lambda s, k: self._clean_categories(s, k, False),
            ColumnType.MULTIPLE: lambda s, k: self._clean_categories(s, k, True),
            ColumnType.YES_NO: lambda s, k: self._clean_categories(s, k, False)
        }

    def _clean_numeric(self, series: pd.Series, default_value: Union[int, float, None] = None) -> pd.Series:
        "Clean numeric values from strings and convert to numbers. Converts to ints if all numbers are whole numbers. Fill NA/NaN with mean val."

        def extract_number(x):
            if pd.isna(x):
                return x

            numbers = re.findall(r'-?\d*\.?\d+', str(x))
            return float(numbers[0]) if numbers else None

        cleaned = series.apply(extract_number)
        cleaned = pd.to_numeric(cleaned, errors='coerce')
        
        if default_value is None:
            default_value = cleaned.mean()
            
        cleaned = cleaned.fillna(default_value)
        
        if all(cleaned.round() == cleaned):
            cleaned = cleaned.astype(int)
            
        return cleaned


    def _clean_categories(self, series: pd.Series, mapping_key: str, return_multiple: bool = False) -> pd.Series:
        "Clean string cols and apply either one class or multi-class categories."
        
        def standardize(value: str) -> Union[str, List[str]]:
            # Handle missing/empty values
            if pd.isna(value) or not str(value).strip():
                return ['Ej angiven'] if return_multiple else 'Ej angiven'
            
            value = str(value).lower().strip()
            
            if return_multiple:
                # Multiple categories: collect all matches
                categories = set()
                for pattern, category in maps[mapping_key].items():
                    if re.search(pattern, value):
                        categories.add(category)
                return list(categories) if categories else ['Övrigt']
            else:
                # Single category: return first match
                for pattern, standardized in maps[mapping_key].items():
                    if re.search(pattern, value):
                        return standardized

                return 'Vet ej' if mapping_key == 'ja_nej_svar' else 'Övrigt'

        return series.apply(standardize)


    def process_df(self, df: pd.DataFrame) -> pd.DataFrame:
        """Process all cols in the dataframe."""
        df_processed = df.copy()
        
        for config in self.column_configs:
            cleaner = self.cleaners[config.column_type]
            df_processed[config.new_col] = cleaner(
                df_processed[config.original_col],
                config.mapping_key
            )
            
        return df_processed[self._get_column_order(df_processed)]

    def _get_column_order(self, df: pd.DataFrame) -> List[str]:
        """Get the col order, keeping original and processed cols together."""
        ordered_cols = []
        for config in self.column_configs:
            ordered_cols.extend([config.original_col, config.new_col])
        
        # Add any remaining columns
        remaining = [col for col in df.columns if col not in ordered_cols]
        return ordered_cols + remaining

class DataAnalyzer:
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