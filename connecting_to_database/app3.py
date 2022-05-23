from tkinter import *
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
#########################
# shahbaz3535s@gmail.com
# s3y5e3d5
# AF95360374
# po57ted


root = Tk()
root.title('Parking-Charge-Notice Payer')
root.geometry("475x450")
root.configure(bg="light blue")
# below will add an icon on the top left of the application
root.iconbitmap("C:/Users/Administrator/Documents/Dissertation/connecting_to_database/parking-meter.ico")

FinalEmailAddress = ''
FinalPassword = ''
PCN_Number = ''
message_LabelC = Label(root, text="Details are being processed...", bg="light blue")
message_LabelA = Label(root, text="Error: User Email Address is Empty !!!", bg="light blue")
message_LabelB = Label(root, text="Error: User Password is Empty !!!", bg="light blue")
noUserFoundLabel = Label(root, text="No User Found With These Details", bg="Light Blue")
userFoundLabel = Label(root, text="User Found", bg="Light Blue")
pcnFailLabel = Label(root, text="Error: PCN Number is Empty ", padx=50, pady=10, bg="Light Blue")
regFailLabel = Label(root, text="Error: Car Registration empty ", padx=50, pady=10, bg="Light Blue")
automationLabel = Label(root, text="The Automation will begin shortly... ", padx=50, pady=10, bg="Light Blue")
# frame = LabelFrame(root, text="Error Message...", padx=10, pady=10)
finalMessageLabel = Label(root, text='', bg="Light Blue")

# import unittest
# from appium import webdriver

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
startURL = 'https://my.redbridge.gov.uk/parkingpcn/'
currentURL = startURL
auto_refNo = ''
auto_numberPlate = ''
auto_name_on_card = ''
auto_card_number = ''
auto_expiry_month = ''
auto_expiry_year = ''
auto_cvv_number = ''
auto_name = ''
auto_email_address = ''
error = ''
current_error = ''
driver = ''

verifyErrorsCount = 0

"""
tB_First_Name = ''
tB_Second_name = ''
tB_Email_Address = ''
tB_Account_Password = ''
tB_Postcode = ''
tB_Door_Number = ''
tB_County = ''
tB_Country = ''
tB_16_Digits = ''
tB_Expiry1 = ''
tB_Expiry2 = ''
tB_CVV = ''
tB_CardHolderName = ''
"""


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
    global auto_refNo
    global auto_numberPlate
    global auto_card_number
    global auto_name_on_card
    global auto_cvv_number
    global auto_email_address
    global auto_expiry_month
    global auto_expiry_year
    global auto_name
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
            noUserFoundLabel.grid(row=8, column=0)
        else:
            # print(accountID)
            auto_email_address = email
            print(auto_email_address)
            final_password = password
            print(final_password)
            noUserFoundLabel.grid_remove()
            userFoundLabel.grid(row=8, column=0)
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
        try:
            cardID = cardDetails[0]
            print("Card ID: "), print(cardID)
            auto_card_number = cardDetails[1]
            print("16 Digits: " + auto_card_number)
            auto_expiry_month = cardDetails[2]
            print("Expiry 1: " + auto_expiry_month)
            auto_expiry_year = cardDetails[3]
            print("Expiry 2: " + auto_expiry_year)
            auto_cvv_number = cardDetails[4]
            print("CVV: " + auto_cvv_number)
            auto_name_on_card = cardDetails[5]
            print("CardHolder Name: " + auto_name_on_card)
        except IndexError:
            pass


    except mysql.connector.errors.ProgrammingError:
        print("Connection to Database Failed")


