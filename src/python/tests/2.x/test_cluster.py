# Start the VI "example 7 - cluster" first then run that script
import lv_ui_testing.front_most_vi as fmv
import lv_ui_testing.sub_panel as sp
import lv_ui_testing.sub_sub_panel as ssp


def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = fmv.get_vi_name()
    assert front_most_vi == "example 7 - cluster.vi"

def test_fmv_cluster_details():
    control_settings = fmv.get_cluster_details("Cluster")
    assert control_settings[1]["Visible"] == False

def test_sp_cluster_details():
    control_settings = sp.get_cluster_details("Cluster","Sub Panel")
    assert control_settings[1]["Visible"] == False

def test_ssp_cluster_details():
    control_settings = ssp.get_cluster_details("Cluster","Sub Panel","Sub Panel Children")
    assert control_settings[1]["Visible"] == False


def test_fmv_cluster_write():
    control_settings = fmv.set_cluster_elem("Boolean","BOOL","False",["Cluster"])
    data = fmv.get_value_xml("Cluster")['LvVariant']['Cluster']
    new_bool = data['Boolean'][0]['Val']
    assert new_bool == "0"
    control_settings = fmv.set_cluster_elem("Boolean", "BOOL", "True", ["Cluster"])
    data = fmv.get_value_xml("Cluster")['LvVariant']['Cluster']
    new_bool = data['Boolean'][0]['Val']
    assert new_bool == "1"

def test_fmv_cluster_str_write():
    control_settings = fmv.set_cluster_elem("String","STR","Hello",["Cluster"])
    data = fmv.get_value_xml("Cluster")['LvVariant']['Cluster']
    new_str = data['String']['Val']
    assert new_str == "Hello"
    control_settings = fmv.set_cluster_elem("String", "STR", "World", ["Cluster"])
    data = fmv.get_value_xml("Cluster")['LvVariant']['Cluster']
    new_str = data['String']['Val']
    assert new_str == "World"

def test_fmv_subcluster_write():
    control_settings = fmv.set_cluster_elem("Boolean","BOOL","False",["Cluster","Cluster 2"])
    data = fmv.get_value_xml("Cluster")['LvVariant']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "0"
    control_settings = fmv.set_cluster_elem("Boolean", "BOOL", "True", ["Cluster","Cluster 2"])
    data = fmv.get_value_xml("Cluster")['LvVariant']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "1"

def test_fmv_subsubcluster_write():
    control_settings = fmv.set_cluster_elem("Boolean","BOOL","False",["Cluster","Cluster 2","Cluster 3"])
    data = fmv.get_value_xml("Cluster")['LvVariant']['Cluster']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "0"
    control_settings = fmv.set_cluster_elem("Boolean", "BOOL", "True", ["Cluster","Cluster 2","Cluster 3"])
    data = fmv.get_value_xml("Cluster")['LvVariant']['Cluster']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "1"

def test_sp_cluster_write():
    control_settings = sp.set_cluster_elem("Boolean","BOOL","False",["Cluster"],"Sub Panel")
    data = sp.get_value_xml("Cluster","Sub Panel")['LvVariant']['Cluster']
    new_bool = data['Boolean'][0]['Val']
    assert new_bool == "0"
    control_settings = sp.set_cluster_elem("Boolean", "BOOL", "True", ["Cluster"],"Sub Panel")
    data = sp.get_value_xml("Cluster","Sub Panel")['LvVariant']['Cluster']
    new_bool = data['Boolean'][0]['Val']
    assert new_bool == "1"

def test_sp_cluster_str_write():
    control_settings = sp.set_cluster_elem("String", "STR", "Hello", ["Cluster"], "Sub Panel")
    data = sp.get_value_xml("Cluster", "Sub Panel")['LvVariant']['Cluster']
    new_str = data['String']['Val']
    assert new_str == "Hello"
    control_settings = sp.set_cluster_elem("String", "STR", "World", ["Cluster"], "Sub Panel")
    data = sp.get_value_xml("Cluster", "Sub Panel")['LvVariant']['Cluster']
    new_str = data['String']['Val']
    assert new_str == "World"


