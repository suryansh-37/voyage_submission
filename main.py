import csv
import json
from database import Database

def print_customer_table(customers):
    if not customers:
        print("\nNo customer records found.\n")
        return

    print("\n" + "=" * 96)
    print(f"{'ID':<6} | {'Company Name':<32} | {'Contact':<20} | {'Country':<16} | {'Credit Limit':<12}")
    print("-" * 96)
    for c in customers:
        cid = str(c[0])
        name = (c[1] or "")[:30]
        contact = f"{c[2] or ''} {c[3] or ''}".strip()[:18]
        country = (c[6] or "")[:14]
        credit = f"${c[7]:,.0f}" if c[7] else "$0"
        print(f"{cid:<6} | {name:<32} | {contact:<20} | {country:<16} | {credit:<12}")
    print("=" * 96)
    print(f"Total records: {len(customers)}\n")

def export_to_csv(customers, filename="exported_customers.csv"):
    if not customers:
        print("\nNo data to export.\n")
        return
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["CustomerID", "CompanyName", "FirstName", "LastName", "Phone", "City", "Country", "CreditLimit"])
            for c in customers:
                writer.writerow(c)
        print(f"\n[Success] Exported {len(customers)} records to {filename}\n")
    except Exception as e:
        print(f"\n[Error] Failed to export CSV: {e}\n")

def export_to_json(customers, filename="exported_customers.json"):
    if not customers:
        print("\nNo data to export.\n")
        return
    try:
        data = []
        for c in customers:
            data.append({
                "customerNumber": c[0],
                "customerName": c[1],
                "contactFirstName": c[2],
                "contactLastName": c[3],
                "phone": c[4],
                "city": c[5],
                "country": c[6],
                "creditLimit": float(c[7] or 0)
            })
        with open(filename, mode="w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"\n[Success] Exported {len(customers)} records to {filename}\n")
    except Exception as e:
        print(f"\n[Error] Failed to export JSON: {e}\n")

def show_customer_orders(db):
    cust_id = input("\nEnter Customer ID (e.g. 103): ").strip()
    if not cust_id.isdigit():
        print("Invalid input. Please enter a valid numeric Customer ID.")
        return

    data = db.get_customer_orders_and_payments(int(cust_id))
    if not data:
        print(f"\nCustomer #{cust_id} not found in database.\n")
        return

    print("\n" + "=" * 60)
    print(f" Customer Details: {data['name']} (ID: {cust_id})")
    print("=" * 60)
    print(f" Phone        : {data['phone']}")
    print(f" Location     : {data['city']}, {data['country']}")
    print(f" Credit Limit : ${data['creditLimit']:,.2f}")
    print(f" Total Paid   : ${data['total_paid']:,.2f}")
    print("-" * 60)
    print(f" Recent Orders ({len(data['orders'])}):")
    if not data['orders']:
        print("   No orders recorded for this customer.")
    else:
        for o in data['orders']:
            print(f"   - Order #{o[0]} | Date: {o[1]} | Status: {o[2]}")
    print("=" * 60 + "\n")

def show_database_stats(db):
    stats = db.get_stats()
    print("\n" + "=" * 50)
    print(" ClassicModels Database Overview")
    print("=" * 50)
    print(f" Total Customers        : {stats['total_customers']}")
    print(f" Total Credit Extended  : ${stats['total_credit']:,.2f}")
    print(f" Distinct Countries     : {stats['total_countries']}")
    print("=" * 50 + "\n")

def main():
    try:
        db = Database()
        # Test connection at startup
        stats = db.get_stats()
    except Exception as e:
        print("\n[Database Connection Error]")
        print("Could not connect to PostgreSQL. Please verify that:")
        print("1. PostgreSQL is running on port 5432.")
        print("2. The database 'practice_db' exists.")
        print("3. DB_USER and DB_PASS in database.py are correct.")
        print(f"Details: {e}\n")
        return

    while True:
        print("=" * 50)
        print("   ClassicModels PostgreSQL Explorer (CLI)")
        print("=" * 50)
        print("1. View All Customers")
        print("2. Search Customers (by name, city, phone, etc.)")
        print("3. Filter Customers by Country")
        print("4. View Customer Orders & Payment Summary")
        print("5. View Database Statistics")
        print("6. Export All Customers to CSV")
        print("7. Export All Customers to JSON")
        print("8. Exit")
        print("=" * 50)

        choice = input("Enter choice (1-8): ").strip()

        if choice == "1":
            customers = db.get_all_customers()
            print_customer_table(customers)

        elif choice == "2":
            term = input("\nEnter search keyword: ").strip()
            if term:
                results = db.search_customers(term)
                print_customer_table(results)
            else:
                print("Search term cannot be empty.")

        elif choice == "3":
            countries = db.get_countries()
            print("\nAvailable Countries:")
            for i, country in enumerate(countries, 1):
                print(f"  {i}. {country}", end="   " if i % 4 != 0 else "\n")
            print("\n")
            selected = input("Enter country name: ").strip()
            if selected:
                results = db.get_customers_by_country(selected)
                print_customer_table(results)

        elif choice == "4":
            show_customer_orders(db)

        elif choice == "5":
            show_database_stats(db)

        elif choice == "6":
            customers = db.get_all_customers()
            filename = input("Enter output CSV filename (default: exported_customers.csv): ").strip()
            if not filename:
                filename = "exported_customers.csv"
            export_to_csv(customers, filename)

        elif choice == "7":
            customers = db.get_all_customers()
            filename = input("Enter output JSON filename (default: exported_customers.json): ").strip()
            if not filename:
                filename = "exported_customers.json"
            export_to_json(customers, filename)

        elif choice == "8":
            print("\nGoodbye!\n")
            break

        else:
            print("\nInvalid selection. Please choose an option from 1 to 8.\n")

if __name__ == "__main__":
    main()
