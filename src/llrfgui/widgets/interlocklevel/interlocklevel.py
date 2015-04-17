#!/usr/bin/env python

###############################################################################
#     InterlockLevel is a widget used for the LLRF Expert GUI.
#
#     Copyright (C) 2013  Max IV Laboratory, Lund Sweden
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see [http://www.gnu.org/licenses/].
###############################################################################

"""
InterlockLevel is a widget used for the LLRF Expert GUI.
"""

__all__ = ['InterlockLevel']

__author__ = "amilan"

__docformat__ = 'restructuredtext'

import PyTango

from taurus.external.qt import Qt, QtCore
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.commons import *
from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget


@UILoadable(with_ui='ui')
class InterlockLevel(BaseLLRFWidget):

    def __init__(self, parent=None):
        BaseLLRFWidget.__init__(self, parent)
        self.loadUi()

    @alert_problems
    def setModel(self, model):
        self._device_name = model
        self._set_comboboxes()
        self._create_attributes_lists()
        self._connect_all_attributes()
        self.connect_with_devices()
        self.connect_signals()

    @alert_problems
    def connect_with_devices(self):
        """This method creates the tango device proxys. """

        self._device_proxy = PyTango.DeviceProxy(self._device_name)

    @alert_problems
    def connect_signals(self):
        QtCore.QObject.connect(self.ui.pushButton_SWITCKA, 
                               QtCore.SIGNAL("clicked()"),
                               self.reset_manual_itck)

    @alert_problems
    def reset_manual_itck(self):
        self._device_proxy.reset_manual_itck()


    @alert_problems
    def _create_attributes_lists(self):
        self._attributes = [
            (self.ui.lineEdit_RvTet1A, "Rvtet1"),
            (self.ui.lineEdit_RvTet2A, "Rvtet2"),
            (self.ui.lineEdit_RvCircA, "Rvcirc"),
            (self.ui.lineEdit_FwLoadA, "Fwload"),
            (self.ui.lineEdit_FwHybLoadA, "Fwhybload"),
            (self.ui.lineEdit_RvCavA, "Rvcav"),
        ]

        self._attributes_readback = [
            (self.ui.tauValueLabel_RvTet1A, "RvTet1"),
            (self.ui.tauValueLabel_RvTet2A, "RvTet2"),
            (self.ui.tauValueLabel_RvCircA, "RvCirc"),
            (self.ui.tauValueLabel_FwLoadA, "Fwload"),
            (self.ui.tauValueLabel_FwHybLoadA, "Fwhybload"),
            (self.ui.tauValueLabel_RvCavA, "Rvcav"),
        ]

        self._comboboxes = []

def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = InterlockLevel()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
