# Start the VI "example 3 - subplot" first then run that script
import time

# Ask the tester daemon what is the front most VI
front_most_vi = ui_testing.FMV_get_vi_name()
assert front_most_vi == "example 3 - subpanel.vi"

# Get the subpanel to load the subpanel example 1
ui_testing.FMV_click_on_button("sub1")
sub1 = ui_testing.SP_get_vi_name("mySub")
assert sub1 == "example 3 - subpanel1.vi"

data = ui_testing.SP_get_value("mySub", "myNumber")
print(data)

# Wait for 3 seconds
time.sleep(3)

# Get the subpanel to load the subpanel example 2
ui_testing.FMV_click_on_button("sub2")
sub1 = ui_testing.SP_get_vi_name("mySub")
assert sub1 == "example 3 - subpanel2.vi"