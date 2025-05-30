from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///grocery_store.db')
Base = declarative_base()

from .product import Product
from .customer import Customer
from .sale import Sale
from .sale_item import SaleItem