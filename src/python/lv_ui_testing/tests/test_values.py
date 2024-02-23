# Start the VI "example 2 - value" first then run that script

from lv_ui_testing import  ui_testing
import pytest

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = ui_testing.get_front_most()
    assert front_most_vi == "example 2 - value.vi"

@pytest.mark.parametrize("number, expected_bool", [ (x, x > 5) for x in range(1, 11)])

def test_set_value(number,expected_bool):
    # Set value to 0
    ui_testing.set_value_dbl("myNumber",number)
    data_number = ui_testing.get_value_dbl("myNumber")
    data_bool = ui_testing.get_value_bool("greater")

    assert data_bool == expected_bool
    assert data_number == number
