import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from TestData.ConfirmPageData import ConfirmPageData
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self, getData):
        log = self.getLogger()
        self.driver.implicitly_wait(4)
        homepage = HomePage(self.driver)
        homepage.shopItems().click()
        checkOutPage = CheckoutPage(self.driver)
        log.info("getting all the  card titles")
        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == getData[0]:
                checkOutPage.getCardFooter()[i].click()
        time.sleep(1)
        checkOutPage.navToCheckOut().click()
        checkOutPage.checkOutItems().click()
        confirmPage = ConfirmPage(self.driver)
        log.info("entering country name as United")
        confirmPage.locationSelection().send_keys(getData[1])
        self.verifyLinkPresence(getData[2])
        confirmPage.locationConfirm().click()
        confirmPage.agreeToTerms().click()
        confirmPage.submitOrder().click()
        success = confirmPage.successConfirm().text
        log.info("Text received  from  application is " +success)

        assert "Success! Thank you!" in success
        self.driver.refresh()

    @pytest.fixture(params=ConfirmPageData.test_ConfirmPage_data)
    def getData(self, request):
        return request.param
