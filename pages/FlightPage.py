import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class FlightPage():

    flight_info_locator = (By.CSS_SELECTOR,"#SearchBoxDesktopCompacted div div")
    flights_options_locator = (By.XPATH,"//div[contains(@id,'WrapperCardFlight')]")
    rates_option_locator = (By.XPATH,"//li[contains(@id,'WrapperBundleCardbundle-detail')]")
    allow_restriction_locator = (By.ID,"undefined-flight-select")
    origin_flight_info = (By.TAG_NAME,"strong")
    continue_btn_locator = (By.ID,"button9")

    wait = None
    actions = None

    def __init__(self,driver):
        self.driver = driver
        FlightPage.wait = WebDriverWait(self.driver,10)
        FlightPage.actions = ActionChains(self.driver)

    def switchWindow(self):
        new_windows_name = self.driver.window_handles
        self.driver.switch_to.window(new_windows_name[1])

    def get_flight_info(self):
        return self.driver.find_element(*FlightPage.flight_info_locator).text

    def select_origin_flight(self):
        list_flight = self.driver.find_elements(*FlightPage.flights_options_locator)

        for index, element in enumerate(list_flight):
            FlightPage.wait.until(expected_conditions.visibility_of(element.find_element(By.XPATH, ".//div/div[2]")))
            if index == 0:
                element.click()
                break

    def select_departure_flight(self):
        time.sleep(6)
        FlightPage.wait.until(expected_conditions.visibility_of(self.driver.find_element(*FlightPage.origin_flight_info)))
        list_flight = self.driver.find_elements(*FlightPage.flights_options_locator)

        for index, element in enumerate(list_flight):
            FlightPage.wait.until(expected_conditions.visibility_of(element.find_element(By.XPATH, ".//div/div[2]")))
            if index == 0:
                element.click()
                break

    def select_rate_of_flight(self, rate_option):
        list_rate = self.driver.find_elements(*FlightPage.rates_option_locator)

        for element in list_rate:
            if rate_option in element.text:
                button_element = element.find_element(By.XPATH, ".//div//div[contains(@class,'SelectContainer')]/button")
                FlightPage.actions.move_to_element(button_element).perform()
                button_element.click()
                break

        self.driver.find_element(*FlightPage.allow_restriction_locator).click()

    def select_continue_without_refundable(self):
        time.sleep(5)
        continue_btn_element = self.driver.find_element(*FlightPage.continue_btn_locator)
        FlightPage.actions.move_to_element(continue_btn_element).perform()
        self.driver.find_element(*FlightPage.continue_btn_locator).click()