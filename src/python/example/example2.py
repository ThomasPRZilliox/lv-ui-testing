# Start the VI "example 2 - value" first then run that script
import pytest
import lv_ui_testing.front_most_vi as fmv
def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = fmv.get_vi_name()
    assert front_most_vi == "example 2 - value.vi"

@pytest.mark.parametrize("number, expected_bool", [ (x, x > 5) for x in range(1, 11)])

def test_set_value(number,expected_bool):
    # Set value to 0
    fmv.set_value_DBL("myNumber", number)
    data_number = fmv.resolve_value("myNumber")
    data_bool = fmv.resolve_value("greater")

    assert data_bool == expected_bool
    assert data_number == number
