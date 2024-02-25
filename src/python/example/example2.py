# Start the VI "example 2 - value" first then run that script
from lv_ui_testing import  lv_ui_testing
import time

# Ask the tester daemon what is the front most VI
front_most_vi = ui_testing.FMV_get_vi_name()
assert front_most_vi == "example 2 - value.vi"

# Set value to 0
ui_testing.FMV_set_value_DBL("myNumber", 0)
data_number = ui_testing.FMV_get_value("myNumber")
data_bool = ui_testing.FMV_get_value_bool("greater")

assert data_bool == False
assert data_number == "0.000000"

# Wait for 3 seconds
time.sleep(3)

# Set value to 0
ui_testing.FMV_set_value_DBL("myNumber", 6)
data_number = ui_testing.FMV_get_value("myNumber")
data_bool = ui_testing.FMV_get_value_bool("greater")

assert data_bool == True
assert data_number == "6.000000"