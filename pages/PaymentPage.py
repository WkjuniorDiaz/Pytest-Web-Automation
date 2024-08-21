import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class PaymentPage:

    confirm_txt_locator = (By.CLASS_NAME,"latam-grid-child")


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,15)

    def get_confirm_tile(self):
        self.wait.until(expected_conditions.visibility_of_element_located(PaymentPage.confirm_txt_locator))
        return self.driver.find_element(*PaymentPage.confirm_txt_locator).text
