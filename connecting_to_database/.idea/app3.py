from tkinter import *
import os
import mysql.connector

#########################

root = Tk()
root.title('PCN PAYER')
root.geometry("400x500")
root.configure(bg = "light blue")
#canvas = Canvas(root, height=50, width=600, bg="light blue")
#canvas.pack()

#frame = Frame(root, bg="light blue")
#frame.place(relwidth=0.8, relheight=0.85, relx=0.1, rely=0.1)
FinalEmailAddress = ''
FinalPassword= ''
PCN_Number= ''
message_LabelC = Label(root, text="Details are being processed...", bg = "light blue")
message_LabelA = Label(root, text="Error: User Email Address is Empty !!!", bg = "light blue")
message_LabelB = Label(root, text="Error: User Password is Empty !!!", bg = "light blue")
noUserFoundLabel = Label(root, text="No User Found With These Details", bg= "Light Blue")
userFoundLabel = Label(root, text="User Found", bg= "Light Blue")
PCNFailLabel = Label(root, text="Error: PCN Number is Empty ", padx = 50, pady = 10, bg= "Light Blue")
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
connect()

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
            userFoundLabel.grid_remove()
            noUserFoundLabel.grid(row= 8,column=0)
        else:
            # print(accountID)
            FinalemailAddress = email
            print(FinalemailAddress)
            FinalPassword = password
            print(FinalPassword)
            noUserFoundLabel.grid_remove()
            userFoundLabel.grid(row= 8,column=0)
            emailLabel.grid_remove()
            emailTextBox.grid_remove()
            passwordLabel.grid_remove()
            passwordTextBox.grid_remove()
            loginButton.grid_remove()
            page2()
            print()
        mycursor.execute("SELECT * FROM pcndb.paymentdetails where AccountsAccount_ID = '{}';".format(accountID))
        for y in mycursor:
            cardDetails = y
        # print(cardDetails)
        try :
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
            CHName = cardDetails[5]
            print("CardHolder Name: "+CHName)
        except IndexError:
            pass



        mydb.close
    except mysql.connector.errors.ProgrammingError:
        print("Connection to Database Failed")


def loginFunction():

    userEmail = emailTextBox.get()
    userPassword = passwordTextBox.get()
    if userEmail == '':
        message_LabelA.grid(row= 6,column= 0)
        noUserFoundLabel.grid_remove()
        userFoundLabel.grid_remove()
    else:
        message_LabelA.grid_remove()
    if userPassword == '':
        message_LabelB.grid(row= 7,column= 0)
        noUserFoundLabel.grid_remove()
        userFoundLabel.grid_remove()
    else:
        message_LabelB.grid_remove()
    if userEmail != '' and userPassword != '':
        message_LabelC.grid(row= 6,column= 0)
        getCardDetails(userEmail,userPassword)

    else:
        message_LabelC.grid_remove()


def page2():

    message_LabelC.grid_remove()
    userFoundLabel.grid_remove()
    page2LabelA = Label(root, text=" Pay For Parking Charge Notice ", padx = 50, pady = 10, bg= "Light Blue").grid(row=1, column=0)
    PCNLabel = Label(root, text=" Enter Full PCN Number Below: ", padx = 50, pady = 10, bg= "Light Blue").grid(row=2, column=0)

    PCNTextBox = Entry(root, width=50, borderwidth= 4)
    PCNTextBox.grid(row= 3,column=0, padx= 50, pady= 10)
    submitButton = Button(root, text=" Login ",width= 15,  command=lambda : submission(PCNTextBox.get()), fg = "black", bg = "light pink")
    submitButton.grid(row= 4,column= 0, padx= 50, pady= 15)



def submission(x):
    print("Submission")
    print("x == "+x)
    PCN_Tiket = x
    if PCN_Tiket == '':
        PCNFailLabel.grid(row=5, column=0)
    else:
        PCNFailLabel.grid_remove()
        # this is where all details from database will be gathered and the automation will begin



emailLabel = Label(root, text="Enter User Email: ", bg = "light blue")
emailLabel.grid(row= 0,column= 0, padx= 50, pady= 10)
emailTextBox = Entry(root, width=50, borderwidth= 4)
emailTextBox.grid(row= 1,column= 0, padx= 50)

passwordLabel = Label(root, text="Enter User Password: Not Caps Sensetive", bg = "light blue")
passwordLabel.grid(row= 3,column= 0, padx= 50, pady= 10)
passwordTextBox = Entry(root, width=50, borderwidth= 4)
passwordTextBox.grid(row= 4,column= 0, padx= 50)

loginButton = Button(root, text=" Login ",width= 15,  command=loginFunction, fg = "black", bg = "light pink")
loginButton.grid(row= 5,column= 0, padx= 50, pady= 15)

root.mainloop()
