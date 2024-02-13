# Start the VI "example 2 - value" first then run that script
from lv_ui_testing import  ui_testing
import time

# Ask the tester daemon what is the front most VI
front_most_vi = ui_testing.get_front_most()
assert front_most_vi == "example 2 - value.vi"

# Set value to 0
ui_testing.set_value_dbl("myNumber",0)
data_number = ui_testing.get_value("myNumber")
data_bool = ui_testing.get_value_bool("greater")

assert data_bool == False
assert data_number == "0.000000"

# Wait for 3 seconds
time.sleep(3)

# Set value to 0
ui_testing.set_value_dbl("myNumber",6)
data_number = ui_testing.get_value("myNumber")
data_bool = ui_testing.get_value_bool("greater")

assert data_bool == True
assert data_number == "6.000000"