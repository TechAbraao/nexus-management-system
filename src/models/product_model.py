from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

directory = '/home/asantos/my-personal-projects/product-registration-system/src/db'
db = create_engine(f'sqlite:///{directory}/database.db')

Base = declarative_base()

class ProductModel(Base):
    __tablename__ = "produtos"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    price = Column("price", Integer)
    quantity = Column("quantity", Integer)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

def create_database():
    directory = '/home/asantos/my-personal-projects/product-registration-system/src/db'
    db = create_engine(f'sqlite:///{directory}/database.db')
    Base.metadata.create_all(db)

def get_session():
    directory = '/home/asantos/my-personal-projects/product-registration-system/src/db'
    db = create_engine(f'sqlite:///{directory}/database.db')
    Session = sessionmaker(bind=db)
    session = Session()
    return session
