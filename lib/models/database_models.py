from sqlalchemy import (ForeignKey, Column, Integer, String, MetaData,DateTime,
                        Index
)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}
metadata = MetaData(naming_convention=convention)

Base = declarative_base(metadata=metadata)


class Suplier(Base):
    __tablename__ = 'suppliers'

    id = Column(Integer(),primary_key=True)
    name = Column(String(20))
    contact = Column(String(10))
    location = Column(String())
    products = relationship('Product', backref= backref('supplier'))

    __table_args__ = (Index('suplier_name_idx', 'name'),)

    def __repr__(self):
        return f'Supplier(id={self.id}, name ={self.name}, contact = {self.contact}, location ={self.location})'
        
    
class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer(),primary_key=True)
    name = Column(String(20))
    category = Column(String())
    quantity_remaining = Column (Integer())
    cost_per_item = Column(Integer())
    supplier_id = Column(Integer(), ForeignKey('suppliers.id'))  
    orders = relationship('Order',backref= backref('product'))

    __table_args__ = (Index('product_name_idx', 'name'),)

    def __repr__(self):
        return f'Product(id={self.id}, name={self.name}, category={self.category}, quantity remaining={self.quantity_remaining}, cost per item = {self.cost_per_item},supplier id={self.supplier_id})'

    
    

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer(), primary_key=True)
    product_id = Column(Integer(),ForeignKey('products.id'))
    product_name = Column(String())
    order_date = Column(DateTime(), default=datetime.now())
    order_quantity = Column(Integer())
    total_cost = Column(Integer())
  

    def __repr__(self):
        return f'Order(id={self.id},product_id={self.product_id},product name = {self.product_name}, order_date={self.order_date}, order_quantity={self.order_quantity}, total cost = {self.total_cost})'