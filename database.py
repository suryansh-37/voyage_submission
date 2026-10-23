import psycopg2

# Database connection settings
DB_HOST = "localhost"
DB_NAME = "practice_db"
DB_USER = "postgres"
DB_PASS = "1234" # update to your postgres password
DB_PORT = 5432

class Database:
    def __init__(self):
        self.host = DB_HOST
        self.name = DB_NAME
        self.user = DB_USER
        self.password = DB_PASS
        self.port = DB_PORT

    def get_connection(self):
        return psycopg2.connect(
            host=self.host,
            database=self.name,
            user=self.user,
            password=self.password,
            port=self.port
        )

    # 1. Fetch all customer records
    def get_all_customers(self):
        conn = self.get_connection()
        cur = conn.cursor()
        query = 'SELECT "customerNumber", "customerName", "contactFirstName", "contactLastName", phone, city, country, "creditLimit" FROM customers ORDER BY "customerName" ASC;'
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    # 2. Search customers by keyword
    def search_customers(self, term):
        conn = self.get_connection()
        cur = conn.cursor()
        search_pattern = f"%{term}%"
        query = '''
            SELECT "customerNumber", "customerName", "contactFirstName", "contactLastName", phone, city, country, "creditLimit" 
            FROM customers 
            WHERE "customerName" ILIKE %s 
               OR city ILIKE %s 
               OR country ILIKE %s 
               OR phone ILIKE %s 
               OR CAST("customerNumber" AS TEXT) ILIKE %s
            ORDER BY "customerName" ASC;
        '''
        cur.execute(query, (search_pattern, search_pattern, search_pattern, search_pattern, search_pattern))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    # 3. Get list of distinct countries
    def get_countries(self):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute('SELECT DISTINCT country FROM customers WHERE country IS NOT NULL ORDER BY country ASC;')
        rows = [r[0] for r in cur.fetchall()]
        cur.close()
        conn.close()
        return rows

    # 4. Filter customers by specific country
    def get_customers_by_country(self, country):
        conn = self.get_connection()
        cur = conn.cursor()
        query = 'SELECT "customerNumber", "customerName", "contactFirstName", "contactLastName", phone, city, country, "creditLimit" FROM customers WHERE country = %s ORDER BY "customerName" ASC;'
        cur.execute(query, (country,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return rows

    # 5. Fetch customer orders and total payments (Relational drilldown)
    def get_customer_orders_and_payments(self, customer_number):
        conn = self.get_connection()
        cur = conn.cursor()
        
        # Get customer basic info
        cur.execute('SELECT "customerName", phone, city, country, "creditLimit" FROM customers WHERE "customerNumber" = %s;', (customer_number,))
        cust_info = cur.fetchone()

        if not cust_info:
            cur.close()
            conn.close()
            return None

        # Fetch recent orders
        cur.execute('SELECT "orderNumber", "orderDate", status FROM orders WHERE "customerNumber" = %s ORDER BY "orderDate" DESC LIMIT 5;', (customer_number,))
        orders = cur.fetchall()

        # Fetch total payment sum
        cur.execute('SELECT COALESCE(SUM(amount), 0) FROM payments WHERE "customerNumber" = %s;', (customer_number,))
        total_paid = float(cur.fetchone()[0])

        cur.close()
        conn.close()

        return {
            "name": cust_info[0],
            "phone": cust_info[1],
            "city": cust_info[2],
            "country": cust_info[3],
            "creditLimit": float(cust_info[4] or 0),
            "orders": orders,
            "total_paid": total_paid
        }

    # 6. Get aggregate stats
    def get_stats(self):
        conn = self.get_connection()
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*), COALESCE(SUM("creditLimit"), 0), COUNT(DISTINCT country) FROM customers;')
        data = cur.fetchone()
        cur.close()
        conn.close()
        return {
            "total_customers": data[0],
            "total_credit": float(data[1]),
            "total_countries": data[2]
        }
