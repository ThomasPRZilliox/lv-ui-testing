# Start the VI "example 12 - enums" first then run that script
import lv_ui_testing.front_most_vi as fmv
import pytest

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = fmv.get_vi_name()
    assert front_most_vi == "example 12 - enums.vi"

string_label = "Selected enum item"
enum_label = "Enum"

def test_ini():
    data = fmv.get_value(string_label)
    assert data == ""

@pytest.mark.parametrize("number, expected_item", [ (0,"a"),(1,"b"),(2,"c"),(3,"d"),(4,"e")])
def test_item(number,expected_item):
    # Unselect previous choices
    fmv.set_value_DBL(enum_label,number)
    data = fmv.resolve_value(string_label)
    assert data == expected_item