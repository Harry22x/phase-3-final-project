#!/usr/bin/env python3

from faker import Faker
import random

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.database_models import Product,Suplier,Order

if __name__ == 'main':
    engine = create_engine('sqlite:///inventory_management.db')
    Session = sessionmaker(bind=engine)
    session = Session()    

    session.query(Product).delete()
    session.query(Suplier).delete()
    session.query(Order).delete()

    fake = Faker()
    def fake_phone_number(fake: Faker) -> str:
        return f'{fake.msisdn()[3:]}'

    locations = ['Nairobi','Lonodon','Paris','Mombasa','Nakuru','Cape Town','Manchester','Chicago']

    categories = ['Tools','Food','Electronics','Furniture','Utensils','Clothing']



    supliers = []
    for i in range(20):
        suplier = Suplier(
            name= fake.unique.name(),
            contact = fake_phone_number(fake),
            location = fake.adress()
        )
        session.add(suplier)
        session.commit()
        supliers.append(suplier)

    products = []
    for supplier in supliers:
        for i in range (random.ranint(1,5)):
            product = Product(
                name = fake.unique.name(),
                category = random.choice(categories),
                quantity_remaining = random.randint(3,20),
                supplier_id = supplier.id,
            )
        products.append(product)

    session.bulk_save_objects(products)
    session.commit()




    session.close()