def loginFunction():
    userEmail = emailTextBox.get()
    userPassword = passwordTextBox.get()
    if userEmail == '':
        message_LabelA.grid(row=6, column=0)
        noUserFoundLabel.grid_remove()
        userFoundLabel.grid_remove()
    else:
        message_LabelA.grid_remove()
    if userPassword == '':
        message_LabelB.grid(row=7, column=0)
        noUserFoundLabel.grid_remove()
        userFoundLabel.grid_remove()
    else:
        message_LabelB.grid_remove()
    if userEmail != '' and userPassword != '':
        message_LabelC.grid(row=6, column=0)
        getCardDetails(userEmail, userPassword)

    else:
        message_LabelC.grid_remove()


def page2():
    message_LabelC.grid_remove()
    userFoundLabel.grid_remove()
    page2LabelA = Label(root, text=" Pay For Parking Charge Notice ", padx=50, pady=10, bg="Light Blue").grid(row=1,
                                                                                                              column=0)
    pcnLabel = Label(root, text=" Enter Full PCN Number Below: ", padx=50, pady=10, bg="Light Blue").grid(row=2,
                                                                                                          column=0)

    pcnTextBox = Entry(root, width=50, borderwidth=4)
    pcnTextBox.grid(row=3, column=0, padx=50, pady=10)

    regLabel = Label(root, text=" Enter Car Registration Without Spaces: ", padx=50, pady=10, bg="Light Blue").grid(
        row=4, column=0)
    regTextBox = Entry(root, width=50, borderwidth=4)
    regTextBox.grid(row=5, column=0, padx=50, pady=10)

    submitButton = Button(root, text=" Submit ", width=15,
                          command=lambda: submission(pcnTextBox.get(), regTextBox.get()), fg="black", bg="light pink")
    submitButton.grid(row=6, column=0, padx=50, pady=15)


def submission(PCN, reg):
    print("PCN: " + PCN + "    , REG: " + reg)
    auto_ref_no = PCN
    auto_number_plate = reg
    if auto_ref_no == '':
        pcnFailLabel.grid(row=7, column=0)
    else:
        pcnFailLabel.grid_remove()
    if auto_number_plate == '':
        regFailLabel.grid(row=8, column=0)
    else:
        regFailLabel.grid_remove()
    if auto_ref_no != '' and auto_number_plate != '':
        pcnFailLabel.grid_remove()
        regFailLabel.grid_remove()

        # this is where all details from database will be gathered and the automation will begin
        automation(auto_ref_no, auto_number_plate)


