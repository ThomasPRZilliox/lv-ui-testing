# Start the VI "example 5 - parent.vi" first then run that script
from lv_ui_testing import ui_testing


def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = ui_testing.FMV_get_vi_name()
    assert front_most_vi ==  "example 5 - parent.vi"

def test_read_string():
    ui_testing.SP_SP_click_on_button("Sub Panel","Sub Panel Children","Clear")
    ui_testing.SP_SP_set_value_STR("Sub Panel","Sub Panel Children","String","Hello")
    assert "Hello" == ui_testing.SP_SP_get_value("Sub Panel", "Sub Panel Children", "String")

def test_read_DBL():
    ui_testing.SP_SP_click_on_button("Sub Panel","Sub Panel Children","Clear")
    ui_testing.SP_SP_set_value_DBL("Sub Panel", "Sub Panel Children", "Double",10)
    assert 10 == ui_testing.SP_SP_get_value_DBL("Sub Panel", "Sub Panel Children", "Double")

def test_read_bool():
    ui_testing.SP_SP_set_value_DBL("Sub Panel", "Sub Panel Children", "Double", 20)
    assert ui_testing.SP_SP_get_value_bool("Sub Panel", "Sub Panel Children", "20?")
    # 20?

test_front_most_vi()
test_read_string()
test_read_DBL()
test_read_bool()

