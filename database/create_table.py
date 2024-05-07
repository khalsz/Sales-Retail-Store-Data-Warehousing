from sqlalchemy import  Column, Integer, ForeignKey, String, DATE
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class Product(Base): 
    __tablename__ = "product_dimension"
    product_id = Column( Integer, primary_key=True)
    name = Column(String(40))
    category = Column(String(40))
    price = Column(Integer)
    description = Column(String(100))
    cost = Column(Integer)
    

class Time(Base): 
    __tablename__ = "date_dimension"
    date_id = Column(Integer, primary_key=True)
    date = Column(DATE)
    month = Column( Integer)
    year = Column(Integer)
    quarter = Column(Integer)
    
class Store(Base): 
    __tablename__ = "store_dimension"
    store_id = Column(Integer, primary_key=True)
    name = Column(String(40))
    location = Column(String(50))

class Promotion(Base): 
    __tablename__ = 'promotion_dimension'
    promotion_id = Column(Integer, primary_key=True)
    type = Column(String(40))  
    date = Column(DATE)  
    cost = Column(Integer)
    
class Sales(Base): 
    __tablename__ = "sales_table"
    sales_id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    sales_revenue = Column(Integer)
    product_id = Column(Integer, ForeignKey("product_dimension.product_id"), nullable=False)
    product = relationship("Product")
    date_id = Column(Integer, ForeignKey("date_dimension.date_id"), nullable=False)
    time = relationship('Time', backref=backref('Fact'))
    store_id = Column( Integer, ForeignKey("store_dimension.store_id"), nullable=False)
    customer = relationship('Store')
    promotion_id = Column(Integer, ForeignKey("promotion_dimension.promotion_id"), nullable=False)
    order = relationship('Promotion')

def create_db_table(engine): 
    """
    Creates database tables based on SQLAlchemy metadata.

    This function drops existing tables (if any) and creates new tables based on the SQLAlchemy metadata defined in Base.

    Args:
        engine (Engine): SQLAlchemy engine object for the database.

    Raises:
        Exception: If an error occurs during the table creation process.
    """
    try: 
        # Drop existing tables
        Base.metadata.drop_all(engine, 
                               tables=[Base.metadata.tables["promotion_dimension"], 
                                       Base.metadata.tables["store_dimension"], 
                                       Base.metadata.tables["product_dimension"], 
                                       Base.metadata.tables["date_dimension"], 
                                       Base.metadata.tables["sales_table"]])
        # Create new tables
        Base.metadata.create_all(engine)
        print("all table successfully created")
        
    except Exception as e: 
        raise Exception(f"Error creating tables: {e}")