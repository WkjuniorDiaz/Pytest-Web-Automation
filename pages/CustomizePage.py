from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class CustomizePage:

    continue_btn_locator = (By.ID,"button-cart-confirm")

    wait = None

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10)

    def select_continue(self):
        self.wait.until(expected_conditions.visibility_of_element_located(CustomizePage.continue_btn_locator))
        self.driver.find_element(*CustomizePage.continue_btn_locator).click()