import time
import lv_ui_testing.front_most_vi as fmv
import subprocess
import pytest

@pytest.mark.parametrize(
    "button_name, test_file",
    [
        ("Start test1", "test_plots.py"),
        ("Start test2", "test_values.py"),
        ("Start test3", "test_subpanels.py"),
        ("Start test4", "test_string.py"),
        ("Start test4b", "test_string2.py"),
        ("Start test5", "test_sub_subpanels.py"),
        ("Start test6", "test_visibility.py"),
        ("Start test7", "test_cluster.py"),
        ("Start test8", "test_click.py"),
        ("Start test9", "test_bool.py"),
        ("Start test10", "test_retrieve_data.py"),
        ("Start test11", "test_tabs.py"),
        ("Start test12", "test_enums.py"),
        ("Start test13", "test_list.py"),
        ("Start test14", "test_splitter.py"),
        ("Start test14 (SP)", "test_splitter_SP.py"),
        ("Start test14 (SSP)", "test_splitter_SSP.py"),
    ]
)


def test_labview_examples(button_name, test_file):
    """Generic test launcher for LabVIEW UI examples."""
    fmv.click_on_button(button_name)
    time.sleep(2)
    subprocess.run(["pytest", test_file], check=True)
    fmv.click_on_close()

#
# def test_example_1():
#     fmv.click_on_button("Start test1")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_plots.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
# def test_example_2():
#     fmv.click_on_button("Start test2")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_values.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
#
# def test_example_3():
#     fmv.click_on_button("Start test3")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_subpanels.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
# def test_example_4():
#     fmv.click_on_button("Start test4")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_string.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
# def test_example_4b():
#     fmv.click_on_button("Start test4b")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_string2.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
# def test_example_5():
#     fmv.click_on_button("Start test5")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_sub_subpanels.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
# def test_example_6():
#     fmv.click_on_button("Start test6")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_visibility.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
# def test_example_7():
#     fmv.click_on_button("Start test7")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_cluster.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
# def test_example_8():
#     fmv.click_on_button("Start test8")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_click.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
# def test_example_9():
#     fmv.click_on_button("Start test9")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_bool.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
#
# def test_example_10():
#     fmv.click_on_button("Start test10")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_retrieve_data.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
# def test_example_11():
#     fmv.click_on_button("Start test11")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_tabs.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
# def test_example_12():
#     fmv.click_on_button("Start test12")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_enums.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
#
# def test_example_13():
#     fmv.click_on_button("Start test13")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_list.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
#
# def test_example_14():
#     fmv.click_on_button("Start test14")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_splitter.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
# def test_example_14():
#     fmv.click_on_button("Start test14 (SP)")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_splitter_SP.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()
#
# def test_example_14():
#     fmv.click_on_button("Start test14 (SSP)")
#     time.sleep(2)
#     subprocess.run(["pytest", "test_splitter_SSP.py"], check=True)  # Runs test_example.py using pytest
#     fmv.click_on_close()