def automation(x, y):
    print("Automation stage for redbridge website")
    automationLabel.grid(row=8, column=0)
    global driver
    driver = webdriver.Chrome()
    driver.get(startURL)

    inputPCNBox = driver.find_element(by=By.XPATH, value='//*[@id="Pcn"]')
    # the box below is where the reference number will go automatically
    inputPCNBox.send_keys(x)
    inputRegNoBox = driver.find_element(by=By.XPATH, value='//*[@id="Vrn"]')
    inputRegNoBox.send_keys(y)
    searchButton1 = driver.find_element(by=By.XPATH,
                                        value='//*[@id="formsubmitpcnsearch"]/div/div/div/div/div/div/div[3]/input[2]')
    driver.implicitly_wait(1)
    searchButton1.click()
    current_url = driver.current_url
    print()
    if startURL == current_url:
        error = "PCN number or vehicle Registration not entered"
        errorChecker(error)
    else:
        """
        try:
            driver.find_element(by=By.XPATH, value='//*[@id="Pcn"]').is_displayed()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        """

        try:
            if driver.find_element(by=By.XPATH, value='//*[@id="Pcn"]').is_displayed():
                print("Error, Still On Page 1: ")
                current_error = driver.find_element(by=By.XPATH, value='//*[@id="MainSection"]/div[3]').text
                errorChecker(current_error)
                print()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        print("on to page 2, No Errors on page 1")
        print()
    try:
        try:
            price = driver.find_element(by=By.XPATH, value='//*[@id="one"]/p/strong').text
            print(price)
        except selenium.common.exceptions.NoSuchElementException:
            pass
        infoContraventionDate = driver.find_element(by=By.XPATH,
                                                    value='//*[@id="one"]/div/div[1]/div/div/div[1]/ul/li[3]').text
        print(infoContraventionDate)
        infoContravention = driver.find_element(by=By.XPATH,
                                                value='//*[@id="one"]/div/div[1]/div/div/div[1]/ul/li[4]').text
        print(infoContravention)
        infoStreet = driver.find_element(by=By.XPATH, value='//*[@id="one"]/div/div[1]/div/div/div[1]/ul/li[5]').text
        print(infoStreet)
        infoLocation = driver.find_element(by=By.XPATH, value='//*[@id="one"]/div/div[1]/div/div/div[1]/ul/li[6]').text
        print(infoLocation)
        try:
            status = driver.find_element(by=By.XPATH, value='//*[@id="one"]/div/div/div/div/div[1]/ul/li[7]').text
            if status == 'Status: Fully Paid':
                errorChecker(status)
        except selenium.common.exceptions.NoSuchElementException:
            pass
            ##///////////////////////////////////////////////////////////////////////////////

            driver.implicitly_wait(2)

        payPCNButton = driver.find_element(by=By.XPATH, value='//*[@id="one"]/div/div[2]/div/div/div/div/a')
        payPCNButton.click()
        payPCNOnlineButton = driver.find_element(by=By.XPATH, value='//*[@id="pcn-pay-fines"]/p[2]/a')
        payPCNOnlineButton.click()
        # After clicking on the Payment button there is also a long wait
        checkoutButton = driver.find_element(by=By.XPATH, value='//*[@id="divShoppingBasketView"]/div[4]/div/div/a[1]')
        checkoutButton.click()
        nameOnCardBox = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_NameOnCard"]')
        nameOnCardBox.send_keys(auto_nameOnCard)
        cardNumberBox = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_CardNumber"]')
        cardNumberBox.send_keys(auto_cardNumber)
        expiryMonthBox = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_SelectedExpiryMonth"]')
        expiryMonthBox.send_keys(auto_expiryMonth)
        expiryYearBox = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_SelectedExpiryYear"]')
        expiryYearBox.send_keys(auto_expiryYear)
        cvcNumberBox = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_CSC"]')
        cvcNumberBox.send_keys(auto_cvvNumber)
        driver.implicitly_wait(1)

        checkoutSummaryButton = driver.find_element(by=By.XPATH, value='//*[@id="CheckOutSummary"]')
        checkoutSummaryButton.click()
        driver.implicitly_wait(2)
        try:
            if driver.find_element(by=By.XPATH, value='//*[@id="error-summary-titleitem-0"]').is_displayed():
                print("Payment Error, Still On Payment Page: ")
                current_error = driver.find_element(by=By.XPATH, value='//*[@id="error-summary-titleitem-0"]').text
                errorChecker(current_error)
                print()
        except selenium.common.exceptions.NoSuchElementException:
            pass
    except selenium.common.exceptions.InvalidSessionIdException:
        pass


def errorChecker(x):
    global finalMessageLabel
    error = x
    if error == '':
        print()
        print("No Errors")
        print()
    elif error != '':
        print()
        print(error)
        print("Error Has Been Found Exit Code Initiated")
        try:
            driver.close()
        except selenium.common.exceptions.NoSuchElementException:
            pass
        root.geometry("450x500")

        finalMessageLabel.config(text=error)
        # frame.grid(row=10, column=0)
        finalMessageLabel.grid(row=10, column=0, padx=10, pady=10)


