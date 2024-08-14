from pages.SearchPage import SearchPage
from utilities.BaseClass import BaseClass


class TestBooking(BaseClass):

    def test_search_flight(self, getData):
        log = self.getLogger()
        search_page = SearchPage(self.driver)

        search_page.enter_flight_details(getData["origin"],getData["destination"])