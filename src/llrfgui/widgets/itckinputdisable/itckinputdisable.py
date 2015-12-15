#!/usr/bin/env python

###############################################################################
#     ItckInputDisable is a widget used for the LLRF Expert GUI.
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
ItckInputDisable is a widget used for the LLRF Expert GUI.
"""

__all__ = ['ItckInputDisable']

__author__ = "amilan"

__docformat__ = 'restructuredtext'

import PyTango

from taurus.external.qt import Qt, QtCore
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget


@UILoadable(with_ui='ui')
class ItckInputDisable(BaseLLRFWidget):

    def __init__(self, parent=None):
        config_file = self._get_config_file_name(__file__)
        BaseLLRFWidget.__init__(self, config_file, parent)
        self.loadUi()

    @alert_problems
    def connect_with_devices(self):
        """This method creates the tango device proxys. """
        self._device_proxy = PyTango.DeviceProxy(self._device_name)

    @alert_problems
    def connect_signals(self):
        QtCore.QObject.connect(self.ui.pushButton_3,
                               QtCore.SIGNAL("clicked()"),
                               self.enable_all_interlocksA)
        QtCore.QObject.connect(self.ui.pushButton_4,
                               QtCore.SIGNAL("clicked()"),
                               self.disable_all_interlocksA)
        QtCore.QObject.connect(self.ui.pushButton_5,
                              QtCore.SIGNAL("clicked()"),
                              self.enable_all_interlocksB)
        QtCore.QObject.connect(self.ui.pushButton_6,
                              QtCore.SIGNAL("clicked()"),
                              self.disable_all_interlocksB)

    @alert_problems
    def enable_all_interlocksA(self):
        for combobox in self._comboboxes:
            if combobox[1].endswith('A'):
                self._device_proxy[combobox[1]] = 1

    @alert_problems
    def disable_all_interlocksA(self):
        for combobox in self._comboboxes:
            if combobox[1].endswith('A'):
                self._device_proxy[combobox[1]] = 0

    @alert_problems
    def enable_all_interlocksB(self):
        for combobox in self._comboboxes:
            if combobox[1].endswith('B'):
                self._device_proxy[combobox[1]] = 1

    @alert_problems
    def disable_all_interlocksB(self):
        for combobox in self._comboboxes:
            if combobox[1].endswith('B'):
                self._device_proxy[combobox[1]] = 0

def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = 'ws/rf/pynutaqdiags_1'
    panel = ItckInputDisable()
    panel.setModel(model)
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
