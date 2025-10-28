# Start the VI "example 14 - splitters" first then run that script
import time

import lv_ui_testing.front_most_vi as fmv

RESULT_LABEL = "Button clicked"

def test_pane_1():
    fmv.click_on_button("A")
    time.sleep(5)
    assert "A" == fmv.resolve_value(RESULT_LABEL)

def test_pane_2():
    fmv.click_on_button("B")
    time.sleep(5)
    assert "B" == fmv.resolve_value(RESULT_LABEL)

def test_pane_3():
    fmv.click_on_button("C")
    time.sleep(5)
    assert "C" == fmv.resolve_value(RESULT_LABEL)