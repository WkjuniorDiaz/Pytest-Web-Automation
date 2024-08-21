import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class SeatsPage:

    select_seats_later_btn_locator = (By.ID, "btnSeatMapLeave")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def select_seats_later(self):
        self.wait.until(expected_conditions.element_to_be_clickable(SeatsPage.select_seats_later_btn_locator))
        self.driver.find_element(*SeatsPage.select_seats_later_btn_locator).click()
