import yaml
import mysql.connector
import pandas as pd

# db = yaml.safe_load(open('config.yaml'))
db = yaml.safe_load(open('config_mrtssales.yaml'))

config = {
    'user' : db['user'],
    'host' : db['host'],
    'database': db['database'],
    'password' : db['password'], 
    'auth_plugin' : 'mysql_native_password'
}

def execute_sql_logic(_query):
    """
        This functions implements the DQL logic i.e., it runs SQL statements. 
        It takes one input as an argument:
            _query: a string of an SQL query
    """

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    # cursor = connection.cursor( buffered=True , dictionary=True)
    # _query = f'select * from actor limit 5;'
    cursor.execute(_query)

    columns = [col[0] for col in cursor.description]
    frame = [dict(zip(columns,row)) for row in cursor.fetchall()]

    df = pd.DataFrame(frame)
    # df.set_index(df.columns[0], inplace=True)
    cursor.close()
    connection.close()

    return df

  
