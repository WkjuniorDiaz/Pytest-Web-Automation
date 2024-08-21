from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class PassengersPage:
    title_locator = (By.CLASS_NAME, "body-title-passengerList")
    first_name_locator = (By.XPATH, "//div[@data-testid='passengerDetails-firstName-ADT_1']")
    last_name_locator = (By.XPATH, "//div[@data-testid='passengerDetails-lastName-ADT_1']")
    date_birth_locator = (By.ID, "passengerInfo-dateOfBirth-ADT_1")
    gender_locator = (By.XPATH, "//div[@data-testid='passengerInfo-gender-ADT_1-select']")
    nationality_locator = (By.ID, "mui-component-select-documentInfo.nationality")
    type_document_locator = (By.ID, "mui-component-select-documentInfo.documentType")
    document_id_locator = (By.XPATH, "//div[@data-testid='documentInfo-documentNumber-ADT_1']")
    email_locator = (By.ID, "passengerInfo-emails-ADT_1-label")
    number_locator = (By.ID, "passengerInfo-phones0-number-ADT_1-label")

    wait = None
    actions = None

    def __init__(self, driver):
        self.driver = driver
        PassengersPage.wait = WebDriverWait(self.driver, 10)
        PassengersPage.actions = ActionChains(self.driver)

    def get_title(self):
        PassengersPage.wait.until(expected_conditions.visibility_of(self.driver.find_element(*PassengersPage.title_locator)))
        return self.driver.find_element(*PassengersPage.title_locator).text

    def fill_passenger_information(self, first_name, last_name, date_birth, gender, nationality, document_id, email, number):
        self.driver.find_element(*PassengersPage.first_name_locator).send_keys(first_name)
        self.driver.find_element(*PassengersPage.last_name_locator).send_keys(last_name)
        self.driver.find_element(*PassengersPage.date_birth_locator).send_keys(date_birth)
        self.driver.find_element(*PassengersPage.gender_locator).click()
        gender_select = self.driver.find_element(By.XPATH, "//li[@data-value='" + gender + "']")
        gender_select.click()
        self.driver.find_element(*PassengersPage.nationality_locator).click()
        nationality_select = self.driver.find_element(By.XPATH, "//li[@data-value='" + nationality + "']")
        PassengersPage.actions.move_to_element(nationality_select).perform()
        nationality_select.click()
        self.driver.find_element(*PassengersPage.document_id_locator).send_keys(document_id)
        self.driver.find_element(*PassengersPage.email_locator).send_keys(email)
        self.driver.find_element(*PassengersPage.number_locator).send_keys(number)
