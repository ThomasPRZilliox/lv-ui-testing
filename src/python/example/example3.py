# Start the VI "example 3 - subplot" first then run that script
from lv_ui_testing import  ui_testing
import time

# Ask the tester daemon what is the front most VI
front_most_vi = ui_testing.get_front_most()
assert front_most_vi == "example 3 - subpanel.vi"

# Get the subpanel to load the subpanel example 1
ui_testing.click_on_button("sub1")
sub1 = ui_testing.get_subpanel("mySub")
assert sub1 == "example 3 - subpanel1.vi"

data = ui_testing.get_subpanel_value("mySub","myNumber")
print(data)

# Wait for 3 seconds
time.sleep(3)

# Get the subpanel to load the subpanel example 2
ui_testing.click_on_button("sub2")
sub1 = ui_testing.get_subpanel("mySub")
assert sub1 == "example 3 - subpanel2.vi"