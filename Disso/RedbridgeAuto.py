import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import mysql.connector
import chromedriver_autoinstaller as chromedriver
chromedriver.install()

# import unittest
# from appium import webdriver

# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait

startURL = 'https://my.redbridge.gov.uk/parkingpcn/'
currentURL = startURL
driver = webdriver.Chrome()
driver.get(startURL)
# cmd input : python Automation1.py
refNo = 'AF88970670'
numberPlate = 'ky12zpz'
nameOnCard = 's syed'
cardNumber = '4658587893730047'
expiryMonth = '08'
expiryYear = '25'
cvcNumber = '091'
name = 'shahbaz'
emailAddress = '17ssyed@gmail.com'
mobileNumber = '07388834444'
error = ''
currentError = ''


def errorChecker(x):
    error = x
    if error == '':
        print()
        print("No Errors")
        print()
    elif error != '':
        print()
        print(error)
        print("Error Has Been Found Exit Code Initiated")
        # driver.quit()
        raise SystemExit(0)


inputPCNBox = driver.find_element(by=By.XPATH, value='//*[@id="Pcn"]')
# the box below is where the reference number will go automatically
inputPCNBox.send_keys(refNo)

inputRegNoBox = driver.find_element(by=By.XPATH, value='//*[@id="Vrn"]')
inputRegNoBox.send_keys(numberPlate)

searchButton1 = driver.find_element(by=By.XPATH,
                                    value='//*[@id="formsubmitpcnsearch"]/div/div/div/div/div/div/div[3]/input[2]')
driver.implicitly_wait(1)
searchButton1.click()

currentURL = driver.current_url

# print()
# print(startURL)
# https://my.redbridge.gov.uk/parkingpcn/
# https://my.redbridge.gov.uk/ParkingPCN
# print(currentURL)
print()

if startURL == currentURL:
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
            currentError = driver.find_element(by=By.XPATH, value='//*[@id="MainSection"]/div[3]').text
            errorChecker(currentError)
            print()
    except selenium.common.exceptions.NoSuchElementException:
        pass

    """
    if driver.find_element(by=By.XPATH, value='//*[@id="Pcn"]').is_displayed():
        print("Error, Still On Page 1: ")
        currentError = driver.find_element(by=By.XPATH, value='//*[@id="MainSection"]/div[3]').text
        errorChecker(currentError)
        print()
    """
    print("on to page 2, No Errors on page 1")
    print()

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# to go to the next page there is about a 15 to 20 second wait because the website is slow.
try:
    price = driver.find_element(by=By.XPATH, value='//*[@id="one"]/p/strong').text
    print(price)
except selenium.common.exceptions.NoSuchElementException:
    pass
infoContraventionDate = driver.find_element(by=By.XPATH, value='//*[@id="one"]/div/div[1]/div/div/div[1]/ul/li[3]').text
print(infoContraventionDate)
infoContravention = driver.find_element(by=By.XPATH, value='//*[@id="one"]/div/div[1]/div/div/div[1]/ul/li[4]').text
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
# tell code to wait
driver.implicitly_wait(2)

payPCNButton = driver.find_element(by=By.XPATH, value='//*[@id="one"]/div/div[2]/div/div/div/div/a')
payPCNButton.click()
payPCNOnlineButton = driver.find_element(by=By.XPATH, value='//*[@id="pcn-pay-fines"]/p[2]/a')
payPCNOnlineButton.click()
# After clicking on the Payment button there is also a long wait
checkoutButton = driver.find_element(by=By.XPATH, value='//*[@id="divShoppingBasketView"]/div[4]/div/div/a[1]')
checkoutButton.click()

nameOnCardBox = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_NameOnCard"]')
nameOnCardBox.send_keys(nameOnCard)
cardNumberBox = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_CardNumber"]')
cardNumberBox.send_keys(cardNumber)
expiryMonthBox = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_SelectedExpiryMonth"]')
expiryMonthBox.send_keys(expiryMonth)
expiryYearBox = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_SelectedExpiryYear"]')
expiryYearBox.send_keys(expiryYear)
cvcNumberBox = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_CSC"]')
cvcNumberBox.send_keys(cvcNumber)
driver.implicitly_wait(1)

checkoutSummaryButton = driver.find_element(by=By.XPATH, value='//*[@id="CheckOutSummary"]')
checkoutSummaryButton.click()
driver.implicitly_wait(2)

try:
    if driver.find_element(by=By.XPATH, value='//*[@id="error-summary-titleitem-0"]').is_displayed():
        print("Payment Error, Still On Payment Page: ")
        currentError = driver.find_element(by=By.XPATH, value='//*[@id="error-summary-titleitem-0"]').text
        errorChecker(currentError)
        print()
except selenium.common.exceptions.NoSuchElementException:
    pass

'''
confirmPayment = driver.find_element(by=By.XPATH, value='//*[@id="SubmitPayment"]')
confirmPayment.click()

try:
    if driver.find_element(by=By.XPATH, value='//*[@id="errorContainerId"]/h2').is_displayed():
        print('Payment has been made Successfully')
        receiptNumber = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div[2]/div[2]/div[1]/div[2]/div/div[1]').text
        print(receiptNumber)
        authCode = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div[2]/div[2]/div[1]/div[2]/div/div[2]').text
        print(authCode)
        cardType = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div[2]/div[2]/div[1]/div[2]/div/div[4]').text
        print(cardType)
        paymentDate = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/div[2]/div[2]/div[1]/div[2]/div/div[7]').text
        print(paymentDate)
        paymentReceivedFrom = driver.find_element(by=By.XPATH, value='//*[@id="Receipt-standard--detail-name"]').text
        print(paymentReceivedFrom)

        emailAddressBox = driver.find_element(by=By.XPATH, value='//*[@id="EmailAddress"]')
        emailAddressBox.send_keys(emailAddress)
        emailAddressButton = driver.find_element(by=By.XPATH, value='//*[@id="Receipt-standard-Email"]')
        emailAddressButton.click()

except selenium.common.exceptions.NoSuchElementException:
    currentError = 'Payment was not made Successfully'
    errorChecker(currentError)

'''
# paymentDetails = driver.find_element(by= By.XPATH, value='//*[@id="content"]/div/div[2]/div[2]/div[1]/div[2]/div')


# Checkout to summary button
# //*[@id="CheckOutSummary"]


# driver.quit() # this will close the browser at the end
