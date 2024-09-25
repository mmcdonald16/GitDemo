from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    def __init__(self, driver):  # this is a constructor that defines driver for any  test using  HomePage class
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    nameField = (By.CSS_SELECTOR, "[name='name']")
    emailField = (By.CSS_SELECTOR, "[name='email']")
    passwordField = (By.CSS_SELECTOR, "#exampleInputPassword1")
    checkBox = (By.CSS_SELECTOR, "#exampleCheck1")
    dropDown = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@class='btn btn-success']")
    alertText = (By.CSS_SELECTOR, ".alert-success")

    def enterName(self):
        return self.driver.find_element(*HomePage.nameField)

    def enterEmail(self):
        return self.driver.find_element(*HomePage.emailField)

    def enterPassword(self):
        return self.driver.find_element(*HomePage.passwordField)

    def checkingBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def selectGender(self):
        return self.driver.find_element(*HomePage.dropDown)

    def submitButton(self):
        return self.driver.find_element(*HomePage.submit)

    def verifySuccess(self):
        return self.driver.find_element(*HomePage.alertText)

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)  # you need to use the * for it to recognize the tuple
