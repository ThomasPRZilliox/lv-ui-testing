import zmq
import logging
import json
import xmltodict
import xml.etree.ElementTree as ET

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

def parse_lvvariant(xml_string):
    root = ET.fromstring(xml_string)

    def is_number(element):
        return element.tag in {"SGL", "EXT", "DBL","FXP","I64", "I32", "I16", "I8", "U64", "U32", "U16", "U8","CDB", "CXT", "CSG"}
    def format_number(element):
        if element.tag in {"SGL", "EXT", "DBL"}:
            val = element.find("Val")
            if val is not None:
                return float(val.text)
        elif element.tag in {"FXP"}:
            val = element.find("Val")
            if val is not None:
                return val.text
        elif element.tag in {"I64", "I32", "I16", "I8", "U64", "U32", "U16", "U8"}:
            val = element.find("Val")
            if val is not None:
                return int(val.text)
        elif element.tag in {"CDB", "CXT", "CSG"}:
            val = element.find("Val")
            if val is not None:
                return complex(val.text.replace("i", "j").replace(" ", ""))

    def is_text(element):
        return element.tag in {"String"}

    def format_text(element):
        val = element.find("Val")
        if val is not None:
            return val.text

    def is_bool(element):
        return element.tag in {"Boolean"}

    def format_bool(element):
        val = element.find("Val")
        if val is not None:
            return int(val.text) != 0





    def parse_element(element):
        # if element.tag == "Array":
        #     values = []
        #     for child in element:
        #         if is_number(child):
        #             values.append(format_number(child))
        #     return values
        if element.tag == "Array":
            # Parse 2D array
            dim_sizes = []
            for dim in element.findall("Dimsize"):
                dim_sizes.append(int(dim.text))

            # Initialize array structure
            values = []
            num_elements = 1
            for dim_size in dim_sizes:
                num_elements *= dim_size

            index = 0
            for child in element:
                if is_number(child):
                    values.append(format_number(child))
                elif is_text(child):
                    values.append(format_text(child))
                elif is_bool(child):
                    values.append(format_bool(child))

            # Reshape the flat array into a 2D array based on the dimensions
            if len(dim_sizes) == 2:
                rows, cols = dim_sizes
                values_2d = [values[i:i + cols] for i in range(0, len(values), cols)]
                return values_2d

            return values

        elif is_number(element):
            return format_number(element)
        elif is_text(element):
            return format_text(element)
        elif is_bool(element):
            return format_bool(element)
        else:
            val = element.find("Val")
            if val is not None:
                return val.text

        return None

    for child in root:
        parsed_value = parse_element(child)
        if parsed_value is not None:
            return parsed_value

    return None  # Return None if no valid data is found
