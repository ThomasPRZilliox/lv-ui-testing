# Start the VI "example 11 - tabs" first then run that script
import lv_ui_testing.front_most_vi as fmv

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = fmv.get_vi_name()
    assert front_most_vi == "example 11 - tabs.vi"

string_label = "Selected tab"
tab_label = "Tab Control"

def test_ini():
    data = fmv.get_value(string_label)
    assert data == ""

def test_tab1():
    button_tab = ("tab button 1")

    # Unselect previous choices
    fmv.set_value_DBL(tab_label,0)
    fmv.click_on_button(button_tab)
    data = fmv.resolve_value(string_label)
    assert data == "tab 1"

def test_tab2():
    button_tab = ("tab button 2")

    # Unselect previous choices
    fmv.set_value_DBL(tab_label,1)
    fmv.click_on_button(button_tab)
    data = fmv.resolve_value(string_label)
    assert data == "tab 2"