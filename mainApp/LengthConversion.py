class LengthConversion():
    def millimeter(self, value, to):
        if to == "cm":
            return round(value / 10, 3)
        elif to == 'm':
            return round(value / 1000, 3)
        elif to == 'km':
            return round(value / 1000000, 3)
        elif to == 'in':
            return round(value / 25.4, 3)
        elif to == 'f':
            return round(value / 304.8, 3)
        elif to == 'yd':
            return round(value / 914.4, 3)
        elif to == 'ml':
            return round(value / 1609344, 3)
        else:
            return "Invalid parameter"

    def meter(self, value, to):
        if to == "cm":
            return round(value * 100, 3)
        elif to == 'mm':
            return round(value * 1000, 3)
        elif to == 'km':
            return round(value / 1000, 3)
        elif to == 'in':
            return round(value * 39.3700787, 3)
        elif to == 'f':
            return round(value * 3.2808399, 3)
        elif to == 'yd':
            return round(value * 1.0936133, 3)
        elif to == 'ml':
            return round(value / 1609.344, 3)
        else:
            return "Invalid parameter"

    def centimeter(self, value, to):
        if to == "mm":
            return round(value * 10, 3)
        elif to == 'm':
            return round(value / 100, 3)
        elif to == 'km':
            return round(value / 100000, 3)
        elif to == 'in':
            return round(value / 2.54, 3)
        elif to == 'f':
            return round(value / 30.48, 3)
        elif to == 'yd':
            return round(value / 91.44, 3)
        elif to == 'ml':
            return round(value / 160934.4, 3)
        else:
            return "Invalid parameter"

    def kilometer(self, value, to):
        if to == "cm":
            return round(value * 100000, 3)
        elif to == 'm':
            return round(value * 1000, 3)
        elif to == 'mm':
            return round(value * 1000000, 3)
        elif to == 'in':
            return round(value * 39370.0787, 3)
        elif to == 'f':
            return round(value * 3280.8399, 3)
        elif to == 'yd':
            return round(value * 1093.6133, 3)
        elif to == 'ml':
            return round(value / 1.609344, 3)
        else:
            return "Invalid parameter"

    def inch(self, value, to):
        if to == "cm":
            return round(value * 2.54, 3)
        elif to == 'mm':
            return round(value * 25.4, 3)
        elif to == 'm':
            return round(value * 0.0254, 3)
        elif to == 'km':
            return round(value * 0.0000254, 3)
        elif to == 'f':
            return round(value / 12, 3)
        elif to == 'yd':
            return round(value / 36, 3)
        elif to == 'ml':
            return round(value / 63360, 3)
        else:
            return "Invalid parameter"

    def foot(self, value, to):
        if to == "cm":
            return round(value * 30.48, 3)
        elif to == 'mm':
            return round(value * 304.8, 3)
        elif to == 'm':
            return round(value * 0.3048, 3)
        elif to == 'km':
            return round(value * 0.0003048, 3)
        elif to == 'in':
            return round(value * 12, 3)
        elif to == 'yd':
            return round(value / 3, 3)
        elif to == 'ml':
            return round(value / 5280, 3)
        else:
            return "Invalid parameter"

    def yard(self, value, to):
        if to == "cm":
            return round(value * 91.44, 3)
        elif to == 'mm':
            return round(value * 914.4, 3)
        elif to == 'm':
            return round(value * 0.9144, 3)
        elif to == 'km':
            return round(value * 0.0009144, 3)
        elif to == 'in':
            return round(value * 36, 3)
        elif to == 'f':
            return round(value * 3, 3)
        elif to == 'ml':
            return round(value / 1760, 3)
        else:
            return "Invalid parameter"

    def mile(self, value, to):
        if to == "cm":
            return round(value * 160934.4, 3)
        elif to == 'mm':
            return round(value * 1609344, 3)
        elif to == 'm':
            return round(value * 1609.344, 3)
        elif to == 'km':
            return round(value * 1.609344, 3)
        elif to == 'in':
            return round(value * 63360, 3)
        elif to == 'f':
            return round(value * 5280, 3)
        elif to == 'yd':
            return round(value * 1760, 3)
        else:
            return "Invalid parameter"

    def convert(self, from_, value, to_):

        if from_==to_:
            return value
        elif value <0:
            return "Negative values are not allowed"
        elif from_ == 'mm':
            return self.millimeter(value, to_)
        elif from_ == 'cm':
            return self.centimeter(value, to_)
        elif from_ == 'm':
            return self.meter(value, to_)
        elif from_ == 'km':
            return self.kilometer(value, to_)
        elif from_ == 'in':
            return self.inch(value, to_)
        elif from_ == 'f':
            return self.foot(value, to_)
        elif from_ == 'yd':
            return self.yard(value, to_)
        elif from_ == 'ml':
            return self.mile(value, to_)
        else:
            return "Invalid parameter(from)"
