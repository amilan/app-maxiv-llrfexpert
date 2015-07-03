#!/usr/bin/env python

###########################################################################
#     LLRF expert Graphical User Interface.
#
#     Copyright (C) 2015  MAX IV Laboratory, Lund Sweden.
#
#     This is free software; you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation; either version 3 of the License, or
#     (at your option) any later version.
#
#     This software is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program; if not, see <http://www.gnu.org/licenses/>.
###########################################################################

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
#@in_different_process
def choose_server(servers):
    """Prompt a selection dialog from a given list of servers.
    The selected server is returned.
    If the user cancel the dialog, the program stops.
    """
    #app = QApplication(sys.argv)
    title = "Server selection"
    label = "Please select a server."
    result, boolean = QInputDialog.getItem(None, title, label,
                                           sorted(servers),
                                           editable=False)
    print boolean
    print result
    if not boolean:
        sys.exit()
    return result