def verify(x, y):
    global verifyErrorsCount
    if x == "Account_ID":
        pass
    if x == "First_Name":
        if y.isalpha() and y != '':
            print("First_Name is a string")
            return True
        else:
            print("First_Name is NOT a string")
            verifyErrorsCount = verifyErrorsCount + 1
            return False

    if x == "Second_name":
        if y.isalpha() and y != '':
            print("Second_name is a string")
            return True
        else:
            print("Second_name is NOT a string")
            verifyErrorsCount = verifyErrorsCount + 1
            return False

    if x == "Email_Address":
        pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if re.match(pat, y):
            print("correct Email Format")
            return True
        else:
            print("incorrect email format.")
            verifyErrorsCount = verifyErrorsCount + 1
            return False

    if x == "Password":
        if len(y) < 8:
            print("password length < 8; should be > 8 ")
            verifyErrorsCount = verifyErrorsCount + 1
            return False
        else:
            print("password length is fine")
            return True

    if x == "Postcode":
        pat = "^[A-Za-z0-9_\s]*$"
        if re.match(pat, y) and y != '':
            print("correct postcode Format")
            return True
        else:
            print("incorrect postcode format.")
            verifyErrorsCount = verifyErrorsCount + 1
            return False

    if x == "Door_Number":
        pat = "^[0-9_A-Za-z]*$"
        if re.match(pat, y) and len(y) <= 5 and y != '':
            print("Door Number is okay")
            return True
        else:
            print("Door Number is Incorrect")
            verifyErrorsCount = verifyErrorsCount + 1
            return False
    if x == "Street_Name":
        pat = "^[A-Za-z\s]*$"
        if y != '' and re.match(pat, y):
            print("Street is a string")
            return True
        else:
            print("Street is NOT a string")
            verifyErrorsCount = verifyErrorsCount + 1
            return False

    if x == "County":
        pat = "^[A-Za-z\s]*$"
        if y != '' and re.match(pat, y):
            print("County is a string")
            return True
        else:
            print("County is NOT a string")
            verifyErrorsCount = verifyErrorsCount + 1
            return False

    if x == "Country":
        pat = "^[A-Za-z\s]*$"
        if y != '' and re.match(pat, y):
            print("Country is a string")
            return True
        else:
            print("Country is NOT a string")
            verifyErrorsCount = verifyErrorsCount + 1
            return False

    if x == "16_Digits":
        if y.isnumeric() and len(y) == 16:
            print("correct 16 digit format")
            return True
        else:
            print("incorrect 16 digits")
            verifyErrorsCount = verifyErrorsCount + 1
            return False

    if x == "Expiry1":
        months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        if y.isnumeric() and len(y) == 2 and y in months:
            # print("expiry 1 ="+ y)
            print("correct Expiry1 format")
            return True
        else:
            print("incorrect Expiry1 format")
            verifyErrorsCount = verifyErrorsCount + 1
            return False

    if x == "Expiry2":
        if y.isnumeric() and len(y) == 2:
            print("correct Expiry2  format")
            return True
        else:
            print("incorrect Expiry2 format")
            verifyErrorsCount = verifyErrorsCount + 1
            return False

    if x == "CVV":
        if y.isnumeric() and len(y) == 3:
            print("correct CVV  format")
            return True
        else:
            print("incorrect CVV format")
            verifyErrorsCount = verifyErrorsCount + 1
            return False

    if x == "CardHolderName":
        pat = "^[A-Za-z_\s]*$"
        if re.match(pat, y) and y != '':
            print("CardHolderName is a string")
            return True
        else:
            print("CardHolderName is NOT a string")
            verifyErrorsCount = verifyErrorsCount + 1
            return False


