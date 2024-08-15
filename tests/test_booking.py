from pages.FlightPage import FlightPage
from pages.SearchPage import SearchPage
from utilities.BaseClass import BaseClass


class TestBooking(BaseClass):

    def test_search_flight(self, getData):
        log = self.getLogger()
        search_page = SearchPage(self.driver)
        flight_page = FlightPage(self.driver)

        origin = getData["origin"]
        destination = getData["destination"]
        departure_date = getData["departureDate"]
        arrival_date = getData["arrivalDate"]

        search_page.select_origin(origin)
        search_page.select_destination(destination)
        search_page.select_departure_date(departure_date)
        search_page.select_arrival_date(arrival_date)
        search_page.select_search()

        flight_page.switchWindow()
        flight_detail = flight_page.get_flight_info()

        assert origin in flight_detail and destination in flight_detail

    def test_select_flight_and_proceed_to_booking(self, getData):
        log = self.getLogger()
        search_page = SearchPage(self.driver)
        flight_page = FlightPage(self.driver)

        origin = getData["origin"]
        destination = getData["destination"]
        departure_date = getData["departureDate"]
        arrival_date = getData["arrivalDate"]
        destination_rate = getData["destinationRate"]

        search_page.select_origin(origin)
        search_page.select_destination(destination)
        search_page.select_departure_date(departure_date)
        search_page.select_arrival_date(arrival_date)
        search_page.select_search()

        flight_page.switchWindow()
        flight_page.select_origin_flight()
        flight_page.select_destination_flight(destination_rate)

