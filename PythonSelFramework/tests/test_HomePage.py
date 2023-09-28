import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass

class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)

        # # open the website
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        log.info("First name is "+getData["firstname"])  # log
        homepage.getName().send_keys(getData["firstname"])
        # homepage.getName().send_keys("Subrata")

        homepage.getEmail().send_keys(getData["email"])
        # homepage.getEmail().send_keys("abc@de.com")

        homepage.getCheckbox().click()

        self.selectOptionByText(homepage.getGender(), getData["gender"])
        # sel = Select(homepage.getGender())
        # sel = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
        # sel.select_by_visible_text("Male")

        homepage.submitForm().click()
        # driver.find_element(By.XPATH, "//input[@value = 'Submit']").click()

        alertText = homepage.getSuccessMessage().text
        # alertText = driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text

        assert("Success" in alertText)
        assert("Success" in alertText) # added by arch 001AAAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        assert("Success" in alertText) # added by arch 001BBBxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

        assert("Success" in alertText) #log.info("added by gitdemo as develop001")
        assert("Success" in alertText) #log.info("added by gitdemo as develop001")


        self.driver.refresh()



    # @pytest.fixture(params=[("subrata", "sbt@gmail.com", "Male"), ("Nobonita", "Paul", "Female")])
    # @pytest.fixture(params=HomePageData.test_HomePageData)
    @pytest.fixture(params=HomePageData.getTestData("TC2"))
    def getData(self, request):
        return request.param
