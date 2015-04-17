#!/usr/bin/env python

###############################################################################
#     AutoTuning is a widget used for the LLRF Expert GUI.
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
AutoTuning is a widget used for the LLRF Expert GUI.
"""

__all__ = ['AutoTuning']

__author__ = "amilan"

__docformat__ = 'restructuredtext'

from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable

#from utils import tih, alert_problems
from llrfgui.utils.commons import *
from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget


@UILoadable(with_ui='ui')
class AutoTuning(BaseLLRFWidget):

    def __init__(self, parent=None):
        BaseLLRFWidget.__init__(self, parent)
        self.loadUi()

    @alert_problems
    def _set_comboboxes(self):
        # Tuning Loop A
        self.ui.comboBox_tuningEn.addValueNames(CB)
        self.ui.comboBox_tuningPosEn.addValueNames(CB)
        self.ui.comboBox_tuningFreq.addValueNames(CC)
        self.ui.comboBox_tuningTrgEnA.addValueNames(CFS)
        self.ui.comboBox_tuningFilterEnA.addValueNames(CB)

        # Tuning Loop B
        # self.ui.comboBox_tuningEn_2.addValueNames(CB)
        # self.ui.comboBox_tuningPosEn_2.addValueNames(CB)
        # self.ui.comboBox_tuningFreq_2.addValueNames(CC)
        # self.ui.comboBox_tuningTrgEnB.addValueNames(CFS)
        # self.ui.comboBox_tuningFilterEnB.addValueNames(CB)

    @alert_problems
    def _create_attributes_lists(self):
        self._attributes = [
            (self.ui.lineEdit_marginUp_2, "MarginUpA"),
            (self.ui.lineEdit_marginLow_2, "MarginLowA"),
            (self.ui.lineEdit_forwardMin, "Fwmina"),
            (self.ui.lineEdit_tuningOffset, "PhaseOffsetA"),
            (self.ui.lineEdit_tuningDelayA, "Tuningdelay"),
        ]

        self._attributes_readback = [
            (self.ui.taurusBoolLed_31, "_Diag_MovingPlungerAuto"),
            (self.ui.taurusBoolLed_32, "Diag_FreqUp"),
            (self.ui.tauValueLabel_tuningEn, "TuningEnableA"),
            (self.ui.tauValueLabel_tuningPosEn, "TuningPosEnA"),
            (self.ui.tauValueLabel_tuningFreq, "PulsesFrequency"),
            (self.ui.tauValueLabel_marginUp, "MarginUpA"),
            (self.ui.tauValueLabel_marginLow, "MarginLowA"),
            (self.ui.tauValueLabel_tuningOffset, "PhaseOffsetA"),
            (self.ui.tauValueLabel_forwardMin_2, "Fwmina"),
            (self.ui.tauValueLabel_tuningFilterEnA,"Tuningfilterenable"),
            (self.ui.tauValueLabel_tuningDelayA, "Tuningdelay"),
            (self.ui.tauValueLabel_tuningTrgEnA, "Tuningtriggerenable"),
        ]

        self._comboboxes = [
            (self.ui.comboBox_tuningEn, "TuningEnableA"),
            (self.ui.comboBox_tuningPosEn, "TuningPosEnA"),
            (self.ui.comboBox_tuningFreq, "PulsesFrequency"),
            (self.ui.comboBox_tuningTrgEnA, "Tuningtriggerenable"),
            (self.ui.comboBox_tuningFilterEnA, "Tuningfilterenable"),
        ]

def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = AutoTuning()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
