import lv_ui_testing._core as core
import logging
import json
import xmltodict


def get_vi_name(subpanel_label):
    """
    Return the VI name of the VI loaded in a specific subpanel of the front most vi name
    :param subpanel_label:
    :return: VI name
    """
    logging.info("Send request for subpanel VI.")
    data = {"message": "SP_get_vi_name",
            "payload": subpanel_label
            }
    subpanel_vi = core.send_message(data)
    logging.info(f"VI in subpanel is {subpanel_vi}")

    return  subpanel_vi

def click_on_button(subpanel_label,control_label):
    """
    Click on a boolean control
    :param subpanel_label:
    :param control_label:
    :return:
    """
    logging.info(f"Send request to click on control named {control_label}.")
    data = {"message": "SP_click_on_button",
            "payload":
                {
                    "subpanel": subpanel_label,
                    "control": control_label
                }
            }
    acknowledgement = core.send_message(data)
    return acknowledgement == "clicked"


##############
# Get values #
##############

def get_value(subpanel_label,control_label,raw=False):
    """
    Obsolete method prefer get_value_xml or resolve_value (only works with specific type)
    :param subpanel_label:
    :param control_label:
    :param raw:
    :return:
    """
    logging.info("Send request for subpanel VI.")
    data = {"message": "SP_get_value",
            "payload": {
                "subpanel":subpanel_label,
                "control": control_label
                }
            }
    control_value = core.send_message(data)
    if not raw:
        control_value = control_value.split('=')[1]

    return control_value

def get_control_details(subpanel_label):
    """
    Get the Caption, Label visibility and Control visibility of all controls
    :param subpanel_label:
    :return:
    """
    logging.info("Send request for subpanel VI.")
    data = {
        "message": "SP_get_control_details",
        "payload":  subpanel_label
    }
    control_details = core.send_message(data)
    control_details = json.loads(control_details)
    return control_details



def get_value_TREE(subpanel_label,control_label):
    """
    Obsolete value prefer get_value_xml or resolve_value
    :param subpanel_label:
    :param control_label:
    :return:
    """
    logging.info(f"Sending request for subpanel VI for value of control named {control_label}")
    message = get_value(subpanel_label,control_label, raw=True)
    selected_tree_element = core.decode_tree(message)
    return selected_tree_element


def get_value_DBL(subpanel_label,control_label):
    """
    Obsolete method prefer resolve_value
    :param subpanel_label:
    :param control_label:
    :return:
    """
    double_string = get_value(subpanel_label, control_label)
    return float(double_string)

def get_value_bool(subpanel_label,control_label):
    """
    Obsolete method prefer resolve_value
    :param subpanel_label:
    :param control_label:
    :return:
    """
    bool_string = get_value(subpanel_label, control_label)
    return bool_string == "TRUE"


def get_cluster_details(control_label,subpanel_label):
    """
    Get the Caption, Label visibility and Control visibility of all controls within a cluster
    :param control_label:
    :param subpanel_label:
    :return:
    """
    logging.info("Send request for front most VI.")
    data = {
        "message": "SP_get_cluster_details",
        "payload": {
            "control": control_label,
            "subpanel": subpanel_label
        }
    }
    control_details = core.send_message(data)
    control_details = json.loads(control_details)
    return control_details

def get_value_xml(control_label, subpanel_label, raw = False):
    """
    Return the XML of a control, recommended way to read a cluster
    :param control_label:
    :param subpanel_label:
    :param raw:
    :return:
    """
    logging.info(f"Sending request for value of control named {control_label}")
    data = {
        "message": "SP_get_value_XML",
        "payload": {
            "control": control_label,
            "subpanel": subpanel_label
        }
    }
    control_value = core.send_message(data)
    if raw:
        data = control_value
    else:
        data = xmltodict.parse(control_value)
    return data

def resolve_value (control_label, subpanel_label):
    """
    Return the value of a control and parse it to its type for python, for example it will return an U32 if the control is of that type (support Numeric, String, Boolean and Array (of the previous types) controls and indicators)
    :param control_label:
    :param subpanel_label:
    :return:
    """
    xml_string = get_value_xml(control_label,subpanel_label,raw=True)
    return core.parse_lvvariant(xml_string)

##############
# Set values #
##############

def set_value_DBL(subpanel_label,control_label,number):
    """
    Set a numeric control
    :param subpanel_label:
    :param control_label:
    :param number:
    :return:
    """
    logging.info(f"Sending request for value update of control named {control_label}")
    number = float(number)
    data = {
        "message": "SP_set_value_DBL",
        "payload": {
            "subpanel": subpanel_label,
            "control": control_label,
            "value": float(number) # LabVIEW might not be happy if it's an integer...
        }
    }
    return core.send_message(data)


def set_value_BOOL(subpanel_label,control_label,bool):
    """
    Set a boolean control (It will not work if it has a latch mechanism !!)
    :param subpanel_label:
    :param control_label:
    :param bool:
    :return:
    """
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {
        "message": "SP_set_value_BOOL",
        "payload": {
            "subpanel": subpanel_label,
            "control": control_label,
            "value": bool
        }
    }
    return core.send_message(data)


def set_value_STR(subpanel_label,control_label,text):
    """
    Set a string control
    :param subpanel_label:
    :param control_label:
    :param text:
    :return:
    """
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {
        "message": "SP_set_value_STR",
        "payload": {
            "subpanel": subpanel_label,
            "control": control_label,
            "value": text
        }
    }
    return core.send_message(data)


def set_value_ARR_STR(subpanel_label,control_label,text):
    """
    Set a string array control (for example, a tree control)
    :param subpanel_label:
    :param control_label:
    :param text:
    :return:
    """
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {
        "message": "SP_set_value_ARR_STR",
        "payload": {
            "subpanel": subpanel_label,
            "control": control_label,
            "value": text
        }
    }
    return core.send_message(data)


def set_cluster_elem(control_label, type, value, layers, subpanel_label):
    """
    Set an element of a cluster
    :param control_label:
    :param type:
    :param value:
    :param layers:
    :param subpanel_label:
    :return:
    """
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {
        "message": "SP_set_cluster_elem",
        "payload": {
            "name": control_label,
            "type": type,
            "value": value,
            "layers": layers,
            "subpanel": subpanel_label
        }
    }
    return core.send_message(data)
