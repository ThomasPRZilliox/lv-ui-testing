# Start the VI "example 3 - subpnael" first then run that script
import lv_ui_testing.front_most_vi as fmv
import lv_ui_testing.sub_panel as sp
import pytest

subpanel_label = "mySub"

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = fmv.get_vi_name()
    assert front_most_vi ==  "example 3 - subpanel.vi"


def test_subpanel1():
    # Get the subpanel to load the subpanel example 1
    fmv.click_on_button("sub1")
    sub1 = sp.get_vi_name(subpanel_label)
    assert sub1 == "example 3 - subpanel1.vi"

@pytest.mark.parametrize("number, expected_bool", [ (x, x > 5) for x in range(1, 11)])

def test_set_value(number,expected_bool):
    # Set value to 0
    sp.set_value_DBL(subpanel_label, "myNumber", number)
    data_number = sp.resolve_value(control_label="myNumber", subpanel_label=subpanel_label)
    data_bool = sp.resolve_value(control_label="greater", subpanel_label=subpanel_label)

    assert data_bool == expected_bool
    assert data_number == number

def test_subpanel2():
    # Get the subpanel to load the subpanel example 1
    fmv.click_on_button("sub2")
    sub1 = sp.get_vi_name("mySub")
    assert sub1 == "example 3 - subpanel2.vi"


def test_random_plot():
    # Generate a random plot and query the data insisde it
    sp.click_on_button("mySub","Random")
    data = sp.resolve_value("Plot", "mySub")
    print(f"data from plot : {data}")

    # Repeate the previous step
    sp.click_on_button("mySub", "Random")
    data2 = sp.resolve_value("Plot", "mySub")
    print(f"data from plot : {data2}")

    # Compare the results, they should be differnet
    assert data != data2
