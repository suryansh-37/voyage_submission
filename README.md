# ClassicModels PostgreSQL CLI Explorer

A simple terminal-based Python application built for the **Chingu Developer (Python)** track. It connects directly to a PostgreSQL database (`practice_db` / ClassicModels) to browse customer accounts, search and filter records, view order histories, and export data to CSV and JSON files without any web framework.

---

## Overview

I created this project to practice Python programming and relational database operations using PostgreSQL. Instead of using mock data or web frameworks, the entire program runs directly in the terminal and queries live tables from the ClassicModels dataset.

### Skills Demonstrated:
- Database connectivity using `psycopg2`
- Relational queries across multiple tables (`customers`, `orders`, `payments`)
- File input/output with CSV and JSON export
- Functions, loops, conditionals, and error handling (`try/except`)
- Terminal user interface with interactive menu

---

## Features

1. **View All Customers**: Displays all 122 customers with phone number, city, country, and credit limit.
2. **Search Customers**: Search by company name, city, country, or customer ID.
3. **Filter by Country**: Filter customer accounts by specific country name.
4. **Customer Orders & Payments**: Enter a Customer ID to view recent orders from the `orders` table and total money paid from the `payments` table.
5. **Database Statistics**: View total customer count, total credit extended, and countries count.
6. **Export to CSV**: Saves the customer list to `customers_export.csv`.
7. **Export to JSON**: Saves customer data to `customers_export.json`.

---

## Project Structure

```text
voyage_submission/
├── main.py             # Main CLI application with database queries
├── requirements.txt    # Python dependencies (psycopg2-binary)
├── .gitignore          # Git exclusion rules
└── README.md           # Documentation & instructions
```

---

## Steps to Run the Project

### 1. Prerequisites
- Python 3.8 or higher installed
- PostgreSQL installed and running on port 5432
- Database named `practice_db` with ClassicModels tables imported

### 2. Clone the Repository
```bash
git clone https://github.com/suryansh-37/voyage_submission.git
cd voyage_submission
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database Password
Open `main.py` and make sure `DB_USER` and `DB_PASS` match your local PostgreSQL login:
```python
DB_HOST = "localhost"
DB_NAME = "practice_db"
DB_USER = "postgres"
DB_PASS = "1234"      # change to your pgAdmin password
DB_PORT = 5432
```

### 5. Run the Application
Start the program from your terminal:
```bash
python main.py
```

---

## Example Menu

```text
==========================================
 ClassicModels PostgreSQL CLI Explorer
==========================================
1. View All Customers
2. Search Customers
3. Filter Customers by Country
4. View Customer Orders and Payments
5. View Database Statistics
6. Export Customers to CSV
7. Export Customers to JSON
8. Exit
Enter choice (1-8):
```

---

## Dataset Reference
This project uses the **[Classic Models Sample Database](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/)**, a relational database originally created for the Eclipse BIRT project.