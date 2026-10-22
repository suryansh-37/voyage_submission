# ClassicModels PostgreSQL Customer Dashboard

A lightweight, full-stack database exploration web app built with **Python (Flask)** and **PostgreSQL**. It allows users to browse customer accounts, search and filter records in real time, view historical orders and payments through relational SQL queries, and export data directly to CSV.

---

## 📌 Dataset Origin & Background

This project uses the well-known **[Classic Models Sample Database](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/)**, originally created by the Eclipse BIRT project as a realistic business model for a scale-model car retailer.

The database features 11 related tables:
- **Core Entities**: `customers`, `employees`, `offices`, `products`, `productlines`
- **Transactions**: `orders`, `orderdetails`, `payments`
- **Custom Analysis Views**: `top_10_clientes_2005`, `top_10_productos_2005`, `ventas_mensuales` (analytical views created during a database lab analyzing 2005 sales data).

---

## 🚀 Key Features

- **Live Database Connection**: Queries PostgreSQL (`practice_db`) directly using Python and `psycopg2`. No mock JSON fixtures.
- **Full Customer Directory**: Displays all 122 customers across 11 columns, including contact names, street addresses, countries, and credit limits.
- **Relational Order Tracking (Drilldown)**: Click **"View Orders"** on any customer row to dynamically fetch their order history and total payments made from the `orders` and `payments` tables.
- **Instant Search & Country Filtering**: Filter customers in real time by company name, city, phone number, or country without reloading the page.
- **Executive Metric Cards**: Summary badges at the top showing Total Customers (122), Total Credit Extended ($8.25M), and Countries Represented (28).
- **Export to CSV**: Download the visible customer table directly to an Excel-friendly `.csv` file with one click.

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask, `flask-cors`
- **Database**: PostgreSQL, `psycopg2-binary`
- **Frontend**: HTML5, Vanilla CSS3, JavaScript (DOM API & Fetch)

---

## 💻 Project Structure

```text
your_app/
├── app.py              # Flask server and PostgreSQL API routes
├── dashbord.html       # Customer dashboard & interactive script
├── dashbord.css        # Dashboard layout, cards & modal styling
├── index.html          # Application home page
├── about.html          # Project architecture overview
├── styles.css          # Shared global styles & navigation
├── requirements.txt    # Python dependencies
├── .gitignore          # Git exclusion rules
└── README.md           # Documentation
```

---

## ⚙️ Step-by-Step Guide to Run This Project

Follow these steps to set up and run the project locally on your machine:

### Step 1: Check Prerequisites
Make sure you have installed on your computer:
1. **Python 3.8 or higher**: Check by opening a terminal and running:
   ```bash
   python --version
   ```
2. **PostgreSQL & pgAdmin**: Check that PostgreSQL service is running on port `5432`.

---

### Step 2: Clone or Download the Project
Open your terminal (or Command Prompt / PowerShell) and navigate to your preferred workspace:
```bash
git clone https://github.com/suryansh-37/your_app.git
cd your_app
```

---

### Step 3: (Recommended) Create a Virtual Environment
A virtual environment keeps your project dependencies clean and isolated:

- **On Windows (PowerShell / Command Prompt)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
- **On macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

---

### Step 4: Install Required Python Packages
Install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```
This will install:
- `Flask` (lightweight web server)
- `flask-cors` (handles browser cross-origin requests)
- `psycopg2-binary` (PostgreSQL driver for Python)

---

### Step 5: Set Up the PostgreSQL Database
1. Open **pgAdmin** (or `psql` command line).
2. Create a new database named **`practice_db`**:
   ```sql
   CREATE DATABASE practice_db;
   ```
3. Import or restore the ClassicModels `.sql` dataset into `practice_db`.
4. Verify the tables exist: `customers`, `orders`, `payments`, `employees`, etc.

---

### Step 6: Configure Database Connection
Open `app.py` in your code editor and verify your PostgreSQL credentials:
```python
# Database connection details in app.py
DB_HOST = "localhost"
DB_NAME = "practice_db"
DB_USER = "postgres"       # your postgres username
DB_PASS = "1234"           # your master password from pgAdmin
DB_PORT = 5432
```

---

### Step 7: Run the Application
Start the Flask server from your terminal:
```bash
python app.py
```

You should see an output like:
```text
Starting Flask server on http://localhost:5000 ...
 * Running on http://127.0.0.1:5000
```

---

### Step 8: Open in Your Browser
Once the server is running, open your web browser (Chrome, Edge, Firefox) and visit:

- **Customer Dashboard**: [http://localhost:5000/dashbord.html](http://localhost:5000/dashbord.html)
- **Home Overview**: [http://localhost:5000/index.html](http://localhost:5000/index.html)
- **Architecture & Notes**: [http://localhost:5000/about.html](http://localhost:5000/about.html)

---

## 🔍 Troubleshooting

| Issue | Likely Cause | Solution |
| :--- | :--- | :--- |
| **"Could not connect to database"** | Incorrect password or PostgreSQL not running | Check `DB_PASS` in `app.py` and ensure the PostgreSQL service is started in Windows Services. |
| **"Address already in use (Port 5000)"** | Another process is using port 5000 | Change `port=5000` to `port=5050` at the bottom of `app.py`, and visit `http://localhost:5050`. |
| **"ModuleNotFoundError: No module named 'psycopg2'"** | Missing dependencies | Run `pip install -r requirements.txt` inside your active virtual environment. |

---

## 📡 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/customers` | Returns all 122 customer records sorted alphabetically |
| `GET` | `/api/stats` | Computes aggregate KPI totals (customers, credit sum, countries) |
| `GET` | `/api/customer/<id>/orders` | Fetches recent orders and total payments for a customer |

---

## 📝 License
This project is open-source and intended for educational and portfolio demonstration purposes.