def allAccountVerify(fn, sn, ea, ap, p, dn, streetname, county, country, digits16, e1, e2, cvv, chn):
    global verifyErrorsCount
    verifyErrorsCount = 0
    verify("First_Name", fn)
    verify("Second_name", sn)
    verify("Email_Address", ea)
    verify("Password", ap)
    verify("Postcode", p)
    verify("Door_Number", dn)
    verify("Street_Name", streetname)
    verify("County", county)
    verify("Country", country)
    verify("16_Digits", digits16)
    verify("Expiry1", e1)
    verify("Expiry2", e2)
    verify("CVV", cvv)
    verify("CardHolderName", chn)
    fNL = Label(top, text=" Correct ", bg="Light Green", fg="Black")
    sNL = Label(top, text=" Correct ", bg="Light Green", fg="Black")
    eAL = Label(top, text=" Correct ", bg="Light Green", fg="Black")
    passL = Label(top, text=" Correct ", bg="Light Green", fg="Black")
    postL = Label(top, text=" Correct ", bg="Light Green", fg="Black")
    dNL = Label(top, text=" Correct ", bg="Light Green", fg="Black")
    streetNL = Label(top, text=" Correct ", bg="Light Green", fg="Black")
    countyL = Label(top, text=" Correct ", bg="Light Green", fg="Black")
    countryL = Label(top, text=" Correct ", bg="Light Green", fg="Black")
    digitsL = Label(top, text=" Correct ", bg="Light Green", fg="Black")
    e1L = Label(top, text=" Correct ", bg="Light Green", fg="Black")
    e2L = Label(top, text=" Correct ", bg="Light Green", fg="Black")
    cvvL = Label(top, text=" Correct ", bg="Light Green", fg="Black")
    cHNL = Label(top, text=" Correct ", bg="Light Green", fg="Black")

    # fNL.grid_remove()
    fNL.grid(row=2, column=3, padx=15, pady=10)
    sNL.grid(row=3, column=3, padx=15, pady=10)
    eAL.grid(row=4, column=3, padx=15, pady=10)
    passL.grid(row=5, column=3, padx=15, pady=10)
    postL.grid(row=6, column=3, padx=15, pady=10)
    dNL.grid(row=7, column=3, padx=15, pady=10)
    streetNL.grid(row=8, column=3, padx=15, pady=10)
    countyL.grid(row=9, column=3, padx=15, pady=10)
    countryL.grid(row=10, column=3, padx=15, pady=10)
    digitsL.grid(row=11, column=3, padx=15, pady=10)
    e1L.grid(row=12, column=3, padx=15, pady=10)
    e2L.grid(row=13, column=3, padx=15, pady=10)
    cvvL.grid(row=14, column=3, padx=15, pady=10)
    cHNL.grid(row=15, column=3, padx=15, pady=10)

    print(verifyErrorsCount)
    if verifyErrorsCount > 0:
        if not verify("First_Name", fn):
            fNL.configure(text="       X       ", bg="Black", fg="Red")
        if not verify("Second_name", sn):
            sNL.configure(text="       X       ", bg="Black", fg="Red")
        if not verify("Email_Address", ea):
            eAL.configure(text="       X       ", bg="Black", fg="Red")
        if not verify("Password", ap):
            passL.configure(text="       X       ", bg="Black", fg="Red")
        if not verify("Postcode", p):
            postL.configure(text="       X       ", bg="Black", fg="Red")
        if not verify("Door_Number", dn):
            dNL.configure(text="       X       ", bg="Black", fg="Red")
        if not verify("Door_Number", dn):
            streetNL.configure(text="       X       ", bg="Black", fg="Red")
        if not verify("County", county):
            countyL.configure(text="       X       ", bg="Black", fg="Red")
        if not verify("Country", country):
            countryL.configure(text="       X       ", bg="Black", fg="Red")
        if not verify("16_Digits", digits16):
            digitsL.configure(text="       X       ", bg="Black", fg="Red")
        if not verify("Expiry1", e1):
            e1L.configure(text="       X       ", bg="Black", fg="Red")
        if not verify("Expiry2", e1):
            e2L.configure(text="       X       ", bg="Black", fg="Red")
        if not verify("CVV", cvv):
            cvvL.configure(text="       X       ", bg="Black", fg="Red")
        if not verify("CardHolderName", chn):
            cHNL.configure(text="       X       ", bg="Black", fg="Red")
    """
    if verifyErrorsCount == 0:
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
       
    """
        # will send data to database for storage


