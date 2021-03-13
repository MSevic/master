import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)


def initDatabase():
    sql = "CREATE DATABASE predictor;"
    sql += "CREATE TABLE GLD (" \
           "Date_entry DATE , " \
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
