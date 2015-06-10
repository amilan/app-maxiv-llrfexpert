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

"""Main module to run the Low Level Radio Frequency expert taurus GUI."""

__all__ = ['run']

__author__ = 'antmil'

__docformat__ = 'restructuredtext'

# Standard library imports
import sys

# 3rd party imports
from taurus.qt.qtgui.taurusgui import TaurusGui
from taurus.qt.qtgui.application import TaurusApplication

# Local imports

def create_application():
    '''
        Create the application and return an (application, taurusgui) tuple.
        
        :return: Tuple compose by a TaurusApplication and a TaurusGUI
        :rtype: tuple
    '''
    app = TaurusApplication()
    gui = TaurusGui(confname='llrfgui.panels.py')
    return app, gui

def hide_toolbars(gui):
    """Hide unnecessary toolbars.
       
       :param TaurusGui gui: TaurusGUI to hide toolbars
    """
    gui.jorgsBar.hide()
    gui.statusBar().hide()
    gui.setLockView(False)

def run():
    """Run LLRF expert GUI"""
    app, gui = create_application()
    hide_toolbars(gui)
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
