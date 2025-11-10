# Start the VI "example 14 - sp" first then run that script
import time

import lv_ui_testing.front_most_vi as fmv
import lv_ui_testing.sub_panel as sp
import lv_ui_testing.sub_sub_panel as ssp

RESULT_LABEL = "Button clicked"
SP_LABEL = "Sub Panel Children"
SSP_LABEL = "Sub Sub Panel Children"

def test_pane_1():
    ssp.click_on_button(subpanel_label=SP_LABEL, subsubpanel_label=SSP_LABEL, control_label="A")
    time.sleep(1)
    assert "A" == ssp.resolve_value(subpanel_label=SP_LABEL, subsubpanel_label=SSP_LABEL, control_label=RESULT_LABEL)

def test_pane_2():
    ssp.click_on_button(subpanel_label=SP_LABEL, subsubpanel_label=SSP_LABEL, control_label="B")
    time.sleep(1)
    assert "B" == ssp.resolve_value(subpanel_label=SP_LABEL, subsubpanel_label=SSP_LABEL, control_label=RESULT_LABEL)

def test_pane_3():
    ssp.click_on_button(subpanel_label=SP_LABEL, subsubpanel_label=SSP_LABEL, control_label="C")
    time.sleep(1)
    assert "C" == ssp.resolve_value(subpanel_label=SP_LABEL, subsubpanel_label=SSP_LABEL, control_label=RESULT_LABEL)