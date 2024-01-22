# Modules
import mysql.connector
import pandas as pd
from google.cloud import bigquery

# Creating the path
path = 'G:\My Drive\Programming\data-eng-studies\data-files\stock_status.csv'

# Defining the project
project = 'learning-data-eng'
dataset = 'demo_dataset'
table = 'book_sales'
table_id = f'{project}.{dataset}.{table}'

# Establishing data connection with MySQL
conn = mysql.connector.connect(option_files='C:/Users/MAYSA/.my.cnf') 

#! Extracting data from MySQL
query = '''
SELECT title, stock_quantity,
CASE
	WHEN stock_quantity <= 50 THEN "Needs stock up"
    WHEN stock_quantity <= 100 THEN "Stock is okay"
    ELSE "Overstock"
END AS stock_status
FROM books;
'''

#! Transforming the data
def sales(quantity):
    if quantity < 50:
        return "Good Sales"
    elif quantity < 100:
        return "Medium Sales"
    else:
        return "Bad Sales"

dataframe = pd.read_sql(query, conn)
dataframe["sales_performance"] = dataframe["stock_quantity"].apply(sales)


# Exporting to a CSV file
dataframe.to_csv(path, index=False) # Set the index to false to not show in csv, so BigQuery won't mix it up.


# Establishing data connection with BigQuery
client = bigquery.Client(project=project) #defined before

#! Loading the data into BigQuery
job_config = bigquery.LoadJobConfig(
    autodetect=True,
    write_disposition='WRITE_TRUNCATE'
)

# Opening the file and loadind it
load_job = client.load_table_from_dataframe(
    dataframe,
    table_id,
    job_config=job_config
)

load_job.result()

# Testing that everything was ok
destination_table = client.get_table(table_id)
print(f'You have {destination_table.num_rows} rows in your table')









