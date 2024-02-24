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

def FMV_click_on_button(control_label):
    logging.info(f"Send request to click on control named {control_label}.")
    json = '{"message":"FMV_click_on_button","payload":"'+ control_label +'"}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    return message.decode("utf-8") == "clicked"

def FMV_get_value(control_label):
    logging.info(f"Sending request for value of control named {control_label}")
    json = '{"message":"FMV_get_value","payload":"'+ control_label + '"}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    data = message.decode("utf-8").split('=')[1]

    return data

def FMV_get_value_DBL(control_label):
    double_string = FMV_get_value(control_label)
    result_double = float(double_string)
    return result_double

def FMV_get_value_bool(control_label):
    bool_string = FMV_get_value(control_label)
    return bool_string == "TRUE"

def FMV_set_value_DBL(control_label,number):
    logging.info(f"Sending request for value update of control named {control_label}")
    number = f"{number}"
    json = '{"message":"FMV_set_value_DBL","payload":{"name":"' + control_label + '","value":'+ number +'}}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    if("Value set !" == message.decode("utf-8")):
        logging.info(f"Update successful !")
    else:
        logging.info(f"Something went wrong with the update...")

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

def SP_click_on_button(subpanel_label,control_label):
    logging.info(f"Send request to click on control named {control_label}.")
    json = '{"message":"SP_click_on_button","payload":{"subpanel":"' + subpanel_label + '","control":"'+ control_label +'"}}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    return message.decode("utf-8") == "clicked"

def SP_get_value(subpanel_label,control_label):
    logging.info("Send request for subpanel VI.")
    json = '{"message":"SP_get_value","payload":{"subpanel":"' + subpanel_label + '","control":"'+ control_label +'"}}'
    socket.send(json.encode())

    #  Get the reply.
    message = socket.recv()
    data = message.decode("utf-8").split('=')[1]
    return  data

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

    #  Get the reply.
    message = socket.recv()
    if("Value set !" == message.decode("utf-8")):
        logging.info(f"Update successful !")
    else:
        logging.info(f"Something went wrong with the update...")
