# Start the VI "example 6 - visibility" first then run that script
import lv_ui_testing.front_most_vi as fmv
import lv_ui_testing.sub_panel as sp
import lv_ui_testing.sub_sub_panel as ssp

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = fmv.get_vi_name()
    assert front_most_vi == "example 6 - visibility.vi"

def test_visibility_fmv():
    control_settings = fmv.get_control_details()
    assert control_settings == [
        {"Caption":"caption - not visible","Label":"Visible - Caption off","Visible":True},
        {"Caption":"Visible - Caption on","Label":"Visible - Caption on","Visible":True},
        {"Caption":"caption - not visible","Label":"Invisible - Caption off","Visible":False},
        {"Caption":"Invisible - Caption on","Label":"Invisible - Caption on","Visible":False},
        {"Caption":"caption - not visible","Label":"Sub Panel","Visible":True}
    ]


def test_visibility_sp():
    sp_vi = sp.get_vi_name("Sub Panel")
    assert sp_vi == "example 6 - child.vi"
    control_settings = sp.get_control_details("Sub Panel")
    assert control_settings == [
        {"Caption":"caption - not visible","Label":"Visible - Caption off","Visible":True},
        {"Caption":"Visible - Caption on","Label":"Visible - Caption on","Visible":True},
        {"Caption":"caption - not visible","Label":"Invisible - Caption off","Visible":False},
        {"Caption":"Invisible - Caption on","Label":"Invisible - Caption on","Visible":False},
        {"Caption":"caption - not visible","Label":"Sub Panel Children","Visible":True}
    ]


def test_visibility_sp_sp():
    ssp_vi = ssp.get_vi_name("Sub Panel","Sub Panel Children")
    assert ssp_vi == "example 6 - grand child.vi"
    control_settings = ssp.get_control_details("Sub Panel","Sub Panel Children")
    assert control_settings == [
        {"Caption":"caption - not visible","Label":"Visible - Caption off","Visible":True},
        {"Caption":"Visible - Caption on","Label":"Visible - Caption on","Visible":True},
        {"Caption":"caption - not visible","Label":"Invisible - Caption off","Visible":False},
        {"Caption":"Invisible - Caption on","Label":"Invisible - Caption on","Visible":False}
    ]