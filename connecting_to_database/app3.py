from tkinter import *
# import os
import mysql.connector
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
import chromedriver_autoinstaller as chromedriver

chromedriver.install()
#########################

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


# AF95360374
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

        # driver.quit()
        # raise SystemExit(0)


def new_account():
    top = Toplevel()
    top.geometry("400x600")
    top.iconbitmap("C:/Users/Administrator/Documents/Dissertation/connecting_to_database/parking-meter.ico")
    top.title("New Account Set Up")
    top.config(bg="Light pink")
    new_button_quit = Button(top, text="Exit", command=top.quit)
    new_button_quit.grid(row=0, column=1)
    titleLabel = Label(top, text="NEW USER ACCOUNT SET UP", bg= "Light Pink").grid(row=0, column=0, padx=50, pady=10)
    """
    label_
    label_
    label_
    label_
    label_
    label_
    label_
    label_
    label_
    label_
    label_
    label_
    label_
    label_
    label_
    """











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

button_quit = Button(root, text="Exit", command=root.quit)
button_quit.grid(row=0, column=1, pady=5)

new_account_button = Button(root, text="New User", command= new_account)
new_account_button.grid(row=1, column=1, pady=5)

root.mainloop()
