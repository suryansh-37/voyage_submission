import psycopg2
import csv
import json

# postgresql database connection settings
DB_HOST = "localhost"
DB_NAME = "practice_db"
DB_USER = "postgres"
DB_PASS = "1234"  # change this to your pgAdmin password
DB_PORT = 5432

def connect():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    return conn

# 1. show all customers from database
def show_all_customers():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('SELECT "customerNumber", "customerName", phone, city, country, "creditLimit" FROM customers ORDER BY "customerName" ASC;')
        rows = cur.fetchall()
        cur.close()
        conn.close()

        print("\n--- ALL CUSTOMERS ---")
        for r in rows:
            print("ID:", r[0], "| Name:", r[1], "| Phone:", r[2], "| City:", r[3], "| Country:", r[4], "| Credit: $" + str(r[5]))
        print("Total customers:", len(rows), "\n")
    except Exception as e:
        print("Error fetching customers:", e)

# 2. search customer by keyword
def search_customers():
    keyword = input("\nEnter keyword to search (name, city, country, or ID): ").strip()
    if not keyword:
        print("Search keyword cannot be empty.\n")
        return

    try:
        conn = connect()
        cur = conn.cursor()
        sql = '''
            SELECT "customerNumber", "customerName", phone, city, country, "creditLimit" 
            FROM customers 
            WHERE "customerName" ILIKE %s 
               OR city ILIKE %s 
               OR country ILIKE %s 
               OR CAST("customerNumber" AS TEXT) ILIKE %s;
        '''
        search_pattern = "%" + keyword + "%"
        cur.execute(sql, (search_pattern, search_pattern, search_pattern, search_pattern))
        rows = cur.fetchall()
        cur.close()
        conn.close()

        print("\n--- SEARCH RESULTS ---")
        if len(rows) == 0:
            print("No customers found matching:", keyword)
        else:
            for r in rows:
                print("ID:", r[0], "| Name:", r[1], "| City:", r[3], "| Country:", r[4], "| Credit: $" + str(r[5]))
            print("Total found:", len(rows))
        print()
    except Exception as e:
        print("Error searching customers:", e)

# 3. filter customers by country
def filter_by_country():
    country = input("\nEnter country name (e.g. USA, France, Germany): ").strip()
    if not country:
        print("Country cannot be empty.\n")
        return

    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('SELECT "customerNumber", "customerName", city, country, "creditLimit" FROM customers WHERE country ILIKE %s ORDER BY "customerName";', (country,))
        rows = cur.fetchall()
        cur.close()
        conn.close()

        print("\n--- CUSTOMERS IN " + country.upper() + " ---")
        if len(rows) == 0:
            print("No customers found in", country)
        else:
            for r in rows:
                print("ID:", r[0], "| Name:", r[1], "| City:", r[2], "| Credit: $" + str(r[4]))
            print("Total in " + country + ":", len(rows))
        print()
    except Exception as e:
        print("Error filtering by country:", e)

# 4. view customer orders and payments (relational data)
def view_customer_orders():
    cust_id = input("\nEnter customer number (e.g. 103): ").strip()
    if not cust_id.isdigit():
        print("Please enter a valid numeric ID.\n")
        return

    try:
        conn = connect()
        cur = conn.cursor()

        # get customer info
        cur.execute('SELECT "customerName", phone, country FROM customers WHERE "customerNumber" = %s;', (cust_id,))
        cust = cur.fetchone()

        if not cust:
            print("Customer not found with ID:", cust_id, "\n")
            cur.close()
            conn.close()
            return

        print("\n-------------------------------------------")
        print("Customer:", cust[0])
        print("Phone   :", cust[1])
        print("Country :", cust[2])

        # get orders from orders table
        cur.execute('SELECT "orderNumber", "orderDate", status FROM orders WHERE "customerNumber" = %s ORDER BY "orderDate" DESC LIMIT 5;', (cust_id,))
        orders = cur.fetchall()

        print("\nRecent Orders:")
        if len(orders) == 0:
            print("  No orders found for this customer.")
        else:
            for o in orders:
                print("  Order #" + str(o[0]) + " | Date: " + str(o[1]) + " | Status: " + str(o[2]))

        # get total payments from payments table
        cur.execute('SELECT COALESCE(SUM(amount), 0) FROM payments WHERE "customerNumber" = %s;', (cust_id,))
        total_paid = cur.fetchone()[0]
        print("\nTotal Payments Made: $" + str(total_paid))
        print("-------------------------------------------\n")

        cur.close()
        conn.close()
    except Exception as e:
        print("Error fetching customer orders:", e)

# 5. show summary statistics
def show_stats():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('SELECT COUNT(*), COALESCE(SUM("creditLimit"), 0), COUNT(DISTINCT country) FROM customers;')
        data = cur.fetchone()
        cur.close()
        conn.close()

        print("\n--- DATABASE SUMMARY ---")
        print("Total Customers       :", data[0])
        print("Total Credit Extended : $" + str(data[1]))
        print("Countries Represented :", data[2])
        print("------------------------\n")
    except Exception as e:
        print("Error fetching stats:", e)

# 6. export to csv file
def export_csv():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('SELECT "customerNumber", "customerName", phone, city, country, "creditLimit" FROM customers ORDER BY "customerName";')
        rows = cur.fetchall()
        cur.close()
        conn.close()

        filename = "customers_export.csv"
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["CustomerNumber", "CustomerName", "Phone", "City", "Country", "CreditLimit"])
            for row in rows:
                writer.writerow(row)

        print("\nSuccess! Exported", len(rows), "customers to", filename, "\n")
    except Exception as e:
        print("Error exporting CSV:", e)

# 7. export to json file
def export_json():
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute('SELECT "customerNumber", "customerName", phone, city, country, "creditLimit" FROM customers ORDER BY "customerName";')
        rows = cur.fetchall()
        cur.close()
        conn.close()

        data_list = []
        for r in rows:
            data_list.append({
                "customerNumber": r[0],
                "customerName": r[1],
                "phone": r[2],
                "city": r[3],
                "country": r[4],
                "creditLimit": float(r[5] or 0)
            })

        filename = "customers_export.json"
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data_list, file, indent=2)

        print("\nSuccess! Exported", len(data_list), "customers to", filename, "\n")
    except Exception as e:
        print("Error exporting JSON:", e)

# main menu
def main():
    print("==========================================")
    print(" ClassicModels PostgreSQL CLI Explorer")
    print("==========================================")
    
    while True:
        print("1. View All Customers")
        print("2. Search Customers")
        print("3. Filter Customers by Country")
        print("4. View Customer Orders and Payments")
        print("5. View Database Statistics")
        print("6. Export Customers to CSV")
        print("7. Export Customers to JSON")
        print("8. Exit")

        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            show_all_customers()
        elif choice == "2":
            search_customers()
        elif choice == "3":
            filter_by_country()
        elif choice == "4":
            view_customer_orders()
        elif choice == "5":
            show_stats()
        elif choice == "6":
            export_csv()
        elif choice == "7":
            export_json()
        elif choice == "8":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid option, please type a number from 1 to 8.\n")

if __name__ == "__main__":
    main()
