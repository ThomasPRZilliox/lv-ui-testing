# Start the VI "example 7 - cluster" first then run that script
from lv_ui_testing import ui_testing

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = ui_testing.FMV_get_vi_name()
    assert front_most_vi == "example 7 - cluster.vi"

def test_fmv_cluster_details():
    control_settings = ui_testing.FMV_get_cluster_details("Cluster")
    assert control_settings[1]["Visible"] == False

def test_sp_cluster_details():
    control_settings = ui_testing.SP_get_cluster_details("Cluster","Sub Panel")
    assert control_settings[1]["Visible"] == False

def test_ssp_cluster_details():
    control_settings = ui_testing.SSP_get_cluster_details("Cluster","Sub Panel","Sub Panel Children")
    assert control_settings[1]["Visible"] == False


def test_fmv_cluster_write():
    control_settings = ui_testing.FMV_set_cluster_elem("Boolean","BOOL","False",["Cluster"])
    data = ui_testing.FMV_get_value_xml("Cluster")['LvVariant']['Cluster']
    new_bool = data['Boolean'][0]['Val']
    assert new_bool == "0"
    control_settings = ui_testing.FMV_set_cluster_elem("Boolean", "BOOL", "True", ["Cluster"])
    data = ui_testing.FMV_get_value_xml("Cluster")['LvVariant']['Cluster']
    new_bool = data['Boolean'][0]['Val']
    assert new_bool == "1"

def test_fmv_cluster_str_write():
    control_settings = ui_testing.FMV_set_cluster_elem("String","STR","Hello",["Cluster"])
    data = ui_testing.FMV_get_value_xml("Cluster")['LvVariant']['Cluster']
    new_str = data['String']['Val']
    assert new_str == "Hello"
    control_settings = ui_testing.FMV_set_cluster_elem("String", "STR", "World", ["Cluster"])
    data = ui_testing.FMV_get_value_xml("Cluster")['LvVariant']['Cluster']
    new_str = data['String']['Val']
    assert new_str == "World"

def test_fmv_subcluster_write():
    control_settings = ui_testing.FMV_set_cluster_elem("Boolean","BOOL","False",["Cluster","Cluster 2"])
    data = ui_testing.FMV_get_value_xml("Cluster")['LvVariant']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "0"
    control_settings = ui_testing.FMV_set_cluster_elem("Boolean", "BOOL", "True", ["Cluster","Cluster 2"])
    data = ui_testing.FMV_get_value_xml("Cluster")['LvVariant']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "1"

def test_fmv_subsubcluster_write():
    control_settings = ui_testing.FMV_set_cluster_elem("Boolean","BOOL","False",["Cluster","Cluster 2","Cluster 3"])
    data = ui_testing.FMV_get_value_xml("Cluster")['LvVariant']['Cluster']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "0"
    control_settings = ui_testing.FMV_set_cluster_elem("Boolean", "BOOL", "True", ["Cluster","Cluster 2","Cluster 3"])
    data = ui_testing.FMV_get_value_xml("Cluster")['LvVariant']['Cluster']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "1"

def test_sp_cluster_write():
    control_settings = ui_testing.SP_set_cluster_elem("Boolean","BOOL","False",["Cluster"],"Sub Panel")
    data = ui_testing.SP_get_value_xml("Cluster","Sub Panel")['LvVariant']['Cluster']
    new_bool = data['Boolean'][0]['Val']
    assert new_bool == "0"
    control_settings = ui_testing.SP_set_cluster_elem("Boolean", "BOOL", "True", ["Cluster"],"Sub Panel")
    data = ui_testing.SP_get_value_xml("Cluster","Sub Panel")['LvVariant']['Cluster']
    new_bool = data['Boolean'][0]['Val']
    assert new_bool == "1"

def test_sp_cluster_str_write():
    control_settings = ui_testing.SP_set_cluster_elem("String", "STR", "Hello", ["Cluster"], "Sub Panel")
    data = ui_testing.SP_get_value_xml("Cluster", "Sub Panel")['LvVariant']['Cluster']
    new_str = data['String']['Val']
    assert new_str == "Hello"
    control_settings = ui_testing.SP_set_cluster_elem("String", "STR", "World", ["Cluster"], "Sub Panel")
    data = ui_testing.SP_get_value_xml("Cluster", "Sub Panel")['LvVariant']['Cluster']
    new_str = data['String']['Val']
    assert new_str == "World"


