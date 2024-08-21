import time

from pages.CustomizePage import CustomizePage
from pages.FlightPage import FlightPage
from pages.PassengersPage import PassengersPage
from pages.PaymentPage import PaymentPage
from pages.SearchPage import SearchPage
from pages.SeatsPage import SeatsPage
from utilities.BaseClass import BaseClass


class TestBooking(BaseClass):

    def test_search_flight(self, get_search_data):
        search_page = SearchPage(self.driver)
        flight_page = FlightPage(self.driver)

        origin = get_search_data["origin"]
        destination = get_search_data["destination"]
        departure_date = get_search_data["departureDate"]
        arrival_date = get_search_data["arrivalDate"]

        search_page.select_origin(origin)
        search_page.select_destination(destination)
        search_page.select_departure_date(departure_date)
        search_page.select_arrival_date(arrival_date)
        search_page.select_search()

        flight_page.switch_window()
        flight_detail = flight_page.get_flight_info()

        assert origin in flight_detail and destination in flight_detail

    def test_select_flight_and_proceed_to_booking(self, get_search_data):
        flight_page = FlightPage(self.driver)
        seats_page = SeatsPage(self.driver)
        customize_page = CustomizePage(self.driver)
        passengers_page = PassengersPage(self.driver)

        origin_rate = get_search_data["originRate"]
        destination_rate = get_search_data["destinationRate"]

        flight_page.select_origin_flight()
        flight_page.select_rate_of_flight(origin_rate)
        flight_page.select_departure_flight()
        flight_page.select_rate_of_flight(destination_rate)
        flight_page.select_continue_without_refundable()

        seats_page.select_seats_later()

        customize_page.select_continue()

        assert "Pasajeros" in passengers_page.get_title()

    def test_fill_booking_details(self, get_search_data, get_passengers_data):
        passengers_page = PassengersPage(self.driver)
        payment_page = PaymentPage(self.driver)

        first_name = get_passengers_data["firstName"]
        last_name = get_passengers_data["lastName"]
        date_birth = get_passengers_data["dateBirth"]
        gender = get_passengers_data["gender"]
        nationality = get_passengers_data["nationality"]
        document_id = get_passengers_data["documentID"]
        email = get_passengers_data["email"]
        number = get_passengers_data["number"]

        passengers_page.fill_passenger_information(first_name, last_name, date_birth, gender, nationality, document_id, email, number)
        passengers_page.submit_booking(first_name)

        assert payment_page.get_confirm_tile() in "Confirma y paga tu compra"
