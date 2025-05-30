from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from . import Base

class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    sale_date = Column(Date)
    sale_items = relationship('SaleItem', backref='sale')