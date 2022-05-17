# import os
# import numpy as np
# import pandas as pd
# from matplotlib import pyplot as plt
# import seaborn as sns

import mysql.connector

email = "shahbaz3535s@gmail.com"
password = "S3y5e3d5"
accountID = "0"
cardDetails = []
try:

    print("hello")
    mydb = mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="S3y5e3d5",
                                   database="pcndb",
                                   auth_plugin="mysql_native_password")
    print(mydb)
    if mydb:
        print("-Successful ")
    else:
        print("-Unsuccessful ")
    print()
    mycursor = mydb.cursor()
    # mycursor.execute("show tables in pcndb")
    # for db in mycursor:
    # print(db)
    # print()

    # mycursor.execute("select * from pcndb.accounts;")
    # for x in mycursor:
    # print(x)
    # print()
    mycursor.execute(
        "select Account_ID from pcndb.accounts where Email_Address = '{}' and Account_Password = '{}'".format(email,
                                                                                                              password))
    for x in mycursor:
        # print('////////')
        accountID = x

    accountID = accountID[0]
    if accountID == "0":
        print("User Not Found With These Details {}, {}".format(email, password))
    else:
        print(accountID)

    print()
    mycursor.execute("SELECT * FROM pcndb.paymentdetails where AccountsAccount_ID = '{}';".format(accountID))
    for y in mycursor:
        cardDetails = y
    #print(cardDetails)



except mysql.connector.errors.ProgrammingError:
    print("Connection to Database Failed")
print("///////")
cardID = cardDetails[0]
print(cardID)
digits16 = cardDetails[1]
print(digits16)
expiry1 = cardDetails[2]
print(expiry1)
expiry2 = cardDetails[3]
print(expiry2)
cvv = cardDetails[4]
print(cvv)

mydb.close