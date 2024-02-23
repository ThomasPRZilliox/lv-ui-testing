import zmq
import logging

# Configure logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

# Configure 0MQ
context = zmq.Context()

#  Socket to talk to server
print("Connecting to LabVIEW server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def SP_click_on_button(subpanel_label,control_label):
    logging.info(f"Send request to click on control named {control_label}.")
    json = '{"message":"SP_click","payload":{"subpanel":"' + subpanel_label + '","control":"'+ control_label +'"}}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    return message.decode("utf-8") == "clicked"


def get_front_most():
    logging.info("Send request for front most VI.")
    json = '{"message":"frontMostVi"}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    front_most_vi = message.decode("utf-8")
    logging.info(f"Received reply {front_most_vi}")
    return  front_most_vi

def get_subpanel(subpanel_label):
    logging.info("Send request for subpanel VI.")
    json = '{"message":"subpanel","payload":"' + subpanel_label + '"}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    subpanel_vi = message.decode("utf-8")
    logging.info(f"VI in subpanel is {subpanel_vi}")
    return  subpanel_vi

def get_subpanel_value(subpanel_label,control_label):
    logging.info("Send request for subpanel VI.")
    json = '{"message":"getSubpanelValue","payload":{"subpanel":"' + subpanel_label + '","control":"'+ control_label +'"}}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    data = message.decode("utf-8").split('=')[1]
    return  data

def get_subpanel_value_DBL(subpanel_label,control_label):
    double_string = get_subpanel_value(subpanel_label,control_label)
    result_double = float(double_string)
    return result_double

def get_subpanel_value_bool(subpanel_label,control_label):
    bool_string = get_subpanel_value(subpanel_label,control_label)
    return bool_string == "TRUE"


def set_subpanel_value_dbl(subpanel_label,control_label,number):
    logging.info(f"Sending request for value update of control named {control_label}")
    number = f"{number}"
    json = '{"message":"setSubpanelValueDBL","payload":{"subpanel":"' + subpanel_label + '","control":"' + control_label + '","value":'+ number +'}}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    if("Value set !" == message.decode("utf-8")):
        logging.info(f"Update successful !")
    else:
        logging.info(f"Something went wrong with the update...")






def click_on_button(control_label):
    logging.info(f"Send request to click on control named {control_label}.")
    json = '{"message":"click","payload":"'+ control_label +'"}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    return message.decode("utf-8") == "clicked"

def get_value(control_label):
    logging.info(f"Sending request for value of control named {control_label}")
    json = '{"message":"getValue","payload":"'+ control_label + '"}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    data = message.decode("utf-8").split('=')[1]

    return data

def get_value_dbl(control_label):
    double_string = get_value(control_label)
    result_double = float(double_string)
    return result_double


def get_value_bool(control_label):
    logging.info(f"Sending request for value of the bool control named {control_label}")
    json = '{"message":"getValue","payload":"'+ control_label + '"}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()

    data = message.decode("utf-8").split('=')[1]

    return data == "TRUE"

def set_value_dbl(control_label,number):
    logging.info(f"Sending request for value update of control named {control_label}")
    number = f"{number}"
    json = '{"message":"setValueDBL","payload":{"name":"' + control_label + '","value":'+ number +'}}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    if("Value set !" == message.decode("utf-8")):
        logging.info(f"Update successful !")
    else:
        logging.info(f"Something went wrong with the update...")

