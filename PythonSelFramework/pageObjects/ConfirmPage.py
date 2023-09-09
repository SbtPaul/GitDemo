from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.CSS_SELECTOR, "input[id='country']")
    countryOption = (By.LINK_TEXT, "Bangladesh")
    agreeChk = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "input[class*='btn-success']")
    success = (By.CSS_SELECTOR, "div[class*='alert-dismissible']")

    def countryField(self):
        return self.driver.find_element(*ConfirmPage.country)

    def selectCountry(self):
        return self.driver.find_element(*ConfirmPage.countryOption)

    def AgreeCheckbox(self):
        return self.driver.find_element(*ConfirmPage.agreeChk)

    def purchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def successTxt(self):
        return self.driver.find_element(*ConfirmPage.success)
