# Homework 3: 
This project shows how we can connect PostgreSQL with flask to update a table, basket_a, and show unique values between two tables, basket_a and basket_b

## Team Members: 
Sofia Azam

## Quick Start
### Local Test Setup
First, we need to install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```
Because we are now inside a virtual environment. We do not need sudo.

Then you can start the server with:
```
python3 main.py
```

Once you have that running, go to the following link in your web browser to update basket_a with a row that has the values (5, 'Cherry')
```
http://127.0.0.1:5000/api/update_basket_a 
```
It will give you an error if you try to run that link in your web browser again since it's already been added to the table.

You can also go to this following link in your web browser to show all the unique values in basket_a and basket_b
```
http://127.0.0.1:5000/api/unique
```

