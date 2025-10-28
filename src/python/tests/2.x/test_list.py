# Start the VI "example 13 - lists" first then run that script
import lv_ui_testing.front_most_vi as fmv
import lv_ui_testing.sub_panel as sp
import lv_ui_testing.sub_sub_panel as ssp
import pytest


list_label = "Listbox"
multi_list_label = "Multicolumn Listbox"
subpanel_label = "Sub Panel"
subsubpanel_label =  "Sub Panel Children"

fmv.set_value_DBL(list_label,0)

def test_front_most_vi():
    assert fmv.get_listbox_header(list_label) == "My header"
    assert fmv.get_listbox_item_names(list_label) == ['a', 'b', 'c']

    assert fmv.get_multicolumn_listbox_header(multi_list_label) == (['name', 'age'], [])
    assert fmv.get_multicolumn_listbox_item_names(multi_list_label) == ['Thomas', '32', 'sarah', '26']


def test_sub_panel():
    assert sp.get_listbox_header(list_label,subpanel_label) == "My sub header"
    assert sp.get_listbox_item_names(list_label,subpanel_label) == ['d', 'e', 'f']

    assert sp.get_multicolumn_listbox_header(multi_list_label,subpanel_label) == (['Name', 'age'], [])
    assert sp.get_multicolumn_listbox_item_names(multi_list_label,subpanel_label) == ['Thomas', '32', 'Sarah', '26']


def test_sub_sub_panel():
    assert ssp.get_listbox_header(list_label,subpanel_label,subsubpanel_label) == "My sub sub header"
    assert ssp.get_listbox_item_names(list_label,subpanel_label,subsubpanel_label) == ['g', 'h', 'i']

    assert ssp.get_multicolumn_listbox_header(multi_list_label,subpanel_label,subsubpanel_label) == (['Name', 'Age'], [])
    assert ssp.get_multicolumn_listbox_item_names(multi_list_label,subpanel_label,subsubpanel_label) == ['thomas', '32', 'Sarah', '26']