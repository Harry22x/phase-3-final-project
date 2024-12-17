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

    print("Getting all products from the database.")
    supliers = session.query(Suplier).all()
    for suplier in supliers:
        print(suplier)
    session.close()

def get_all_orders():
    print("Getting all orders from the database.")
    orders = session.query(Order).all()
    for order in orders:
        print(order)
    session.close()

def add_product():
    name = input("Enter product name: ")
    category = input("Enter product category: ")
    quantity_remaining = int(input("Enter product quantity remaining: "))
    supplier_id = int(input("Enter supplier ID: "))

    product = Product(name=name, category=category, quantity_remaining=quantity_remaining, supplier_id=supplier_id)
    session.add(product)
    session.commit()
    session.close()


def exit_program():
    print("Goodbye!")
    exit()
