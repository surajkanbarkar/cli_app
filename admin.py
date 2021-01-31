import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="online_selling", user='online_user', password='123456789', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

class Admin():
	def auth(username=None, password=None):
		cursor.execute("SELECT customer_id FROM customers WHERE username = '{}' AND password = '{}';".format(username, password))
		lst = [i for i in cursor.fetchall()]
		conn.commit()
		if len(lst) > 0 and lst[0][-1] == 1:
			return True
		else:
			return False
		
	def add_user(first_name=None, last_name=None, username=None, password=None, super_user=None):
		print(first_name, last_name, username, password, super_user)
		sql = """INSERT INTO customers(first_name, last_name, username, password, super_user) VALUES (%s, %s, %s, %s, %s);"""
		cursor.execute(sql, (first_name, last_name, username, password,super_user))
		conn.commit()
		return True
	def add_product(categorie_name=None, product_name=None, price=None, description=None):
		sql = """INSERT INTO products(categorie_name, product_name, price, description) VALUES (%s, %s, %s, %s);"""
		cursor.execute(sql, (categorie_name, product_name, price, description))
		conn.commit()
		print(categorie_name, product_name, price, description)
		return True
	def check_products(cid=None, categorie_name=None, product_name=None):
		if cid == categorie_name == product_name == None:
			#sql = """SELECT * FROM products WHERE categorie_name = '{}'""".format(categorie_name)
			sql = """SELECT * FROM products"""
			cursor.execute(sql)
			print(cursor.fetchall())
			conn.commit()
			return True
		elif categorie_name:
			sql = """SELECT * FROM products WHERE categorie_name = '{}'""".format(categorie_name)
			cursor.execute(sql)
			print(cursor.fetchall())
			conn.commit()
			return True
		elif product_name:
			sql = """SELECT * FROM products WHERE product_name = '{}'""".format(product_name)
			cursor.execute(sql)
			print(cursor.fetchall())
			conn.commit()
			return True
	def check_cart():
		sql = """SELECT * FROM cart"""
		cursor.execute(sql)
		print(cursor.fetchall())
		conn.commit()
		return True


if __name__ == '__main__':
	print("Login as superuser")
	ad_u = input('username: ')
	if ad_u:
		ad_p = input('password: ')
		user = Admin.auth(ad_u, ad_p)
		if user == True:
			ad_u = input('Do you wish to add new user (Y/n): ')
			if ad_u in ('Y', 'y'):
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
			else:
				pr = input('Do you want to add new product (Y/n) ?: ')
				if pr in ('Y', 'y'):
					cat_name = input('categorie_name: ')
					pro_name = input('product_name: ')
					price = input('price: ')
					description = input('description: ')
					if cat_name and pro_name and price and description:
						Admin.add_product(cat_name, pro_name, price, description)
				ck = input('Do you want to check all product list ? (Y/n): ')
				if ck in ('Y', 'y'):
					Admin.check_products()
				
				crt = input('Do you want to check cart ? (Y/n): ')
				if crt in ('Y', 'y'):
					Admin.check_cart()
		else:
			print("Unauthorized :(")
	else:
		print("Unauthorized :(")
