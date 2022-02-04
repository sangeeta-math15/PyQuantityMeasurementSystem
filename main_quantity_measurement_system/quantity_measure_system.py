import logging

"""
Author: Sangeeta Math
"""

logging.basicConfig(filename='quantity_measurement_system.log', level=logging.DEBUG,
                    format='%(name)s | %(levelname)s | %(asctime)s | %(message)s')


class QuantityMeasurementSystem:
    """
    Created a class to compute quantity measurement of length, weight and temperature
    """

    METER_TO_CENTIMETER = 100
    METER_TO_KILOMETER = .001  # 1km = 10^3 meter, 1/10^3 km=1 meter, 10^-3km=1meter,.001=1meter
    GRAMS_TO_KILOGRAM = .001
    GRAMS_TO_MILLIGRAM = 1000
    KELVIN_TEMPERATURE = 273.15

    def get_input(self, choice, value):
        """

        :param choice: given by user
        :param value: numeric value given by user input
        :return:
        """
        choice_dict = {1: self.length_meter_to_centimeter_conversion,
                       2: self.length_meter_to_kilometer_conversion,
                       3: self.weight_grams_to_kilograms_conversion,
                       4: self.weight_grams_to_milligrams_conversion,
                       5: self.temperature_celsius_to_fareheit,
                       6: self.temperature_farenheit_to_celsius,
                       7: self.temperature_celsius_to_kelvin,
                       }
        converted_value = choice_dict.get(choice)(value)
        return converted_value

    def length_meter_to_centimeter_conversion(self, input_length):
        """
        :param input_length: The length to be converted which is given by user
        :return: converted centimeter length
        """
        try:
            centi_meter_length = round((input_length * self.METER_TO_CENTIMETER), 2)
            logging.debug("centimeter length is {}".format(centi_meter_length))
            return centi_meter_length
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')

    def length_meter_to_kilometer_conversion(self, input_length):
        """
        :param input_length: The length to be converted which is given by user
        :return: converted kilometer length
        """
        try:
            kilo_meter_length = round((input_length * self.METER_TO_KILOMETER), 5)
            logging.debug("kilometer length is {}".format(kilo_meter_length))
            return kilo_meter_length
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')

    def weight_grams_to_kilograms_conversion(self, input_weight):
        """
        :param input_weight: The weight to be converted which is given by user
        :return: converted kilogram weight
        """
        try:
            kilo_gram_weight = round((input_weight * self.GRAMS_TO_KILOGRAM), 5)
            logging.debug("kilogram weight is {}".format(kilo_gram_weight))
            return kilo_gram_weight
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')

    def weight_grams_to_milligrams_conversion(self, input_weight):
        """
        :param input_weight: the weight to be converted which is given by user
        :return: converted milligram weight
        """
        try:
            milli_gram_weight = round((input_weight * self.GRAMS_TO_MILLIGRAM), 2)
            logging.debug("milli gram weight is {}".format(milli_gram_weight))
            return milli_gram_weight
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')

    def temperature_celsius_to_fareheit(self, input_temperature):
        """
        :param input_temperature: The temperature to be converted which is given by user
        :return: converted fahrenheit temperature
        """
        try:
            fahrenheit_temperature = round((((9 / 5) * input_temperature) + 32), 2)
            logging.debug("fahrenheit temperature is {}".format(fahrenheit_temperature))
            return fahrenheit_temperature
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')

    def temperature_farenheit_to_celsius(self, input_temperature):
        """
        :param input_temperature: The temperature to be converted which is given by user
        :return: converted celsius temperature
        """
        try:
            celsius_temperature = round(((input_temperature - 32) * (5 / 9)), 2)
            logging.debug("celsius temperature is {}".format(celsius_temperature))
            return celsius_temperature
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')

    def temperature_celsius_to_kelvin(self, input_temperature):
        """
        :param input_temperature: The temperature to be converted which is given by user
        :return: converted kelvin temperature
        """
        try:
            kelvin_temperature = round((input_temperature + self.KELVIN_TEMPERATURE), 2)
            logging.debug("kelvin temperature is {}".format(kelvin_temperature))
            return kelvin_temperature
        except TypeError:
            logging.exception("Exception due to invalid input")
            print('Please give valid number input')


if __name__ == '__main__':

    quantity = QuantityMeasurementSystem()

    while True:

        print("""            
               1.meter_to_centimeter_conversion
               2.meter_to_kilometer_conversion
               3.grams_to_kilograms_conversion
               4.grams_to_milligrams_conversion
               5.celsius_to_farenheit
               6.farenheit_to_celsius
               7.celsius_to_kelvin
               """)
        try:
            choice = int(input("Enter your choice:- "))
            input_m = int(input("Enter number: "))
            res = quantity.get_input(choice, input_m)
            print(res)

        except TypeError:
            logging.exception("Enter proper value!!!")

