import time

from selenium.webdriver.common.by import By



class FlightPage():

    flight_info_locator = (By.CSS_SELECTOR,"#SearchBoxDesktopCompacted div div")
    flights_options_locator = (By.XPATH,"//div[contains(@id,'WrapperCardFlight')]")
    rates_option_locator = (By.XPATH,"//li[contains(@id,'WrapperBundleCardbundle-detail')]")



    def __init__(self,driver):
        self.driver = driver

    def switchWindow(self):
        new_windows_name = self.driver.window_handles
        self.driver.switch_to.window(new_windows_name[1])

    def get_flight_info(self):
        return self.driver.find_element(*FlightPage.flight_info_locator).text

    def select_origin_flight(self):
        list_flight = self.driver.find_elements(*FlightPage.flights_options_locator)

        for index, element in enumerate(list_flight):
            if index == 0:
                element.click()

    def select_destination_flight(self,rate_option):
        list_flight = self.driver.find_elements(*FlightPage.flights_options_locator)

        for index, element in enumerate(list_flight):
            if index == 0:
                element.click()

        list_rate = self.driver.find_elements(*FlightPage.rates_option_locator)

        for element in list_rate:
            if rate_option in element.text:
                button_element = element.find_element(By.XPATH, ".//div//div[contains(@class,'SelectContainer')]/button")
                button_element.click()

