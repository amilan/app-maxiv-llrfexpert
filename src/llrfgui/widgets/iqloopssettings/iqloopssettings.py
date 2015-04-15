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

"""
IQ Loop Settings is a widget used for the LLRF Expert GUI.
"""

__all__ = ['IqLoopsSettings']

__author__ = "amilan"

__docformat__ = 'restructuredtext'

from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.commons import *
from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget


@UILoadable(with_ui='ui')
class IqLoopsSettings(BaseLLRFWidget):

    def __init__(self, parent=None):
        BaseLLRFWidget.__init__(self, parent)
        self.loadUi()

   # @alert_problems
   # def setModel(self, model):
   #     self._device_name = model
   #     self._set_comboboxes()
   #     self._create_attributes_lists()
   #     self._connect_all_attributes()

    @alert_problems
    def _set_comboboxes(self):
        self.ui.comboBox_voltInc.addValueNames(CV)
        self.ui.comboBox_phaseIncRate.addValueNames(CPIR)
        self.ui.comboBox_quad.addValueNames(CQ)
        self.ui.comboBox_lookRef.addValueNames(CB)
        self.ui.comboBox_loopEn.addValueNames(CB)
        self.ui.comboBox_loopInputA.addValueNames(CB)
        self.ui.comboBox_phaseShiftEn.addValueNames(CB)
        self.ui.comboBox_DACsGainEn.addValueNames(CB)
        self.ui.comboBox_GainTetA1En.addValueNames(CB)

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
   #     widget.setModel(attribute)

   # @alert_problems
   # def connect_combobox(self, widget, attribute):
   #     widget.setModelName(attribute)

    @alert_problems
    def _create_attributes_lists(self):
        self._attributes = [
                (self.ui.lineEdit_AmpLoopA, "Amprefin"),
                (self.ui.lineEdit_PhaseLoopA, "Phrefin"),

                (self.ui.lineEdit_ampRefMinA, "Amprefmin"),
                (self.ui.lineEdit_phaseRefMinA, "Phrefmin"),

                (self.ui.lineEdit_PILimit, "PILimitA"),
                (self.ui.lineEdit_ki, "KiA"),
                (self.ui.lineEdit_kp, "KpA"),

                (self.ui.lineEdit_gainola, "GainOL"),

                (self.ui.lineEdit_phaseShift, "PhaseShiftCav"),
                (self.ui.lineEdit_phaseShift_10, "PhaseShiftFwTet1"),
                (self.ui.lineEdit_phaseShift_11, "PhaseShiftFwTet2"),
                (self.ui.lineEdit_phaseShift_13, "PhaseShiftFwCircin"),
                (self.ui.lineEdit_phaseShift_15, "PhaseShiftFwCav"),

                (self.ui.lineEdit_phaseShift_3, self._device_name + "PhaseShiftControlSignalTet1"),
                (self.ui.lineEdit_phaseShift_5, self._device_name + "PhaseShiftControlSignalTet2"),

                (self.ui.lineEdit_Tetrode1A, "GainTetrode1"),
                (self.ui.lineEdit_Tetrode2A, "GainTetrode2"),

                (self.ui.lineEdit_filterStage, "FilterStages"),
                (self.ui.lineEdit_samplesAv, "SamplesToAverage"),
                ]

        self._attributes_readback = [
                (self.ui.tauValueLabel_AmpLoop, "Amprefin"),
                (self.ui.tauValueLabel_PhaseLoop, "Phrefin"),

                (self.ui.tauValueLabel_voltInc, "VoltageIncreaseRate"),
                (self.ui.tauValueLabel_phaseIncRate, "PhaseIncreaseRate"),

                (self.ui.tauValueLabel_ampRefMinA, "Amprefmin"),
                (self.ui.tauValueLabel_phaseRefMinA, "Phrefmin"),

                (self.ui.tauValueLabel_PILimit_2, "PILimitA"),
                (self.ui.tauValueLabel_ki_2, "KiA"),
                (self.ui.tauValueLabel_kp_2, "KpA"),
                (self.ui.tauValueLabel_quad, "QuadrantSelectionA"),
                (self.ui.tauValueLabel_lookRef, "LookRefA"),
                (self.ui.tauValueLabel_IqLoopsEn, "SlowIqLoopEnable"),
                (self.ui.tauValueLabel_IqloopsInputA, "SlowIqLoopInputSelection"),

                #(self.ui.tauValueLabel_loopInputA, self._device_name + "/LoopInputA"),
                (self.ui.tauValueLabel_gainola, "GainOLA"),
                (self.ui.tauValueLabel_phaseShiftEn, "ADCsPhaseShiftEnableA"),
                (self.ui.tauValueLabel_phaseShift_2, "PhaseShiftCav"),
                (self.ui.tauValueLabel_phaseShift_11, "PhaseShiftFwTet1"),
                (self.ui.tauValueLabel_phaseShift_12, "PhaseShiftFwTet2"),
                (self.ui.tauValueLabel_phaseShift_14, "PhaseShiftFwCirc"),
                (self.ui.tauValueLabel_phaseShift_16, "PhaseShiftFwCav"),
                (self.ui.tauValueLabel_DACsGainEn, "DACsPhaseShiftEnableA"),

                (self.ui.tauValueLabel_phaseShift_4, self._device_name + "PhaseShiftControlSignalTet1"),
                (self.ui.tauValueLabel_phaseShift_6, self._device_name + "PhaseShiftControlSignalTet2"),
                #(self.ui.tauValueLabel_Tetrode1AEn, self._device_name + "/GainTetrodeEnableA"),

                (self.ui.tauValueLabel_Tetrode1A, "GainTetrode1"),
                (self.ui.tauValueLabel_Tetrode2A, "GainTetrode2"),

                (self.ui.tauValueLabel_filterStage, "FilterStages"),
                (self.ui.tauValueLabel_samplesAv, "NumSamplesAverage"),
                ]

        self._comboboxes = [
                (self.ui.comboBox_voltInc, "VoltageIncreaseRate"),
                (self.ui.comboBox_phaseIncRate, "PhaseIncreaseRate"),
                (self.ui.comboBox_quad, "QuadrantSelectionA"),
                (self.ui.comboBox_lookRef, "LookRefA"),
                (self.ui.comboBox_loopEn, "SlowIqLoopEnable"),
                (self.ui.comboBox_loopInputA, "SlowIqLoopInputSelection"),
                (self.ui.comboBox_phaseShiftEn, "ADCsPhaseShiftEnableA"),
                (self.ui.comboBox_DACsGainEn, "DACsPhaseShiftEnableA"),
                #(self.ui.comboBox_GainTetA1En, self._device_name + "/GainTetrodeEnableA"),
                ]

def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = IqLoopsSettings()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