def new_account():
    global top
    top = Toplevel()
    top.geometry("685x725")
    top.iconbitmap("C:/Users/Administrator/Documents/Dissertation/connecting_to_database/parking-meter.ico")
    top.title("New Account Set Up")
    top.config(bg="Light pink")
    new_button_quit = Button(top, text="Exit", command=top.destroy, bg="RED")
    new_button_quit.grid(row=0, column=3)
    titleLabel = Label(top, text="NEW USER ACCOUNT SET UP", bg="Light Pink").grid(row=0, column=0, padx=50, pady=10)

    """
    tB_First_Name, tB_Second_name, tB_Email_Address, tB_Account_Password, tB_Postcode ,tB_Door_Number, tB_County, tB_Country, tB_16_Digits, tB_Expiry1 ,tB_Expiry2 ,tB_CVV, tB_CardHolderName
    """

    # label_Account_ID = Label(top, text=" ", bg="Light Pink").grid(row= 1, column=0, padx=15, pady=10)
    # tB_Account_ID = Entry(top, width=50, borderwidth= 4).grid(row= 1, column=2 , padx=15, pady=10)

    label_First_Name = Label(top, text="First Name: ", bg="Light Pink").grid(row=2, column=0, padx=15, pady=10)
    tB_First_Name = Entry(top, width=50, borderwidth=4)
    tB_First_Name.grid(row=2, column=2, padx=15, pady=10)

    label_Second_name = Label(top, text="Surname: ", bg="Light Pink").grid(row=3, column=0, padx=15, pady=10)
    tB_Second_name = Entry(top, width=50, borderwidth=4)
    tB_Second_name.grid(row=3, column=2, padx=15, pady=10)

    label_Email_Address = Label(top, text="Email Address: ", bg="Light Pink").grid(row=4, column=0, padx=15, pady=10)
    tB_Email_Address = Entry(top, width=50, borderwidth=4)
    tB_Email_Address.grid(row=4, column=2, padx=15, pady=10)

    label_Account_Password = Label(top, text="Password: ", bg="Light Pink").grid(row=5, column=0, padx=15, pady=10)
    tB_Account_Password = Entry(top, width=50, borderwidth=4)
    tB_Account_Password.grid(row=5, column=2, padx=15, pady=10)

    label_Postcode = Label(top, text="Postcode: ", bg="Light Pink").grid(row=6, column=0, padx=15, pady=10)
    tB_Postcode = Entry(top, width=50, borderwidth=4)
    tB_Postcode.grid(row=6, column=2, padx=15, pady=10)

    label_Door_Number = Label(top, text="Door Number: ", bg="Light Pink").grid(row=7, column=0, padx=15, pady=10)
    tB_Door_Number = Entry(top, width=50, borderwidth=4)
    tB_Door_Number.grid(row=7, column=2, padx=15, pady=10)

    label_Street_Name = Label(top, text="Street Name: ", bg="Light Pink").grid(row=8, column=0, padx=15, pady=10)
    tB_Street_Name = Entry(top, width=50, borderwidth=4)
    tB_Street_Name.grid(row=8, column=2, padx=15, pady=10)

    label_County = Label(top, text="County: ", bg="Light Pink").grid(row=9, column=0, padx=15, pady=10)
    tB_County = Entry(top, width=50, borderwidth=4)
    tB_County.grid(row=9, column=2, padx=15, pady=10)

    label_Country = Label(top, text="Country: ", bg="Light Pink").grid(row=10, column=0, padx=15, pady=10)
    tB_Country = Entry(top, width=50, borderwidth=4)
    tB_Country.grid(row=10, column=2, padx=15, pady=10)

    label_16_Digits = Label(top, text="Card Number (16 Digits): ", bg="Light Pink").grid(row=11, column=0, padx=15,
                                                                                         pady=10)
    tB_16_Digits = Entry(top, width=50, borderwidth=4)
    tB_16_Digits.grid(row=11, column=2, padx=15, pady=10)

    label_Expiry1 = Label(top, text="Expiry Month (2 Digits) : ", bg="Light Pink").grid(row=12, column=0, padx=15,
                                                                                        pady=10)
    tB_Expiry1 = Entry(top, width=50, borderwidth=4)
    tB_Expiry1.grid(row=12, column=2, padx=15, pady=10)

    label_Expiry2 = Label(top, text="Expiry Year (2 Digits): ", bg="Light Pink").grid(row=13, column=0, padx=15,
                                                                                      pady=10)
    tB_Expiry2 = Entry(top, width=50, borderwidth=4)
    tB_Expiry2.grid(row=13, column=2, padx=15, pady=10)

    label_CVV = Label(top, text="CVV Number (3 Digits):  ", bg="Light Pink").grid(row=14, column=0, padx=15, pady=10)
    tB_CVV = Entry(top, width=50, borderwidth=4)
    tB_CVV.grid(row=14, column=2, padx=15, pady=10)

    label_CardHolderName = Label(top, text="Cardholder Name (as on card): ", bg="Light Pink").grid(row=15, column=0,
                                                                                                   padx=15, pady=10)
    tB_CardHolderName = Entry(top, width=50, borderwidth=4)
    tB_CardHolderName.grid(row=15, column=2, padx=15, pady=10)

    button_details_Submit = Button(top, text="Submit Account Details",
                                   command=lambda: allAccountVerify(tB_First_Name.get(), tB_Second_name.get(),
                                                                    tB_Email_Address.get(), tB_Account_Password.get(),
                                                                    tB_Postcode.get(), tB_Door_Number.get(),
                                                                    tB_Street_Name.get(), tB_County.get(),
                                                                    tB_Country.get(), tB_16_Digits.get(),
                                                                    tB_Expiry1.get(),
                                                                    tB_Expiry2.get(), tB_CVV.get(),
                                                                    tB_CardHolderName.get()), bg="Light Green")
    button_details_Submit.grid(row=16, column=2, padx=15, pady=10)

    # , tB_Second_name.get(), tB_Email_Address.get(), tB_Account_Password.get(), tB_Postcode.get(),tB_Door_Number.get(), tB_County.get(), tB_Country.get(), tB_16_Digits.get(), tB_Expiry1.get(), tB_Expiry2.get(), tB_CVV.get(), tB_CardHolderName.get()


