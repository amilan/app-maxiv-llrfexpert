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

__author__ = 'antmil'

__docformat__ = 'restructuredtext'

# Standard library imports
import os
import sys

# 3rd party imports
from PyQt4 import QtGui
#from functools import partial

from taurus.qt.qtgui.taurusgui import TaurusGui
from taurus.qt.qtgui.application import TaurusApplication
from taurus.qt.qtgui.taurusgui.utils import PanelDescription, ExternalApp, Qt_Qt

# local imports


# Configuration constants
GUI_NAME = 'llrfExpertGUI'
ORGANIZATION = 'MAXIV'
LOGO = 'images/maxivlogo.png'
CONSOLE = False

# Models dictionary. Keys are the classnames and values are models
loops_device = 'rf/nutaq/loops-1'
diags_device = 'rf/nutaq/diags-1'
models_dict = {
    'AutoStartUp': loops_device,
    'AutoTuning': loops_device,
    'Conditioning': loops_device,
    'Diagdc': loops_device,
    'Diags':diags_device,
    'Fdl':loops_device,
    'Fpgaclock': [loops_device, diags_device],
    'FpgaVersion': [loops_device, diags_device],
    'InterlockLevel': diags_device,
    'IqLoopsSettings': loops_device,
    'ItckInDiags': diags_device,
    'ItckInputDisable': diags_device,
    'ItckOutDiag': diags_device,
    'ItckOutDisable': diags_device,
    'Landau': [loops_device, diags_device],
    'ManualTuning': loops_device,
    'Ramping': loops_device,
    'RampingDiag': loops_device,
    'Start': [loops_device, diags_device],
    'TuningDiag': [loops_device, diags_device],
    'Vcxo': loops_device,
}

# Create application
def create_application():
    """Return an (application, taurusgui) tuple."""
    app = TaurusApplication()
    gui = TaurusGui(confname=__file__)
    return app, gui

# Hide unnecessary bars
def hide_toolbars(gui):
    """Hide toolbars."""
    gui.jorgsBar.hide()
    gui.statusBar().hide()
    #gui.panelsToolBar.hide()
    gui.setLockView(False)

# Create panels
def create_panels():
    """Create panels and set application name."""
    for widget in models_dict:
        name = '{0}'.format(widget)
        globals()[name] = PanelDescription(
            name,
            classname = name,
            modulename = 'llrfgui.widgets.' + name.lower(),
            model = models_dict[name]
        )

create_panels()

# Main function
def run():
    """Run llrf expert gui"""
    app, gui = create_application()

    hide_toolbars(gui)

    gui.show()
    app.exec_()

# Main execution
if __name__ == '__main__':
    run()
