class TemperatureConverter():

    def celsius(self, value, to):
        if to == 'f':
            return round((value * (9/5)) + 32, 2)
        elif to == 'k':
            return round(value + 273.15, 2)
        else:
            return "Invalid parameter"

    def fahrenheit(self, value, to):
        if to == 'c':
            return round((value - 32) * (5/9), 2)
        elif to == 'k':
            return round((value - 32) * (5/9) + 273.15, 2)
        else:
            return "Invalid parameter"

    def kelvin(self, value, to):
        if to == 'f':
            return round((value - 273.15) * (9/5) + 32, 2)
        elif to == 'c':
            return round(value - 273.15, 2)
        else:
            return "Invalid parameter"

    def convert(self, value, from_, to_):
        if from_ == to_:
            return value
        elif from_ == 'c':
            return self.celsius(value, to_)
        elif from_ == 'f':
            return self.fahrenheit(value, to_)
        elif from_ == 'k':
            return self.kelvin(value, to_)
        else:
            return "Invalid parameter(from)"
