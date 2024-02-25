# Start the VI "example 1 - Plot" first then run that script

from lv_ui_testing import  lv_ui_testing

# Ask the tester daemon what is the front most VI
front_most_vi = ui_testing.FMV_get_vi_name()
assert front_most_vi == "example 1 - plot.vi"

# Generate a random plot and query the data insisde it
ui_testing.FMV_click_on_button("Random")
data = ui_testing.FMV_get_value("Plot")
print(f"data from plot : {data}")

# Repeate the previous step
ui_testing.FMV_click_on_button("Random")
data2 = ui_testing.FMV_get_value("Plot")
print(f"data from plot : {data2}")

# Compare the results, they should be differnet
assert data != data2