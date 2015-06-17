#!/usr/bin/env python

###############################################################################
#     ItckInDiags is a widget used for the LLRF Expert GUI.
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
ItckInDiags is a widget used for the LLRF Expert GUI.
"""

__all__ = ['ItckInDiags']

__author__ = "amilan"

__docformat__ = 'restructuredtext'

from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.commons import *
from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget


@UILoadable(with_ui='ui')
class ItckInDiags(BaseLLRFWidget):

    def __init__(self, parent=None):
        BaseLLRFWidget.__init__(self, parent)
        self.loadUi()

   # @alert_problems
   # def setModel(self, model):
   #     self._device_name = model
   #     self._set_comboboxes()
   #     self._create_attributes_lists()
   #     self._connect_all_attributes()
   #     self.connect_with_devices()
   #     self.connect_signals()

   # @alert_problems
   # def connect_with_devices(self):
   #     """This method creates the tango device proxys. """
   #     pass
   #     #self._device_proxy = PyTango.DeviceProxy(self._device_name)

   # @alert_problems
   # def connect_signals(self):
   #     pass

   # @alert_problems
   # def _set_comboboxes(self):
   #     pass

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
        self._attributes = [
            (self.ui.taurusWheelEdit, "ItckNumberA")
        ]

        self._attributes_readback = [
            (self.ui.taurusBoolLed, "Diag_Rvtet1A"),
            (self.ui.taurusBoolLed_2, "Diag_Rvtet2A"),
            (self.ui.taurusBoolLed_3, "Diag_RvcircA"),
            (self.ui.taurusBoolLed_4, "Diag_FwloadA"),
            (self.ui.taurusBoolLed_5, "Diag_FwhybloadA"),
            (self.ui.taurusBoolLed_6, "Diag_RvcavA"),
            (self.ui.taurusBoolLed_7, "Diag_ManualInterlockA"),
            (self.ui.taurusBoolLed_8, "Diag_ArcsA"),
            (self.ui.taurusBoolLed_9, "Diag_VacuumA"),
            (self.ui.taurusBoolLed_10, "Diag_ExternalItckA"),
            (self.ui.taurusBoolLed_41, "Diag_PlungerEndSwitchUpA"),
            (self.ui.taurusBoolLed_43, "Diag_PlungerEndSwitchDownA"),
            #(self.ui.tauValueLabel_itckTimestamp, "ITCKTimestampA"),
        ]

        self._comboboxes = []

def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = ItckInDiags()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
