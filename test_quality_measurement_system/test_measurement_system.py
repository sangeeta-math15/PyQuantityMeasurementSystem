import pytest
from main_quantity_measurement_system.quantity_measure_system import QuantityMeasurementSystem

instance_of_main_class = QuantityMeasurementSystem()


def test_length_meter_to_kilometer_conversion():
    """
    test the length_meter_to_kilometer_conversion
    """
    result = instance_of_main_class.length_meter_to_kilometer_conversion(10)
    assert result == 0.01


def test_meter_to_centimeter():
    """
    Test the conversion of meter to centimeter.
    """
    result = instance_of_main_class.length_meter_to_kilometer_conversion(10)
    assert result == 1000


def test_grams_to_kilograms():
    """
    Test the grams_to_kilograms
    """
    result = instance_of_main_class.weight_grams_to_kilograms_conversion(10)
    assert result == 0.01


def test_grams_to_miligrams():
    """
    Test the grams_to_miligrams
    """
    result = instance_of_main_class.weight_grams_to_milligrams_conversion(10)
    assert result == 10000


def test_celsius_to_farenhit():
    """
    Test the celsius_to_farenhit
    """
    result = instance_of_main_class.temperature_celsius_to_fareheit(10)
    assert result == 50


def test_farenheit_to_celsius():
    """
    Test the farenheit_to_celsius
    """
    result = instance_of_main_class.temperature_farenheit_to_celsius(10)
    assert result == -12.22


def test_celsius_to_kelvin():
    """
    Test the _celsius_to_kelvin.
    """
    result = instance_of_main_class.temperature_celsius_to_kelvin(10)
    assert result == 283.15
