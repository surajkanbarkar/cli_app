import psycopg2

#Establishing the connection
conn = psycopg2.connect(
   database="online_selling", user='online_user', password='123456789', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Doping EMPLOYEE table if already exists.
cursor.execute("DROP TABLE IF EXISTS customers CASCADE")

#Creating table as per requirement
sql ='''CREATE TABLE customers(
   customer_id INT GENERATED ALWAYS AS IDENTITY,
   PRIMARY KEY(customer_id),
   first_name VARCHAR(20),
   last_name VARCHAR(20),
   username VARCHAR(255) NOT NULL,
   password VARCHAR(255),
   super_user BOOLEAN NOT NULL
)'''
cursor.execute(sql)
cursor.execute("GRANT ALL PRIVILEGES ON TABLE customers TO online_user")
print("customers table created successfully........")

#Creating table as per requirement
cursor.execute("DROP TABLE IF EXISTS products")
sql ='''CREATE TABLE products(
   product_id INT GENERATED ALWAYS AS IDENTITY,
   PRIMARY KEY(product_id),
   categorie_name VARCHAR(255),
   product_name VARCHAR(255),
   price NUMERIC NOT NULL,
   description TEXT NOT NULL
)'''
cursor.execute(sql)
cursor.execute("GRANT ALL PRIVILEGES ON TABLE products TO online_user")
print("products table created successfully........")

print("preparing products table wait....")
#cursor.execute("\COPY products FROM '/home/suraj/projects/cli_app/categories.csv' DELIMITER ',' CSV HEADER")
#f = open('/home/suraj/projects/cli_app/categories.csv')
#cursor.copy_from(f, 'products', sep=',', columns=('category_name', 'product_name', 'price', 'description'))
#f.close()

#Creating table as per requirement
cursor.execute("DROP TABLE IF EXISTS cart")
sql ='''CREATE TABLE cart(
   cart_id INT GENERATED ALWAYS AS IDENTITY,
   PRIMARY KEY(cart_id),
   fk_customer_id INTEGER,
   categorie_name VARCHAR(255),
   product_name VARCHAR(255),
   price FLOAT NOT NULL,
   description TEXT NOT NULL
)'''
cursor.execute(sql)
cursor.execute("GRANT ALL PRIVILEGES ON TABLE cart TO online_user")
print("cart table created successfully........")

# adding foreign key to cart table
cursor.execute("ALTER TABLE cart ADD CONSTRAINT fk_customer FOREIGN KEY (fk_customer_id)  REFERENCES customers(customer_id);")
print("added foreign key to cart table successfully........")

#Creating table as per requirement
cursor.execute("DROP TABLE IF EXISTS payments")
sql ='''CREATE TABLE payments(
   payment_id INT GENERATED ALWAYS AS IDENTITY,
   PRIMARY KEY(payment_id),
   fk_customer_id INTEGER,
   product_name VARCHAR(255),
   price FLOAT NOT NULL
)'''
cursor.execute(sql)
cursor.execute("GRANT ALL PRIVILEGES ON TABLE payments TO online_user")
print("payments table created successfully........")

# adding foreign key to payments table
cursor.execute("ALTER TABLE payments ADD CONSTRAINT fk_customer FOREIGN KEY (fk_customer_id)  REFERENCES customers(customer_id);")
print("added foreign key to payments table successfully........")

#Closing the connection
conn.commit()
conn.close()
