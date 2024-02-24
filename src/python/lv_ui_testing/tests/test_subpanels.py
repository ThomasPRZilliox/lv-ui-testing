# Start the VI "example 1 - Plot" first then run that script
from lv_ui_testing import  ui_testing
import pytest

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = ui_testing.FMV_get_vi_name()
    assert front_most_vi ==  "example 3 - subpanel.vi"


def test_subpanel1():
    # Get the subpanel to load the subpanel example 1
    ui_testing.FMV_click_on_button("sub1")
    sub1 = ui_testing.SP_get_vi_name("mySub")
    assert sub1 == "example 3 - subpanel1.vi"

@pytest.mark.parametrize("number, expected_bool", [ (x, x > 5) for x in range(1, 11)])

def test_set_value(number,expected_bool):
    # Set value to 0
    ui_testing.SP_set_value_DBL("mySub", "myNumber", number)
    data_number = ui_testing.SP_get_value_DBL("mySub", "myNumber")
    data_bool = ui_testing.SP_get_value_bool("mySub", "greater")

    assert data_bool == expected_bool
    assert data_number == number

def test_subpanel2():
    # Get the subpanel to load the subpanel example 1
    ui_testing.FMV_click_on_button("sub2")
    sub1 = ui_testing.SP_get_vi_name("mySub")
    assert sub1 == "example 3 - subpanel2.vi"


def test_random_plot():
    # Generate a random plot and query the data insisde it
    ui_testing.SP_click_on_button("mySub","Random")
    data = ui_testing.SP_get_value("mySub", "Plot")
    print(f"data from plot : {data}")

    # Repeate the previous step
    ui_testing.SP_click_on_button("mySub","Random")
    data2 = ui_testing.SP_get_value("mySub", "Plot")
    print(f"data from plot : {data2}")

    # Compare the results, they should be differnet
    assert data != data2