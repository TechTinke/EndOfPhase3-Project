from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contact = Column(String)
    sales = relationship('Sale', backref='customer')