def test_sp_subcluster_write():
    control_settings = ui_testing.SP_set_cluster_elem("Boolean","BOOL","False",["Cluster","Cluster 2"],"Sub Panel")
    data = ui_testing.SP_get_value_xml("Cluster","Sub Panel")['LvVariant']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "0"
    control_settings = ui_testing.SP_set_cluster_elem("Boolean", "BOOL", "True", ["Cluster","Cluster 2"],"Sub Panel")
    data = ui_testing.SP_get_value_xml("Cluster","Sub Panel")['LvVariant']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "1"

def test_sp_subsubcluster_write():
    control_settings = ui_testing.SP_set_cluster_elem("Boolean","BOOL","False",["Cluster","Cluster 2","Cluster 3"],"Sub Panel")
    data = ui_testing.SP_get_value_xml("Cluster","Sub Panel")['LvVariant']['Cluster']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "0"
    control_settings = ui_testing.SP_set_cluster_elem("Boolean", "BOOL", "True", ["Cluster","Cluster 2","Cluster 3"],"Sub Panel")
    data = ui_testing.SP_get_value_xml("Cluster","Sub Panel")['LvVariant']['Cluster']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "1"

def test_ssp_cluster_write():
    control_settings = ui_testing.SP_SP_set_cluster_elem("Boolean","BOOL","False",["Cluster"],"Sub Panel","Sub Panel Children")
    data = ui_testing.SP_SP_get_value_xml("Cluster","Sub Panel","Sub Panel Children")['LvVariant']['Cluster']
    new_bool = data['Boolean'][0]['Val']
    assert new_bool == "0"
    control_settings = ui_testing.SP_SP_set_cluster_elem("Boolean", "BOOL", "True", ["Cluster"],"Sub Panel","Sub Panel Children")
    data = ui_testing.SP_SP_get_value_xml("Cluster","Sub Panel","Sub Panel Children")['LvVariant']['Cluster']
    new_bool = data['Boolean'][0]['Val']
    assert new_bool == "1"

def test_ssp_cluster_str_write():
    control_settings = ui_testing.SP_SP_set_cluster_elem("String", "STR", "Hello", ["Cluster"], "Sub Panel",
                                                         "Sub Panel Children")
    data = ui_testing.SP_SP_get_value_xml("Cluster", "Sub Panel", "Sub Panel Children")['LvVariant']['Cluster']
    new_str = data['String']['Val']
    assert new_str == "Hello"

    control_settings = ui_testing.SP_SP_set_cluster_elem("String", "STR", "World", ["Cluster"], "Sub Panel",
                                                         "Sub Panel Children")
    data = ui_testing.SP_SP_get_value_xml("Cluster", "Sub Panel", "Sub Panel Children")['LvVariant']['Cluster']
    new_str = data['String']['Val']
    assert new_str == "World"



def test_ssp_subcluster_write():
    control_settings = ui_testing.SP_SP_set_cluster_elem("Boolean","BOOL","False",["Cluster","Cluster 2"],"Sub Panel","Sub Panel Children")
    data = ui_testing.SP_SP_get_value_xml("Cluster","Sub Panel","Sub Panel Children")['LvVariant']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "0"
    control_settings = ui_testing.SP_SP_set_cluster_elem("Boolean", "BOOL", "True", ["Cluster","Cluster 2"],"Sub Panel","Sub Panel Children")
    data = ui_testing.SP_SP_get_value_xml("Cluster","Sub Panel","Sub Panel Children")['LvVariant']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "1"

def test_ssp_subsubcluster_write():
    control_settings = ui_testing.SP_SP_set_cluster_elem("Boolean","BOOL","False",["Cluster","Cluster 2","Cluster 3"],"Sub Panel","Sub Panel Children")
    data = ui_testing.SP_SP_get_value_xml("Cluster","Sub Panel","Sub Panel Children")['LvVariant']['Cluster']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "0"
    control_settings = ui_testing.SP_SP_set_cluster_elem("Boolean", "BOOL", "True", ["Cluster","Cluster 2","Cluster 3"],"Sub Panel","Sub Panel Children")
    data = ui_testing.SP_SP_get_value_xml("Cluster","Sub Panel","Sub Panel Children")['LvVariant']['Cluster']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "1"