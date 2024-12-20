# lib/helpers.py
from models.database_models import Product,Suplier,Order
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///inventory_management.db')
Session = sessionmaker(engine)
session = Session()

def get_all_products():
    print("Getting all products from the database.")
    products = session.query(Product).all()
    for product in products:
        print(product)
    session.close()

def get_all_suppliers():

    print("Getting all Suppliers from the database.")
    supliers = session.query(Suplier).all()
    for suplier in supliers:
        print(suplier)
    session.close()

def get_all_orders():
    print("Getting all orders from the database.")
    orders = session.query(Order).all()
    if orders:
        for order in orders:
            print(order)
        session.close()
    else:
        print("No orders have been made")

def add_product():
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    quantity_remaining = int(input("Enter product quantity remaining: "))
    cost_per_item = int(input("Enter cost of item: "))
    supplier_id = int(input("Enter supplier ID: "))
    try:
        product = Product(name=name, category=category, quantity_remaining=quantity_remaining,cost_per_item = cost_per_item, supplier_id=supplier_id)
        session.add(product)
        session.commit()
        session.close()
        print("Successfully added product")
    except Exception as exc:
        print("Error adding product: ", exc)

def add_suplier():
    name = input("Enter supplier name: ")
    contact = input("Enter supplier contact: ")
    location = input("Enter supplier location: ")
    try:
        suplier = Suplier(name=name, contact=contact, location=location)
        session.add(suplier)
        session.commit()
        session.close()
        print("Suplier added successfully")
    except Exception as exc:
        print("Error adding supplier: ", exc)

def delete_product():
    product_id = int(input("Enter product ID to delete: "))

    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        try:
            session.delete(product)
            session.commit()
            print("Product deleted successfully.")
        except Exception as exc:
            print("Error deleting product", exc)
    else:
        print("Product not found.")
    session.close()

def delete_suplier():
    suplier_id = int(input("Enter supplier ID to delete: "))

    suplier = session.query(Suplier).filter_by(id=suplier_id).first()
    if suplier:
        try:
            session.delete(suplier)
            session.commit()
            print("Suplier deleted successfully.")
        except Exception as exc:
            print("Error deleting supplier", exc)
    else:
        print("Supplier not found.")
    session.close()

def get_product_by_id():
    product_id = int(input("Enter product ID: "))

    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        print(product)
    else:
        print("Product not found.")
    session.close()

def get_supplier_by_id():
    suplier_id = int(input("Enter supplier ID: "))

    suplier = session.query(Suplier).filter_by(id=suplier_id).first()
    if suplier:
        print(suplier)
    else:
        print("Supplier not found.")
    session.close()

def make_order():
    product_id = int(input("Enter product ID: "))
    quantity = int(input("Enter quantity: "))

    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        try:
            product.quantity_remaining += quantity            

            order = Order(product_id=product_id,product_name = product.name, order_quantity=quantity, total_cost = product.cost_per_item * quantity)
            session.add(order)
            session.commit()
            print("Successfully made order.")
        except Exception as exc:
            session.rollback()
            print("Error making order: ", exc)
    else:
        print("Product not found.")
    session.close()

def find_order_by_id():
    order_id = int(input("Enter order ID: "))

    order = session.query(Order).filter_by(id=order_id).first()
    if order:
        print(order)
    else:
        print("Order not found.")
    session.close()

def delete_order():
    order_id = int(input("Enter order ID to delete: "))

    order = session.query(Order).filter_by(id=order_id).first()
    if order:
        try:
            session.delete(order)
            session.commit()
            print("Succesfully deleted order")
        except Exception as exc:
            print("Error deleting order", exc)
    else:
        print("Order not found.")
    session.close()

def low_stock_products():
    products = session.query(Product).filter(Product.quantity_remaining<10).all()
    if products:
        for product in products:
            print(product)
    else:
        print("No products have a quantity remaining of less than 10.")
    session.close()

def find_supplier_products():
    supplier_id = int(input("Enter Supplier ID: "))
    products =  session.query(Product).filter(Product.supplier_id == supplier_id).all()
    if products:
        for product in products:
            print(product)
    else:
        print("No products found for this Supplier.")

def update_product():
    product_id = int(input("Enter product ID: "))
    new_name = input("Enter new name: ")
    new_category = input("Enter new category: ")
    new_supplier_id = int(input("Enter new supplier ID: "))
    new_quantity = int(input("Enter new quantity: "))

    product = session.query(Product).filter_by(id=product_id).first()
    if product:
        try:
            product.name = new_name
            product.category = new_category
            product.supplier_id = new_supplier_id
            product.quantity_remaining = new_quantity
            session.commit()
            print("Successfully updated product.")
            print(product)
        except Exception as exc:
            print("Error updating product: ", exc)
    else:
        print("Product not found.")
    session.close()

def update_supplier():
    supplier_id = int(input("Enter supplier ID: "))
    new_name = input("Enter new name: ")
    new_contact = input("Enter new contact: ")
    new_location = input("Enter new location: ")

    suplier = session.query(Suplier).filter_by(id=supplier_id).first()
    if suplier:
        try:
            suplier.name = new_name
            suplier.contact = new_contact
            suplier.location = new_location
            session.commit()
            print("Successfully updated supplier")
            print(suplier)
        except Exception as exc:
            print("Error updating supplier: ", exc)
    else:
        print("Supplier not found.")
    session.close()

def filter_products_by_category():
    category = input("Enter product category: ")

    products = session.query(Product).filter_by(category=category).all()
    if products:
        for product in products:
            print(product)
    else:
        print("No products found in this category.")
    session.close()

def exit_program():
    print("Goodbye!")
    exit()
