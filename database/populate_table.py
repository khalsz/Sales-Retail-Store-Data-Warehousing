from sqlalchemy import insert
from sqlalchemy.orm import  Session
from database.create_table import Time, Product, Promotion, Sales, Store

def populate_tables(engine, sales_dicts, product_dicts, store_dicts, date_dicts, promotion_dicts): 
    """
    Populates database tables with data.

    Args:
        engine (Engine): SQLAlchemy engine object for the database.
        sales_dicts (list of dict): List of dictionaries containing data for the Sales table.
        product_dicts (list of dict): List of dictionaries containing data for the Product table.
        store_dicts (list of dict): List of dictionaries containing data for the Store table.
        date_dicts (list of dict): List of dictionaries containing data for the Date table.
        promotion_dicts (list of dict): List of dictionaries containing data for the Promotion table.

    Raises:
        Exception: If an error occurs during the data insertion process.
    """
    try: 
        with Session(engine) as session: 
            # Insert data into Product table
            session.execute(insert(Product), product_dicts)
            # Insert data into Date table
            session.execute(insert(Time), date_dicts)
            # Insert data into Store table
            session.execute(insert(Store), store_dicts)
            # Insert data into Promotion table
            session.execute(insert(Promotion), promotion_dicts)
            # Insert data into Sales table
            session.execute(insert(Sales), sales_dicts)
            session.commit()
    except Exception as e: 
        raise Exception("Error populating table with data: {e}")
    #add more
