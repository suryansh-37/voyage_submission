from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import psycopg2

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

# Database connection details
DB_HOST = "localhost"
DB_NAME = "practice_db"
DB_USER = "postgres"
DB_PASS = "1234"
DB_PORT = 5432

def connect_db():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    return conn

# Home page route
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# 1. API: Get all customer records
@app.route('/api/customers')
def get_customers():
    try:
        conn = connect_db()
        cur = conn.cursor()
        
        cur.execute('SELECT * FROM customers ORDER BY "customerName" ASC')
        rows = cur.fetchall()
        
        columns = [desc[0] for desc in cur.description]
        customers_list = []
        for row in rows:
            customer = {}
            for i in range(len(columns)):
                customer[columns[i]] = row[i]
            customers_list.append(customer)
            
        cur.close()
        conn.close()
        return jsonify(customers_list)
        
    except Exception as e:
        print("Error fetching customers:", e)
        return jsonify({"error": str(e)}), 500

# 2. API: Get summary statistics for dashboard cards
@app.route('/api/stats')
def get_stats():
    try:
        conn = connect_db()
        cur = conn.cursor()
        
        cur.execute('SELECT COUNT(*), COALESCE(SUM("creditLimit"), 0), COUNT(DISTINCT country) FROM customers;')
        total_customers, total_credit, total_countries = cur.fetchone()
        
        cur.close()
        conn.close()
        
        return jsonify({
            "total_customers": total_customers,
            "total_credit": float(total_credit),
            "total_countries": total_countries
        })
    except Exception as e:
        print("Error fetching stats:", e)
        return jsonify({"error": str(e)}), 500

# 3. API: Get orders and payment info for a specific customer
@app.route('/api/customer/<int:cust_id>/orders')
def get_customer_orders(cust_id):
    try:
        conn = connect_db()
        cur = conn.cursor()
        
        # Fetch up to 5 recent orders for this customer
        cur.execute('SELECT "orderNumber", "orderDate", status FROM orders WHERE "customerNumber" = %s ORDER BY "orderDate" DESC LIMIT 5;', (cust_id,))
        order_rows = cur.fetchall()
        
        orders = []
        for r in order_rows:
            orders.append({
                "orderNumber": r[0],
                "orderDate": str(r[1]),
                "status": r[2]
            })
            
        # Fetch total payments made by this customer
        cur.execute('SELECT COALESCE(SUM(amount), 0) FROM payments WHERE "customerNumber" = %s;', (cust_id,))
        total_paid = float(cur.fetchone()[0])
        
        cur.close()
        conn.close()
        
        return jsonify({
            "orders": orders,
            "total_paid": total_paid
        })
    except Exception as e:
        print("Error fetching customer orders:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server on http://localhost:5000 ...")
    app.run(debug=True, port=5000)
