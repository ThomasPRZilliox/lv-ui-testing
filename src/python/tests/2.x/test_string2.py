# Start the VI "example 4b - string" first then run that script
import lv_ui_testing.front_most_vi as fmv
import lv_ui_testing.sub_panel as sp
import lv_ui_testing.sub_sub_panel as ssp

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = fmv.get_vi_name()
    assert front_most_vi == "example 4b - string.vi"

def test_fmv_update_string():
    # Generate a random plot and query the data insisde it
    string_label = "String"

    fmv.set_value_STR(string_label,"Hello")
    data = fmv.get_value(string_label)
    fmv.set_value_STR(string_label, data + " World")
    data = fmv.get_value(string_label)

    assert data == "Hello World"

def test_fmv_update_string2():
    # Generate a random plot and query the data insisde it
    string_label = "String"

    fmv.set_value_STR(string_label,"Hello")
    data = fmv.resolve_value(string_label)
    fmv.set_value_STR(string_label, data + " World")
    data = fmv.resolve_value(string_label)
    fmv.set_value_STR(string_label, data + " °")
    data = fmv.resolve_value(control_label=string_label)

    assert data == "Hello World °"

def test_fmv_update_tree():
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

def test_fmv_update_tree2():
    tree_label = ("Tree")

    # Unselect previous choices
    fmv.set_value_ARR_STR("Tree", [])
    data = fmv.resolve_value(tree_label)
    assert data == [None]

    # Only select the parent node
    fmv.set_value_ARR_STR("Tree",["Parent"])
    data = fmv.resolve_value(tree_label)
    assert data == ["Parent"]

    # Select the two children nodes
    fmv.set_value_ARR_STR("Tree", ["Child 1","Child 2"])
    data = fmv.resolve_value(tree_label)
    assert data == ["Child 1","Child 2"]

subpanel_label = "Sub Panel"
def test_subpanel_vi():
    sp_vi = sp.get_vi_name("Sub Panel")
    assert sp_vi == "example 4b - child.vi"


def test_sp_update_string():
    # Generate a random plot and query the data insisde it
    string_label = "String"

    sp.set_value_STR(subpanel_label, string_label, "Hello")
    data = sp.get_value(subpanel_label, string_label)
    sp.set_value_STR(subpanel_label, string_label, data + " World")
    data = sp.get_value(subpanel_label, string_label)

    assert data == "Hello World"

def test_sp_update_string2():
    # Generate a random plot and query the data insisde it
    string_label = "String"

    sp.set_value_STR(subpanel_label, string_label, "Hello")
    data = sp.resolve_value(control_label=string_label,subpanel_label=subpanel_label)
    sp.set_value_STR(subpanel_label, string_label, data + " World")
    data = sp.resolve_value(control_label=string_label, subpanel_label=subpanel_label)
    sp.set_value_STR(subpanel_label, string_label, data + " °")
    data = sp.resolve_value(control_label=string_label, subpanel_label=subpanel_label)

    assert data == "Hello World °"

def test_sp_update_tree():
    tree_label = ("Tree")

    # Unselect previous choices
    sp.set_value_ARR_STR(subpanel_label, "Tree", [])
    data = sp.get_value_TREE(subpanel_label, tree_label)
    assert data == []

    # Only select the parent node
    sp.set_value_ARR_STR(subpanel_label, "Tree",["Parent"])
    data = sp.get_value_TREE(subpanel_label, tree_label)
    assert data == ["Parent"]

    # Select the two children nodes
    sp.set_value_ARR_STR(subpanel_label, "Tree", ["Child 1","Child 2"])
    data = sp.get_value_TREE(subpanel_label, tree_label)
    assert data == ["Child 1","Child 2"]

