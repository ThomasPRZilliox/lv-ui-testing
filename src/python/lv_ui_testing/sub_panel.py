import lv_ui_testing._core as core
import logging

def get_vi_name(subpanel_label):
    logging.info("Send request for subpanel VI.")
    data = {"message": "SP_get_vi_name",
            "payload": subpanel_label
            }
    subpanel_vi = core.send_message(data)
    logging.info(f"VI in subpanel is {subpanel_vi}")

    return  subpanel_vi

def click_on_button(subpanel_label,control_label):
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

def get_value_TREE(subpanel_label,control_label):
    logging.info(f"Sending request for subpanel VI for value of control named {control_label}")
    message = get_value(subpanel_label,control_label, raw=True)
    selected_tree_element = core.decode_tree(message)

    return selected_tree_element


def get_value_DBL(subpanel_label,control_label):
    double_string = get_value(subpanel_label, control_label)
    result_double = float(double_string)
    return result_double

def get_value_bool(subpanel_label,control_label):
    bool_string = get_value(subpanel_label, control_label)
    return bool_string == "TRUE"



##############
# Set values #
##############

def set_value_DBL(subpanel_label,control_label,number):
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
