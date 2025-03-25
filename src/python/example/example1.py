# Start the VI "example 1 - Plot" first then run that script

import lv_ui_testing.front_most_vi as fmv

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = fmv.get_vi_name()
    assert front_most_vi == "example 1 - plot.vi"

def test_random_plot():
    # Generate a random plot and query the data insisde it
    fmv.click_on_button("Random")
    data = fmv.resolve_value("Plot")
    print(f"data from plot : {data}")

    # Repeate the previous step
    fmv.click_on_button("Random")
    data2 = fmv.resolve_value("Plot")
    print(f"data from plot : {data2}")

    # Compare the results, they should be differnet
    assert data != data2