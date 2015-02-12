#!/usr/bin/env python

###############################################################################
#     Landau is a widget used for the LLRF Expert GUI.
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

from landau import *


from taurus.external.qt import Qt, QtCore
from taurus.qt.qtgui.util.ui import UILoadable
from utils import tih, alert_problems

import PyTango

@UILoadable(with_ui='ui')
class Landau(Qt.QWidget):

    def __init__(self, parent=None):
        Qt.QWidget.__init__(self, parent)
        self.loadUI()

    @alert_problems
    def setModel(self, model):
        """
        :param model: Array of strings with the names of the device name
                      and the diagnostics device name
        """
        self._device_name = model[0]
        self._device_diag = model[1]
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
        QtCore.QObject.connect(self.ui.pushButton_rTU_3,
                               QtCore.SIGNAL("clicked()"),
                               self.landau_reset)

    @alert_problems
    def landau_reset(self):
        self._device_proxy['LandauTuningReset'] = True
        self._device_proxy['LandauTuningReset'] = False

    @alert_problems
    def _set_comboboxes(self):
        self.ui.comboBox_moveUp_3.addValueNames(CB)
        self.ui.comboBox_movePlg_3.addValueNames(CB)

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
            (self.ui.lineEdit_numberPulses_3, self._device_diag + "/NumSteps"),
            (self.ui.lineEdit_tuningOffset_3, self._device_diag + "/LandauPhaseOffset"),
            (self.ui.lineEdit_marginUp_4, self._device_diag + "/LandauMarginUp"),
            (self.ui.lineEdit_marginLow_4, self._device_diag + "/LandauMarginLow"),
            (self.ui.lineEdit_forwardMin_3, self._device_diag + "/MinLandauAmplitude"),
        ]

        self._attributes_readback = [
            (self.ui.taurusBoolLed_37, self._device_diag + "/PlungerMvMTDiagA"),
            (self.ui.taurusBoolLed_38, self._device_diag + "/PlungerMvUpMTDiagA"),
            (self.ui.tauValueLabel_numberPulses_4, self._device_diag + "/NumSteps"),
            (self.ui.tauValueLabel_moveUp_3, self._device_diag + "/MoveLandauUp"),
            (self.ui.tauValueLabel_movePlg1_3, self._device_diag + "/MoveLandauPLG"),
            (self.ui.taurusBoolLed_39, self._device_diag + "/PlungerMvATDiagA"),
            (self.ui.taurusBoolLed_40, self._device_diag + "/PlungerMvUpATDiagA"),

            (self.ui.tauValueLabel_tuningOffset_3, self._device_diag + "/LandauPhaseOffset"),
            (self.ui.tauValueLabel_marginUp_3, self._device_diag + "/LandauMarginUp"),
            (self.ui.tauValueLabel_marginLow_3, self._device_diag + "/LandauMarginLow"),
            (self.ui.tauValueLabel_forwardMin_4, self._device_diag + "/MinLandauAmplitude"),
        ]

        self._comboboxes = [
            #(self.ui.comboBox_moveUp_3, self._device_diag + "/MoveLandauUp"),
            #(self.ui.comboBox_movePlg_3, self._device_diag + "/MoveLandauPLG"),
            # (self.ui.comboBox_tuningEn_3, self._device_diag + "/LandauTuningEnable"),
            # (self.ui.comboBox_tuningPosEn_3, self._device_diag + "/LandauPositiveEn"),
        ]

def main():
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = Landau()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
