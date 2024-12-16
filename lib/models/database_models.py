from sqlalchemy import (ForeignKey, Column, Integer, String, MetaData,DateTime,
                        CheckConstraint, PrimaryKeyConstraint, UniqueConstraint,Index
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)


class Suplier:
    __tablename__ = 'suppliers'

    id = Column(Integer(),primary_key=True)
    name = Column(String(20))
    contact = Column(Integer(10))
    location = Column(String())
    products = relationship('Product', backref= backref('supplier'))

    def __repr__(self):
        return f'Supplier(id={self.id}, name ={self.name}, contact = {self.contact}, location ={self.location})'
        
    Index('suplier_name', 'name')

class Product:
    __tablename__ = 'products'

    id = Column(Integer(),primary_key=True)
    name = Column(String(20))
    category = Column(String())
    quantity_remaining = Column (Integer())
    supplier_id = Column(Integer(), ForeignKey('suppliers.id'))  
    orders = relationship('Order',backref= backref('product'))

    def __repr__(self):
        return f'Produt(id={self.id}, name={self.name},category={self.category},quantity remaining={self.quantity_remaining},supllier={self.supplier_id})'
    
    Index('produt_name', 'name')

class Order:
    __tablename__ = 'orders'

    id = Column(Integer(), primary_key=True)
    product_id = Column(Integer(),ForeignKey('products.id'))
    order_date = Column(DateTime(), default=datetime.now())
    order_quantity = Column(Integer())

    def __repr__(self):
        return f'Order(id={self.id},product_id={self.product_id}, order date={self.order_date}, order quantity={self.order_quantity})'