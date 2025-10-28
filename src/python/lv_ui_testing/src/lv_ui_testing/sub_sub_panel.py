import lv_ui_testing._core as core
import logging
import json
import xmltodict

def get_vi_name(subpanel_label,subsubpanel_label):
    """
    Return the VI name of loaded VI in a specific subsubpanel of the front most vi name
    :param subpanel_label:
    :param subsubpanel_label:
    :return: VI name
    """
    logging.info("Send request for subpanel VI.")
    data = {"message": "SP_SP_get_vi_name",
            "payload": {
                    "subpanel": subpanel_label,
                    "subsubpanel": subsubpanel_label
                }
            }
    subpanel_vi = core.send_message(data)
    logging.info(f"VI in subpanel is {subpanel_vi}")
    return subpanel_vi


def click_on_button(subpanel_label,subsubpanel_label,control_label):
    """
    Click on a boolean control
    :param subpanel_label:
    :param subsubpanel_label:
    :param control_label:
    :return:
    """
    logging.info(f"Send request to click on control named {control_label}.")
    data = {"message": "SP_SP_click_on_button",
            "payload":
                {
                    "subpanel": subpanel_label,
                    "subsubpanel": subsubpanel_label,
                    "control": control_label
                }
            }
    acknowledgement = core.send_message(data)
    return acknowledgement == "clicked"

##############
# Get values #
##############

def get_value(subpanel_label,subsubpanel_label,control_label, raw = False):
    """
    Obsolete method prefer get_value_xml or resolve_value (only works with specific type)
    :param subpanel_label:
    :param subsubpanel_label:
    :param control_label:
    :param raw:
    :return:
    """
    logging.info("Send request for subpanel VI.")
    data = {"message": "SP_SP_get_value",
            "payload": {
                "subpanel": subpanel_label,
                "subsubpanel": subsubpanel_label,
                "control": control_label
            }
            }
    control_value = core.send_message(data)
    if not raw:
        control_value = control_value.split('=')[1]

    return control_value


def get_value_DBL(subpanel_label,subsubpanel_label,control_label):
    """
    Obsolete method prefer resolve_value
    :param subpanel_label:
    :param subsubpanel_label:
    :param control_label:
    :return:
    """
    double_string = get_value(subpanel_label,subsubpanel_label, control_label)
    return float(double_string)

def get_value_bool(subpanel_label,subsubpanel_label,control_label):
    """
    Obsolete method prefer resolve_value
    :param subpanel_label:
    :param subsubpanel_label:
    :param control_label:
    :return:
    """
    bool_string = get_value(subpanel_label,subsubpanel_label, control_label)
    return bool_string == "TRUE"

def get_control_details(subpanel_label,subsubpanel_label):
    """
    Get the Caption, Label visibility and Control visibility of all controls
    :param subpanel_label:
    :param subsubpanel_label:
    :return:
    """
    logging.info("Send request for front most VI.")
    data = {
        "message": "SP_SP_get_control_details",
        "payload": {
            "subpanel": subpanel_label,
            "subsubpanel": subsubpanel_label
        }
    }
    control_details = core.send_message(data)
    control_details = json.loads(control_details)
    return control_details

def get_cluster_details(control_label,subpanel_label,subsubpanel_label):
    """
    Get the Caption, Label visibility and Control visibility of all controls within a cluster
    :param control_label:
    :param subpanel_label:
    :param subsubpanel_label:
    :return:
    """
    logging.info("Send request for front most VI.")
    json_message = '{"message":"SSP_get_cluster_details"}'

    data = {
        "message": "SSP_get_cluster_details",
        "payload": {
            "control": control_label,
            "subpanel": subpanel_label,
            "subsubpanel": subsubpanel_label
        }
    }
    control_details = core.send_message(data)
    control_details = json.loads(control_details)
    return control_details

def get_value_xml(control_label, subpanel_label,subsubpanel_label ,raw = False):
    """
    Return the XML of a control, recommended way to read a cluster
    :param control_label:
    :param subpanel_label:
    :param subsubpanel_label:
    :param raw:
    :return:
    """
    logging.info(f"Sending request for value of control named {control_label}")
    data = {
        "message": "SSP_get_value_XML",
        "payload": {
            "control": control_label,
            "subpanel": subpanel_label,
            "subsubpanel": subsubpanel_label,
        }
    }
    control_value = core.send_message(data)
    if raw:
        data = control_value
    else:
        data = xmltodict.parse(control_value)
    return data

def resolve_value (control_label, subpanel_label, subsubpanel_label):
    """
    Return the value of a control and parse it to its type for python, for example it will return an U32 if the control is of that type (support Numeric, String, Boolean and Array (of the previous types) controls and indicators)
    :param control_label:
    :param subpanel_label:
    :param subsubpanel_label:
    :return:
    """
    xml_string = get_value_xml(control_label,subpanel_label,subsubpanel_label,raw=True)
    return core.parse_lvvariant(xml_string)


def get_value_TREE(subpanel_label,subsubpanel_label,control_label):
    """
    Obsolete method prefer resolve_value
    :param subpanel_label:
    :param subsubpanel_label:
    :param control_label:
    :return:
    """
    logging.info(f"Sending request for subpanel VI for value of control named {control_label}")
    message = get_value(subpanel_label,subsubpanel_label,control_label, raw=True)
    selected_tree_element = core.decode_tree(message)
    return selected_tree_element

