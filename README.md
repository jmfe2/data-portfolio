# 📊 Data Analytics Portfolio – Juan M. Flores Espinoza

Welcome to my personal data analytics portfolio. This repository showcases end-to-end data projects focused on real-world scenarios and business insights. Each folder represents a self-contained case study with data cleaning, transformation, storage, and visualization workflows.

---

## 🧠 About Me

I'm a data analyst in transition to data engineering, with a background in Financial Administration and a Master's degree in Big Data & Business Analytics. I focus on practical applications of data science, particularly in Python, SQL, and BI tools.

---

## 📂 Project Index

| Project | Description | Tools & Topics |
|--------|-------------|----------------|
| [`Supermarket Sales`](./notebooks/02_supermarket_sales) | ETL pipeline with PostgreSQL, data validation, and Power BI dashboard | Python, pandas, SQLAlchemy, PostgreSQL, Power BI |
| [`Students Performance`](./notebooks/01_students) | Exploratory data analysis of student scores and demographics | Python, seaborn, matplotlib, EDA |

*More projects coming soon (financial datasets, APIs, predictive models).*

---

## 🔧 Tech Stack Across Projects

- Python 3.11
- pandas, numpy, matplotlib, seaborn
- PostgreSQL (local setup)
- SQLAlchemy, dotenv
- Power BI (via UTM on Mac)
- Git & GitHub for version control

---

## 📌 Folder Structure

```bash
data-portfolio/
├── notebooks/               # Jupyter notebooks for each project
├── scripts/                 # Custom Python scripts (ETL, cleaning, etc.)
├── data/                    # Raw and cleaned CSV files
├── figures/                 # Power BI images and dashboards
├── logs/                    # ETL and data validation logs
├── requirements.txt         # Python dependencies
└── README.md                # This file

--- 

## ⚙️ How to Run

1. Clone the repo:

```bash

git clone https://github.com/jmfe2/data-portfolio.git
cd data-portfolio

```
   
2. Set up the enviroment:

```bash

pip install -r requirements.txt

```

3. Create a .env file with your database credentials:

```bash
DB_USER=your_username
DB_PASS=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_database
```

4. Open the project folders and run notebooks in order.

---

📫 Contact

📸 Instagram: @jmfloreslab
💼 LinkedIn: linkedin.com/in/juanmartinflores

---

⚖️ License

This project is licensed under the MIT License. See the LICENSE file for details.