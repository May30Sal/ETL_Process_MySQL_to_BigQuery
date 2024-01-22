# modules
from google.cloud import bigquery

#! Instantiate the client
client = bigquery.Client(project='learning-data-eng')

#! querying the database using bigquery and python

# sql_query = '''
# SELECT *
# FROM demo_dataset.books_after_2001;
# '''
# query_job = client.query(sql_query)

# results = query_job.result()

# for r in results:
#     print(r.id, r.title, r.released_year)

#! Loading data to BigQuery
targe_table = 'learning-data-eng.demo_dataset.books'

# config the table we'll be loading
job_config = bigquery.LoadJobConfig(
    skip_leading_rows=1, #skip the header row
    source_format=bigquery.SourceFormat.CSV,
    autodetect=True
)

# defining the path
file_path='G:\My Drive\Programming\data-eng-studies\data-files\_book_size.csv'

# opening the file and loadind it
with open(file_path, 'rb') as source_file:
    load_job = client.load_table_from_file(
        source_file,
        targe_table,
        job_config=job_config
    )

load_job.result()

destination_table = client.get_table(targe_table)
print(f'You have {destination_table.num_rows} rows in your table')

