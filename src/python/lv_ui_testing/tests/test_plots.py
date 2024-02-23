# Start the VI "example 1 - Plot" first then run that script

from lv_ui_testing import  ui_testing

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = ui_testing.get_front_most()
    assert front_most_vi == "example 1 - plot.vi"

def test_random_plot():
    # Generate a random plot and query the data insisde it
    ui_testing.click_on_button("Random")
    data = ui_testing.get_value("Plot")
    print(f"data from plot : {data}")

    # Repeate the previous step
    ui_testing.click_on_button("Random")
    data2 = ui_testing.get_value("Plot")
    print(f"data from plot : {data2}")

    # Compare the results, they should be differnet
    assert data != data2