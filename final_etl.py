# Modules
import mysql.connector
import pandas as pd
from google.cloud import bigquery

# Creating the path
path = 'G:\My Drive\Programming\data-eng-studies\data-files\stock_status.csv'

# Defining the project
project = 'learning-data-eng'
dataset = 'demo_dataset'
table = 'stock_status'
table_id = f'{project}.{dataset}.{table}'

# Establishing data connection with MySQL
conn = mysql.connector.connect(read_default_file='C:/Users/USER/.my.cnf') 

# Extracting data from MySQL and Transforming it
query = '''
SELECT title, stock_quantity,
CASE
	WHEN stock_quantity <= 50 THEN "Needs stock up"
    WHEN stock_quantity <= 100 THEN "Stock is okay"
    ELSE "Overstock"
END AS stock_status
FROM books;
'''

# Exporting to a CSV file
dataframe = pd.read_sql(query, conn)
dataframe.to_csv(path, index=False) # Set the index to false to not show in csv, so BigQuery won't mix it up.


# Establishing data connection with BigQuery
client = bigquery.Client(project=project) #defined before

# Config the table we'll be loading into BigQuery
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1, #skip the header row, because BigQuery already have it
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True,
    write_disposition='WRITE_TRUNCATE'
)

# Opening the file and loadind it
with open(path, 'rb') as source_file:
    load_job = client.load_table_from_file(
        source_file,
        table_id,
        job_config=job_config
    )

load_job.result()

# Testing that everything was ok
destination_table = client.get_table(table_id)
print(f'You have {destination_table.num_rows} rows in your table')









