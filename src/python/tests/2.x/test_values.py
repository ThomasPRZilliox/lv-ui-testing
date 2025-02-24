# Start the VI "example 2 - value" first then run that script
import lv_ui_testing.front_most_vi as fmv
import pytest

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = fmv.get_vi_name()
    assert front_most_vi == "example 2 - value.vi"

@pytest.mark.parametrize("number, expected_bool", [ (x, x > 5) for x in range(1, 11)])

def test_set_value(number,expected_bool):
    numeric_label = "myNumber"
    boolean_label = "greater"

    fmv.set_value_DBL(numeric_label,number)
    data_number = fmv.get_value_DBL(numeric_label)
    data_bool = fmv.get_value_bool(boolean_label)

    assert data_bool == expected_bool
    assert data_number == number

