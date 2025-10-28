import lv_ui_testing._core as core
import logging
import json
import xmltodict
import time


def get_vi_name():
    """
    Return the front most vi name
    :return: VI name
    """
    logging.info("Send request for front most VI.")
    data = {"message": "FMV_get_vi_name"}
    front_most_vi = core.send_message(data)
    logging.info(f"Received reply from: {front_most_vi}")

    return front_most_vi

def click_on_button(control_label):
    """
    Click on a boolean control
    :param control_label:
    :return:
    """
    logging.info(f"Send request to click on control named {control_label}.")
    data = {
        "message": "FMV_click_on_button",
        "payload": control_label
    }
    acknowledgement = core.send_message(data)
    return acknowledgement == "clicked"

def click_on_close():
    """
    Click on the close button (red cross) of the main window
    :return:
    """
    logging.info(f"Send request to click on close.")
    data = {
        "message": "FMV_click_on_close"
    }
    acknowledgement = core.send_message(data)
    return acknowledgement == "clicked"

#########
# Utils #
#########

def wait_for_window(
    window_name: str,
    waiting_time: float = 0.1,
    maximum_waiting_time: float = 20.0
) -> bool:
    """
    Waits until the specified window becomes the frontmost window.

    Args:
        window_name (str): The target window name to wait for.
        waiting_time (float): Time to wait between checks, in seconds. Default is 0.1.
        maximum_waiting_time (float): Maximum total waiting time, in seconds. Default is 20.

    Returns:
        bool: True if the window appeared within the timeout, False otherwise.
    """
    start_time = time.time()

    while (time.time() - start_time) <= maximum_waiting_time:
        front_most_vi = get_vi_name()
        if front_most_vi == window_name:
            elapsed = time.time() - start_time
            logging.info("Window '%s' is frontmost after %.2f seconds.", window_name, elapsed)
            return True

        logging.debug("Current frontmost window: '%s'", front_most_vi)
        time.sleep(waiting_time)

    logging.warning("Window '%s' did not appear within %.2f seconds.", window_name, maximum_waiting_time)
    return False



##############
# Get values #
##############

def get_value(control_label, raw = False):
    """
    Obsolete method prefer get_value_xml or resolve_value (only works with specific type)
    :param control_label:
    :param raw:
    :return:
    """
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
    """
    Get the Caption, Label visibility and Control visibility of all controls
    :return:
    """
    logging.info("Send request for front most VI.")
    data = {
        "message": "FMV_get_control_details"
    }
    control_details = core.send_message(data)
    control_details = json.loads(control_details)
    return control_details


def get_value_TREE(control_label):
    """
    Obsolete method prefer resolve_value
    :param control_label:
    :return:
    """
    message = get_value(control_label, raw = True)
    selected_tree_element = core.decode_tree(message)
    return selected_tree_element

def get_value_DBL(control_label):
    """
    Obsolete method prefer resolve_value
    :param control_label:
    :return:
    """
    double_string = get_value(control_label)
    return float(double_string)

def get_value_bool(control_label):
    """
    Obsolete method prefer resolve_value
    :param control_label:
    :return:
    """
    bool_string = get_value(control_label)
    return bool_string == "TRUE"

def get_cluster_details(control_label):
    """
    Get the Caption, Label visibility and Control visibility of all controls within a cluster
    :param control_label:
    :return:
    """
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
    """
    Return the XML of a control, recommended way to read a cluster
    :param control_label:
    :param raw:
    :return:
    """
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

def resolve_value(control_label):
    """
    Return the value of a control and parse it to its type for python, for example it will return an U32 if the control is of that type (support Numeric, String, Boolean and Array (of the previous types) controls and indicators)
    :param control_label:
    :return:
    """
    xml_string = get_value_xml(control_label,raw=True)
    return core.parse_lvvariant(xml_string)


def get_listbox_index(control_label):
    """
    Return the index of a list box
    :param control_label:
    :return:
    """

    return resolve_value(control_label)

def _format_get_request(control_label, command):
    data = {
        "message": f"FMV_{command}",
        "payload": control_label
    }
    return data

def get_listbox_item_names(control_label):
    """
    Return the item names (string in the list) of a list box
    :param control_label:
    :return:
    """
    logging.info(f"Sending request for item names of control (listbox) named {control_label}")
    data = _format_get_request(control_label,"get_listbox_item_names")
    item_names_xml = core.send_message(data)
    item_names_dict = xmltodict.parse(item_names_xml)['Array']['String']
    item_names = [el["Val"] for el in item_names_dict]
    return item_names


def get_multicolumn_listbox_item_names(control_label):
    """
    Return the item names (string in the list) of a list box
    :param control_label:
    :return:
    """
    logging.info(f"Sending request for item names of control (multicolumn listbox) named {control_label}")
    data = _format_get_request(control_label,"get_multicolumn_listbox_item_names")
    item_names_xml = core.send_message(data)
    item_names_dict = xmltodict.parse(item_names_xml)['Array']['String']
    item_names = [el["Val"] for el in item_names_dict]
    return item_names

def get_listbox_header(control_label):
    """
    Return the header of a list box
    :param control_label:
    :return:
    """
    logging.info(f"Sending request for header of control (listbox) named {control_label}")
    data = _format_get_request(control_label, "get_listbox_header")
    header_xml = core.send_message(data)
    header = xmltodict.parse(header_xml)['String']['Val']
    return header

def get_multicolumn_listbox_header(control_label):
    """
    Return the header of a list box
    :param control_label:
    :return: header_column, header_row
    """
    logging.info(f"Sending request for header of control (multicolumn listbox) named {control_label}")
    data = _format_get_request(control_label, "get_multicolumn_listbox_header")
    header_xml = core.send_message(data)
    header = xmltodict.parse(header_xml)['Cluster']['Array']
    header_col = [el["Val"] for el in header[0]['String']]
    try:
        header_row = [el["Val"] for el in header[1]['String']]
    except:
        header_row = []
    return header_col, header_row

#############
# Set Value #
#############

def set_value_STR(control_label,text):
    """
    Set a string control
    :param control_label:
    :param text:
    :return:
    """
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
    """
    Set a string array control (for example a tree control)
    :param control_label:
    :param text:
    :return:
    """
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
    """
    Set a numeric control
    :param control_label:
    :param number:
    :return:
    """
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
    """
    Set a boolean control (It will not work if it has a latch mechanism !!)
    :param control_label:
    :param bool:
    :return:
    """
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
    """
    Set an element of a cluster
    :param control_label:
    :param type:
    :param value:
    :param layers:
    :return:
    """
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


