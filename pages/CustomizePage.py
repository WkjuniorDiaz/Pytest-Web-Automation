from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class CustomizePage:

    continue_btn_locator = (By.ID,"button-cart-confirm")

    wait = None

    def __init__(self,driver):
        self.driver = driver
        wait = WebDriverWait(self.driver,10)

    def select_continue(self):
        CustomizePage.wait.until(expected_conditions.visibility_of(self.driver.find_element(*CustomizePage.continue_btn_locator)))
        self.driver.find_element(*CustomizePage.continue_btn_locator).click()