emailLabel = Label(root, text="Enter User Email: ", bg="light blue")
emailLabel.grid(row=0, column=0, padx=25, pady=10)
emailTextBox = Entry(root, width=50, borderwidth=4)
emailTextBox.grid(row=1, column=0, padx=25)

passwordLabel = Label(root, text="Enter User Password: Not Caps Sensitive", bg="light blue")
passwordLabel.grid(row=3, column=0, padx=25, pady=10)
passwordTextBox = Entry(root, width=50, borderwidth=4)
passwordTextBox.grid(row=4, column=0, padx=25)

loginButton = Button(root, text=" Login ", width=15, command=loginFunction, fg="black", bg="light pink")
loginButton.grid(row=5, column=0, padx=25, pady=15)

button_quit = Button(root, text="Exit", command=root.quit, bg="RED")
button_quit.grid(row=0, column=1, pady=5)

new_account_button = Button(root, text="New User", command=new_account, bg="Light Pink")
new_account_button.grid(row=1, column=1, pady=5)

"""
verify("First_Name", "shahbaz")
verify("Second_name", "syed")
verify("Email_Address", "shahbaz3535s@gmail.com")
verify("Password", "shahbaz123")
verify("Postcode", "ebw")
verify("Door_Number", "5545a")
verify("Country", "ebw")
verify("County", "ebw")
verify("16_Digits", "4658587893730047")
verify("Expiry1", "07")
verify("Expiry2", "29")
verify("CVV", "4444")
verify("CardHolderName", "shah a")
"""
root.mainloop()
