import mysql.connector
from sqlalchemy import create_engine
mydb = create_engine('mysql+pymysql://root:password@database:3306/mysql')



def initDatabase():
    sql = "DROP DATABASE IF EXISTS predictor"
    sql += "CREATE DATABASE predictor;"
    sql += " USE predictor;"
    for table in ['GLD']:
        sql += "CREATE TABLE " + table + \
               " (Date_entry DATE , " \
               "Close FLOAT(20) DEFAULT NULL ," \
               "High FLOAT(20) DEFAULT NULL , " \
               "Low FLOAT(20) DEFAULT NULL , " \
               "Volume FLOAT(20) DEFAULT NULL , " \
               "S_3 FLOAT(20) DEFAULT NULL , " \
               "S_9 FLOAT(20) DEFAULT NULL , " \
               "deaths FLOAT(20) DEFAULT NULL , " \
               "cases FLOAT(20) DEFAULT NULL , " \
               "D_7 FLOAT(20) DEFAULT NULL , " \
               "C_7 FLOAT(20) DEFAULT NULL );"
        i = 0
        sql += "ALTER TABLE GLD"
        while i <= 15:
            i += 1
            sql += "ADD COLUMN creal" + str(i) + " FLOAT(20) DEFAULT NULL ,"
            if i == 15:
                sql += "ADD COLUMN cpred" + str(i) + " FLOAT(20) DEFAULT NULL;"
            else:
                sql += "ADD COLUMN cpred" + str(i) + " FLOAT(20) DEFAULT NULL ,"

    mycursor = mydb.cursor()
    mycursor.execute(sql)
    mydb.commit()
