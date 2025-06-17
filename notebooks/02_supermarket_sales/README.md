# 🛒 Supermarket Sales – ETL and Data Validation Project

## 📌 Project Overview

This project demonstrates a complete ETL (Extract, Transform, Load) pipeline using a real-world dataset of supermarket transactions. The goal is to extract sales data from a CSV file, transform and clean it using Python, and load it into a PostgreSQL database. We then validate the inserted data and prepare it for visualization in Power BI or other BI tools.

---

## 🧰 Tech Stack

- **Python 3.11**
- **PostgreSQL** (local instance)
- **pandas** – data manipulation
- **SQLAlchemy** – database connection
- **dotenv** – environment variable management
- **Power BI** – for dashboards (planned in next stage)
- **Git + GitHub** – version control

---

## 📁 Project Structure

02_supermarket_sales/
│
├── 02_supermarket_postgresql.ipynb # ETL process: load data into PostgreSQL
├── 03_validate_and_git.ipynb # Data validation with SQLAlchemy + Git workflow
├── README.md # Project description (this file)


Other folders in root project:

/data/02_supermarket_sales/ # Contains the original CSV file
/scripts/02_supermarket/ # Custom Python cleaning functions (e.g., cleaning.py)
/figures/02_supermarket/ # Visual outputs from data analysis


---

## 📄 Dataset Description

The dataset used is [`supermarket_sales.csv`](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales), which contains:

- Invoice details
- Branch and city
- Customer type and gender
- Product line and quantity
- Pricing, VAT, payment method
- Date and time of transaction

📦 Rows: 1,000  
📊 Columns: 17

---

## ⚙️ How to Run

1. Clone the repo and set up a Python virtual environment (optional):

   ```bash
   git clone https://github.com/jmfe2/data-portfolio.git
   cd data-portfolio

2. Install libraries
  ```bash
  pip install -r requirements.txt

3. Create a .env file in the root directory with the following keys

 ```bash
 DB_USER=your_username
 DB_PASS=your_password
 DB_HOST=localhost
 DB_PORT=5432
 DB_NAME=your_database

4. Run notebooks in order
 02_supermarket_postgresql.ipynb – loads CSV into PostgreSQL
 03_validate_and_git.ipynb – runs validation queries and tracks changes with Git




 
