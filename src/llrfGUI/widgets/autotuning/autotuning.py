#!/usr/bin/env python

###############################################################################
##     AutoTuning is a widget used for the LLRF Expert GUI.
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

from autotuning import *
from widgets.basellrfwidget import BaseLLRFWidget

from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable
#from utils import tih, alert_problems
from utils.tih import *
from utils.decorators import alert_problems

@UILoadable(with_ui='ui')
class AutoTuning(BaseLLRFWidget):

    def __init__(self, parent=None):
        BaseLLRFWidget.__init__(self, parent)
        self.loadUi()

  #  @alert_problems
  #  def setModel(self, model):
  #      self._device_name = model
  #      self._set_comboboxes()
  #      self._create_attributes_lists()
  #      self._connect_all_attributes()

    @alert_problems
    def _set_comboboxes(self):
        ## Tuning Loop A //////////////////////////////////////////////////////
        self.ui.comboBox_tuningEn.addValueNames(CB)
        self.ui.comboBox_tuningPosEn.addValueNames(CB)
        self.ui.comboBox_tuningFreq.addValueNames(CC)
        self.ui.comboBox_tuningTrgEnA.addValueNames(CFS)
        self.ui.comboBox_tuningFFEnA.addValueNames(CB)
        self.ui.comboBox_tuningFilterEnA.addValueNames(CB)

        ## Tuning Loop B //////////////////////////////////////////////////////
        # self.ui.comboBox_tuningEn_2.addValueNames(CB)
        # self.ui.comboBox_tuningPosEn_2.addValueNames(CB)
        # self.ui.comboBox_tuningFreq_2.addValueNames(CC)
        # self.ui.comboBox_tuningTrgEnB.addValueNames(CFS)
        # self.ui.comboBox_tuningFFEnB.addValueNames(CB)
        # self.ui.comboBox_tuningFilterEnB.addValueNames(CB)

  #  @alert_problems
  #  def _connect_all_attributes(self):
  #      for attribute in self._attributes:
  #          self.connect_attribute(attribute[0], attribute[1])

  #      for attribute in self._attributes_readback:
  #          self.connect_attribute(attribute[0], attribute[1])

  #      for combobox in self._comboboxes:
  #          self.connect_combobox(combobox[0], combobox[1])

  #  @alert_problems
  #  def connect_attribute(self, widget, attribute):
  #      widget.setModel(attribute)

  #  @alert_problems
  #  def connect_combobox(self, widget, attribute):
  #      widget.setModelName(attribute)

    @alert_problems
    def _create_attributes_lists(self):
        self._attributes = [
            (self.ui.lineEdit_tuningOffset, self._device_name + "/PhaseOffsetA"),
            (self.ui.lineEdit_marginUp_2, self._device_name + "/MarginUpA"),
            (self.ui.lineEdit_marginLow_2, self._device_name + "/MarginLowA"),
            (self.ui.lineEdit_forwardMin, self._device_name + "/FwMinA"),
            #(self.ui.lineEdit_tuningDelayA, self._device_name + "/TuningDelayA"),
            # (self.ui.lineEdit_tuningFFStepsA, self._device_name + "/TuningFFStepsA"),
        ]

        self._attributes_readback = [
            (self.ui.taurusBoolLed_31, self._device_name + "/TuningOnDiagA"),
            (self.ui.taurusBoolLed_32, self._device_name + "/FreqUpA"),
            (self.ui.tauValueLabel_tuningEn, self._device_name + "/TuningEnableA"),
            (self.ui.tauValueLabel_tuningPosEn, self._device_name + "/TuningPosEnA"),
            (self.ui.tauValueLabel_tuningFreq, self._device_name + "/PulsesFrequencyA"),
            (self.ui.tauValueLabel_marginUp, self._device_name + "/MarginUpA"),
            (self.ui.tauValueLabel_marginLow, self._device_name + "/MarginLowA"),
            (self.ui.tauValueLabel_tuningOffset, self._device_name + "/PhaseOffsetA"),
            (self.ui.tauValueLabel_forwardMin_2, self._device_name + "/FwMinA"),
            (self.ui.tauValueLabel_tuningFilterEnA, self._device_name + "/TuningFilterEnableA"),
            (self.ui.tauValueLabel_tuningDelayA, self._device_name + "/TuningDelayA"),
            (self.ui.tauValueLabel_tuningTrgEnA, self._device_name + "/TuningTriggerEnableA"),
            (self.ui.tauValueLabel_tuningFFEnA, self._device_name + "/TuningFFA"),
            (self.ui.tauValueLabel_tuningFFStepsA, self._device_name + "/TuningFFStepsA"),
        ]

        self._comboboxes = [
            (self.ui.comboBox_tuningEn, self._device_name + "/TuningEnableA"),
            (self.ui.comboBox_tuningPosEn, self._device_name + "/TuningPosEnA"),
            (self.ui.comboBox_tuningFreq, self._device_name + "/PulsesFrequency"),
            #(self.ui.comboBox_tuningTrgEnA, self._device_name + "/TuningTriggerEnableA"),
            #(self.ui.comboBox_tuningFFEnA, self._device_name + "/TuningFFA"),
            #(self.ui.comboBox_tuningFilterEnA, self._device_name + "/TuningFilterEnableA"),
        ]

def main():
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = AutoTuning()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
