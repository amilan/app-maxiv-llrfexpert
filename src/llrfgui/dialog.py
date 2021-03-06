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
# from commons import sections_dict


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


def get_model(is_expert, section=None):
    """
    Return the models choosen from a dialog.

    :return: list of models to be applied in the GUI.
    :rtype: tuple
    """
    if section is not None and section.lower() == 'test':
        from commons import sections_dict_tests
        sections_dict = sections_dict_tests
    else:
        from commons import sections_dict

    list_of_options = sections_dict.keys()
    if section is None:
        choose = choose_server(list_of_options)
        section = str(choose)

    loops = sections_dict[section]['loops']
    diags = sections_dict[section]['diags']
    rftrans1 = sections_dict[section]['rftransmitter1']
    rftrans2 = sections_dict[section]['rftransmitter2']
    if not is_expert:
        llrf = sections_dict[section]['llrf']
        llrfdiags = sections_dict[section]['llrfdiags']
        return section, loops, diags, llrf, llrfdiags, rftrans1, rftrans2
    else:
        return section, loops, diags, rftrans1, rftrans2


@in_different_process
def choose_server(servers):
    """
    Server selection dialog.

    Prompt a selection dialog from a given list of servers.
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
