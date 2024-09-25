import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("first name is "+getData["firstname"])
        homepage.enterName().send_keys(getData["firstname"])
        log.info("email is " + getData["email"])
        homepage.enterEmail().send_keys(getData["email"])
        log.info("password is " + getData["pass"])
        homepage.enterPassword().send_keys(getData["pass"])
        log.info("accepting terms")
        homepage.checkingBox().click()
        log.info("gender choice is "+ getData["gender"])
        homepage.selectGender()
        self.selectOptionByText(homepage.selectGender(), getData["gender"])
        log.info("submitting information")
        homepage.submitButton().click()
        successText = homepage.verifySuccess().text
        log.info("login success is " +successText)

        assert ("Success" in successText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getTestData("testcase2"))
    def getData(self, request):
        return request.param