import yaml
import mysql.connector


db = yaml.safe_load(open('config.yaml'))

config = {
    'user' : db['user'],
    'host' : db['host'],
    'password' : db['password'], 
    'auth_plugin' : 'mysql_native_password'
}

def execute_ddl_logic(*args):
    """
        This functions implements the DDL logic i.e., it creates the database and table. 
        In our case the database and table are mrtssales and estimate_of_monthly_retail_and_food_services_sales,
    """
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    query = f"""
                DROP DATABASE IF EXISTS `mrtssales`;
                CREATE DATABASE IF NOT EXISTS `mrtssales`;

                USE `mrtssales`;
                
                DROP TABLE IF EXISTS `estimate_of_monthly_retail_and_food_services_sales`;
                CREATE TABLE IF NOT EXISTS `estimate_of_monthly_retail_and_food_services_sales` (
                `id`              INT NOT NULL AUTO_INCREMENT,
                `business_kind`   VARCHAR(100) NOT NULL,
                `month`           DATE NOT NULL,
                `amount_million`  FLOAT,
                PRIMARY KEY(`id`)

                )ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4 COLLATE=utf8mb4_0900_ai_ci;        
            """
    cursor.execute(query)
    cursor.close()
    connection.close()

    print('ddl logic is executed')

# connection.commit()
