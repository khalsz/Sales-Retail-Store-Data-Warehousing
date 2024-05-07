import pandas as pd
from faker import Faker
import datetime
from datetime import datetime as dt
import random
import pandas as pd

fake = Faker('en_US')


def product_data(): 
    name = fake.word()
    category = fake.word(ext_word_list=["Electronics", "Clothing", "Home Appliances"])
    price = random.randrange(1000,5000, 500)
    
    product = {
        'product_id': fake.random_number(digits=5), 
        'name': name, 
        'price': price, 
        'category':category, 
        'description':str.lower(f"this name of product is {name} and and it belongs to catgeory {category}"),  
        'cost' : (price - (lambda x: 10/x * 100)(price)) 
    }
    return product

def store_data(): 
    store = {
        'store_id': fake.random_number(digits=5),
        'name': fake.name(),
        "location": fake.street_name(),
    }
    return store
def time_data(date, sn): 
    times = {
        'date_id': sn,
        'date': date, 
        'month': date.month,
        'quarter': pd.Timestamp(date).quarter,
        'year': date.year
    }
    return times

def promotion_data(): 
    types = fake.word(ext_word_list=["E-marketing", "rebanding", "influencer marketing", "affiliate marketing"])
    # generating prmotion campaign date whcih is different from others date. 
    date =  dt.strptime(fake.date(pattern="%Y-%m-%d", 
                end_datetime=datetime.date(2024, 4,1)), 
                "%Y-%m-%d").date()
    order = {
        'promition_id': fake.random_number(digits=5), 
        'type': types, 
        'date': date, 
        'cost': random.randrange(3000,10000, 500), 
        'company_name': fake.name()
    }
    return order
    
def sales_data(product_data, store_data, date, promotion_data, time_data): 

    fact = {
        'sales_id': fake.random_number(digits=6),
        'product_id': product_data['product_id'], 
        'store_id': store_data['store_id'],
        'promotion_id': promotion_data['promition_id'],
        'date_id': time_data['date_id'],
        'order_date': date, 
        'quantity': fake.random_number(digits=3), 
        'sales_revenue': fake.random_number(digits=5)
    }
    return fact



def generate_tables(records): 
    """
    Generate synthetic data tables.

    Args:
        records (int): Number of records to generate for each table.

    Returns:
        tuple: A tuple containing list of dictionaries for the sales, product, store, date, promotion dictionary.

    """
    sales_dicts = []
    date_dicts = []
    product_dicts = []
    store_dicts = []
    promotion_dicts = []
    
    # Generate data for the specified number of records
    for i in range(records): 
        # Generate a random date within the specified range
        date = dt.strptime(fake.date(pattern="%Y-%m-%d", 
                            end_datetime=datetime.date(2024, 4,1)), 
                           "%Y-%m-%d").date()
        # Generate data for each table
        product = promotion_data()
        store = store_data(date)
        promotion = promotion_data()
        times = time_data(date=date, sn=i)
        sales = sales_data(product, store, date, promotion, times)
        
        # append data record to list
        product_dicts.append(product)
        date_dicts.append(times)
        sales_dicts.append(sales)
        store_dicts.append(store)
        promotion_dicts.append(promotion)

    return sales_dicts, product_dicts, store_dicts, date_dicts, promotion_dicts
