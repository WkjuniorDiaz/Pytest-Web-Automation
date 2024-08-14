from selenium.webdriver.common.by import By



class SearchPage():

    origin_locator = (By.ID,"txtInputOrigin_field")
    destination_locator = (By.ID,"txtInputDestination_field")
    departure_date_locator = (By.ID,"departureDate")
    arrival_date_locator = (By.ID,"arrivalDate")

    def __init__(self,driver):
        self.driver = driver

    def enter_flight_details(self,origin,destination,departureDate,arrivalDate):
        self.driver.find_element(*SearchPage.origin_locator).send_keys(origin)
        self.driver.find_element(*SearchPage.destination_locator).send_keys(destination)




