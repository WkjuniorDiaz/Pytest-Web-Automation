from pages.CustomizePage import CustomizePage
from pages.FlightPage import FlightPage
from pages.PassengersPage import PassengersPage
from pages.PaymentPage import PaymentPage
from pages.SearchPage import SearchPage
from pages.SeatsPage import SeatsPage


class PageFactory:
    def __init__(self,driver):
        self.driver = driver
        self.page_map = {
            "search": SearchPage,
            "flight": FlightPage,
            "seats": SeatsPage,
            "customize": CustomizePage,
            "passengers": PassengersPage,
            "payment": PaymentPage
        }

    def get_page(self,page_name):
        page_class = self.page_map.get(page_name)
        if page_class is None:
            raise ValueError(f"Page '{page_name}' does not exist in PageFactory")
        return page_class(self.driver)