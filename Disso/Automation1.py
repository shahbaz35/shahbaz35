from selenium import webdriver
from selenium.webdriver.common.by import By

# import unittest
# from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get(
    'https://www.civicaepay.co.uk/NewhamEstore/estore/default/Catalog/Index?catalogueItemReference=F0000008&showSingleProduct=True&recurringOnly=False')
# cmd input : python Automation1.py
refNo = 'PN40363890'
consentButton = driver.find_element(by=By.XPATH, value='//*[@id="cookiepolicy-buttons"]/input[1]')
consentButton.click()

searchBox = driver.find_element(by=By.XPATH, value='//*[@id="ItemDetails_AccountReference"]')
# the box below is where the reference number will go automatically
searchBox.send_keys(refNo)

searchButton1 = driver.find_element(by=By.XPATH, value='//*[@id="CatalogueItems_0__validate-button"]')
searchButton1.click()

# tell code to wait
driver.implicitly_wait(2)

driver.implicitly_wait(2)

addToBasketButton = driver.find_element(by=By.XPATH, value='//*[@id="CatalogueItems_0__add-to-basket"]')
addToBasketButton.click()

driver.implicitly_wait(2)
# basketButton = driver.find_element_by_xpath('//*[@id="basket-indicator"]/a[1]')
basketButton = driver.find_element(by=By.XPATH, value='//*[@id="basket-indicator"]/a[1]')
basketButton.click()

viewBasketButton = driver.find_element(by=By.XPATH, value='//*[@id="hideMe"]/div/div[1]/div/span[1]/a')
driver.implicitly_wait(2)
viewBasketButton.click()

driver.implicitly_wait(2)

price = driver.find_element(by=By.XPATH, value='//*[@id="lblAmountInRowValue"]').text
print('PENALTY CHARGE PAYMENT PRICE IS: ' + price)

driver.implicitly_wait(2)
checkout = driver.find_element(by=By.XPATH, value='//*[@id="divShoppingBasketView"]/div[4]/div/div/a[1]')
checkout.click()
nameOnCard = 's syed'
cardNumber = '4658587893730000'
expiry1 = '07'
expiry2 = '24'
cvcNumber = '091'
name = 'shahbaz'
buildingNumber = '35'
postcode = 'e6 1bw'
street = 'Elizabeth Road'
area = ''
town = ''
county = 'Newham'
country = 'United Kingdom'
emailAddress = '17ssyed@gmail.com'
mobileNumber = '07388834444'

nameOnCardBox = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_NameOnCard"]')
nameOnCardBox.send_keys(nameOnCard)
cardNumberBox = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_CardNumber"]')
cardNumberBox.send_keys(cardNumber)
expiry1Box = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_SelectedExpiryMonth"]')
expiry1Box.send_keys(expiry1)
expiry2Box = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_SelectedExpiryYear"]')
expiry2Box.send_keys(expiry2)
cvcNumberBox = driver.find_element(by=By.XPATH, value='//*[@id="CardDetailsModel_CSC"]')
cvcNumberBox.send_keys(cvcNumber)

enterAddressManualButton = driver.find_element(by=By.XPATH, value='//*[@id="lnkAddess"]')
enterAddressManualButton.click()

"""
postcodeAutoBox = driver.find_element(by=By.XPATH, value='//*[@id="SearchPostCode"]')
postcodeAutoBox.send_keys(postcode)
postcodeAutoButton = driver.find_element(by=By.XPATH, value='//*[@id="findAddress"]')
postcodeAutoButton.click()
driver.implicitly_wait(3)

addressDropDownBox = driver.find_element(by=By.XPATH, value='//*[@id="AddressesFound"]/option[19]')
addressDropDownBox.click()
"""

nameBox = driver.find_element(by=By.XPATH, value='//*[@id="AccountHolderName"]')
nameBox.send_keys(name)
buildingNumberBox = driver.find_element(by=By.XPATH, value='//*[@id="BuildingNumber"]')
buildingNumberBox.send_keys(buildingNumber)
postcodeBoxM = driver.find_element(by=By.XPATH, value='//*[@id="PostCode"]')
postcodeBoxM.send_keys(postcode)
streetBox = driver.find_element(by=By.XPATH, value='//*[@id="Street"]')
streetBox.send_keys(street)
areaBox = driver.find_element(by=By.XPATH, value='//*[@id="Area"]')
areaBox.send_keys(area)
townBox = driver.find_element(by=By.XPATH, value='//*[@id="Town"]')
townBox.send_keys()
countyBox = driver.find_element(by=By.XPATH, value='//*[@id="County"]')
countyBox.send_keys(county)
countryBox = driver.find_element(by=By.XPATH, value='//*[@id="Country"]')
countryBox.send_keys(country)
emailAddressBox = driver.find_element(by=By.XPATH, value='//*[@id="EmailAddress"]')
emailAddressBox.send_keys(emailAddress)
mobileNumberBox = driver.find_element(by=By.XPATH, value='//*[@id="TelephoneNumber"]')
mobileNumberBox.send_keys(mobileNumber)

# Checkout to summary button
# //*[@id="CheckOutSummary"]


# driver.quit() # this will close the browser at the end
