from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    navButton = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    checkOut = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckoutPage.cardFooter)

    def navToCheckOut(self):
        return self.driver.find_element(*CheckoutPage.navButton)

    def checkOutItems(self):
        return self.driver.find_element(*CheckoutPage.checkOut)

