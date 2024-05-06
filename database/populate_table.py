from sqlalchemy import insert
from sqlalchemy.orm import  Session
from database import Time, Product, Customer, Order, Fact

def populate_tables(engine, fact_dicts, product_dicts, customer_dicts, time_dicts, order_dicts): 
    """
    Populates database tables with data.

    Args:
        engine (Engine): SQLAlchemy engine object for the database.
        fact_dicts (list of dict): List of dictionaries containing data for the Fact table.
        product_dicts (list of dict): List of dictionaries containing data for the Product table.
        customer_dicts (list of dict): List of dictionaries containing data for the Customer table.
        time_dicts (list of dict): List of dictionaries containing data for the Time table.
        order_dicts (list of dict): List of dictionaries containing data for the Order table.

    Raises:
        Exception: If an error occurs during the data insertion process.
    """
    try: 
        with Session(engine) as session: 
            # Insert data into Product table
            session.execute(insert(Product), product_dicts)
            # Insert data into Time table
            session.execute(insert(Time), time_dicts)
            # Insert data into Customer table
            session.execute(insert(Customer), customer_dicts)
            # Insert data into Order table
            session.execute(insert(Order), order_dicts)
            # Insert data into Fact table
            session.execute(insert(Fact), fact_dicts)
            session.commit()
    except Exception as e: 
        raise Exception("Error populating table with data: {e}")
    #add more
