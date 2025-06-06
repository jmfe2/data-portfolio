def clean_column_names(df):
    df.columns = df.columns.str.strip().str.lower()
    return df
