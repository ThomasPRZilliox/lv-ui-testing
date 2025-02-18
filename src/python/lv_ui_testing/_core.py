import zmq
import logging
import json
import xmltodict

print("start core")

# Configure logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)

# Configure 0MQ
context = zmq.Context()

#  Socket to talk to server
print("Connecting to LabVIEW server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def send_message(data, decode = True):
    """
    Send the message to the LabVIEW daemon and wait for the reply
    :param data: Payload to be sent to the LabVIEW VI under test
    :param decode: Return the decoded message (0MQ returns a binary payload)
    :return: Response from the LabVIEW daemon
    """
    data_json = json.dumps(data)
    socket.send(data_json.encode())

    #  Get the reply.
    message = socket.recv()
    if decode:
        message = message.decode("utf-8")

    return message

# All the methods for the communication

def decode_value_update(socket):
    #  Get the reply.
    message = socket.recv()
    if("Value set !" == message.decode("utf-8")):
        logging.info(f"Update successful !")
    else:
        logging.info(f"Something went wrong with the update...")


def decode_tree(message):
    data = message.split("Tree")[2:]  # To remove the space before the first tree word and the tree size

    selected_tree_element = []
    for element in data:
        selected_tree_element.append(element.split("=")[1])

    return selected_tree_element

