from data_cleaner import *
from viz import *

from utils import search_df

def main():

    configs = [
        ColumnConfig('example_column_age', 'ålder_clean', '', ColumnType.NUMBER),
        ColumnConfig('example_column_work_title', 'yrkesroll_cat', 'yrkesroller', ColumnType.SINGLE),
        ColumnConfig('example_column_yes_no_but_its_not_a_choice_but_free_text', 'yes_no_clean', 'ja_nej_svar', ColumnType.YES_NO),
        ColumnConfig('example_column_time', 'tillräcklig_tid_cat', 'ja_nej_svar', ColumnType.YES_NO),
        ColumnConfig('example_column_places', 'platser_cat', 'när_var', ColumnType.MULTIPLE),
        ColumnConfig('example_column_obs', 'hinder_cat', 'hinder', ColumnType.MULTIPLE),
        ColumnConfig('example_column_topics', 'ämnen_cat', 'ämnen_frågor', ColumnType.MULTIPLE),
        ColumnConfig('example_column_values', 'värde_cat', 'värde', ColumnType.MULTIPLE),
    ]

    df = pd.read_excel("data/svar.xlsx")
    df = pd.read_excel("example_data/example_sv.xlsx")

    cleaner = DataCleaner(configs)
    df_processed = cleaner.process_df(df)

    analyzer = DataAnalyzer()
    results = analyzer.analyze_categories(df_processed, configs)
    
    for col_name, distribution in results.items():
        print(f"\n{col_name}:")
        print(distribution)
    
    analyzer.save_results(df_processed)

    # Visualizations

    create_visualizations(df_processed)
    create_topic_value_graphs(df_processed)

    
if __name__ == "__main__":
    main()