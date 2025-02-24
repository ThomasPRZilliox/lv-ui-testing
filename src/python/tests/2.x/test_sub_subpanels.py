# Start the VI "example 5 - parent.vi" first then run that script
import lv_ui_testing.front_most_vi as fmv
import lv_ui_testing.sub_sub_panel as ssp

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = fmv.get_vi_name()
    assert front_most_vi ==  "example 5 - parent.vi"

def test_read_string():
    ssp.click_on_button("Sub Panel","Sub Panel Children","Clear")
    ssp.set_value_STR("Sub Panel","Sub Panel Children","String","Hello")
    assert "Hello" == ssp.get_value("Sub Panel", "Sub Panel Children", "String")

def test_read_DBL():
    ssp.click_on_button("Sub Panel","Sub Panel Children","Clear")
    ssp.set_value_DBL("Sub Panel", "Sub Panel Children", "Double",10)
    assert 10 == ssp.get_value_DBL("Sub Panel", "Sub Panel Children", "Double")

def test_read_bool():
    ssp.set_value_DBL("Sub Panel", "Sub Panel Children", "Double", 20)
    assert ssp.get_value_bool("Sub Panel", "Sub Panel Children", "20?")
    # 20?



