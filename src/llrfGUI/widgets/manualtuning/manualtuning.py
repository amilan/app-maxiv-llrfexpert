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

from manualtuning import *


from taurus.external.qt import Qt, QtCore
from taurus.qt.qtgui.util.ui import UILoadable
from utils import tih, alert_problems

import PyTango


@UILoadable(with_ui='ui')
class ManualTuning(Qt.QWidget):

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
        QtCore.QObject.connect(self.ui.pushButton_rTU,
                               QtCore.SIGNAL("clicked()"),
                               self.tuning_resetA)
        QtCore.QObject.connect(self.ui.pushButton_rTU_2,
                               QtCore.SIGNAL("clicked()"),
                               self.tuning_resetB)

    @alert_problems
    def tuning_resetA(self):
        self._device_proxy['TuningResetA'] = True
        self._device_proxy['TuningResetA'] = False

    @alert_problems
    def tuning_resetB(self):
        self._device_proxy['TuningResetB'] = True
        self._device_proxy['TuningResetB'] = False

    @alert_problems
    def _set_comboboxes(self):
        self.ui.comboBox_moveUp.addValueNames(CB)
        self.ui.comboBox_movePlg.addValueNames(CB)
        self.ui.comboBox_freqPulses.addValueNames(CC)

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
        self._attributes = [
            (self.ui.lineEdit_numberPulses, self._device_name + "/NumStepsA")
        ]

        self._attributes_readback = [
            (self.ui.taurusBoolLed_27, self._device_name + "/ManualTuningOnA"),
            (self.ui.taurusBoolLed_28, self._device_name + "/ManualFreqUpA"),
            (self.ui.tauValueLabel_numberPulses_2, self._device_name + "/NumStepsA"),
            (self.ui.tauValueLabel_moveUp, self._device_name + "/MoveUpA"),
            (self.ui.tauValueLabel_movePlg1, self._device_name + "/MoveA"),
            (self.ui.tauValueLabel_freqPulses, self._device_name + "/PulsesFrequencyA"),
        ]

        self._comboboxes = [
            (self.ui.comboBox_moveUp, self._device_name + "/MoveUpA"),
            (self.ui.comboBox_movePlg, self._device_name + "/MoveA"),
            (self.ui.comboBox_freqPulses, self._device_name + "/PulsesFrequency"),
            ]

def main():
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = ManualTuning()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
