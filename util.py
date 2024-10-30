import psycopg2
from psycopg2 import Error

# Functions are from the util.py files from example 3 and example 4

# connect to the database
def connect_to_db(username='raywu1990',password='test',host='127.0.0.1',port='5432',database='dvdrental'):
	try:
	    # Connect to an existing database
	    connection = psycopg2.connect(user=username,
	                                  password=password,
	                                  host=host,
	                                  port=port,
	                                  database=database)

	    # Create a cursor to perform database operations
	    cursor = connection.cursor()
	    print("connected to the database")

	    return cursor, connection

	except (Exception, Error) as error:
	    print("Error while connecting to PostgreSQL", error)
	
# disconnecting from the database using the connection and the cursor
def disconnect_from_db(connection,cursor):
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
    else:
    	print("Connection does not work.")

# committing the sql changes made
def run_and_commit_sql(cursor, connection, sql_string=""):
	try:
	    # Executing a SQL query
	    cursor.execute(sql_string)
	    # if some changes are made, you need to commit your changes
	    connection.commit()
	    # use 1 to represent the commit was success
	    return 1
	# return the error if the commit was unsuccessful
	except (Exception, Error) as error:
		return error

# for just retaining information to display it
def run_and_fetch_sql(cursor, sql_string=""):
	try:
	    # Executing a SQL query
	    cursor.execute(sql_string)
	    # Fetch result
	    record = cursor.fetchall()
	    return record
	except (Exception, Error) as error:
		return ("Error: ", error)
