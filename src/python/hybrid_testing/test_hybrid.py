# Start the VI main first then run that script
import lv_ui_testing.front_most_vi as fmv
import pytest
import pychrome # pip install pychrome
import time
import requests


# Connect to the remote debugging port
browser = pychrome.Browser(url="http://localhost:9222")

# List available tabs and pick the first one
tab = browser.list_tab()[0]

tab.start()

# Enable required domains
tab.call_method("DOM.enable")
tab.call_method("Runtime.enable")

NUM_OF_ITER = 3


def control_float_calculator(input1, input2, operation="divide", waiting_time=0.5):
    """
    Automates the Float Calculator WebView2 app using pychrome.

    Args:
        input1 (float): First input number.
        input2 (float): Second input number.
        operation (str): Operation to perform ('sum', 'subtract', 'multiply', 'divide').
    """

    # Helper to evaluate JavaScript
    def eval_js(js):
        return tab.call_method("Runtime.evaluate", expression=js)

    # Set input values
    eval_js(f"document.getElementById('input1').value = {input1};")
    eval_js(f"document.getElementById('input2').value = {input2};")

    # Click the operation button
    eval_js(f"document.getElementById('{operation}').click();")

    # Wait for the result to update (adjust if needed)
    time.sleep(waiting_time)


#
# control_float_calculator(1, 2, "sum")
# print(fmv.resolve_value("number"))

@pytest.mark.parametrize("input_1, input_2, expected_sum", [
    (i, j, i + j) for i in range(1, NUM_OF_ITER) for j in range(1, NUM_OF_ITER)
])
def test_sum(input_1, input_2, expected_sum):
    control_float_calculator(input_1, input_2, "sum")
    assert expected_sum == fmv.resolve_value("number")


@pytest.mark.parametrize("input_1, input_2, expected_sub", [
    (i, j, i - j) for i in range(1, NUM_OF_ITER) for j in range(1, NUM_OF_ITER)
])
def test_subtract(input_1, input_2, expected_sub):
    control_float_calculator(input_1, input_2, "subtract")
    assert expected_sub == fmv.resolve_value("number")


@pytest.mark.parametrize("input_1, input_2, expected_mul", [
    (i, j, i * j) for i in range(1, NUM_OF_ITER) for j in range(1, NUM_OF_ITER)
])
def test_mutlitply(input_1, input_2, expected_mul):
    control_float_calculator(input_1, input_2, "multiply")
    assert expected_mul == fmv.resolve_value("number")


@pytest.mark.parametrize("input_1, input_2, expected_div", [
    (i, j, i / j) for i in range(1, NUM_OF_ITER) for j in range(1, NUM_OF_ITER)
])
def test_divide(input_1, input_2, expected_div):
    control_float_calculator(input_1, input_2, "divide")
    assert expected_div == pytest.approx(fmv.resolve_value("number"), rel=1e-12)