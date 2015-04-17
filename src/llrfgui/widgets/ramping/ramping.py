#!/usr/bin/env python

###############################################################################
#     Ramping is a widget used for the LLRF Expert GUI.
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
Ramping is a widget used for the LLRF Expert GUI.
"""

__all__ = ['Ramping']

__author__ = "amilan"

__docformat__ = 'restructuredtext'

import PyTango

from taurus.external.qt import Qt, QtCore
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.commons import *
from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget


@UILoadable(with_ui='ui')
class Ramping(BaseLLRFWidget):

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
        QtCore.QObject.connect(self.ui.pushButton_rampingA,
                               QtCore.SIGNAL("clicked()"),
                               self.resetRampingUpA)
        QtCore.QObject.connect(self.ui.pushButton_rampingA_2,
                               QtCore.SIGNAL("clicked()"),
                               self.resetRampingDownA)
        QtCore.QObject.connect(self.ui.pushButton_writeSlopesA,
                               QtCore.SIGNAL("clicked()"),
                               self.writeSlopesA)

    @alert_problems
    def resetRampingUpA(self):
        self._device_proxy['RampUpA'] = True
        self._device_proxy['RampUpA'] = False
        
    @alert_problems
    def resetRampingDownA(self):
        self._device_proxy['RampDownA'] = True
        self._device_proxy['RampDownA'] = False

    @alert_problems
    def writeSlopesA(self):
        self._device_proxy.WriteSlopesA()

    @alert_problems
    def _set_comboboxes(self):
        self.ui.comboBox_rampingEnA.addValueNames(CB)

   # @alert_problems
   # def _connect_all_attributes(self):
   #     for attribute in self._attributes:
   #         self.connect_attribute(attribute[0], attribute[1])

   #     for attribute in self._attributes_readback:
   #         self.connect_attribute(attribute[0], attribute[1])

   #     for combobox in self._comboboxes:
   #         self.connect_combobox(combobox[0], combobox[1])

   # @alert_problems
   # def connect_attribute(self, widget, attribute):
   #     attribute = self._device_name + '/' + attribute
   #     widget.setModel(attribute)

   # @alert_problems
   # def connect_combobox(self, widget, attribute):
   #     attribute = self._device_name + '/' + attribute
   #     widget.setModelName(attribute)

    @alert_problems
    def _create_attributes_lists(self):
        self._attributes = []

        self._attributes_readback = [
            (self.ui.tauValueLabel_RampingEnA, "RampingEnA"),
            (self.ui.tauValueLabel_timeRampUpA, "TimeRampUpA"),
            (self.ui.tauValueLabel_timeRampDownA, "TimeRampDownA"),
            (self.ui.tauValueLabel_ampRampInitA, "AmpRampInitA"),
            (self.ui.tauValueLabel_ampRampEndA, "AmpRampEndA"),
            (self.ui.tauValueLabel_phaseRampInitA, "PhaseRampInitA"),
            (self.ui.tauValueLabel_phaseRampEndA, "PhaseRampEndA"),
            
            (self.ui.tauValueLabel_IRampInitA, "IRampInitA"),
            (self.ui.tauValueLabel_QRampInitA, "QRampInitA"),
            (self.ui.tauValueLabel_IRampEndA, "IRampEndA"),
            (self.ui.tauValueLabel_QRampEndA, "QRampEndA"),
            (self.ui.tauValueLabel_AmpSlopeRampUpA, "AmpSlopeRampUpA"),
            (self.ui.tauValueLabel_PhaseSlopeRampUpA, "PhaseSlopeRampUpA"),
            (self.ui.tauValueLabel_AmpSlopeRampDownA, "AmpSlopeRampDownA"),
            (self.ui.tauValueLabel_PhaseSlopeRampDownA, "PhaseSlopeRampDownA"),
        ]

        self._comboboxes = [
            (self.ui.comboBox_rampingEnA, "RampingEnA"),
        ]

def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = Ramping()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
