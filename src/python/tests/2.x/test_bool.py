# Start the VI "example 9 - bool" first then run that script
import lv_ui_testing.front_most_vi as fmv
import lv_ui_testing.sub_panel as sp
import lv_ui_testing.sub_sub_panel as ssp

control_label = "Boolean"
sp_label = "Sub Panel"
ssp_label = "Sub Panel Children"


def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = fmv.get_vi_name()
    assert front_most_vi == "example 9 - bool.vi"


def test_fmv():
    for status in [True, False, True]:
        fmv.set_value_BOOL(control_label,status)
        assert fmv.get_value_bool(control_label) == status

def test_fmv2():
    for status in [True, False, True]:
        fmv.set_value_BOOL(control_label,status)
        assert fmv.resolve_value(control_label) == status


def test_sp():
    for status in [True, False, True]:
        sp.set_value_BOOL(sp_label,control_label,status)
        assert sp.get_value_bool(sp_label,control_label) == status

def test_sp2():
    for status in [True, False, True]:
        sp.set_value_BOOL(sp_label,control_label,status)
        assert sp.resolve_value(control_label=control_label,subpanel_label=sp_label) == status

def test_ssp():
    for status in [True, False, True]:
        ssp.set_value_BOOL(sp_label,ssp_label,control_label,status)
        assert ssp.get_value_bool(sp_label,ssp_label,control_label) == status


def test_ssp2():
    for status in [True, False, True]:
        ssp.set_value_BOOL(sp_label,ssp_label,control_label,status)
        print(ssp.resolve_value(control_label=control_label,subpanel_label=sp_label,subsubpanel_label=ssp_label))
        assert ssp.resolve_value(control_label=control_label,subpanel_label=sp_label,subsubpanel_label=ssp_label) == status