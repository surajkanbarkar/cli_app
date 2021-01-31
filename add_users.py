#!/usr/bin/python

import psycopg2
import sys
from config import config

conn = psycopg2.connect(
   database="online_selling", user='online_user', password='123456789', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

def add_user(first_name, last_name, username, password, super_user):
	print(first_name, last_name, username, password, super_user)
	sql = """INSERT INTO customers(first_name, last_name, username, password, super_user) VALUES (%s, %s, %s, %s, %s);"""
	cursor.execute(sql, (first_name, last_name, username, password,super_user))
	conn.commit()
	#cursor.execute("SELECT * FROM customers;")
	return 'ok'

if __name__ == "__main__":
	#arg = sys.argv
	#if len(arg) > 1:
	#	print(arg)
	#	add_user(arg)
	#else:
	#	print("You need to specify the arguments <first_name> <last_name>")
	first_name = input('first name: ')
	while True:
		
		if first_name is not None and first_name != '':
			last_name = input('last name: ')
			if last_name is not None and last_name != '':
				username = input('username: ')
				if username is not None and username != '':
					password = input('password: ')
					if password is not None and password != '':
						super_user = input('super_user: ')
						if super_user:
							lst = [first_name, last_name, username, password, super_user]
						break
					else:
						print('password is required..')
						password = input('password: ')
				else:
					print('username is required..')
					username = input('username: ')
			else:
				print('last name is required..')
				last_name = input('last name: ')
			
		else:
			print('first name is required..')
			first_name = input('first name: ')
	add_user(lst[0], lst[1], lst[2], lst[3], lst[4])
#	else:

		
