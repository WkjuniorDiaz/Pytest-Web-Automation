from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class PassengersPage:

    first_name_locator = (By.XPATH,"//div[@data-testid='passengerDetails-firstName-ADT_1']")
    last_name_locator = (By.XPATH,"//div[@data-testid='passengerDetails-lastName-ADT_1']")
    date_birth_locator = (By.ID,"passengerInfo-dateOfBirth-ADT_1")
    gender_locator = (By.XPATH,"//div[@data-testid='passengerInfo-gender-ADT_1-select']")
    nationality_locator = (By.XPATH,"//div[@data-testid='']")
    type_document_locator = (By.XPATH,"//div[@data-testid='']")
    document_id_locator = (By.XPATH,"//div[@data-testid='']")
    email_locator = (By.XPATH,"//div[@data-testid='']")
    number_locator = (By.XPATH,"//div[@data-testid='']")


wait = None

    def __init__(self,driver):
        self.driver = driver
        wait = WebDriverWait(self.driver,10)

    def fill_passenger_information(self):