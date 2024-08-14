import pytest
import inspect
import logging
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def verifyElementIsVisible(self,element):
        wait = WebDriverWait(self.driver,10)
        wait.until(expected_conditions.visibility_of(element))

    def enter_data(self, element, data):
        element.send_keys(data)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler) #fileHandler object

        logger.setLevel(logging.INFO)

        return logger