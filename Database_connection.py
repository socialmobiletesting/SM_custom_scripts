import mysql.connector

# mydb1 = mysql.connector.connect(host="localhost", user="root", passwd="Innominds@123")
# mycursor1 = mydb1.cursor()
# mycursor1.execute("show databases")
# for x in mycursor1:
#     print(x)

# Used to login mysql workspace
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Innominds@123", database='iq_connect')

# Taking variable mycursor to fetching mysql commands
mycursor = mydb.cursor()

# Executing mysql commands with help of mycursor variable so later can be iterate
mycursor.execute("show tables")

for i in mycursor:
    print(i)

# If I want to fetch one details
result = mycursor.fetchone()
# mycursor.execute("select * from Student")

# for i in result:
#     print(i)
