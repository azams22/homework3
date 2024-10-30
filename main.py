from flask import Flask, render_template
import util

# create an application instance
app = Flask(__name__)

# global variables that can be used in a config file
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/

# URL: 127.0.0.1:5000/api/update_basket_a - for updating basket_a with the row (5, 'Cherry')
@app.route('/api/update_basket_a')
def update_basket_a():

    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    
    # execute SQL commands
    record = util.run_and_commit_sql(cursor, connection, "INSERT INTO basket_a (a, fruit_a) VALUES (5,'Cherry');")
    
    # display the error if there was one, otherwise, just print success
    if record != 1:
        log = "Error: " + str(record)
    else:
        log = 'Success!'
    
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    
    # using render_template function, Flask will search the file named index.html under templates folder
    return render_template('index.html', log_html = log)

# URL: 127.0.0.1:5000/api/unique - to display all the unique values in basket_a and basket_b
@app.route('/api/unique')
def unique():
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    
    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "select a, fruit_a, b, fruit_b from basket_a full join basket_b on fruit_a=fruit_b where a is NULL or b is NULL;")

    # Display the error if there was one, otherwise just display the table
    if record[0] == "Error: ":
        logMessage = record[0] + str(record[1])
    else:
        # this will return all column names of the select result table
        col_names = [desc[0] for desc in cursor.description]
        log = record[:5]
        logMessage = 'Unique fruits in each basket, where fruit_a is from basket_a and fruit_b is from basket_b'

    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search the file named index.html under templates folder
    return render_template('index.html', sql_table = log, log_html = logMessage, table_title=col_names)


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

