# Retail Store Data Warehouse
This project implements a star schema data warehouse for a retail store that operates multiple stores in different regions and sells various products. The data warehouse is designed to facilitate analytical queries and generate insights into sales performance, product categories, store locations, and promotion effectiveness.

## Overview
The data warehouse is built using SQLAlchemy, a Python SQL toolkit and Object-Relational Mapping (ORM) library, along with PostgreSQL as the underlying database management system. The project comprises several components:

1. **Data Generation**: Synthetic data is generated for the sales, product, store, time, and promotion tables using Faker, a Python library for generating fake data.
2. **Database Schema**: The star schema consists of multiple tables representing different dimensions and a fact table for recording sales transactions. The tables include:
    - Product Dimension
    - Store Dimension
    - Date Dimension
    - Promotion Dimension
    - Sales Fact Table
3. **Data Population**: The generated synthetic data is inserted into the corresponding database tables using SQLAlchemy's ORM functionality.
4. **Query Execution**: Analytical queries are executed against the populated database tables to derive insights into various aspects of the retail store's operations, such as total sales revenue by year, quarter, and month, sales performance by product category and store location, top-selling and least-selling product categories, comparisons of sales performance across different regions or stores, and evaluation of promotion campaign effectiveness on sales.

## Installation and Setup
To set up and run the data warehouse project, follow these steps:
1. **Clone the Repository**: Clone the repository to your local machine using Git:
    `git clone https://github.com/khalsz/Sales-Retail-Store-Data-Warehousing.git`
2. **Install Dependencies**: Install the required Python dependencies listed in the requirements.txt file using pip:
    `pip install -r requirements.txt`
3. **Database Configuration**: Configure the PostgreSQL database connection details in the config.py file, including the username, password, host, and database name.
4. **Run the Main Script**: Execute the main.py script to generate synthetic data, create database tables, populate them with data, and execute analytical queries:
    `python main.py`
5. **Review Query Results**: Review the results of the executed queries printed to the console for insights into the retail store's operations and performance metrics.

## Contributing
Contributions to this project are welcome! If you encounter any issues, have suggestions for improvements, or would like to contribute new features, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
