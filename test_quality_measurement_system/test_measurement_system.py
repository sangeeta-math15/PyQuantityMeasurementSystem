import pytest
from main_quantity_measurement_system.quantity_measure_system import QuantityMeasurementSystem


instance_of_main_class = QuantityMeasurementSystem()


def test_length_meter_to_kilometer_conversion():
    result = instance_of_main_class.length_meter_to_kilometer_conversion(10)
    assert result == 0.01

