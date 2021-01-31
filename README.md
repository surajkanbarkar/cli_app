# User guide for admin and users

# Admin
I am using linux system so this app will be compatible for all linux.
python version: Python 3.6.9

# Step 1:
	clone or download the git repository

	Installation instructions

	$ sudo apt-get update
	$ sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib

	Now configure the CLI app

	$ chmod +x create_db.sh
	$ ./create_db.sh

	to create all tables run
	$ python3 create_tables.py

	All set :)
	now you can use the app

# Step 2:
	Add users
	you need to run
	$ python add_users.py
	for admin type 
	username = <username>
	password = <password>
	superuser = <y>
	'y' for superuser and 'n' for customers

# Step 3:
	for admin interface run
	$ python3 admin.py

	Now go with the flow

	login as superuser
	username: 
	password:
	Do you wish to add new user (Y/n):
	Do you want to add new product (Y/n) ?:
	Do you want to check cart ? (Y/n): 

# Customer

# Step 1:
	Run cli_app.py
	$ python3 cli_app.py
	Do you want to see all categories(Y/n): 
	please type any category: 
	Do you want to add any product to cart (<id>/n):
	Do you wish to check your cart (Y/n):
	Type any id's to buy (seperated by comma please): 


# cli_app
