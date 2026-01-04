import mysql.connector
import pandas as pd
conn = mysql.connector.connect(host = 'localhost' , user = 'root' , password='' , database = 'world')
df = pd.read_sql_query('SELECT * FROM city where CountryCode = "USA"' , conn)
print(df.head())