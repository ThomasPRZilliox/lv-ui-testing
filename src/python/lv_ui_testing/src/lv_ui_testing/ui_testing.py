import zmq
import logging
import json
import xmltodict

# Configure logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

# Configure 0MQ
context = zmq.Context()

#  Socket to talk to server
print("Connecting to LabVIEW server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# All the methods for the communication

def decode_value_update(socket):
    #  Get the reply.
    message = socket.recv()
    if("Value set !" == message.decode("utf-8")):
        logging.info(f"Update successful !")
    else:
        logging.info(f"Something went wrong with the update...")


# All methods related to the Front Most Vis

def FMV_get_vi_name():
    logging.info("Send request for front most VI.")
    json = '{"message":"FMV_get_vi_name"}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    front_most_vi = message.decode("utf-8")
    logging.info(f"Received reply {front_most_vi}")
    return  front_most_vi

def FMV_get_control_details():
    logging.info("Send request for front most VI.")
    json_message = '{"message":"FMV_get_control_details"}'
    socket.send(json_message.encode())

    #  Get the reply.
    message = socket.recv()
    control_details = message.decode("utf-8")
    # logging.info(f"Received reply {front_most_vi}")
    control_details = json.loads(control_details)
    return  control_details

def FMV_get_cluster_details(control_label):
    logging.info("Send request for front most VI.")
    json_message = '{"message":"FMV_get_cluster_details"}'

    data = {
        "message": "FMV_get_cluster_details",
        "payload": {
            "control": control_label
        }
    }
    data_json = json.dumps(data)
    socket.send(data_json.encode())

    #  Get the reply.
    message = socket.recv()
    control_details = message.decode("utf-8")
    # logging.info(f"Received reply {front_most_vi}")
    control_details = json.loads(control_details)
    return  control_details

def SP_get_cluster_details(control_label,subpanel_label):
    logging.info("Send request for front most VI.")
    json_message = '{"message":"SP_get_cluster_details"}'

    data = {
        "message": "SP_get_cluster_details",
        "payload": {
            "control": control_label,
            "subpanel": subpanel_label
        }
    }
    data_json = json.dumps(data)
    socket.send(data_json.encode())

    #  Get the reply.
    message = socket.recv()
    control_details = message.decode("utf-8")
    # logging.info(f"Received reply {front_most_vi}")
    control_details = json.loads(control_details)
    return  control_details

def SSP_get_cluster_details(control_label,subpanel_label,subsubpanel_label):
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
    data_json = json.dumps(data)
    socket.send(data_json.encode())

    #  Get the reply.
    message = socket.recv()
    control_details = message.decode("utf-8")
    # logging.info(f"Received reply {front_most_vi}")
    control_details = json.loads(control_details)
    return  control_details

def FMV_click_on_button(control_label):
    logging.info(f"Send request to click on control named {control_label}.")
    json = '{"message":"FMV_click_on_button","payload":"'+ control_label +'"}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    return message.decode("utf-8") == "clicked"

def FMV_get_value(control_label, raw = False):
    logging.info(f"Sending request for value of control named {control_label}")
    json = '{"message":"FMV_get_value","payload":"'+ control_label + '"}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    if raw:
        data = message.decode("utf-8")
    else:
        data = message.decode("utf-8").split('=')[1]

    return data

def FMV_get_value_xml(control_label, raw = False):
    logging.info(f"Sending request for value of control named {control_label}")
    json = '{"message":"FMV_get_value_XML","payload":"'+ control_label + '"}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    if raw:
        data = message.decode("utf-8")
    else:
        data = xmltodict.parse(message.decode("utf-8"))

    return data


def SP_get_value_xml(control_label, subpanel_label, raw = False):
    logging.info(f"Sending request for value of control named {control_label}")
    # json = '{"message":"SP_get_value_XML","payload":{"subpanel":"' + subpanel_label + '","control":"' + control_label + '"}}'
    data = {
        "message": "SP_get_value_XML",
        "payload": {
            "control": control_label,
            "subpanel": subpanel_label
        }
    }
    data_json = json.dumps(data)
    socket.send(data_json.encode())

    #  Get the reply.
    message = socket.recv()
    if raw:
        data = message.decode("utf-8")
    else:
        data = xmltodict.parse(message.decode("utf-8"))

    return data

def SP_SP_get_value_xml(control_label, subpanel_label,subsubpanel_label ,raw = False):
    logging.info(f"Sending request for value of control named {control_label}")
    data = {
        "message": "SSP_get_value_XML",
        "payload": {
            "control": control_label,
            "subpanel": subpanel_label,
            "subsubpanel": subsubpanel_label,
        }
    }
    data_json = json.dumps(data)
    socket.send(data_json.encode())

    #  Get the reply.
    message = socket.recv()
    if raw:
        data = message.decode("utf-8")
    else:
        data = xmltodict.parse(message.decode("utf-8"))

    return data

def decode_tree(message):
    data = message.decode("utf-8").split("Tree")[2:]  # To remove the space before the first tree word and the tree size

    selected_tree_element = []
    for element in data:
        selected_tree_element.append(element.split("=")[1])

    return selected_tree_element

def FMV_get_value_TREE(control_label):
    logging.info(f"Sending request for value of control named {control_label}")
    json = '{"message":"FMV_get_value","payload":"'+ control_label + '"}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    selected_tree_element = decode_tree(message)

    return selected_tree_element

def FMV_get_value_DBL(control_label):
    double_string = FMV_get_value(control_label)
    result_double = float(double_string)
    return result_double

def FMV_get_value_bool(control_label):
    bool_string = FMV_get_value(control_label)
    return bool_string == "TRUE"




def FMV_set_cluster_elem(control_label,type,value,layers):
    logging.info(f"Sending request for value update of control named {control_label}")
    # json = '{"message":"FMV_set_value_ARR_STR","payload":{"name":"' + control_label + '","value":"'+ text +'"}}'
    data = {"message": "FMV_set_cluster_elem", "payload": {"name": control_label, "type": type, "value": value, "layers":layers}}
    data_json = json.dumps(data)
    socket.send(data_json.encode())
    decode_value_update(socket)


def SP_set_cluster_elem(control_label,type,value,layers,subpanel_label):
    logging.info(f"Sending request for value update of control named {control_label}")
    # json = '{"message":"FMV_set_value_ARR_STR","payload":{"name":"' + control_label + '","value":"'+ text +'"}}'
    data = {
        "message": "SP_set_cluster_elem",
        "payload": {
            "name": control_label,
            "type": type,
            "value": value,
            "layers":layers,
            "subpanel": subpanel_label
        }
    }
    data_json = json.dumps(data)
    socket.send(data_json.encode())
    decode_value_update(socket)

def SP_SP_set_cluster_elem(control_label,type,value,layers,subpanel_label,subsubpanel_label):
    logging.info(f"Sending request for value update of control named {control_label}")
    # json = '{"message":"FMV_set_value_ARR_STR","payload":{"name":"' + control_label + '","value":"'+ text +'"}}'
    data = {
        "message": "SSP_set_cluster_elem",
        "payload": {
            "name": control_label,
            "type": type,
            "value": value,
            "layers":layers,
            "subpanel": subpanel_label,
            "subsubpanel": subsubpanel_label
        }
    }
    data_json = json.dumps(data)
    socket.send(data_json.encode())
    decode_value_update(socket)


def FMV_set_value_DBL(control_label,number):
    logging.info(f"Sending request for value update of control named {control_label}")
    number = f"{number}"
    json = '{"message":"FMV_set_value_DBL","payload":{"name":"' + control_label + '","value":'+ number +'}}'
    socket.send(json.encode())
    decode_value_update(socket)

def FMV_set_value_STR(control_label,text):
    logging.info(f"Sending request for value update of control named {control_label}")
    json = '{"message":"FMV_set_value_STR","payload":{"name":"' + control_label + '","value":"'+ text +'"}}'
    socket.send(json.encode())
    decode_value_update(socket)

def FMV_set_value_ARR_STR(control_label,text):
    logging.info(f"Sending request for value update of control named {control_label}")
    # json = '{"message":"FMV_set_value_ARR_STR","payload":{"name":"' + control_label + '","value":"'+ text +'"}}'
    data = {"message":"FMV_set_value_ARR_STR","payload":{"name":control_label,"value": text }}
    data_json = json.dumps(data)
    socket.send(data_json.encode())
    decode_value_update(socket)


# All methods related to the Sub Panel :

def SP_get_vi_name(subpanel_label):
    logging.info("Send request for subpanel VI.")
    json = '{"message":"SP_get_vi_name","payload":"' + subpanel_label + '"}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    subpanel_vi = message.decode("utf-8")
    logging.info(f"VI in subpanel is {subpanel_vi}")
    return  subpanel_vi

def SP_get_control_details(subpanel_label):
    logging.info("Send request for front most VI.")
    json_message = '{"message":"SP_get_control_details","payload":"' + subpanel_label + '"}'
    socket.send(json_message.encode())

    #  Get the reply.
    message = socket.recv()
    control_details = message.decode("utf-8")
    # logging.info(f"Received reply {front_most_vi}")
    control_details = json.loads(control_details)
    return  control_details

def SP_SP_get_vi_name(subpanel_label,subsubpanel_label):
    logging.info("Send request for subpanel VI.")
    json = '{"message":"SP_SP_get_vi_name","payload":{"subpanel":"' + subpanel_label + '","subsubpanel":"' + subsubpanel_label + '"}}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    subpanel_vi = message.decode("utf-8")
    logging.info(f"VI in subsubpanel is {subpanel_vi}")
    return  subpanel_vi

def SP_SP_get_control_details(subpanel_label,subsubpanel_label):
    logging.info("Send request for front most VI.")
    json_message = '{"message":"SP_SP_get_control_details","payload":{"subpanel":"' + subpanel_label + '","subsubpanel":"' + subsubpanel_label + '"}}'
    socket.send(json_message.encode())

    #  Get the reply.
    message = socket.recv()
    control_details = message.decode("utf-8")
    # logging.info(f"Received reply {front_most_vi}")
    control_details = json.loads(control_details)
    return  control_details

def SP_click_on_button(subpanel_label,control_label):
    logging.info(f"Send request to click on control named {control_label}.")
    json = '{"message":"SP_click_on_button","payload":{"subpanel":"' + subpanel_label + '","control":"'+ control_label +'"}}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    return message.decode("utf-8") == "clicked"

def SP_get_value(subpanel_label,control_label,raw=False):
    logging.info("Send request for subpanel VI.")
    json = '{"message":"SP_get_value","payload":{"subpanel":"' + subpanel_label + '","control":"'+ control_label +'"}}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    if raw:
        data = message
    else:
        data = message.decode("utf-8").split('=')[1]
    return  data

def SP_get_value_TREE(subpanel_label,control_label):
    logging.info(f"Sending request for subpanel VI for value of control named {control_label}")
    json = '{"message":"SP_get_value","payload":{"subpanel":"' + subpanel_label + '","control":"'+ control_label +'"}}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    selected_tree_element = decode_tree(message)

    return selected_tree_element

def SP_get_value_DBL(subpanel_label,control_label):
    double_string = SP_get_value(subpanel_label, control_label)
    result_double = float(double_string)
    return result_double

def SP_get_value_bool(subpanel_label,control_label):
    bool_string = SP_get_value(subpanel_label, control_label)
    return bool_string == "TRUE"

def SP_set_value_DBL(subpanel_label,control_label,number):
    logging.info(f"Sending request for value update of control named {control_label}")
    number = f"{number}"
    json = '{"message":"SP_set_value_DBL","payload":{"subpanel":"' + subpanel_label + '","control":"' + control_label + '","value":'+ number +'}}'
    socket.send(json.encode())
    decode_value_update(socket)



def SP_set_value_STR(subpanel_label,control_label,text):
    logging.info(f"Sending request for value update of control named {control_label}")
    json = '{"message":"SP_set_value_STR","payload":{"subpanel":"' + subpanel_label + '","control":"' + control_label + '","value":' + text + '}}'
    socket.send(json.encode())
    decode_value_update(socket)


def SP_set_value_ARR_STR(subpanel_label,control_label,text):
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {"message":"SP_set_value_ARR_STR","payload":{"subpanel": subpanel_label ,"control": control_label ,"value": text }}
    data_json = json.dumps(data)
    socket.send(data_json.encode())
    decode_value_update(socket)

def SP_SP_click_on_button(subpanel_label,subsubpanel_label,control_label):
    logging.info(f"Send request to click on control named {control_label}.")
    json = '{"message":"SP_SP_click_on_button","payload":{"subpanel":"' + subpanel_label + '", "subsubpanel":"' + subsubpanel_label + '","control":"'+ control_label +'"}}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    return message.decode("utf-8") == "clicked"


def SP_SP_get_value(subpanel_label,subsubpanel_label,control_label, raw = False):
    logging.info("Send request for subpanel VI.")
    json = '{"message":"SP_SP_get_value","payload":{"subpanel":"' + subpanel_label + '","subsubpanel":"' + subsubpanel_label + '","control":"'+ control_label +'"}}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    if raw:
        data = message
    else:
        data = message.decode("utf-8").split('=')[1]
    return  data


def SP_SP_set_value_DBL(subpanel_label,subsubpanel_label,control_label,value):
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {"message":"SP_SP_set_value_DBL","payload":{"subpanel": subpanel_label, "subsubpanel":subsubpanel_label ,"control": control_label ,"value": value }}
    data_json = json.dumps(data)
    socket.send(data_json.encode())
    decode_value_update(socket)

def SP_SP_set_value_STR(subpanel_label,subsubpanel_label,control_label,value):
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {"message":"SP_SP_set_value_STR","payload":{"subpanel": subpanel_label, "subsubpanel":subsubpanel_label ,"control": control_label ,"value": value }}
    data_json = json.dumps(data)
    socket.send(data_json.encode())
    decode_value_update(socket)

def SP_SP_set_value_ARR_STR(subpanel_label,subsubpanel_label,control_label,text):
    logging.info(f"Sending request for value update of control named {control_label}")
    data = {"message":"SP_SP_set_value_ARR_STR","payload":{"subpanel": subpanel_label, "subsubpanel":subsubpanel_label ,"control": control_label ,"value": text }}
    data_json = json.dumps(data)
    socket.send(data_json.encode())
    decode_value_update(socket)

def SP_SP_get_value_TREE(subpanel_label,subsubpanel_label,control_label):
    logging.info(f"Sending request for subpanel VI for value of control named {control_label}")
    data = {"message": "SP_SP_get_value",
            "payload": {"subpanel": subpanel_label, "subsubpanel": subsubpanel_label, "control": control_label}}
    data_json = json.dumps(data)
    socket.send(data_json.encode())

    #  Get the reply.
    message = socket.recv()
    selected_tree_element = decode_tree(message)

    return selected_tree_element

def SP_SP_get_value_DBL(subpanel_label,subsubpanel_label,control_label):
    double_string = SP_SP_get_value(subpanel_label,subsubpanel_label, control_label)
    result_double = float(double_string)
    return result_double

def SP_SP_get_value_bool(subpanel_label,subsubpanel_label,control_label):
    bool_string = SP_SP_get_value(subpanel_label,subsubpanel_label, control_label)
    return bool_string == "TRUE"

