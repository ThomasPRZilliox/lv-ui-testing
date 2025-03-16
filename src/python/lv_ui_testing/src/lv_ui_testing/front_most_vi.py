import lv_ui_testing._core as core
import logging
import json
import xmltodict


def get_vi_name():
    logging.info("Send request for front most VI.")
    data = {"message": "FMV_get_vi_name"}
    front_most_vi = core.send_message(data)
    logging.info(f"Received reply from: {front_most_vi}")

    return  front_most_vi

def click_on_button(control_label):
    logging.info(f"Send request to click on control named {control_label}.")
    data = {
        "message": "FMV_click_on_button",
        "payload": control_label
    }
    acknowledgement = core.send_message(data)
    return acknowledgement == "clicked"

def click_on_close():
    logging.info(f"Send request to click on close.")
    data = {
        "message": "FMV_click_on_close"
    }
    acknowledgement = core.send_message(data)
    return acknowledgement == "clicked"



##############
# Get values #
##############

def get_value(control_label, raw = False):
    logging.info(f"Sending request for value of control named {control_label}")
    data = {
        "message": "FMV_get_value",
        "payload": control_label
    }
    control_value = core.send_message(data)
    print(control_value)
    if not raw:
        control_value = control_value.split('=')[1]

    return control_value





def get_control_details():
    logging.info("Send request for front most VI.")
    data = {
        "message": "FMV_get_control_details"
    }
    control_details = core.send_message(data)
    control_details = json.loads(control_details)
    return control_details


def get_value_TREE(control_label):
    message = get_value(control_label, raw = True)
    selected_tree_element = core.decode_tree(message)
    return selected_tree_element

def get_value_DBL(control_label):
    double_string = get_value(control_label)
    return float(double_string)

def get_value_bool(control_label):
    bool_string = get_value(control_label)
    return bool_string == "TRUE"

def get_cluster_details(control_label):
    logging.info("Send request for front most VI.")
    data = {
        "message": "FMV_get_cluster_details",
        "payload": {
            "control": control_label
        }
    }
    control_details = core.send_message(data)
    control_details = json.loads(control_details)
    return control_details

def get_value_xml(control_label, raw = False):
    logging.info(f"Sending request for value of control named {control_label}")
    data = {
        "message": "FMV_get_value_XML",
        "payload": control_label
    }
    control_value = core.send_message(data)
    if raw:
        data = control_value
    else:
        data = xmltodict.parse(control_value)
    return data

def resolve_value (control_label):
    # logging.info(f"Sending request for value of control named {control_label}")
    # data = {
    #     "message": "FMV_get_value_XML",
    #     "payload": control_label
    # }
    # xml_string = core.send_message(data)
    xml_string = get_value_xml(control_label,raw=True)
    return core.parse_lvvariant(xml_string)

#############
# Set Value #
#############

def set_value_STR(control_label,text):
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {
        "message": "FMV_set_value_STR",
        "payload": {
            "name": control_label,
            "value": text
        }
    }
    return core.send_message(data)

def set_value_ARR_STR(control_label,text):
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {
        "message": "FMV_set_value_ARR_STR",
        "payload": {
            "name": control_label,
            "value": text
        }
    }
    return core.send_message(data)

def set_value_DBL(control_label,number):
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {
        "message": "FMV_set_value_DBL",
        "payload": {
            "name": control_label,
            "value": float(number) # LabVIEW might not be happy if it's an integer...
        }
    }
    return core.send_message(data)


def set_value_BOOL(control_label,bool):
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {
        "message": "FMV_set_value_BOOL",
        "payload": {
            "name": control_label,
            "value": bool
        }
    }
    return core.send_message(data)


def set_cluster_elem(control_label, type, value, layers):
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {
        "message": "FMV_set_cluster_elem",
        "payload": {
            "name": control_label,
            "type": type,
            "value": value,
            "layers": layers
        }
    }
    return core.send_message(data)


