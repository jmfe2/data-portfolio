# cleaning.py
import pandas as pd  # <-- ¡Sí, aquí debe estar!


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardizes column names by:
    - Lowercasing all column names
    """
    df.columns = df.columns.str.lower()
    return df
