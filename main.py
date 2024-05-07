from database.db_connect import db_connection
from database.query import query_table
from data.generate_data import generate_tables
from config.config import dbconfig
from database.create_table import create_db_table
from database.populate_table import populate_tables


def main(num_records): 
    """
    Main function to generate data tables, create database tables,  and execute queries.

    Args:
        num_records (int): Number of records to generate for each table.

    """
    try:
        # Generate data tables
        fact_dicts, product_dicts, store_dicts, time_dicts, promotion_dicts = generate_tables(records=num_records)
        
        
        # Establish database connection
        connection, engine = db_connection(dbconfig['USERNAME'], dbconfig['PASSWORD'], 
                    dbconfig['HOST'], 'retail_store')
        
        # Create database tables
        create_db_table(engine)
        
        populate_tables(engine,  fact_dicts, product_dicts, store_dicts, time_dicts, promotion_dicts)
        
        # Execute query statement list
        query_statements = [ # Calculating total sales revenue by year, quarter, and month
                            "SELECT d.year, d.quarter, d.month,  sum(s.sales_revenue) as total_sales_rev  \
                                from sales_table s \
                                INNER JOIN date_dimension d ON d.date_id=s.date_id \
                                GROUP BY d.year, d.quarter, d.month" ,
                             
                            # Analyzing sales performance by product category and store location
                           "SELECT p.category, sd.location, sum(s.sales_revenue) as total_sales_rev \
                                from sales_table s \
                                INNER JOIN product_dimension p ON p.product_id=s.product_id \
                                INNER JOIN store_dimension sd ON sd.store_id=s.store_id \
                                GROUP BY p.category, sd.location", 
                            
                            #  Identifying top-5-selling product category and least-5-selling product catgeory
                            "(SELECT p.category, sum(s.sales_revenue) as total_sales_rev \
                                from sales_table s \
                                INNER JOIN product_dimension p ON p.product_id=s.product_id \
                                GROUP BY p.category\
                                order by total_sales_rev DESC \
                                limit 5) \
                            Union \
                            (SELECT p.category, sum(s.sales_revenue) as total_sales_rev \
                                from sales_table s \
                                INNER JOIN product_dimension p ON p.product_id=s.product_id \
                                GROUP BY p.category\
                                order by total_sales_rev ASC \
                                limit 5) \
                            order by total_sales_rev DESC",
                            
                            # Comparing sales performance across different regions or stores
                            "SELECT store_id, sum(sales_revenue) as total_sales_rev \
                                from sales_table \
                                GROUP BY store_id",

                            # Evaluating promotion campaign on sales  
                           "SELECT p.type, avg(s.sales_revenue) as avg_sales_rev \
                               FROM sales_table s \
                                INNER JOIN promotion_dimension p ON p.promotion_id=s.promotion_id \
                                GROUP BY p.type"]

        for statement in query_statements: 
            query_result = query_table(statement, connection)
            print(query_result)
            
    except Exception as e: 
        raise Exception(f"Error: {e}")

if __name__ == "__main__": 
    main(20)
        