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

from llrfgui.utils.commons import *
from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget


@UILoadable(with_ui='ui')
class ItckInputDisable(BaseLLRFWidget):

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
        QtCore.QObject.connect(self.ui.pushButton_3,
                               QtCore.SIGNAL("clicked()"),
                               self.enableAllInterlocksA)
        QtCore.QObject.connect(self.ui.pushButton_4,
                               QtCore.SIGNAL("clicked()"),
                               self.disableAllInterlocksA)
        #QtCore.QObject.connect(self.ui.pushButton_5,
        #                       QtCore.SIGNAL("clicked()"),
        #                       self.enableAllInterlocksB)
        #QtCore.QObject.connect(self.ui.pushButton_6,
        #                       QtCore.SIGNAL("clicked()"),
        #                       self.disableAllInterlocksB)

    @alert_problems
    def enableAllInterlocksA(self):
        attrs_to_enable = [ "DisableItckRvTet1A",
                            "DisableItckRvTet2A",
                            "DisableItckRvcircA",
                            "DisableItckFwloadA",
                            "DisableItckFwhybloadA",
                            "DisableItckRvcavA",
                            "DisableItckManualInterlockA",
                            "DisableItckArcsA",
                            "DisableItckVacuumA",
                            #"DisableItckExtITCKA",
                            "DisableItckPlungerEndSwitchesUpA",
                            "DisableItckPlungerEndSwitchesDownA"
                            ]
        for att in attrs_to_enable:
            #self._device_proxy[att] = 'Enable'
            self._device_proxy[att] = 1

    @alert_problems
    def disableAllInterlocksA(self):
        attrs_to_disable = [ "DisableItckRvTet1A",
                             "DisableItckRvTet2A",
                             "DisableItckRvcircA",
                             "DisableItckFwloadA",
                             "DisableItckFwhybloadA",
                             "DisableItckRvcavA",
                             "DisableItckManualInterlockA",
                             "DisableItckArcsA",
                             "DisableItckVacuumA",
                             #"DisableItckExtITCKA",
                             "DisableItckPlungerEndSwitchesUpA",
                             "DisableItckPlungerEndSwitchesDownA"
                            ]
        for att in attrs_to_disable:
            #self._device_proxy[att] = 'Disable'
            self._device_proxy[att] = 0


    @alert_problems
    def _set_comboboxes(self):
        self.ui.comboBox_RvTet1DisA.addValueNames(CEN)
        self.ui.comboBox_RvTet2DisA.addValueNames(CEN)
        self.ui.comboBox_RvCircDisA.addValueNames(CEN)
        self.ui.comboBox_FwLoadDisA.addValueNames(CEN)
        self.ui.comboBox_FwHybLoadDisA.addValueNames(CEN)
        self.ui.comboBox_RvCavDisA.addValueNames(CEN)
        self.ui.comboBox_ManualITCKDisA.addValueNames(CEN)
        self.ui.comboBox_ArcsDisA.addValueNames(CEN)
        self.ui.comboBox_VacuumDisA.addValueNames(CEN)
        self.ui.comboBox_ExtDisA.addValueNames(CEN)
        self.ui.comboBox_ExtITCKDisB_2.addValueNames(CEN)
        self.ui.comboBox_ExtITCKDisB_3.addValueNames(CEN)

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
            (self.ui.tauValueLabel_RvTet1DisA, "DisableItckRvTet1A"),
            (self.ui.tauValueLabel_RvTet2DisA, "DisableItckRvTet2A"),
            (self.ui.tauValueLabel_RvCircDisA, "DisableItckRvcircA"),
            (self.ui.tauValueLabel_FwLoadDisA, "DisableItckFwloadA"),
            (self.ui.tauValueLabel_FwHybLoadDisA, "DisableItckFwhybloadA"),
            (self.ui.tauValueLabel_RvCavDisA, "DisableItckRvcavA"),
            (self.ui.tauValueLabel_ManualITCKDisA, "DisableItckManualInterlockA"),
            (self.ui.tauValueLabel_ArcsDisA, "DisableItckArcsA"),
            (self.ui.tauValueLabel_VacuumDisA, "DisableItckVacuumA"),
            # (self.ui.tauValueLabel_ExtITCKDisA, "ExtITCKDisA"),
            (self.ui.tauValueLabel_ExtITCKDisB_2, "DisableItckPlungerEndSwitchesUpA"),
            (self.ui.tauValueLabel_ExtITCKDisB_3, "DisableItckPlungerEndSwitchesDownA"),
        ]

        self._comboboxes = [
            (self.ui.comboBox_RvTet1DisA, "DisableItckRvTet1A"),
            (self.ui.comboBox_RvTet2DisA, "DisableItckRvTet2A"),
            (self.ui.comboBox_RvCircDisA, "DisableItckRvcircA"),
            (self.ui.comboBox_FwLoadDisA, "DisableItckFwloadA"),
            (self.ui.comboBox_FwHybLoadDisA, "DisableItckFwhybloadA"),
            (self.ui.comboBox_RvCavDisA, "DisableItckRvcavA"),
            (self.ui.comboBox_ManualITCKDisA, "DisableItckManualInterlockA"),
            (self.ui.comboBox_ArcsDisA, "DisableItckArcsA"),
            (self.ui.comboBox_VacuumDisA, "DisableItckVacuumA"),
            # (self.ui.comboBox_ExtDisA, "ExtITCKDisA"),
            (self.ui.comboBox_ExtITCKDisB_2, "DisableItckPlungerEndSwitchesUpA"),
            (self.ui.comboBox_ExtITCKDisB_3, "DisableItckPlungerEndSwitchesDownA"),
        ]

def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = ItckInputDisable()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
