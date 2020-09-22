# https://skeoop.github.io/assignments/PA3-UnitConverter.pdf
# A general unit converter that can convert values of different types of units, including Length, Weight, Temperature


class Unit:

    def __init__(self, unit_value):
        self.unit_value = unit_value


class Length(Unit):

    def __init__(self, unit_value):
        Unit.__init__(self, unit_value)

    def Length_lookup(self):
        val = 0.0                                       # val = multiplying factor
        if self.unit_value == "kilometer":
            val = 1.0
        if self.unit_value == "meter":
            val = 1000.0
        if self.unit_value == "centimeter":
            val = 100000.0
        if self.unit_value == "mile":
            val = 0.62137119
        return val


class Weight(Unit):

    def __init__(self, unit_value):
        Unit.__init__(self, unit_value)

    def Weight_lookup(self):
        val = 0.0
        if self.unit_value == "kilogram":
            val = 1.0
        if self.unit_value == "gram":
            val = 1000.0
        if self.unit_value == "milligram":
            val = 1000000.0
        if self.unit_value == "pound":
            val = 2.20462262
        return val


class Temperature(Unit):

    def __init__(self, unit_value):
        Unit.__init__(self, unit_value)

    def Temperature_lookup(self):
        val = 0.0
        if self.unit_value == "Celsius":
            val = 1.0
        if self.unit_value == "Fahrenheit":
            val = 1.0
        return val


class Conversion:

    def __init__(self, value, from_unit, to_unit):      # Conversion class takes value, it's unit and unit to convert
        self.value = value
        self.from_unit = from_unit
        self.to_unit = to_unit

    def convertLength(self):
        if Length(self.from_unit).Length_lookup() == 0:
            return ("Wrong input!")                  # If input not according to unit names mentioned above, then error
        else:
            return self.value * (Length(self.to_unit).Length_lookup()) / (Length(self.from_unit).Length_lookup())

    def convertWeight(self):
        if Weight(self.from_unit).Weight_lookup() == 0:
            return ("Wrong input!")
        else:
            return self.value * (Weight(self.to_unit).Weight_lookup()) / (Weight(self.from_unit).Weight_lookup())

    def convertTemperature(self):
        if Temperature(self.from_unit).Temperature_lookup() == 0:
            return "Wrong input!"
        elif Temperature(self.from_unit).unit_value == "Fahrenheit":    # For temp conversions, no direct multiplication
            return (self.value - 32) / 1.8
        else:
            return (self.value * 1.8) + 32


# Taking input for unit conversion
unit_type_string = raw_input("Which unit type to convert, Length, Weight or Temperature?, Press 1, 2 or 3 resp.: ")
unit_type = int(unit_type_string)
if unit_type != 1 or unit_type != 2 or unit_type != 3:
    print ("Choose from 1, 2 or 3!")
else:
    input_val_string = raw_input("Enter the value: ")
    input_val = int(input_val_string)
    input_fromUnit_string = raw_input("Enter the unit of the value: ")
    input_toUnit_string = raw_input("Enter the unit the value needs to be converted: ")
    if unit_type == 1:
        con_val = Conversion(input_val, input_fromUnit_string, input_toUnit_string).convertLength()
        print (con_val)
    elif unit_type == 2:
        con_val = Conversion(input_val, input_fromUnit_string, input_toUnit_string).convertWeight()
        print (con_val)
    elif unit_type == 3:
        con_val = Conversion(input_val, input_fromUnit_string, input_toUnit_string).convertTemperature()
        print (con_val)
