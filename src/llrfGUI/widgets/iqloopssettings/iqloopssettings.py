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

from iqloopssettings import * 


from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable
from utils import tih, alert_problems

@UILoadable(with_ui='ui')
class IqLoopsSettings(Qt.QWidget):

    def __init__(self, parent=None):
        Qt.QWidget.__init__(self, parent)
        self.loadUI()
        # self.set_comboboxes()
        # self.connect_comboboxes()
        # self.connect_attributes()

    @alert_problems
    def setModel(self, model):
        self._device_name = model
        self._set_comboboxes()
        self._create_attributes_lists()
        self._connect_all_attributes()

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
                (self.ui.lineEdit_cavVolt, self._device_name + "/AmpRefIn"),
                (self.ui.lineEdit_cavPhase, self._device_name + "/PhaseRefIn"),

                (self.ui.lineEdit_ampRefMinA, self._device_name + "/AmpRefMin"),
                (self.ui.lineEdit_phaseRefMinA, self._device_name + "/PhaseRefMin"),

                (self.ui.lineEdit_PILimit, self._device_name + "/PILimitA"),
                (self.ui.lineEdit_ki, self._device_name + "/KiA"),
                (self.ui.lineEdit_kp, self._device_name + "/KpA"),

                (self.ui.lineEdit_gainola, self._device_name + "/GainOL"),

                (self.ui.lineEdit_phaseShift, self._device_name + "/PhaseShiftCav"),
                (self.ui.lineEdit_phaseShift_10, self._device_name + "/PhaseShiftFwTet1"),
                (self.ui.lineEdit_phaseShift_11, self._device_name + "/PhaseShiftFwTet2"),
                (self.ui.lineEdit_phaseShift_13, self._device_name + "/PhaseShiftFwCirc"),
                (self.ui.lineEdit_phaseShift_15, self._device_name + "/PhaseShiftFwCav"),

#                 (self.ui.lineEdit_phaseShift_3, self._device_name + "/PhaseShiftDACA1"),
#                 (self.ui.lineEdit_phaseShift_5, self._device_name + "/PhaseShiftDACA2"),

                (self.ui.lineEdit_Tetrode1A, self._device_name + "/GainTetrode1"),
                (self.ui.lineEdit_Tetrode2A, self._device_name + "/GainTetrode2"),

                (self.ui.lineEdit_filterStage, self._device_name + "/FilterStages"),
                (self.ui.lineEdit_samplesAv, self._device_name + "/SamplesToAverage"),
                ]

        self._attributes_readback = [
                (self.ui.tauValueLabel_cavVolt_2, self._device_name + "/AmpRefIn"),
                (self.ui.tauValueLabel_cavPhase_2, self._device_name + "/PhRefIn"),

                (self.ui.tauValueLabel_voltInc, self._device_name + "/VoltageRateIncrease"),
                (self.ui.tauValueLabel_phaseIncRate, self._device_name + "/PhaseIncreaseRateA"),

                (self.ui.tauValueLabel_ampRefMinA, self._device_name + "/AmpRefMin"),
                (self.ui.tauValueLabel_phaseRefMinA, self._device_name + "/PhRefMin"),

                (self.ui.tauValueLabel_PILimit_2, self._device_name + "/PILimitA"),
                (self.ui.tauValueLabel_ki_2, self._device_name + "/KiA"),
                (self.ui.tauValueLabel_kp_2, self._device_name + "/KpA"),
                (self.ui.tauValueLabel_quad, self._device_name + "/QuadrantSelectionA"),
                (self.ui.tauValueLabel_lookRef, self._device_name + "/LookRefA"),
                (self.ui.tauValueLabel_lookEn, self._device_name + "/LoopEnableA"),

                #(self.ui.tauValueLabel_loopInputA, self._device_name + "/LoopInputA"),
                (self.ui.tauValueLabel_gainola, self._device_name + "/GainOLA"),
                (self.ui.tauValueLabel_phaseShiftEn, self._device_name + "/ADCsPhaseShiftEnableA"),
                (self.ui.tauValueLabel_phaseShift_2, self._device_name + "/PhaseShiftCav"),
                (self.ui.tauValueLabel_phaseShift_11, self._device_name + "/PhaseShiftFwTet1A"),
                (self.ui.tauValueLabel_phaseShift_12, self._device_name + "/PhaseShiftFwTet2A"),
                (self.ui.tauValueLabel_phaseShift_14, self._device_name + "/PhaseShiftFwCircA"),
                (self.ui.tauValueLabel_phaseShift_16, self._device_name + "/PhaseShiftFwCavA"),
                (self.ui.tauValueLabel_DACsGainEn, self._device_name + "/DACsPhaseShiftEnableA"),

                #(self.ui.tauValueLabel_phaseShift_4, self._device_name + "/PhaseShiftDACA1"),
                #(self.ui.tauValueLabel_phaseShift_6, self._device_name + "/PhaseShiftDACA2"),
                #(self.ui.tauValueLabel_Tetrode1AEn, self._device_name + "/GainTetrodeEnableA"),

                (self.ui.tauValueLabel_Tetrode1A, self._device_name + "/GainTetrode1"),
                (self.ui.tauValueLabel_Tetrode2A, self._device_name + "/GainTetrode2"),

                (self.ui.tauValueLabel_filterStage, self._device_name + "/FilterStagesA"),
                (self.ui.tauValueLabel_samplesAv, self._device_name + "/NumSamplesAverageA"),
                ]

        self._comboboxes = [
                (self.ui.comboBox_voltInc, self._device_name + "/VoltageRateIncrease"),
                (self.ui.comboBox_phaseIncRate, self._device_name + "/PhaseIncreaseRate"),
                (self.ui.comboBox_quad, self._device_name + "/QuadrantSelectionA"),
                (self.ui.comboBox_lookRef, self._device_name + "/LookRefA"),
                (self.ui.comboBox_loopEn, self._device_name + "/LoopEnableA"),

                #(self.ui.comboBox_loopInputA, self._device_name + "/LoopInputA"),
                (self.ui.comboBox_phaseShiftEn, self._device_name + "/ADCsPhaseShiftEnableA"),
                (self.ui.comboBox_DACsGainEn, self._device_name + "/DACsPhaseShiftEnableA"),
                #(self.ui.comboBox_GainTetA1En, self._device_name + "/GainTetrodeEnableA"),
                ]

def main():
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = IqLoopsSettings()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


