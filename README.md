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

## ⚙️ Setup and Running Locally

### 1. Prerequisites
- Python 3.8 or higher installed
- PostgreSQL installed and running locally on port `5432`
- A database named `practice_db` with the ClassicModels tables loaded

### 2. Clone the Repository
```bash
git clone https://github.com/suryansh-37/your_app.git
cd your_app
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database Credentials
Open `app.py` and verify your local PostgreSQL credentials:
```python
DB_HOST = "localhost"
DB_NAME = "practice_db"
DB_USER = "postgres"
DB_PASS = "1234"      # replace with your master password
DB_PORT = 5432
```

### 5. Start the Flask Server
```bash
python app.py
```
The server will start at: `http://localhost:5000`

### 6. View in Browser
- **Home Page**: [http://localhost:5000/index.html](http://localhost:5000/index.html)
- **Customer Dashboard**: [http://localhost:5000/dashbord.html](http://localhost:5000/dashbord.html)
- **Architecture Overview**: [http://localhost:5000/about.html](http://localhost:5000/about.html)

---

## 📡 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/api/customers` | Returns all customer records sorted by company name |
| `GET` | `/api/stats` | Computes aggregate totals (customers, credit sum, countries) |
| `GET` | `/api/customer/<id>/orders` | Fetches recent orders and total payments for a customer |

---

## 📝 License
This project is open-source and intended for educational and portfolio demonstration purposes.