def get_listbox_index(control_label, subpanel_label, subsubpanel_label):
    """
    Return the index of a list box
    :param control_label:
    :param subpanel_label:
    :param subsubpanel_label:
    :return:
    """

    return resolve_value(control_label, subpanel_label, subsubpanel_label)


def _format_get_request(control_label, subpanel_label, subsubpanel_label, command):
    data = {
        "message": f"SSP_{command}",
        "payload": {
            "control": control_label,
            "subpanel": subpanel_label,
            "subsubpanel": subsubpanel_label,
        }
    }
    return data

def get_listbox_item_names(control_label, subpanel_label, subsubpanel_label):
    """
    Return the item names (string in the list) of a list box
    :param control_label:
    :param subpanel_label:
    :param subsubpanel_label:
    :return:
    """
    logging.info(f"Sending request for item names of control (listbox) named {control_label}")
    data = _format_get_request(control_label, subpanel_label, subsubpanel_label, command="get_listbox_item_names")
    item_names_xml = core.send_message(data)
    item_names_dict = xmltodict.parse(item_names_xml)['Array']['String']
    item_names = [el["Val"] for el in item_names_dict]
    return item_names

def get_listbox_header(control_label, subpanel_label, subsubpanel_label):
    """
    Return the header of a list box
    :param control_label:
    :param subpanel_label:
    :param subsubpanel_label:
    :return:
    """
    logging.info(f"Sending request for header of control (listbox) named {control_label}")
    data = _format_get_request(control_label, subpanel_label, subsubpanel_label, command="get_listbox_header")
    item_names_xml = core.send_message(data)
    header = xmltodict.parse(item_names_xml)['String']['Val']
    return header

def get_multicolumn_listbox_item_names(control_label, subpanel_label, subsubpanel_label):
    """
    Return the item names (string in the list) of a list box
    :param control_label:
    :param subpanel_label:
    :param subsubpanel_label:
    :return:
    """
    logging.info(f"Sending request for item names of control (multicolumn listbox) named {control_label}")
    data = _format_get_request(control_label,subpanel_label, subsubpanel_label,"get_multicolumn_listbox_item_names")
    item_names_xml = core.send_message(data)
    item_names_dict = xmltodict.parse(item_names_xml)['Array']['String']
    item_names = [el["Val"] for el in item_names_dict]
    return item_names

def get_multicolumn_listbox_header(control_label, subpanel_label, subsubpanel_label):
    """
    Return the header of a list box
    :param control_label:
    :param subpanel_label:
    :param subsubpanel_label:
    :return: header_column, header_row
    """
    logging.info(f"Sending request for header of control (multicolumn listbox) named {control_label}")
    data = _format_get_request(control_label,subpanel_label, subsubpanel_label, "get_multicolumn_listbox_header")
    header_xml = core.send_message(data)
    header = xmltodict.parse(header_xml)['Cluster']['Array']
    header_col = [el["Val"] for el in header[0]['String']]
    try:
        header_row = [el["Val"] for el in header[1]['String']]
    except:
        header_row = []
    return header_col, header_row


##############
# Set values #
##############

def set_value_STR(subpanel_label,subsubpanel_label,control_label,value):
    """
    Set a string control
    :param subpanel_label:
    :param subsubpanel_label:
    :param control_label:
    :param value:
    :return:
    """
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {
        "message":"SP_SP_set_value_STR",
        "payload": {
            "subpanel": subpanel_label,
            "subsubpanel":subsubpanel_label,
            "control": control_label,
            "value": value
        }
    }
    return core.send_message(data)

def set_value_ARR_STR(subpanel_label,subsubpanel_label,control_label,text):
    """
    Set a string array control (for example, a tree control)
    :param subpanel_label:
    :param subsubpanel_label:
    :param control_label:
    :param text:
    :return:
    """
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {
        "message": "SP_SP_set_value_ARR_STR",
        "payload": {
            "subpanel": subpanel_label,
            "subsubpanel":subsubpanel_label,
            "control": control_label,
            "value": text
        }
    }
    return core.send_message(data)

def set_value_DBL(subpanel_label,subsubpanel_label,control_label,number):
    """
    Set a numeric control
    :param subpanel_label:
    :param subsubpanel_label:
    :param control_label:
    :param number:
    :return:
    """
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {
        "message":"SP_SP_set_value_DBL",
        "payload": {
            "subpanel": subpanel_label,
            "subsubpanel": subsubpanel_label,
            "control": control_label,
            "value": float(number) # LabVIEW might not be happy if it's an integer...
        }
    }
    return core.send_message(data)


def set_value_BOOL(subpanel_label,subsubpanel_label,control_label,bool):
    """
    Set a boolean control (It will not work if it has a latch mechanism !!)
    :param subpanel_label:
    :param subsubpanel_label:
    :param control_label:
    :param bool:
    :return:
    """
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {
        "message":"SSP_set_value_BOOL",
        "payload": {
            "subpanel": subpanel_label,
            "subsubpanel": subsubpanel_label,
            "control": control_label,
            "value": bool
        }
    }
    return core.send_message(data)


def set_cluster_elem(control_label, type, value, layers, subpanel_label, subsubpanel_label):
    """
    Set an element of a cluster
    :param control_label:
    :param type:
    :param value:
    :param layers:
    :param subpanel_label:
    :param subsubpanel_label:
    :return:
    """
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {
        "message": "SSP_set_cluster_elem",
        "payload": {
            "name": control_label,
            "type": type,
            "value": value,
            "layers": layers,
            "subpanel": subpanel_label,
            "subsubpanel": subsubpanel_label
        }
    }
    return core.send_message(data)