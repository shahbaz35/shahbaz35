



from tkinter import *
from tkinter import ttk
# import os
import mysql.connector
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
import chromedriver_autoinstaller as chromedriver
import re

chromedriver.install()

def connect():


    try:
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="S3y5e3d5",
                                       database="pcndb",
                                       auth_plugin="mysql_native_password")

        mycursor = mydb.cursor()
        mycursor.execute("select * from pcndb.accounts;")
        for x in mycursor:
            print(x)


        print(mydb)
        if mydb:
            print("-Successful ")
        else:
            print("-Unsuccessful ")
    except mysql.connector.errors.ProgrammingError:
        print("Connection to Database Failed")


connect()




def send_details():

    try:
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="S3y5e3d5",
                                       database="pcndb",
                                       auth_plugin="mysql_native_password")

        mycursor = mydb.cursor()

        mycursor.execute(
            "insert into pcndb.accounts(First_Name, Second_Name,Email_Address,Account_Password, Phone_Number, Postcode, Door_Number, Street_Name, County, Country) VALUES ( 'sofiya', 'sayed', 'thehagisback@gmail.com', 's3y5e3d5', '07824777747', 'e6 1bw', '35', 'elizabeth road', 'newham',  'united kingdom');"
        )
        mydb.commit()

        connect()
        #print("INSERT INTO pcndb.accounts(First_Name, Second_Name,Email_Address,Account_Password, Phone_Number, Postcode, Door_Number, Street_Name, County, Country) VALUES ( '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');".format(fn, sn, ea, ap, pn, p, dn, streetname, county, country))

    except mysql.connector.errors.ProgrammingError:
        print("Connection to Database Failed")


