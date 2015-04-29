"""Contain dialogs for server selection."""

# Imports
import sys
from functools import wraps
from multiprocessing import Queue, Process
from PyQt4.QtGui import QInputDialog, QApplication

# local imports
from commons import sections_dict

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
