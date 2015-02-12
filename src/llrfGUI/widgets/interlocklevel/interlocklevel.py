#!/usr/bin/env python

###############################################################################
#     IQ Loop Settings is a widget used for the LLRF Expert GUI.
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

__author__ = "amilan"

from interlocklevel import * 


from taurus.external.qt import Qt, QtCore
from taurus.qt.qtgui.util.ui import UILoadable
from utils import tih, alert_problems

@UILoadable(with_ui='ui')
class InterlockLevel(Qt.QWidget):

    def __init__(self, parent=None):
        Qt.QWidget.__init__(self, parent)
        self.loadUI()

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
                               self.resetManualITCKA)

    @alert_problems
    def resetManualITCKA(self):
        self._device_proxy.resetManualITCKA()

    @alert_problems
    def _set_comboboxes(self):
        pass

    @alert_problems
    def _connect_all_attributes(self):
        for attribute in self._attributes):
            self.connect_attribute(attribute[0], attribute[1])

        for attribute in self._attributes_readback):
            self.connect_attribute(attribute[0], attribute[1])

        for combobox in self._comboboxes:
            self.connect_combobox(combobox[0], combobox[1])

    @alert_problems
    def connect_attribute(self, widget, attribute):
        attribute = self._device_name + '/' + attribute
        widget.setModel(attribute)

    @alert_problems
    def connect_combobox(self, widget, attribute):
        attribute = self._device_name + '/' + attribute
        widget.setModelName(attribute)

    @alert_problems
    def _create_attributes_lists(self):
        self._attributes = [
            (self.ui.lineEdit_RvTet1A, "/RvTet1A"),
            (self.ui.lineEdit_RvTet2A, "/RvTet2A"),
            (self.ui.lineEdit_RvCircA, "/RvCircA"),
            (self.ui.lineEdit_FwLoadA, "/FwLoadA"),
            (self.ui.lineEdit_FwHybLoadA, "/FwHybLoadA"),
            (self.ui.lineEdit_RvCavA, "/RvCavA"),
        ]

        self._attributes_readback = [
            (self.ui.tauValueLabel_RvTet1A, "/RvTet1A"),
            (self.ui.tauValueLabel_RvTet2A, "/RvTet2A"),
            (self.ui.tauValueLabel_RvCircA, "/RvCircA"),
            (self.ui.tauValueLabel_FwLoadA, "/FwLoadA"),
            (self.ui.tauValueLabel_FwHybLoadA, "/FwHybLoadA"),
            (self.ui.tauValueLabel_RvCavA, "/RvCavA"),
        ]

        self._comboboxes = []

def main():
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = InterlockLevel()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
