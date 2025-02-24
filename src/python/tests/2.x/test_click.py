import lv_ui_testing.front_most_vi as fmv
import lv_ui_testing.sub_panel as sp
import lv_ui_testing.sub_sub_panel as ssp
import pytest
import time

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = fmv.get_vi_name()
    assert front_most_vi == "example 8 - mouse click.vi"


def show_menu_and_toolbar():
    fmv.click_on_button("Show menu")
    fmv.click_on_button("Show toolbar")
    time.sleep(1)

def show_menu_only():
    fmv.click_on_button("Show menu")
    fmv.click_on_button("Hide toolbar")
    time.sleep(1)

def show_toolbar_only():
    fmv.click_on_button("Hide menu")
    fmv.click_on_button("Show toolbar")
    time.sleep(1)

def hide_both():
    fmv.click_on_button("Hide menu")
    fmv.click_on_button("Hide toolbar")
    time.sleep(1)



@pytest.mark.parametrize("label", ["m-label-vis","m-label-unvis","n-label-vis","n-label-unvis"])
def test_fmv(label):
    states = [
        show_menu_and_toolbar,
        show_menu_only,
        show_toolbar_only,
        hide_both
    ]

    for state in states:
        state()
        fmv.click_on_button(label)
        assert fmv.get_value("String") == label, f"Failed for state: {state.__name__}"
        fmv.click_on_button("Reset")
        time.sleep(0.5)

@pytest.mark.parametrize("label", ["m-label-vis","m-label-unvis","n-label-vis","n-label-unvis"])
def test_sp(label):
    subpanel_label = "Sub Panel"
    states = [
        show_menu_and_toolbar,
        show_menu_only,
        show_toolbar_only,
        hide_both
    ]

    for state in states:
        state()
        sp.click_on_button(subpanel_label, label)
        assert sp.get_value(subpanel_label, "String") == label, f"Failed for state: {state.__name__}"
        sp.click_on_button(subpanel_label, "Reset")
        time.sleep(0.5)

@pytest.mark.parametrize("label", ["m-label-vis","m-label-unvis","n-label-vis","n-label-unvis"])
def test_ssp(label):
    subpanel_label = "Sub Panel"
    subsubpanel_label = "Sub Panel Children"
    states = [
        show_menu_and_toolbar,
        show_menu_only,
        show_toolbar_only,
        hide_both
    ]

    for state in states:
        state()
        ssp.click_on_button(subpanel_label, subsubpanel_label, label)
        assert ssp.get_value(subpanel_label, subsubpanel_label, "String") == label, f"Failed for state: {state.__name__}"
        ssp.click_on_button(subpanel_label, subsubpanel_label, "Reset")
        time.sleep(0.5)