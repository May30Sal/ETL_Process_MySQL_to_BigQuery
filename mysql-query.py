import mysql.connector
import pandas as pd
import os # To predefine the path and file name of the files we'll export


#! Establishing a connection with the DB
cnx = mysql.connector.connect(option_files='C:/Users/USER/.my.cnf') 

#! Creating a cursor object using the cursor() method to read the queries
# cursor = cnx.cursor()
query = "SELECT title, released_year, pages FROM books LIMIT 10"
# cursor.execute(query)
# for (query) in cursor:
#     print(query[0])

#! Using Pandas to read the queries
dataframe = pd.read_sql(query, cnx)
print(dataframe)
# print(dataframe.dtypes) #! Print the data types
# print(type(dataframe)) #! The type of data is a bidimensional array

#! Using filters with Pandas (TRANSFORM PHASE)
# query = "SELECT title, released_year FROM books WHERE released_year > 2000 ORDER BY released_year ASC"
# dataframe = pd.read_sql(query, cnx)
# print(dataframe["released_year"].unique())

#! Creating a Series (will only show books released in 2001) with pandas (TRANSFORM PHASE)
# year_2001 = dataframe["released_year"] == 2001
# print(dataframe[year_2001]) # If we use a ~ before will show the books NOT released in 2001, ex dataframe[~year_2001]

#! Export data as a csv file (EXTRACT PHASE)
#dataframe.to_csv('C:/Users/MAYSA/sample.csv')
#dataframe.to_csv('G:\My Drive\Programming\data-eng-studies\data-files\sample.csv')

# path = os.getcwd()
# file = 'books_after_2000.csv'
# file_path = os.path.join(path, ' data-files', file)

# dataframe.to_csv(file_path)
# print(path)

#! Creating a table with "case" query using pandas (TRANSFORM PHASE)
# query = '''
# SELECT *, 
# CASE
# WHEN stock_quantity < 100 THEN "low stock"
#     WHEN stock_quantity < 500 THEN "medium stock"
#     ELSE "high stock"
# END AS stock_status
# FROM books; '''

# dataframe = pd.read_sql(query, cnx)
# print (dataframe)

#! (EXTRACT PHASE)
# dataframe.to_csv('G:\My Drive\Programming\data-eng-studies\data-files\stock_status.csv')

#! Creating python functions to transform the data (TRANSFORM PHASE)
# query = '''
# SELECT *  
# FROM books;"
# '''
# dataframe = pd.read_sql(query, cnx)

# def book_size(size):
#     if size < 200:
#         return "small book"
#     elif size < 500:
#         return "medium book"
#     else:
#         return "big book"

#! In dataframe["size"] I'm creating a new column called size in the dataframe array.
#! Then I say that this new column is equal to the dataframe["pages"] column.
#! to finish I apply the function book_size to the column dataframe["pages"].
# dataframe["size"] = dataframe["pages"].apply(book_size)
# print(dataframe)

#! Here I export the results of the new table with the new function in it
# dataframe.to_csv('G:\My Drive\Programming\data-eng-studies\data-files\_book_size.csv')

#! TRANSFORMING A TABLE STRUCTURE TO LOOK MORE CLEAN
# query = '''
# SELECT *
# FROM books_sold
# '''

# dataframe = pd.read_sql(query, cnx)
# #print(dataframe)

# #! defining a new index, instead of pandas index
# dataframe.set_index("date_sold", inplace=True)

# #! stack method will pin the columns as rows, reset.index will make the genre only a column not an index
# dataframe = dataframe.stack().reset_index()

# #! defining the new columns
# dataframe.columns = ["date_sold", "city", "quantity_of_books_sold"]

# #! exporting as a csv file (without the preset index)
# dataframe.to_csv('G:\My Drive\Programming\data-eng-studies\data-files\_books_sold.csv', index=False)

cnx.close()
