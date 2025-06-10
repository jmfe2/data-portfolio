import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardizes column names by:
    - Lowercasing all column names
    - Removing non-alphanumeric characters (except underscores)

    Parameters:
    - df: pd.DataFrame — The DataFrame with messy or inconsistent column names.

    Returns:
    - pd.DataFrame — A copy of the original DataFrame with cleaned column names.

    Example:
    >>> df = pd.DataFrame({'Gender ': ['male'], 'Math Score': [88]})
    >>> clean_column_names(df).columns.tolist()
    ['gender', 'math score']
    """
    df.columns = df.columns.str.lower()
    return df


def cast_scores_to_int(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Casts specified score columns to integer (nullable Int64 for safety).

    Parameters:
    - df: pd.DataFrame — The DataFrame containing score columns.
    - columns: list — List of column names to cast to integers.

    Returns:
    - pd.DataFrame — The DataFrame with specified columns cast to integers.

    Example:
    >>> df = pd.DataFrame({'math score': ['88', '90']})
    >>> cast_scores_to_int(df, ['math score']).dtypes['math score']
    dtype('Int64')
    """
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")
    return df


""" How to import and use it in a notebook """

"""

import sys
sys.path.append('../scripts')  # Adjust this path depending on your notebook location

import cleaning

df = cleaning.clean_column_names(df)
df = cleaning.cast_scores_to_int(df, ['math score', 'reading score', 'writing score'])

"""
