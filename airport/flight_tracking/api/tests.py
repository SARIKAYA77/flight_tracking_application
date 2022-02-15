from django.test import TestCase
from django.utils import timezone
from .models import Airport, Flight


class AirportModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Airport.objects.create(code='IST', city='Istanbul')

    def test_code_label(self):
        airport = Airport.objects.get(id=1)
        field = airport.code
        self.assertEqual(field, 'IST')

    def test_city_label(self):
        airport = Airport.objects.get(id=1)
        field = airport.city
        self.assertEqual(field, 'Istanbul')


class FlightTestModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        airport = Airport.objects.create(code='IST', city='Istanbul')
        airport.save()
        Flight.objects.create(
            flight_number="XYZ123",
            take_off=timezone.now(),
            landing=timezone.now(),
            from_airport=airport,
            to_airport=airport)

    def test_flight_number_label(self):
        flight = Flight.objects.get(id=1)
        field = flight.flight_number
        self.assertEqual(field, 'XYZ123')

    def test_from_airport_label(self):
        flight = Flight.objects.get(id=1)
        field = flight.from_airport.code
        self.assertEqual(field, 'IST')

    def test_from_airport_label(self):
        flight = Flight.objects.get(id=1)
        field = flight.to_airport.code
        self.assertEqual(field, 'IST')


class CountTestModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        airport = Airport.objects.create(code='IST', city='Istanbul')
        airport.save()
        Flight.objects.create(
            flight_number="XYZ123",
            take_off=timezone.now(),
            landing=timezone.now(),
            from_airport=airport,
            to_airport=airport)

    def test_flight_number_label(self):
        flight = Flight.objects.get(id=1)
        field = flight.flight_number
        self.assertEqual(field, 'XYZ123')

    def test_count_number(self):
        count = len(Flight.objects.filter(flight_number="XYZ123"))
        self.assertEqual(count, 1)


class TestUrls(TestCase):

    def test_desired_airport_url(self):
        response = self.client.get('/airports/')
        self.assertEqual(response.status_code, 200)

    def test_desired_flight_url(self):
        response = self.client.get('/flights/')
        self.assertEqual(response.status_code, 200)

    def test_desired_flight_url(self):
        response = self.client.get('/count/')
        self.assertEqual(response.status_code, 200)
