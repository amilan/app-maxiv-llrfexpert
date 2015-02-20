#!/usr/bin/env python

###############################################################################
##     ItckInputDisable is a widget used for the LLRF Expert GUI.
##
##     Copyright (C) 2013  Max IV Laboratory, Lund Sweden
##
##     This program is free software: you can redistribute it and/or modify
##     it under the terms of the GNU General Public License as published by
##     the Free Software Foundation, either version 3 of the License, or
##     (at your option) any later version.
##
##     This program is distributed in the hope that it will be useful,
##     but WITHOUT ANY WARRANTY; without even the implied warranty of
##     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##     GNU General Public License for more details.
##
##     You should have received a copy of the GNU General Public License
##     along with this program.  If not, see [http://www.gnu.org/licenses/].
###############################################################################

__author__ = "amilan"

from itckinputdisable import * 
from widgets.basellrfwidget import BaseLLRFWidget

from taurus.external.qt import Qt, QtCore
from taurus.qt.qtgui.util.ui import UILoadable
from utils.tih import *
from utils.decorators import alert_problems

import PyTango

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
        attrs_to_enable = [ "RvTet1DisA",
                            "RvTet2DisA",
                            "RvCircDisA",
                            "FwLoadDisA",
                            "FwHybLoadDisA",
                            "RvCavDisA",
                            "ManualITCKDisA",
                            "ArcsDisA",
                            "VacuumDisA",
                            "ExtITCKDisA",
                            "PlungerEndSwitchUpDisA",
                            "PlungerEndSwitchDownDisA"
                            ]
        for att in attrs_to_enable:
            self._device_proxy[att] = 'Enable'

    @alert_problems
    def disableAllInterlocksA(self):
        attrs_to_disable = [ "RvTet1DisA",
                             "RvTet2DisA",
                             "RvCircDisA",
                             "FwLoadDisA",
                             "FwHybLoadDisA",
                             "RvCavDisA",
                             "ManualITCKDisA",
                             "ArcsDisA",
                             "VacuumDisA",
                             "ExtITCKDisA",
                             "PlungerEndSwitchUpDisA",
                             "PlungerEndSwitchDownDisA"
                            ]
        for att in attrs_to_disable:
            self._device_proxy[att] = 'Disable'


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
            (self.ui.tauValueLabel_RvTet1DisA, "RvTet1DisA"),
            (self.ui.tauValueLabel_RvTet2DisA, "RvTet2DisA"),
            (self.ui.tauValueLabel_RvCircDisA, "RvCircDisA"),
            (self.ui.tauValueLabel_FwLoadDisA, "FwLoadDisA"),
            (self.ui.tauValueLabel_FwHybLoadDisA, "FwHybLoadDisA"),
            (self.ui.tauValueLabel_RvCavDisA, "RvCavDisA"),
            (self.ui.tauValueLabel_ManualITCKDisA, "ManualITCKDisA"),
            (self.ui.tauValueLabel_ArcsDisA, "ArcsDisA"),
            (self.ui.tauValueLabel_VacuumDisA, "VacuumDisA"),
            (self.ui.tauValueLabel_ExtITCKDisA, "ExtITCKDisA"),
            (self.ui.tauValueLabel_ExtITCKDisB_2, "PlungerEndSwitchUpDisA"),
            (self.ui.tauValueLabel_ExtITCKDisB_3, "PlungerEndSwitchDownDisA"),
        ]

        self._comboboxes = [
            (self.ui.comboBox_RvTet1DisA, "RvTet1DisA"),
            (self.ui.comboBox_RvTet2DisA, "RvTet2DisA"),
            (self.ui.comboBox_RvCircDisA, "RvCircDisA"),
            (self.ui.comboBox_FwLoadDisA, "FwLoadDisA"),
            (self.ui.comboBox_FwHybLoadDisA, "FwHybLoadDisA"),
            (self.ui.comboBox_RvCavDisA, "RvCavDisA"),
            (self.ui.comboBox_ManualITCKDisA, "ManualITCKDisA"),
            (self.ui.comboBox_ArcsDisA, "ArcsDisA"),
            (self.ui.comboBox_VacuumDisA, "VacuumDisA"),
            (self.ui.comboBox_ExtDisA, "ExtITCKDisA"),
            (self.ui.comboBox_ExtITCKDisB_2, "PlungerEndSwitchUpDisA"),
            (self.ui.comboBox_ExtITCKDisB_3, "PlungerEndSwitchDownDisA"),
        ]

def main():
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = ItckInputDisable()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
