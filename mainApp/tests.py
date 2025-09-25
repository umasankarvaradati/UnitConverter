from django.test import TestCase,Client
from .LengthConversion import LengthConversion
from .TemperatureConversion import TemperatureConverter
from .WeightConversion import WeightConversion
from django.urls import reverse
# Create your tests here.
from.views import UnitConverter
class TestLengthConversion(TestCase):
    def setUp(self):
        self.converter = LengthConversion()
        self.convert = self.converter.convert
        
    def test_convert_to_cm(self):
        self.assertEqual(3300, self.convert("m",33,'cm'))
        self.assertEqual("Negative values are not allowed", self.convert("m",-33,'cm'))
    
    def test_convert_zero_to_cm(self):
        self.assertEqual(0,self.convert("m",0,'cm'))

    def test_convert_to_m(self):
        self.assertEqual(33, self.convert("m",33,'m'))
    
    def test_convert_to_km(self):
        self.assertEqual(333.333, self.convert("m",333333,'km'))
   
    def test_convert_to_in(self):
        self.assertEqual(1299.213, self.convert("m",33,'in'))
    
    def test_convert_to_foot(self):
        self.assertEqual(108.268, self.convert("m",33,'f'))
    
    def test_convert_to_yard(self):
        self.assertEqual(36.089, self.convert("m",33,'yd'))
    
    def test_convert_to_mile(self):
        self.assertEqual(2071.237, self.convert("m",3333333,'ml'))
    
    def test_convert_to_else(self):
        self.assertEqual("Invalid parameter",self.convert("m",50,'kkk'))

    def test_convert_inch_to_cm(self):
        self.assertEqual(2.54, self.convert("in",1,'cm'))

    def test_convert_mile_to_km(self):
        self.assertEqual(1.609, self.convert("ml",1,'km'))

class TestTemperatureConversion(TestCase):
    def setUp(self):
        self.converter = TemperatureConverter()
        self.convert = self.converter.convert

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(32.0, self.convert(0, 'c', 'f'))
        self.assertEqual(77.0, self.convert(25, 'c', 'f'))
        self.assertEqual(-13, self.convert(-25, 'c', 'f'))


    def test_celsius_to_kelvin(self):
        self.assertEqual(273.15, self.convert(0, 'c', 'k'))
        self.assertEqual(298.15, self.convert(25, 'c', 'k'))
        self.assertEqual(248.15, self.convert(-25, 'c', 'k'))

    def test_fahrenheit_to_celsius(self):
        self.assertEqual(0.0, self.convert(32, 'f', 'c'))
        self.assertEqual(25.0, self.convert(77, 'f', 'c'))
        self.assertEqual(-66.67, self.convert(-88, 'f', 'c'))

    def test_fahrenheit_to_kelvin(self):
        self.assertEqual(273.15, self.convert(32, 'f', 'k'))
        self.assertEqual(298.15, self.convert(77, 'f', 'k'))
        self.assertEqual(206.48, self.convert(-88, 'f', 'k'))

    def test_kelvin_to_celsius(self):
        self.assertEqual(0.0, self.convert(273.15, 'k', 'c'))
        self.assertEqual(25.0, self.convert(298.15, 'k', 'c'))
        self.assertEqual(-325.15, self.convert(-52, 'k', 'c'))

    def test_kelvin_to_fahrenheit(self):
        self.assertEqual(32.0, self.convert(273.15, 'k', 'f'))
        self.assertEqual(77.0, self.convert(298.15, 'k', 'f'))
        self.assertEqual(-904.27, self.convert(-247, 'k', 'f'))

    def test_same_unit(self):
        self.assertEqual(25, self.convert(25, 'c', 'c'))
        self.assertEqual(77, self.convert(77, 'f', 'f'))
        self.assertEqual(298.15, self.convert(298.15, 'k', 'k'))

    def test_invalid_to(self):
        self.assertEqual("Invalid parameter", self.convert(25, 'c', 'x'))

    def test_invalid_from(self):
        self.assertEqual("Invalid parameter(from)", self.convert(25, 'x', 'f'))

class TestWeightConversion(TestCase):
    def setUp(self):
        self.converter = WeightConversion()
        self.convert = self.converter.convert

    def test_gram_to_kilogram(self):
        self.assertEqual(1.0, self.convert(1000, 'g', 'kg'))
        self.assertEqual("Negative values are not allowed", self.convert(-1000, 'g', 'kg'))

    def test_kilogram_to_gram(self):
        self.assertEqual(1000.0, self.convert(1, 'kg', 'g'))

    def test_pound_to_ounce(self):
        self.assertEqual(16.0, self.convert(1, 'lb', 'oz'))

    def test_ounce_to_pound(self):
        self.assertEqual(1.0, self.convert(16, 'oz', 'lb'))

    def test_milligram_to_gram(self):
        self.assertEqual(1.0, self.convert(1000, 'mg', 'g'))

    def test_gram_to_milligram(self):
        self.assertEqual(1000.0, self.convert(1, 'g', 'mg'))

    def test_kilogram_to_pound(self):
        self.assertEqual(2.205, self.convert(1, 'kg', 'lb'))

    def test_pound_to_kilogram(self):
        self.assertEqual(1.0, self.convert(2.205, 'lb', 'kg'))

    def test_same_unit(self):
        self.assertEqual(100, self.convert(100, 'g', 'g'))
        self.assertEqual(5, self.convert(5, 'kg', 'kg'))

    def test_invalid_to(self):
        self.assertEqual("Invalid parameter", self.convert(100, 'g', 'x'))

    def test_invalid_from(self):
        self.assertEqual("Invalid parameter(from)", self.convert(100, 'x', 'g'))

class TestUnitConverter(TestCase):
    def setUp(self):
        self.client= Client()
        self.home_url = reverse('home')
    def test_home_GET(self):
        response = self.client.get(self.home_url)
        self.assertEqual(200,response.status_code)
        self.assertTemplateUsed('home.html')
        self.assertTemplateNotUsed("")
    def test_uniconvertetr_POST_length(self):
        post_data = {
            'measurement': 'length',
            'value': '10',
            'from': 'm',
            'to': 'cm'
        }
        response = self.client.post(self.home_url, post_data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json()['result'], 1000)
    def test_unit_converter_view_POST_temperature(self):
        post_data = {
            'measurement': 'temperature',
            'value': '25',
            'from': 'c',
            'to': 'f'
        }
        response = self.client.post(self.home_url, post_data)

        self.assertEqual(response.status_code, 200)
        # Assert the JSON response is correct (25°C = 77°F)
        self.assertEqual(response.json()['result'], 77.0)

    def test_unit_converter_view_POST_invalid_params(self):
        # Test with missing data
        post_data = {
            'measurement': 'weight',
            'value': '5'
            # 'from' and 'to' are missing
        }
        response = self.client.post(self.home_url, post_data)

        # Assert the request was a "Bad Request" (status code 400)
        self.assertEqual(response.status_code, 400)
        # Check the error message in the JSON response
        self.assertIn('error', response.json())
        self.assertEqual(response.json()['error'], 'Missing parameters')