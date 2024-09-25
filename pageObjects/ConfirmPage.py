from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self,driver):
        self.driver = driver

    locationField = (By.CSS_SELECTOR, "#country")
    location = (By.LINK_TEXT, "United States of America")
    agreeBtn = (By.XPATH, "//div[@class='checkbox checkbox-primary']/label")
    submit = (By.XPATH, "//input[@type='submit']")
    success = (By.CSS_SELECTOR, ".alert-success")

    def locationSelection(self):
        return self.driver.find_element(*ConfirmPage.locationField)

    def locationConfirm(self):
        return self.driver.find_element(*ConfirmPage.location)

    def agreeToTerms(self):
        return self.driver.find_element(*ConfirmPage.agreeBtn)

    def submitOrder(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def successConfirm(self):
        return self.driver.find_element(*ConfirmPage.success)
