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

from diags import *


from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable
from utils import tih, alert_problems

@UILoadable(with_ui='ui')
class Diags(Qt.QWidget):

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
        self._attributes = []

        self._attributes_readback = [
            #(self.ui.tauValueLabel_IFwCavVolt_3, "ICavVolt"),
            (self.ui.tauValueLabel_IcavRef, "IRefDiagA"),
            (self.ui.tauValueLabel_IcavVolt, "ICavA"),
            (self.ui.tauValueLabel_FwTet1Loop, "IFwTet1ALoop"),
            #(self.ui.tauValueLabel_IcavRef_3, "IFwTet2ALoop"),
            #(self.ui.tauValueLabel_IcavRef_5, "IFwCircInLoop"),
            #(self.ui.tauValueLabel_IcavRef_7, "IFwCavLoop"),
            #(self.ui.tauValueLabel_IcavRef_9, "ILoopInput"),
            (self.ui.tauValueLabel_IerrorP, "IErrorA"),
            (self.ui.tauValueLabel_IerrorA, "IErrorAccumA"),
            (self.ui.tauValueLabel_IcrtlA, "IControlA"),
            (self.ui.tauValueLabel_IcrtlAc, "IControl1A"),
            (self.ui.tauValueLabel_IcrtlAc2, "IControl2A"),
            (self.ui.tauValueLabel_IMOA, "IMOA"),
            #(self.ui.tauValueLabel_IMO_3, "ILandau"),

            #(self.ui.tauValueLabel_QFwCavVolt_3, "QCavVolt"),
            (self.ui.tauValueLabel_QcavRef, "QRefDiagA"),
            (self.ui.tauValueLabel_QcavVolt, "QCavA"),
            (self.ui.tauValueLabel_FwTet1Loop_2, "QFwTet1ALoop"),
            #(self.ui.tauValueLabel_QcavRef_3, "QFwTet2ALoop"),
            #(self.ui.tauValueLabel_QcavRef_5, "QFwCircInLoop"),
            #(self.ui.tauValueLabel_QcavRef_7, "QFwCavLoop"),
            #(self.ui.tauValueLabel_QcavRef_9, "QLoopInput"),
            (self.ui.tauValueLabel_QerrorP, "QErrorA"),
            (self.ui.tauValueLabel_QerrorA, "QErrorAccumA"),
            (self.ui.tauValueLabel_QctrlA, "QControlA"),
            (self.ui.tauValueLabel_QctrlAc, "QControl1A"),
            (self.ui.tauValueLabel_QctrlAc2, "QControl2A"),
            (self.ui.tauValueLabel_QMOA, "/QMOA"),
            #(self.ui.tauValueLabel_QMO_3, "QLandau"),

            #(self.ui.tauValueLabel_ampFwCavVolt_3, "AmpCavVolt"),
            (self.ui.tauValueLabel_ampCavRef, "AmpRefDiagA"),
            (self.ui.tauValueLabel_ampCavVolt, "AmpCavA"),
            (self.ui.tauValueLabel_FwTet1Loop_3, "AmpFwTet1ALoop"),
            #(self.ui.tauValueLabel_ampCavRef_3, "AmpFwTet2ALoop"),
            #(self.ui.tauValueLabel_ampCavRef_5, "AmpFwCircInLoop"),
            #(self.ui.tauValueLabel_ampCavRef_7, "AmpFwCavLoop"),
            #(self.ui.tauValueLabel_ampCavRef_9, "AmpLoopInput"),
            (self.ui.tauValueLabel_ampErrorP, "AmpErrorA"),
            (self.ui.tauValueLabel_ampErrorA, "AmpErrorAccumA"),
            (self.ui.tauValueLabel_ampCtrlA, "AmpControlA"),
            (self.ui.tauValueLabel_ampCtrlAc, "AmpControl1A"),
            (self.ui.tauValueLabel_ampCtrlAc2, "AmpControl2A"),
            (self.ui.tauValueLabel_AmpMOA, self.device + "/AmpMOA"),
            #(self.ui.tauValueLabel_ampMO_3, "AmpLandau"),

            #(self.ui.tauValueLabel_phaseFwCavVolt_3, "PhCavVolt"),
            (self.ui.tauValueLabel_phaseCavRef, "PhRefDiagA"),
            (self.ui.tauValueLabel_phaseCavVolt, "PhCavA"),
            (self.ui.tauValueLabel_FwTet1Loop_4, "PhFwTet1ALoop"),
            #(self.ui.tauValueLabel_ampCavRef_3, "AmpFwTet2ALoop"),
            #(self.ui.tauValueLabel_phaseCavRef_5, "PhFwCircInLoop"),
            #(self.ui.tauValueLabel_phaseCavRef_7, "PhFwCavLoop"),
            #(self.ui.tauValueLabel_phaseCavRef_9, "PhLoopInput"),
            (self.ui.tauValueLabel_phaseErrorP, "PhErrorA"),
            (self.ui.tauValueLabel_phaseErrorA, "PhErrorAccumA"),
            (self.ui.tauValueLabel_PhCrtlA, "PhControlA"),
            (self.ui.tauValueLabel_phaseCtrlAc, "PhControl1A"),
            (self.ui.tauValueLabel_phaseCtrlAc_2, "PhControl2A"),
            (self.ui.tauValueLabel_PhMOA, "PhMOA"),
            #(self.ui.tauValueLabel_phaseMO_3, "PhLandau"),
        ]

        self._comboboxes = []

def main():
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = Diags()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()