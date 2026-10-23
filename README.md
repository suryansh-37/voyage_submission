# ClassicModels PostgreSQL CLI Explorer

A terminal-based Python application built for the **Chingu Developer (Python)** track. It connects directly to a PostgreSQL database (`practice_db` / ClassicModels) to browse, search, inspect relational records, and export data to CSV and JSON files without any web framework.

---

## Overview

This project was created to demonstrate core Python programming and relational database connectivity. Rather than using mock data, it connects directly to a local PostgreSQL instance to query real-world business data from the ClassicModels dataset.

### Skills Demonstrated (Chingu Python Track):
- **Object-Oriented Programming (OOP)**: Clean separation of concerns with a dedicated `Database` manager class (`database.py`) and application controller (`main.py`).
- **Database Connectivity**: Direct queries, parameterization, and relational lookups across multiple tables (`customers`, `orders`, and `payments`) using `psycopg2`.
- **File I/O**: Exporting query results to `.csv` using Python's `csv` module and `.json` using Python's `json` module.
- **Data Structures**: Working with lists, dictionaries, tuples, and sets for in-memory operations and formatting.
- **Error Handling**: Graceful error handling using `try/except` blocks for database connection failures and invalid user inputs.

---

## Features

1. **View All Customers**: Displays all 122 customers in a clean, formatted terminal table.
2. **Search Customers**: Real-time search across company name, city, country, phone number, or customer ID.
3. **Filter by Country**: Lists available countries and filters customers by selection.
4. **Relational Order & Payment Summary**: Enter any Customer ID to view their recent orders (from `orders` table) and total payment amount (from `payments` table).
5. **Database Statistics**: Summarizes total customer count, total credit extended, and distinct countries served.
6. **Export to CSV**: Saves the customer list directly into an Excel-ready CSV file.
7. **Export to JSON**: Saves structured customer records into a formatted JSON file.

---

## Project Structure

```text
voyage_submission/
├── main.py             # Interactive CLI application & menus
├── database.py         # PostgreSQL database queries & connection class
├── requirements.txt    # Python dependencies (psycopg2-binary)
├── .gitignore          # Git exclusion rules
└── README.md           # Documentation & instructions
```

---

## Quick Start Guide

### 1. Prerequisites
- Python 3.8 or higher (`python --version`)
- PostgreSQL running on port `5432` with the `practice_db` database loaded

### 2. Clone the Repository
```bash
git clone https://github.com/suryansh-37/voyage_submission.git
cd voyage_submission
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Configuration
Open `database.py` and verify your local PostgreSQL credentials:
```python
DB_HOST = "localhost"
DB_NAME = "practice_db"
DB_USER = "postgres"
DB_PASS = "1234"      # update with your master password
DB_PORT = 5432
```

### 5. Run the Application
Start the CLI tool:
```bash
python main.py
```

---

## Example Usage

```text
==================================================
   ClassicModels PostgreSQL Explorer (CLI)
==================================================
1. View All Customers
2. Search Customers (by name, city, phone, etc.)
3. Filter Customers by Country
4. View Customer Orders & Payment Summary
5. View Database Statistics
6. Export All Customers to CSV
7. Export All Customers to JSON
8. Exit
==================================================
Enter choice (1-8):
```

---

## Dataset Reference
This project utilizes the **[Classic Models Sample Database](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/)**, a relational schema originally designed for the Eclipse BIRT project.