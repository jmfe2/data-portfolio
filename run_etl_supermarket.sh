#!/bin/bash
# Activate virtual environment
source .venv/bin/activate

# Run the ETL
python -m scripts.02_supermarket.etl_pipeline