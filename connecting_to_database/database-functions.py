import mysql.connector
import string


def connect():
    try:
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
    except mysql.connector.errors.ProgrammingError:
        print("Connection to Database Failed")


# //////////////////////////////////////////////////////////////////////////
connect()
# //////////////////////////////////////////////////////////////////////////



def getCardDetails(x, y):
    email = x
    password = y
    cardDetails = []
    accountID = "0"
    try:
        mydb = mysql.connector.connect(host="localhost",
                                       user="root",
                                       passwd="S3y5e3d5",
                                       database="pcndb",
                                       auth_plugin="mysql_native_password")

        mycursor = mydb.cursor()

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
            # print(accountID)
            print()
        mycursor.execute("SELECT * FROM pcndb.paymentdetails where AccountsAccount_ID = '{}';".format(accountID))
        for y in mycursor:
            cardDetails = y
        # print(cardDetails)

        cardID = cardDetails[0]
        print("Card ID: "), print(cardID)
        digits16 = cardDetails[1]
        print("16 Digits: " + digits16)
        expiry1 = cardDetails[2]
        print("Expiry 1: " + expiry1)
        expiry2 = cardDetails[3]
        print("Expiry 2: " + expiry2)
        cvv = cardDetails[4]
        print("CVV: " + cvv)

        mydb.close
    except mysql.connector.errors.ProgrammingError:
        print("Connection to Database Failed")


# //////////////////////////////////////////////////////////////////////////
getCardDetails("shahbaz3535s@gmail.com", "S3y5e3d5")
# //////////////////////////////////////////////////////////////////////////
