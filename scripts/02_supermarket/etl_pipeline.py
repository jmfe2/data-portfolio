import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from datetime import datetime
from .cleaning import clean_column_names  # '.' means to import from the same package"
from pathlib import Path


# ETL Pipeline for Supermarket Data

# === Logging Helper ===


def log_message(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    full_message = f"{timestamp} {message}"
    print(full_message)

    log_path = Path(__file__).resolve().parents[2] / "logs" / "etl_supermarket.log"
    with open(log_path, "a") as log_file:
        log_file.write(full_message + "\n")


#  === Load .env variables ===


def load_env_vars():
    load_dotenv()
    return {
        "DB_USER": os.getenv("DB_USER"),
        "DB_PASS": os.getenv("DB_PASS"),
        "DB_HOST": os.getenv("DB_HOST"),
        "DB_PORT": os.getenv("DB_PORT"),
        "DB_NAME": os.getenv("DB_NAME"),
    }


# === Create DB engine ===


def create_db_engine(env):
    return create_engine(
        f"postgresql+psycopg2://{env['DB_USER']}:{env['DB_PASS']}@{env['DB_HOST']}:{env['DB_PORT']}/{env['DB_NAME']}"
    )


# === Path to CSV ===


def data_directory():
    return (
        Path(__file__).resolve().parents[2]
        / "data"
        / "02_supermarket_sales"
        / "supermarket_sales.csv"
    )


"""
__file__ = location of etl_pipeline.py
.resolve() = gets the absolute path
.parents[2] = goes up two levels from scripts/02_supermarket/ to data-portfolio/
Then navigates to data/02_supermarket_sales/...
"""

# === Run ETL ===


def run_etl():
    try:
        log_message("Starting ETL pipeline...")

        env = load_env_vars()
        engine = create_db_engine(env)

        csv_path = data_directory()
        if not csv_path.exists():
            raise FileNotFoundError("CSV not found")

        log_message("Reading CSV ...")
        df = pd.read_csv(csv_path)

        # Clean the data
        log_message("Cleaning data...")
        df_clean = clean_column_names(df)

        # Load into PostgreSQL
        log_message("Loading cleaned data to PostgreSQL...")
        df_clean.to_sql("supermarket_sales", engine, if_exists="replace", index=False)

        log_message("ETL pipeline completed successfully.")

    except Exception as e:
        log_message(f"ETL pipeline failed: {e}")


# Prevent auto-execution when imported
if __name__ == "__main__":
    run_etl()
