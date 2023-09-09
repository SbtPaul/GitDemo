import inspect
import logging

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # __name__ will get the file name, by default it prints root.. import inbuild logging
        fileHandler = logging.FileHandler('logfile.log')  # fileName where the log will be saved under the same folder
        formatter = logging.Formatter(
            "%(asctime)s :%(levelname)s :%(name)s :%(message)s")  # braces and % will evaluate at runtime
        # timestamp, severity level, name of the file, actual message.. S indicates string
        fileHandler.setFormatter(formatter)  # to create connection of formatter with logger obj
        logger.addHandler(fileHandler)  # filename and formatter passed onto the logger

        logger.setLevel(logging.DEBUG)  # this will log all from INFO upto the highest hierarcy level.. and so on
        # following part is not needed as we are adding the message on testcase file
        # logger.debug("this is debug for dev")
        # logger.info("this is info - you have xxx dollar balance")
        # logger.warning("this is warning - you minimum balance if exceeded")
        # logger.error("error - assertion failed")
        # logger.critical("critical issue - script will not proceed further")
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)


# C:\Users\SudipNobonita\PycharmProjects\pythonProject\PythonTesting\pytestsDemo\BaseClass.py
