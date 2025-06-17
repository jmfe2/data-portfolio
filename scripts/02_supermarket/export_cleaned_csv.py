import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

# Create DB engine
engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# Load cleaned data from PostgreSQL
query = "SELECT * FROM supermarket_sales"
df = pd.read_sql(query, engine)

# Define export path
output_path = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "02_supermarket_sales"
    / "cleaned_data"
    / "supermarket_cleaned.csv"
)

# Export to CSV
df.to_csv(output_path, index=False)
print("Cleaned data exported")

# Display the columns and first few rows of the DataFrame
print(df.columns)

print(df.head())
