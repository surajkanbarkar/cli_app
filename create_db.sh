#!/bin/bash
echo Configuring Database...
#sudo -u postgres psql
#"CREATE DATABASE mytemplate1 WITH ENCODING 'UTF8' TEMPLATE template0"
sudo -u postgres psql -c "DROP DATABASE online_selling"
sudo -u postgres psql -c "CREATE DATABASE online_selling WITH ENCODING 'UTF8'"
echo Database created successfully...
sudo -u postgres psql -c "CREATE USER online_user WITH PASSWORD '123456789'"
sudo -u postgres psql -c "ALTER ROLE online_user SET client_encoding TO 'utf8'"
sudo -u postgres psql -c "ALTER ROLE online_user SET default_transaction_isolation TO 'read committed'"
sudo -u postgres psql -c "ALTER ROLE online_user SET timezone TO 'UTC'"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE online_selling TO online_user"

#sudo -u postgres psql online_selling -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SEQUENCES online_selling TO online_user;"
#sudo -u postgres psql online_selling -c "DROP TABLE IF EXISTS customers"
#sudo -u postgres psql online_selling -c "CREATE TABLE customers(customer_id INT GENERATED ALWAYS AS IDENTITY, PRIMARY KEY(customer_id), first_name VARCHAR(20), last_name VARCHAR(20), username VARCHAR(255) NOT NULL, password VARCHAR(255))"
#sudo -u postgres psql online_selling -c "GRANT ALL PRIVILEGES ON TABLE customers TO online_user"
