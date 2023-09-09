from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    items = (By.XPATH, "//div[@class='card h-100']")
    checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    secondCheckOut = (By.XPATH, "//button[@class='btn btn-success']")

    def itemList(self):
        return self.driver.find_elements(*CheckoutPage.items)
    def checkOutBtn(self):
        return self.driver.find_element(*CheckoutPage.checkOut)
    def secondChkOutBtn(self):
        self.driver.find_element(*CheckoutPage.secondCheckOut).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

