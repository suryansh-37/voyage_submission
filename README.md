# PostgreSQL Customer & Business Intelligence Dashboard

A full-stack web application connecting a PostgreSQL database (`practice_db` / ClassicModels) with a Python (Flask) backend and a clean, responsive frontend.

## Features
- **Live PostgreSQL Integration**: Connects to database tables using `psycopg2`.
- **Customer Directory**: Displays all 122 customer accounts with addresses, contact persons, and credit limits.
- **Relational Data Drilldown**: Click **"View Orders"** on any customer to see their recent order history and total payments made across related tables (`orders` and `payments`).
- **Real-Time Search & Country Filter**: Instant filtering by company name, contact, city, phone, or country without reloading the page.
- **Summary Metrics**: High-level KPI cards showing Total Customers, Total Credit Extended, and Distinct Countries Served.
- **CSV Data Export**: One-click export of visible customer data to `.csv` for Excel reporting.

## Project Structure
```text
your_app/
├── app.py              # Python Flask backend & API endpoints
├── dashbord.html       # Customer & Order dashboard with interactive JS
├── dashbord.css        # Dashboard styling & modal design
├── index.html          # Project home page
├── about.html          # Architecture overview
├── styles.css          # Main stylesheet
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Documentation
```

## Setup & Running Locally

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd your_app
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Database Connection:**
   In `app.py`, update the `DB_HOST`, `DB_NAME`, `DB_USER`, and `DB_PASS` variables with your PostgreSQL credentials:
   ```python
   DB_HOST = "localhost"
   DB_NAME = "practice_db"
   DB_USER = "postgres"
   DB_PASS = "1234"
   DB_PORT = 5432
   ```

4. **Start the application:**
   ```bash
   python app.py
   ```

5. **Open in your browser:**
   - Home: `http://localhost:5000/index.html`
   - Dashboard: `http://localhost:5000/dashbord.html`
