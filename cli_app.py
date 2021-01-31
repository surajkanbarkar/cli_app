import psycopg2
from functools import reduce
#Establishing the connection
conn = psycopg2.connect(
   database="online_selling", user='online_user', password='123456789', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

class OnlineApp():
	def auth(username, password):
		cursor.execute("SELECT customer_id FROM customers WHERE username = '{}' AND password = '{}';".format(username, password))
		lst = [i for i in cursor.fetchall()]
		print("Authorized")
		return lst[0][0]
	def categories():
		cursor.execute("SELECT categorie_name FROM products")
		conn.commit()
		print(cursor.fetchall())
		return True
	def products(cat):
		cursor.execute("SELECT * FROM products where categorie_name = '{}'".format(cat))
		conn.commit()
		print(cursor.fetchall())
		return True
	def add_to_cart(pid, cid):
		cursor.execute("SELECT * FROM products where product_id = '{}'".format(pid))
		lst = [i for i in cursor.fetchall()]

		categorie_name = lst[0][1]
		product_name = lst[0][2]
		price = lst[0][3]
		description = lst[0][4]
		print(lst)
		
		cursor.execute("INSERT INTO cart (fk_customer_id, categorie_name, product_name, price, description) VALUES ('{}','{}','{}','{}', '{}')".format(cid, categorie_name, product_name, price, description))
		print('product added to cart.')
		conn.commit()
		return True

	def check_cart(cid):
		
		cursor.execute("SELECT cart_id, categorie_name, product_name, price, description FROM cart WHERE fk_customer_id = '{}'".format(cid))
		print(cursor.fetchall())
		conn.commit()
		return True

	def buy_products(cid, pid):
		lst = [id_ for id_ in pid.split(',')]
		cart_ele = []
		for i in lst:
			cursor.execute("SELECT cart_id, categorie_name, product_name, price, description FROM cart WHERE fk_customer_id = '{}' AND cart_id = '{}'".format(cid, i))
			[cart_ele.append(j) for j in cursor.fetchall()]
		print(cart_ele)
		actual_payable = reduce(lambda x,y: x+y, [pri[3] for pri in cart_ele])
		
		if actual_payable > 10000:
			payable = actual_payable - 500
			print("You got 500 OFF on your order \n the actual amount was {} \n final payable amount is {}".format(actual_payable, payable))
		else:
			print("final payable amount is {}".format(payable))
		conn.commit()
		return True
	

if __name__ == '__main__':
	
	u_name = input('username: ')
	cid = None
	while True:
		if u_name is not None:
			p_word = input('password: ')
		if u_name and p_word:
			cid = OnlineApp.auth(u_name, p_word)
			break	
	if cid is not None:
		print("Hint ---\nDo you want to see all categories(Y/n).\nplease type any category to see all products.")
		cat_true = input('Do you want to see all categories(Y/n): ')
		if cat_true in ('y', 'Y'):
			OnlineApp.categories()
	
			cat = input('please type any category: ')
			if cat:
				OnlineApp.products(cat)
		
				ele = input('Do you want to add any product to cart (<id>/n):')
				if ele != 'n':
					OnlineApp.add_to_cart(ele, cid)
				
		cart_true = input('Do you wish to check your cart (Y/n): ')
		if cart_true in ('y', 'Y'):
			OnlineApp.check_cart(cid)
			buy_pro = input("Type any id's to buy (seperated by comma please): ")
			if buy_pro not in (None, ''):
				OnlineApp.buy_products(cid, buy_pro)
	
	conn.close()