def test_sp_subcluster_write():
    control_settings = sp.set_cluster_elem("Boolean","BOOL","False",["Cluster","Cluster 2"],"Sub Panel")
    data = sp.get_value_xml("Cluster","Sub Panel")['LvVariant']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "0"
    control_settings = sp.set_cluster_elem("Boolean", "BOOL", "True", ["Cluster","Cluster 2"],"Sub Panel")
    data = sp.get_value_xml("Cluster","Sub Panel")['LvVariant']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "1"

def test_sp_subsubcluster_write():
    control_settings = sp.set_cluster_elem("Boolean","BOOL","False",["Cluster","Cluster 2","Cluster 3"],"Sub Panel")
    data = sp.get_value_xml("Cluster","Sub Panel")['LvVariant']['Cluster']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "0"
    control_settings = sp.set_cluster_elem("Boolean", "BOOL", "True", ["Cluster","Cluster 2","Cluster 3"],"Sub Panel")
    data = sp.get_value_xml("Cluster","Sub Panel")['LvVariant']['Cluster']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "1"

def test_ssp_cluster_write():
    control_settings = ssp.set_cluster_elem("Boolean","BOOL","False",["Cluster"],"Sub Panel","Sub Panel Children")
    data = ssp.get_value_xml("Cluster","Sub Panel","Sub Panel Children")['LvVariant']['Cluster']
    new_bool = data['Boolean'][0]['Val']
    assert new_bool == "0"
    control_settings = ssp.set_cluster_elem("Boolean", "BOOL", "True", ["Cluster"],"Sub Panel","Sub Panel Children")
    data = ssp.get_value_xml("Cluster","Sub Panel","Sub Panel Children")['LvVariant']['Cluster']
    new_bool = data['Boolean'][0]['Val']
    assert new_bool == "1"

def test_ssp_cluster_str_write():
    control_settings = ssp.set_cluster_elem("String", "STR", "Hello", ["Cluster"], "Sub Panel",
                                                         "Sub Panel Children")
    data = ssp.get_value_xml("Cluster", "Sub Panel", "Sub Panel Children")['LvVariant']['Cluster']
    new_str = data['String']['Val']
    assert new_str == "Hello"

    control_settings = ssp.set_cluster_elem("String", "STR", "World", ["Cluster"], "Sub Panel",
                                                         "Sub Panel Children")
    data = ssp.get_value_xml("Cluster", "Sub Panel", "Sub Panel Children")['LvVariant']['Cluster']
    new_str = data['String']['Val']
    assert new_str == "World"



def test_ssp_subcluster_write():
    control_settings = ssp.set_cluster_elem("Boolean","BOOL","False",["Cluster","Cluster 2"],"Sub Panel","Sub Panel Children")
    data = ssp.get_value_xml("Cluster","Sub Panel","Sub Panel Children")['LvVariant']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "0"
    control_settings = ssp.set_cluster_elem("Boolean", "BOOL", "True", ["Cluster","Cluster 2"],"Sub Panel","Sub Panel Children")
    data = ssp.get_value_xml("Cluster","Sub Panel","Sub Panel Children")['LvVariant']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "1"

def test_ssp_subsubcluster_write():
    control_settings = ssp.set_cluster_elem("Boolean","BOOL","False",["Cluster","Cluster 2","Cluster 3"],"Sub Panel","Sub Panel Children")
    data = ssp.get_value_xml("Cluster","Sub Panel","Sub Panel Children")['LvVariant']['Cluster']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "0"
    control_settings = ssp.set_cluster_elem("Boolean", "BOOL", "True", ["Cluster","Cluster 2","Cluster 3"],"Sub Panel","Sub Panel Children")
    data = ssp.get_value_xml("Cluster","Sub Panel","Sub Panel Children")['LvVariant']['Cluster']['Cluster']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "1"


def test_bug_cluster_1():
    """
    When there was a cluster followed by a n
    :return:
    """