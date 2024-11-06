from typing import Union, List
import pandas as pd

def search_df(
    df: pd.DataFrame,
    search_phrase: str,
    column_name: str,
    case_sensitive: bool = False,
    exact_match: bool = False,
    return_matches: bool = False
) -> Union[pd.DataFrame, tuple[pd.DataFrame, List[str]]]:
    "Search for a phrase within a specified DataFrame col."

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in DataFrame")
    
    if not search_phrase:
        raise ValueError("Search phrase cannot be empty")
    
    df = df.copy()
    df[column_name] = df[column_name].astype(str)
    
    if not case_sensitive:
        search_phrase = search_phrase.lower()
    
    if exact_match:
        if case_sensitive:
            mask = df[column_name] == search_phrase
        else:
            mask = df[column_name].str.lower() == search_phrase
    else:
        if case_sensitive:
            mask = df[column_name].str.contains(search_phrase, regex=True, na=False)
        else:
            mask = df[column_name].str.lower().str.contains(
                search_phrase, regex=True, na=False
            )
    
    filtered_df = df[mask]
    
    if return_matches:
        matches = filtered_df[column_name].tolist()
        return filtered_df, matches
    
    return filtered_df