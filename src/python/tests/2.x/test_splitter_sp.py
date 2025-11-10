# Start the VI "example 14 - sp" first then run that script
import time

import lv_ui_testing.front_most_vi as fmv
import lv_ui_testing.sub_panel as sp

RESULT_LABEL = "Button clicked"
SP_LABEL = "Sub Panel Children"

def test_pane_1():
    sp.click_on_button(SP_LABEL,"A")
    time.sleep(1)
    assert "A" == sp.resolve_value(subpanel_label=SP_LABEL,control_label=RESULT_LABEL)

def test_pane_2():
    sp.click_on_button(SP_LABEL,"B")
    time.sleep(1)
    assert "B" == sp.resolve_value(subpanel_label=SP_LABEL,control_label=RESULT_LABEL)

def test_pane_3():
    sp.click_on_button(SP_LABEL,"C")
    time.sleep(1)
    assert "C" == sp.resolve_value(subpanel_label=SP_LABEL,control_label=RESULT_LABEL)