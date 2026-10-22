# Classic Models Customer Dashboard

A web application built with Python (Flask) and PostgreSQL to explore customer records, search by name or country, and check order history.

## Dataset Origin

This project uses the Classic Models sample database, originally created for the Eclipse BIRT project to simulate a scale-model car and vehicle retailer.

The database includes 11 tables:
- Core tables: customers, employees, offices, products, productlines
- Orders and transactions: orders, orderdetails, payments
- Summary views: top_10_clientes_2005, top_10_productos_2005, ventas_mensuales (views created for a 2005 sales analysis lab).

Dataset reference: [PostgreSQL Tutorial ClassicModels](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/)

## Features

- Live database queries: Connects directly to PostgreSQL (practice_db) using psycopg2.
- Full customer list: Displays all 122 customers with address, contact person, phone, and credit limit.
- Order history popup: Click "View Orders" on any customer to see their recent orders and total payments made.
- Search and country filter: Filter rows instantly without page reloads.
- Summary cards: Shows total customers, total credit extended, and countries served.
- Export CSV: Downloads the visible table as a .csv file for Excel.

## Technologies Used

- Python 3
- Flask and flask-cors
- PostgreSQL
- psycopg2-binary
- HTML, CSS, JavaScript (Vanilla)

## Project Files

- app.py - Flask backend with database connection and API routes
- dashbord.html - Customer table page with search and popup script
- dashbord.css - Styles for table and modal
- index.html - Home landing page
- about.html - Project description and notes
- styles.css - Main styles for navbar and cards
- requirements.txt - List of Python libraries needed
- .gitignore - Files git should ignore

## Steps to Run the Project

### 1. Prerequisites
- Python 3 installed
- PostgreSQL installed and running on port 5432
- Database named practice_db with ClassicModels tables imported

### 2. Clone or download
Open terminal or command prompt in your folder:
```bash
git clone https://github.com/suryansh-37/your_app.git
cd your_app
```

### 3. Install requirements
Run pip install:
```bash
pip install -r requirements.txt
```

### 4. Check database password
Open app.py and make sure DB_USER and DB_PASS match your local postgres login:
```python
DB_HOST = "localhost"
DB_NAME = "practice_db"
DB_USER = "postgres"
DB_PASS = "1234" # change to your pgAdmin password
DB_PORT = 5432
```

### 5. Run the server
Run the python script:
```bash
python app.py
```

You should see:
```text
Starting Flask server on http://localhost:5000 ...
```

### 6. Open in browser
Open your browser and visit:
- Dashboard: http://localhost:5000/dashbord.html
- Home: http://localhost:5000/index.html
- About: http://localhost:5000/about.html

## Common Issues

- "Could not connect to database": Double check your PostgreSQL service is started in Windows and your password in app.py is correct.
- "Port 5000 in use": You can change port=5000 to port=5050 in app.py and open http://localhost:5050/dashbord.html.
- "No module named psycopg2": Run pip install psycopg2-binary in your terminal.