def test_sp_update_tree2():
    tree_label = ("Tree")

    # Unselect previous choices
    sp.set_value_ARR_STR(subpanel_label, "Tree", [])
    data = sp.resolve_value(control_label=tree_label,subpanel_label=subpanel_label)
    assert data == [None]

    # Only select the parent node
    sp.set_value_ARR_STR(subpanel_label, "Tree",["Parent"])
    data = sp.resolve_value(control_label=tree_label,subpanel_label=subpanel_label)
    assert data == ["Parent"]

    # Select the two children nodes
    sp.set_value_ARR_STR(subpanel_label, "Tree", ["Child 1","Child 2"])
    data = sp.resolve_value(control_label=tree_label,subpanel_label=subpanel_label)
    assert data == ["Child 1","Child 2"]

subsubpanel_label = "Sub Panel Children"

def test_subsubpanel_vi():
    ssp_vi = ssp.get_vi_name("Sub Panel","Sub Panel Children")
    assert ssp_vi == "example 4b - grand child.vi"


def test_ssp_update_string():
    # Generate a random plot and query the data insisde it
    string_label = "String"

    ssp.set_value_STR(subpanel_label, subsubpanel_label, string_label,"Hello")
    data = ssp.get_value(subpanel_label, subsubpanel_label, string_label)
    ssp.set_value_STR(subpanel_label, subsubpanel_label, string_label, data + " World")
    data = ssp.get_value(subpanel_label, subsubpanel_label, string_label)

    assert data == "Hello World"

def test_ssp_update_string2():
    # Generate a random plot and query the data insisde it
    string_label = "String"

    ssp.set_value_STR(subpanel_label, subsubpanel_label, string_label,"Hello")
    data = ssp.resolve_value(string_label, subpanel_label, subsubpanel_label)
    ssp.set_value_STR(subpanel_label, subsubpanel_label, string_label, data + " World")
    data = ssp.resolve_value(string_label, subpanel_label, subsubpanel_label)
    ssp.set_value_STR(subpanel_label, subsubpanel_label, string_label, data + " °")
    data = ssp.resolve_value(string_label, subpanel_label, subsubpanel_label)

    assert data == "Hello World °"

def test_ssp_update_tree():
    tree_label = ("Tree")

    # Unselect previous choices
    ssp.set_value_ARR_STR(subpanel_label, subsubpanel_label, "Tree", [])
    data = ssp.get_value_TREE(subpanel_label, subsubpanel_label, tree_label)
    assert data == []

    # Only select the parent node
    ssp.set_value_ARR_STR(subpanel_label, subsubpanel_label, "Tree",["Parent"])
    data = ssp.get_value_TREE(subpanel_label, subsubpanel_label, tree_label)
    assert data == ["Parent"]

    # Select the two children nodes
    ssp.set_value_ARR_STR(subpanel_label, subsubpanel_label, "Tree", ["Child 1","Child 2"])
    data = ssp.get_value_TREE(subpanel_label, subsubpanel_label, tree_label)
    assert data == ["Child 1","Child 2"]


def test_ssp_update_tree2():
    tree_label = ("Tree")

    # Unselect previous choices
    ssp.set_value_ARR_STR(subpanel_label, subsubpanel_label, "Tree", [])
    data = ssp.resolve_value(control_label=tree_label, subpanel_label=subpanel_label,subsubpanel_label=subsubpanel_label)
    assert data == [None]

    # Only select the parent node
    ssp.set_value_ARR_STR(subpanel_label, subsubpanel_label, "Tree",["Parent"])
    data = ssp.resolve_value(control_label=tree_label, subpanel_label=subpanel_label,subsubpanel_label=subsubpanel_label)
    assert data == ["Parent"]

    # Select the two children nodes
    ssp.set_value_ARR_STR(subpanel_label, subsubpanel_label, "Tree", ["Child 1","Child 2"])
    data = ssp.resolve_value(control_label=tree_label, subpanel_label=subpanel_label,subsubpanel_label=subsubpanel_label)
    assert data == ["Child 1","Child 2"]