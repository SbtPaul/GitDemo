from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class HomePage:

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[class*='form-control'][name='name']")
    email = (By.NAME, "email")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value = 'Submit']")
    success = (By.CSS_SELECTOR, "[class*='alert-success']")

    def __init__ (self, driver): #this driver is coming from test_e2e as input there during HomePage obj creation
        self.drvr = driver # this means the local driver (self.drvr) is eq to driver on test_e2e that we got as an input while HomePage obj creation

    def shopItems(self):

        # return self.drvr.find_element(*HomePage.shop) #self.drvr means driver of this class and it's constructor
        self.drvr.find_element(*HomePage.shop).click()
        checkOutPage = CheckoutPage(self.drvr)
        return checkOutPage


    def getName(self):
        return self.drvr.find_element(*HomePage.name)

    def getEmail(self):
        return self.drvr.find_element(*HomePage.email)

    def getCheckbox(self):
        return self.drvr.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.drvr.find_element(*HomePage.gender)

    def submitForm(self):
        return self.drvr.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.drvr.find_element(*HomePage.success)