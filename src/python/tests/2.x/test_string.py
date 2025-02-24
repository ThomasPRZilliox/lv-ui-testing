# Start the VI "example 4 - string" first then run that script
import lv_ui_testing.front_most_vi as fmv

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = fmv.get_vi_name()
    assert front_most_vi == "example 4 - string.vi"

def test_update_string():
    # Generate a random plot and query the data insisde it
    string_label = "String"

    fmv.set_value_STR(string_label,"Hello")
    data = fmv.get_value(string_label)
    fmv.set_value_STR(string_label, data + " World")
    data = fmv.get_value(string_label)

    assert data == "Hello World"

def test_update_tree():
    tree_label = ("Tree")

    # Unselect previous choices
    fmv.set_value_ARR_STR("Tree", [])
    data = fmv.get_value_TREE(tree_label)
    assert data == []

    # Only select the parent node
    fmv.set_value_ARR_STR("Tree",["Parent"])
    data = fmv.get_value_TREE(tree_label)
    assert data == ["Parent"]

    # Select the two children nodes
    fmv.set_value_ARR_STR("Tree", ["Child 1","Child 2"])
    data = fmv.get_value_TREE(tree_label)
    assert data == ["Child 1","Child 2"]
