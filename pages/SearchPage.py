import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class SearchPage():
    origin_locator = (By.ID, "txtInputOrigin_field")
    destination_locator = (By.ID, "txtInputDestination_field")
    country_opt_locator = (By.XPATH, "//li[contains(@id,'lstItem')]")
    departure_date_locator = (By.ID, "departureDate")
    arrival_date_locator = (By.ID, "arrivalDate")
    search_btn_locator = (By.ID, "btnSearchCTA")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def select_origin(self, origin):
        time.sleep(1)
        self.wait.until(expected_conditions.visibility_of_element_located(SearchPage.origin_locator))
        self.driver.find_element(*SearchPage.origin_locator).send_keys(origin)
        self.select_country(origin)

    def select_destination(self, destination):
        self.wait.until(expected_conditions.visibility_of_element_located(SearchPage.destination_locator))
        self.driver.find_element(*SearchPage.destination_locator).send_keys(destination)
        self.select_country(destination)

    def select_country(self, country):
        self.wait.until(expected_conditions.visibility_of_all_elements_located(SearchPage.country_opt_locator))
        list_opt = self.driver.find_elements(*SearchPage.country_opt_locator)

        for element in list_opt:
            if country in element.text:
                element.click()
                break

    def select_departure_date(self, departure_date):
        self.wait.until(expected_conditions.visibility_of_element_located(SearchPage.departure_date_locator))
        self.driver.find_element(*SearchPage.departure_date_locator).click()
        date_element = self.driver.find_element(By.XPATH, "//td[contains(@aria-label,'" + departure_date + "')]")
        date_element.click()

    def select_arrival_date(self, arrival_date):
        self.wait.until(expected_conditions.visibility_of_element_located(SearchPage.arrival_date_locator))
        self.driver.find_element(*SearchPage.arrival_date_locator).click()
        date_element = self.driver.find_element(By.XPATH, "//td[contains(@aria-label,'" + arrival_date + "')]")
        date_element.click()

    def select_search(self):
        self.wait.until(expected_conditions.visibility_of_element_located(SearchPage.search_btn_locator))
        self.driver.find_element(*SearchPage.search_btn_locator).click()
