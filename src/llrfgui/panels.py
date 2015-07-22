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

"""
    Here we define the panels to be created in the main gui. 
"""

__author__ = 'antmil'

__docformat__ = 'restructuredtext'

from taurus.qt.qtgui.taurusgui.utils import PanelDescription
from dialog import get_model

# Configuration constants
GUI_NAME = 'llrfExpertGUI'
ORGANIZATION = 'MAXIV'
LOGO = 'images/maxivlogo.png'
CONSOLE = False

def get_models_dict(loops_device, diags_device):
    """
        In this function we create a dictionary with the relationship
        between widgets and models to be applied.

        :param str loops_device: String with the model for the loops device.
        :param str diags_device: String with the model for the diags device.
        :return: Dictionary with the info about the model \
                                  to be set in each widget.
        :rtype: dict
    """
    models_dict = {
        'AutoStartUp': loops_device,
        'AutoTuning': loops_device,
        'Conditioning': loops_device,
        'Diagdc': loops_device,
        'Diags': [loops_device, diags_device],
        'Fdl': [loops_device, diags_device],
        'Fpgaclock': [loops_device, diags_device],
        'FpgaVersion': [loops_device, diags_device],
        'InterlockLevel': diags_device,
        'IqLoopsSettings': loops_device,
        'ItckInDiags': diags_device,
        'ItckInputDisable': diags_device,
        'ItckOutDiag': diags_device,
        'ItckOutDisable': diags_device,
        'Landau': diags_device,
        'ManualTuning': loops_device,
        'Ramping': loops_device,
        'RampingDiag': loops_device,
        'Start': [loops_device, diags_device],
        'TuningDiag': loops_device,
        'Vcxo': loops_device,
        'PolarDiag': loops_device,
        'FIM': diags_device,
    }
    return models_dict

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
# :todo: fix this and set it in a __main__ or add all
#       this functions in another library, and don't include it in the doc.
loops, diags = get_model()
models_dict = get_models_dict(loops, diags)
create_panels()

