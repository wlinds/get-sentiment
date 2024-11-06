# get-sentiment | Data Analysis Pipeline

A Python-based data processing and visualization pipeline for analyzing Swedish survey responses in Excel/Google Sheets/Tabular data format with a focus on categorizing and cleaning text strings using predefined mappings.

## Features

- **Flexible Data Cleaning**: Supports multiple types of data processing:
  - Numeric value extraction and standardization
  - Single category classification
  - Multiple category classification
  - Yes/No response standardization
  
- **Pipeline**: Easy to configure new columns and mapping rules through customizable `ColumnConfig` objects
  
- **Visualizations**: Includes various visualization types:
  - Bar charts for topic and value distributions
  - Treemaps, Violin plots, Sunburst diagrams
  - Role-based time adequacy analysis

## Installation

1. Clone the repository
2. Install required dependencies:
```bash
pip install pandas plotly
```

## Project Structure

- `data_cleaner.py`: Core data processing classes and functions
- `maps.py`: Regular expression mapping rules for categorization
- `viz.py`: Visualization functions using Plotly
- `utils.py`: Helper functions including DataFrame search capabilities
- `main.py`: Main execution script

## Usage

1. Configure your column mappings in `maps.py`
2. Set up your column configurations in `main.py`:

```python
configs = [
    ColumnConfig('original_col', 'new_col', 'mapping_key', ColumnType.SINGLE),
]
```

3. Run the pipeline:

```python
python main.py
```

### Example Configuration

```python
configs = [
    ColumnConfig('example_column_age', 'ålder_clean', '', ColumnType.NUMBER),
    ColumnConfig('example_column_work_title', 'yrkesroll_cat', 'yrkesroller', ColumnType.SINGLE),
    ColumnConfig('example_column_places', 'platser_cat', 'när_var', ColumnType.MULTIPLE)
]
```

## Data Processing Types

- `NUMBER`: Extracts and standardizes numeric values
- `SINGLE`: Maps text to a single category using regex patterns
- `MULTIPLE`: Maps text to multiple categories using regex patterns
- `YES_NO`: Standardizes yes/no responses with various expressions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request