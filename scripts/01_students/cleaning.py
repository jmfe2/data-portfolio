import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans column names by stripping spaces and converting to snake_case."""
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w\s]", "", regex=True)
    )
    return df
