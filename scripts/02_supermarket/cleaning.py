import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans column names by stripping spaces and converting to snake_case."""
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace(r"[^\w\s]", "", regex=True)
    )
    # Convert date and time columns to appropriate formats

    df["date"] = pd.to_datetime(df["date"])
    df["time"] = pd.to_datetime(df["time"], format="%H:%M").dt.time

    return df
