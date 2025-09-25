class WeightConversion():
    def milligram(self, value, to):
        if to == "g":
            return round(value / 1000, 3)
        elif to == "kg":
            return round(value / 1000000, 3)
        elif to == "oz":
            return round(value / 28349.5, 3)
        elif to == "lb":
            return round(value / 453592, 3)
        else:
            return "Invalid parameter"

    def gram(self, value, to):
        if to == "mg":
            return round(value * 1000, 3)
        elif to == "kg":
            return round(value / 1000, 3)
        elif to == "oz":
            return round(value / 28.3495, 3)
        elif to == "lb":
            return round(value / 453.592, 3)
        else:
            return "Invalid parameter"

    def kilogram(self, value, to):
        if to == "mg":
            return round(value * 1000000, 3)
        elif to == "g":
            return round(value * 1000, 3)
        elif to == "oz":
            return round(value * 35.274, 3)
        elif to == "lb":
            return round(value * 2.20462, 3)
        else:
            return "Invalid parameter"

    def ounce(self, value, to):
        if to == "mg":
            return round(value * 28349.5, 3)
        elif to == "g":
            return round(value * 28.3495, 3)
        elif to == "kg":
            return round(value / 35.274, 3)
        elif to == "lb":
            return round(value / 16, 3)
        else:
            return "Invalid parameter"

    def pound(self, value, to):
        if to == "mg":
            return round(value * 453592, 3)
        elif to == "g":
            return round(value * 453.592, 3)
        elif to == "kg":
            return round(value / 2.20462, 3)
        elif to == "oz":
            return round(value * 16, 3)
        else:
            return "Invalid parameter"

    def convert(self, value, from_, to_):
        if value<0:
            return "Negative values are not allowed"
        elif from_ == to_:
            return value
        elif from_ == "mg":
            return self.milligram(value, to_)
        elif from_ == "g":
            return self.gram(value, to_)
        elif from_ == "kg":
            return self.kilogram(value, to_)
        elif from_ == "oz":
            return self.ounce(value, to_)
        elif from_ == "lb":
            return self.pound(value, to_)
        else:
            return "Invalid parameter(from)"
