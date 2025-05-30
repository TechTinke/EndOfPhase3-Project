from sqlalchemy.orm import sessionmaker
from models import engine, Product, Customer, Sale, SaleItem
from helpers import exit_program
from datetime import date

Session = sessionmaker(bind=engine)
session = Session()

def main():
    while True:
        print("\nWelcome to the Grocery Store Manager!")
        print("1. Manage Products")
        print("2. Manage Customers")
        print("3. Manage Sales")
        print("4. Manage Sale Items")
        print("0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            manage_products()
        elif choice == "2":
            manage_customers()
        elif choice == "3":
            manage_sales()
        elif choice == "4":
            manage_sale_items()
        elif choice == "0":
            exit_program()
        else:
            print("Invalid choice, try again.")

def manage_products():
    while True:
        print("\nProduct Management")
        print("1. Add Product")
        print("2. Delete Product")
        print("3. View All Products")
        print("4. Find Product by Name")
        print("5. View Sale Items for Product")
        print("0. Back")
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                name = input("Product name: ")
                if not name:
                    raise ValueError("Name cannot be empty!")
                price = float(input("Price: "))
                if price < 0:
                    raise ValueError("Price cannot be negative!")
                stock = int(input("Stock quantity: "))
                if stock < 0:
                    raise ValueError("Stock cannot be negative!")
                product = Product(name=name, price=price, stock=stock)
                session.add(product)
                session.commit()
                print("Product added!")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                product_id = int(input("Product ID to delete: "))
                product = session.query(Product).get(product_id)
                if not product:
                    print("Product not found!")
                    continue
                session.delete(product)
                session.commit()
                print("Product deleted!")
            except ValueError:
                print("Error: Invalid ID!")
        elif choice == "3":
            products = session.query(Product).all()  # List usage
            if not products:
                print("No products found.")
            else:
                for p in products:
                    print(f"ID: {p.id}, Name: {p.name}, Price: ${p.price}, Stock: {p.stock}")
        elif choice == "4":
            name = input("Enter product name to find: ")
            product = session.query(Product).filter_by(name=name).first()
            if product:
                print(f"ID: {product.id}, Name: {product.name}, Price: ${product.price}, Stock: {product.stock}")
            else:
                print("Product not found!")
        elif choice == "5":
            try:
                product_id = int(input("Product ID: "))
                product = session.query(Product).get(product_id)
                if not product:
                    print("Product not found!")
                    continue
                sale_items = product.sale_items  # Related objects
                if not sale_items:
                    print("No sale items for this product.")
                else:
                    for si in sale_items:
                        print(f"Sale ID: {si.sale_id}, Qty: {si.quantity}, Price at Sale: ${si.price_at_sale}")
            except ValueError:
                print("Error: Invalid ID!")
        elif choice == "0":
            break
        else:
            print("Invalid choice, try again.")

def manage_customers():
    while True:
        print("\nCustomer Management")
        print("1. Add Customer")
        print("3. View All Customers")
        print("0. Back")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Customer name: ")
            contact = input("Contact info: ")
            customer = Customer(name=name, contact=contact)
            session.add(customer)
            session.commit()
            print("Customer added!")
        elif choice == "3":
            customers = session.query(Customer).all()  # List usage
            for c in customers:
                print(f"ID: {c.id}, Name: {c.name}, Contact: {c.contact}")
        elif choice == "0":
            break
        # Add more options later

def manage_sales():
    while True:
        print("\nSales Management")
        print("1. Create Sale")
        print("3. View All Sales")
        print("0. Back")
        choice = input("Enter your choice: ")
        if choice == "1":
            customer_id = int(input("Customer ID: "))
            customer = session.query(Customer).get(customer_id)
            if not customer:
                print("Customer not found!")
                continue
            sale = Sale(customer_id=customer_id, sale_date=date.today())
            session.add(sale)
            session.commit()
            print(f"Sale {sale.id} created! Add items in Sale Items menu.")
        elif choice == "3":
            sales = session.query(Sale).all()  # List usage
            for s in sales:
                print(f"ID: {s.id}, Customer: {s.customer.name}, Date: {s.sale_date}")
        elif choice == "0":
            break
        # Add more options later

def manage_sale_items():
    while True:
        print("\nSale Items Management")
        print("1. Add Sale Item")
        print("3. View All Sale Items")
        print("0. Back")
        choice = input("Enter your choice: ")
        if choice == "1":
            sale_id = int(input("Sale ID: "))
            product_id = int(input("Product ID: "))
            quantity = int(input("Quantity: "))
            sale = session.query(Sale).get(sale_id)
            product = session.query(Product).get(product_id)
            if not sale or not product:
                print("Sale or Product not found!")
                continue
            if product.stock < quantity:
                print("Not enough stock!")
                continue
            sale_item = SaleItem(sale_id=sale_id, product_id=product_id, quantity=quantity, price_at_sale=product.price)
            product.stock -= quantity
            session.add(sale_item)
            session.commit()
            print("Sale item added!")
        elif choice == "3":
            items = session.query(SaleItem).all()  # List usage
            for i in items:
                print(f"ID: {i.id}, Sale: {i.sale_id}, Product: {i.product.name}, Qty: {i.quantity}")
        elif choice == "0":
            break
        # Add more options later

if __name__ == "__main__":
    main()