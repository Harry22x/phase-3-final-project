#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.database_models import Product, Suplier, Order

if __name__ == '__main__':
    engine = create_engine('sqlite:///inventory_management.db')
    Session = sessionmaker(bind=engine)
    session = Session()

 
    session.query(Product).delete()
    session.query(Suplier).delete()
    session.query(Order).delete()

    fake = Faker()

    def fake_phone_number(fake: Faker) -> str:
        return f'{fake.msisdn()[3:]}'

    categories = ['Tools', 'Food', 'Electronics', 'Furniture', 'Utensils', 'Clothing']

    
    category_products = {
        'Tools': ['Hammer', 'Screwdriver', 'Wrench', 'Pliers', 'Drill'],
        'Food': ['Bread', 'Milk', 'Cheese', 'Apple', 'Pasta'],
        'Electronics': ['Smartphone', 'Laptop', 'Headphones', 'Camera', 'Tablet'],
        'Furniture': ['Chair', 'Table', 'Couch', 'Bed', 'Shelf'],
        'Utensils': ['Fork', 'Knife', 'Spoon', 'Plate', 'Cup'],
        'Clothing': ['Shirt', 'Pants', 'Jacket', 'Shoes', 'Hat']
    }

    suplier_names=['ABC solutions','Wix fixes', 'Tryarch supplies','Leonard supplies','Iketo supplies',
                   'Lanard supplies','Global supplies','env supplies']

    
    supliers = []
    for i in suplier_names:
        suplier = Suplier(
            name=i,
            contact=fake_phone_number(fake),
            location=fake.address()
        )
        session.add(suplier)
        supliers.append(suplier)
        session.commit()  

    

    products = []
    
    for category in categories:
            for i in range(random.randint(2, 5)): 
                product_name = category_products[category][i]
                product = Product(
                    name=product_name,
                    category=category,
                    quantity_remaining=random.randint(3, 20),
                    supplier_id=random.randint(1,8)
                )
                products.append(product)

    session.bulk_save_objects(products)
    session.commit()

    session.close()
