# Start the VI "example 4 - string" first then run that script

from lv_ui_testing import ui_testing
# from lv_ui_testing import  ui_testing

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = ui_testing.FMV_get_vi_name()
    assert front_most_vi == "example 4 - string.vi"

def test_update_string():
    # Generate a random plot and query the data insisde it
    ui_testing.FMV_set_value_STR("String","Hello")
    data = ui_testing.FMV_get_value("String")
    ui_testing.FMV_set_value_STR("String", data +  " World")
    data = ui_testing.FMV_get_value("String")


    # Compare the results, they should be differnet
    assert data == "Hello World"

def test_update_tree():
    # Generate a random plot and query the data insisde it

    data = ui_testing.FMV_get_value("Tree")
    ui_testing.FMV_set_value_ARR_STR("Tree",["Parent"])
    data = ui_testing.FMV_get_value_TREE("Tree")

    ui_testing.FMV_set_value_ARR_STR("Tree", ["Child 1","Child 2"])
    data = ui_testing.FMV_get_value_TREE("Tree")


    # Compare the results, they should be differnet
    assert data == ["Child 1","Child 2"]