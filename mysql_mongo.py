from debugpy import is_client_connected
import pymongo
from pymongo import MongoClient
import mysql.connector as msql
from mysql.connector import Error
import pandas as pd
from scipy import cluster
from sqlalchemy import column

try:
    connection = msql.connect(host='localhost',database='mt_db',user='root',password='root')  # noqa: E501
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print('Connnected to Mysql server version',db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You are connected to database:",record)
        mycursor = connection.cursor()
        mycursor.execute("Select * from branch")
        rows = mycursor.fetchall()
        print(rows)

except Error as e:
    print('Error in connecting to MYSql',e)

finally:
    if connection.is_connected():
        cursor.close()
        print('Mysql connection is closed')
df = pd.DataFrame(rows,columns=["bid","bname","bcity"])  # noqa: E501

#newdf=df.drop(columns=["atype","astatus"])
print(df)
cluster = pymongo.MongoClient("mongodb://localhost:27017")  # noqa: F811

db = cluster["testdb"]
collection = db["test1"]

x= collection.insert_many(df.to_dict('records'))
print(len(x.inserted_ids))
print(x)