"""Contain dialogs for server selection."""

# Imports
import sys
from functools import wraps
from multiprocessing import Queue, Process
from PyQt4.QtGui import QInputDialog, QApplication, QMessageBox
from PyTango import Database, DeviceProxy

# local imports
from commons import sections_dict

#
# # Parse arguments and get the device list
# def parse_argv_and_get_device_list(classes):
#     """Parse arguments from sys.argv and
#     return the device list for the corresponding classes and arguments.
#     """
#     # No argument case
#     try:
#         server = next(arg for arg in sys.argv[1:] if not arg.startswith("-"))
#     except StopIteration:
#         return get_device_list(classes)
#     return get_device_list(classes, server)


# Process decorator
def in_different_process(func):
    """Decorator to run the function in a different process."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        queue = Queue(1) 
        target = lambda: queue.put(func(*args, **kwargs))
        process = Process(target=target)
        process.start()
        process.join()
        if process.exitcode:
            sys.exit(process.exitcode)
        return queue.get(False)
    return wrapper


# Database interface
#
# def get_device_server_dict(cls):
#     """Get device to server dictionary for a given Tango class."""
#     db = Database()
#     devices = db.get_device_exported_for_class(cls)
#     get_server_name = lambda device: db.get_device_info(device).ds_full_name
#     return dict((device, get_server_name(device)) for device in devices)
#
# def get_device_server_dict_from_classes(classes):
#     """Get device to server dictionary for given Tango classes."""
#     merge = lambda dct1, dct2: dct1.update(dct2) or  dct1
#     iterator = map(get_device_server_dict, classes)
#     return reduce(merge, iterator, {})


# Device list

# def get_device_list(classes, server=None):
#     """Get the device list for given tango classes.
#
#     If no device is found, a dialog is displayed and the program stops.
#     If more than one coresponding server is found, prompt a selection dialog.
#     """
#     # Get device and servers
#     dct = get_device_server_dict_from_classes(classes)
#     # Filter
#     if server:
#         servers = set(name for name in dct.values()
#                       if name.split("/")[-1] == server)
#     else:
#         servers = set(dct.values())
#     # Use the right dialog
#     if not len(servers):
#         return no_server_found()
#     elif len(servers) == 1:
#         server = servers.pop()
#     else:
#         server = choose_server(servers)
#     # return the devices
#     filt = lambda device: dct[device] == server
#     return sorted(filter(filt, dct)), server


# # Attribute list
# def get_attr_list(devices):
#     """Get the attribute list of the first device in a given device list."""
#     return DeviceProxy(devices[0]).get_attribute_list()
#
#
# # No server dialog
# def no_server_found():
#     """Prompt a 'no server found' dialog then exit."""
#     app = QApplication(sys.argv)
#     title = "No server found"
#     text = "No corresponding server is running in the database."
#     QMessageBox.information(None, title, text, 0)
#     sys.exit()


def get_model():
    list_of_options = sections_dict.keys()
    choose = choose_server(list_of_options)
    loops = sections_dict[str(choose)]['loops']
    diags = sections_dict[str(choose)]['diags']

    return loops, diags

# Server selection dialog
@in_different_process
def choose_server(servers):
    """Prompt a selection dialog from a given list of servers.
    The selected server is returned.
    If the user cancel the dialog, the program stops.
    """
    app = QApplication(sys.argv)
    title = "Server selection"
    label = "Please select a server."
    result, boolean = QInputDialog.getItem(None, title, label, 
                                           sorted(servers),
                                           editable=False)
    if not boolean:
        sys.exit()
    return result
