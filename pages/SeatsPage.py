import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class SeatsPage:

    select_seats_later_btn_locator = (By.ID, "btnSeatMapLeave")

    wait = None

    def __init__(self, driver):
        self.driver = driver
        SeatsPage.wait = WebDriverWait(self.driver, 10)

    def select_seats_later(self):
        time.sleep(10)
        SeatsPage.wait.until(
            expected_conditions.visibility_of(self.driver.find_element(*SeatsPage.select_seats_later_btn_locator)))
        self.driver.find_element(*SeatsPage.select_seats_later_btn_locator).click()
