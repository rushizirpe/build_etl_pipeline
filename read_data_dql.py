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
