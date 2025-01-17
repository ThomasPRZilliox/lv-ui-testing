# Start the VI "example 1 - Plot" first then run that script
import importlib.util
import sys
spec = importlib.util.spec_from_file_location("lv_ui_testing", "../src/lv_ui_testing/ui_testing.py")
ui_testing = importlib.util.module_from_spec(spec)
sys.modules["lv_ui_testing"] = ui_testing
spec.loader.exec_module(ui_testing)

def test_front_most_vi():
    # Ask the tester daemon what is the front most VI
    front_most_vi = ui_testing.FMV_get_vi_name()
    assert front_most_vi == "example 7 - cluster.vi"

def test_cluster_write():
    control_settings = ui_testing.FMV_set_cluster_elem("Boolean","BOOL","True",["Cluster"])
    data = ui_testing.FMV_get_value_xml("Cluster")['LvVariant']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "1"
    control_settings = ui_testing.FMV_set_cluster_elem("Boolean", "BOOL", "False", ["Cluster"])
    data = ui_testing.FMV_get_value_xml("Cluster")['LvVariant']['Cluster']
    new_bool = data['Boolean']['Val']
    assert new_bool == "0"

def test_subcluster_write():
    control_settings = ui_testing.FMV_set_cluster_elem("Boolean","BOOL","True",["Cluster","Cluster 2"])
    assert True
    control_settings = ui_testing.FMV_set_cluster_elem("Boolean", "BOOL", "False", ["Cluster","Cluster 2"])

def test_subsubcluster_write():
    control_settings = ui_testing.FMV_set_cluster_elem("Boolean","BOOL","True",["Cluster","Cluster 2","Cluster 3"])
    assert True
    control_settings = ui_testing.FMV_set_cluster_elem("Boolean", "BOOL", "False", ["Cluster","Cluster 2","Cluster 3"])