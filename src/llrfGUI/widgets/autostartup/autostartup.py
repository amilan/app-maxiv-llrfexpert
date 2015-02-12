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

from autostartup import *


from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable
from utils import tih, alert_problems

@UILoadable(with_ui='ui')
class AutoStartUp(Qt.QWidget):

    def __init__(self, parent=None):
        Qt.QWidget.__init__(self, parent)
        self.loadUI()

    @alert_problems
    def setModel(self, model):
        self._device_name = model
        self._set_comboboxes()
        self._create_attributes_lists()
        self._connect_all_attributes()

    @alert_problems
    def _set_comboboxes(self):
        self.ui.comboBox_autoStartUpA.addValueNames(CB)
        self.ui.comboBox_CommandStartA.addValueNames(CCMDSTART)

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
        widget.setModel(attribute)

    @alert_problems
    def connect_combobox(self, widget, attribute):
        widget.setModelName(attribute)

    @alert_problems
    def _create_attributes_lists(self):
        self._attributes = []

        self._attributes_readback = [
            (self.ui.tauValueLabel_autoStartUpA, self._device_name + "/AutoStartUpEnA"),
            (self.ui.tauValueLabel_CommandStartA, self._device_name + "/CommandStartA"),
        ]

        self._comboboxes = [
            (self.ui.comboBox_autoStartUpA, self._device_name + "/AutomaticStartUpEn"),
            (self.ui.comboBox_CommandStartA, self._device_name + "/CommandStart"),
        ]

def main():
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = AutoStartUp()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
