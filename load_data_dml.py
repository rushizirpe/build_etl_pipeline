import yaml
import mysql.connector


db = yaml.safe_load(open('config.yaml'))

config = {
    'user' : db['user'],
    'host' : db['host'],
    'password' : db['password'], 
    'auth_plugin' : 'mysql_native_password'
}

def execute_dml_logic(_business_kind, _month, _amount_million):
    """
        This functions implements the DML logic i.e., it it inserts the records in a table.
        
        It takes three arguments as an input:
            _business_kind: Kind or type of business
            _month: A month if yyyy-mm-dd format
            _amount_million: dollar amount in millions a business has made in a given month

    """

    connection = mysql.connector.connect(**config)
    connection.autocommit = True
    cursor = connection.cursor()

    query = f"""
                USE `mrtssales`;
                INSERT INTO `estimate_of_monthly_retail_and_food_services_sales` (business_kind, month, amount_million)
                VALUES("{_business_kind}", "{_month}", "{_amount_million}");   
            """
    cursor.execute(query)
    cursor.close()
    connection.close()
