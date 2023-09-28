import time
import pytest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver) #creating an objct of HomePage class on Homepage file. Pass local driver (self.driver) as an arguement so that on HomePage we can pass that into constructor as an arguement and then define HomePage driver as this driver under constructor
        # checkoutpage = CheckoutPage(self.driver)    #moved to home page> shopitems()
        # confirmpage = ConfirmPage(self.driver)   #moved to ConfirmPage

        # open the website
        self.driver.get("https://rahulshettyacademy.com/angularpractice/")

        # click 'shop' link
        checkoutpage = homepage.shopItems()
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

        # take all the items in a list
        log.info("getting all the items into itemlist") #log
        itemList = checkoutpage.itemList()
        # items = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")

        # iterate through the names - if name ==Blackberry, click 'Add'
        for item in itemList:
            log.info(item.find_element(By.XPATH, "div/h4/a").text)
            if item.find_element(By.XPATH, "div/h4/a").text == "Blackberry":
                item.find_element(By.XPATH, "div/button").click()
        time.sleep(2)

        # click checkout
        checkoutpage.checkOutBtn().click()
        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        # click checkout on next page*
        confirmpage = checkoutpage.secondChkOutBtn() #obj of ConfirmPage class returned by secondChkOutBtn method
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        # Write partial country name in input field - auto suggestive drop down*
        log.info("inputting Ban in dropdown inputbox")
        confirmpage.countryField().send_keys("Bang")
        # self.driver.find_element(By.ID, "country").send_keys("Bang")

        # explicitly wait for country name element*
        self.verifyLinkPresence("Bangladesh")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Bangladesh")))
        # # wait.until(expected_conditions.presence_of_element_located(confirmpage.countryOption))

        # once element appears, click to select*
        log.info("selecting the country")
        confirmpage.selectCountry().click()
        # self.driver.find_element(By.LINK_TEXT, "Bangladesh").click()


        # click 'I agree..' checkbox*
        confirmpage.AgreeCheckbox().click()
        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()


        # Click purchase*
        confirmpage.purchaseButton().click()
        # self.driver.find_element(By.CSS_SELECTOR, "input[class*='btn-success']").click()

        # validate 'success' in the whole success message*
        successTxt = confirmpage.successTxt().text
        log.info("success text is "+successTxt)
        # successTxt = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-dismissible']").text

        assert 'Success' in successTxt
        assert 'Suc' in successTxt #added by 2nd person working in GitDemo
        assert 'ess' in successTxt #added by 2nd person working in GitDemo
        log.info("this is from GitX") #added parenthesis by GitX user
        log.info("from GitDemo 0001")

        log.info("added by architect 001..AAAA")
        log.info("added by architect 001...BBBB")
        log.info("added by architect 001...CCCC")

        log.info("added by gitdemo as develop001")


