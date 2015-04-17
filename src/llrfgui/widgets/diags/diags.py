#!/usr/bin/env python

###############################################################################
#     Diags is a widget used for the LLRF Expert GUI.
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
Diags is a widget used for the LLRF Expert GUI.
"""

__all__ = ['Diags']

__author__ = "amilan"

__docformat__ = 'restructuredtext'

from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.commons import *
from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget


@UILoadable(with_ui='ui')
class Diags(BaseLLRFWidget):

    def __init__(self, parent=None):
        BaseLLRFWidget.__init__(self, parent)
        self.loadUi()

    @alert_problems
    def setModel(self, model):
        """
        :param model: Array of strings with the names of the device name
                      and the diagnostics device name
        """
        self._device_name = model[0]
        self._device_diag = model[1]
        # self._set_comboboxes()
        self._create_attributes_lists()
        self._connect_all_attributes()

    @alert_problems
    def connect_attribute(self, widget, attribute):
        widget.setModel(attribute)

    @alert_problems
    def _create_attributes_lists(self):
        self._attributes = []

        self._attributes_readback = [
            # I signals
            (self.ui.tauValueLabel_ICavVolt, self._device_name + "/Diag_IcavLoops"),
            (self.ui.tauValueLabel_IFwCavVolt_5, self._device_name + "/Diag_IFwCavLoops"),
            (self.ui.tauValueLabel_IRvCavVolt_3, self._device_diag + "/Diag_Irvcav"),
            (self.ui.tauValueLabel_IFwTet1_3, self._device_name + "/Diag_IFwTet1Loops"),
            (self.ui.tauValueLabel_IFwTet2_3, self._device_name + "/Diag_IFwTet2Loops"),
            (self.ui.tauValueLabel_IRvTet1_3, self._device_diag + "/Diag_Irvtet1"),
            (self.ui.tauValueLabel_IRvTet2_3, self._device_diag + "/Diag_Irvtet2"),
            (self.ui.tauValueLabel_IFwCirc_3, self._device_name + "/Diag_IFwCircInLoops"),
            (self.ui.tauValueLabel_IRvCirc_3, self._device_diag + "/Diag_Irvcirc"),
            (self.ui.tauValueLabel_IFwLoad_3, self._device_diag + "/Diag_Ifwload"),
            (self.ui.tauValueLabel_IFwHybLoad_3, self._device_diag + "/Diag_Ifwhybload"),
            (self.ui.tauValueLabel_IMO_5, self._device_diag + "/Diag_Imo"),
            (self.ui.tauValueLabel_Landau, self._device_diag + "/Diag_Ilandau"),
            # Q signals
            (self.ui.tauValueLabel_QCavVolt, self._device_name + "/Diag_QcavLoops"),
            (self.ui.tauValueLabel_QFwCavVolt_5, self._device_name + "/Diag_QFwCavLoops"),
            (self.ui.tauValueLabel_QRvCavVolt_3, self._device_diag + "/Diag_Qrvcav"),
            (self.ui.tauValueLabel_QFwTet1_3, self._device_name + "/Diag_QFwTet1Loops"),
            (self.ui.tauValueLabel_QFwTet2_3, self._device_name + "/Diag_QFwTet2Loops"),
            (self.ui.tauValueLabel_QRvTet1_3, self._device_diag + "/Diag_Qrvtet1"),
            (self.ui.tauValueLabel_QRvTet2_3, self._device_diag + "/Diag_Qrvtet2"),
            (self.ui.tauValueLabel_QFwCirc_3, self._device_name + "/Diag_QFwCircInLoops"),
            (self.ui.tauValueLabel_QRvCirc_3, self._device_diag + "/Diag_Qrvcirc"),
            (self.ui.tauValueLabel_QFwLoad_3, self._device_diag + "/Diag_Qfwload"),
            (self.ui.tauValueLabel_QFwHybLoad_3, self._device_diag + "/Diag_Qfwhybload"),
            (self.ui.tauValueLabel_QMO_5, self._device_diag + "/Diag_Qmo"),
            (self.ui.tauValueLabel_QMO_6, self._device_diag + "/Diag_Qlandau"),
            # Amp signals
            (self.ui.tauValueLabel_ampFwCavVolt_6, self._device_name + "/Diag_AmpCavLoops"),
            (self.ui.tauValueLabel_ampFwCavVolt_5, self._device_name + "/Diag_AmpFwCavLoops"),
            (self.ui.tauValueLabel_ampRvCavVolt_3, self._device_diag + "/Diag_AmpRvcav"),
            (self.ui.tauValueLabel_ampFwTet1_3, self._device_name + "/Diag_AmpFwTet1Loops"),
            (self.ui.tauValueLabel_ampFwTet2_3, self._device_name + "/Diag_AmpFwTet2Loops"),
            (self.ui.tauValueLabel_ampRvTet1_3, self._device_diag + "/Diag_AmpRvtet1"),
            (self.ui.tauValueLabel_ampRvTet2_3, self._device_diag + "/Diag_AmpRvtet2"),
            (self.ui.tauValueLabel_ampFwCirc_3, self._device_name + "/Diag_AmpFwCircInLoops"),
            (self.ui.tauValueLabel_ampRvCirc_3, self._device_diag + "/Diag_AmpRvcirc"),
            (self.ui.tauValueLabel_ampFwLoad_3, self._device_diag + "/Diag_AmpFwload"),
            (self.ui.tauValueLabel_ampFwHybLoad_3, self._device_diag + "/Diag_AmpFwhybload"),
            (self.ui.tauValueLabel_ampMO_5, self._device_diag + "/Diag_AmpMo"),
            (self.ui.tauValueLabel_ampMO_6, self._device_diag + "/Diag_AmpLandau"),
            # Amp signals
            (self.ui.tauValueLabel_phaseFwCavVolt_6, self._device_name + "/Diag_PhCavLoops"),
            (self.ui.tauValueLabel_phaseFwCavVolt_5, self._device_name + "/Diag_PhFwCavLoops"),
            (self.ui.tauValueLabel_phaseRvCavVolt_3, self._device_diag + "/Diag_PhRvcav"),
            (self.ui.tauValueLabel_phaseFwTet1_3, self._device_name + "/Diag_PhFwTet1Loops"),
            (self.ui.tauValueLabel_phaseFwTet2_3, self._device_name + "/Diag_PhFwTet2Loops"),
            (self.ui.tauValueLabel_phaseRvTet1_3, self._device_diag + "/Diag_PhRvtet1"),
            (self.ui.tauValueLabel_phaseRvTet2_3, self._device_diag + "/Diag_PhRvtet2"),
            (self.ui.tauValueLabel_phaseFwCirc_3, self._device_name + "/Diag_PhFwCircInLoops"),
            (self.ui.tauValueLabel_phaseRvCirc_3, self._device_diag + "/Diag_PhRvcirc"),
            (self.ui.tauValueLabel_phaseFwLoad_3, self._device_diag + "/Diag_PhFwload"),
            (self.ui.tauValueLabel_phaseFwHybLoad_3, self._device_diag + "/Diag_PhFwhybload"),
            (self.ui.tauValueLabel_phaseMO_5, self._device_diag + "/Diag_PhMo"),
            (self.ui.tauValueLabel_phaseMO_6, self._device_diag + "/Diag_PhLandau"),
        ]

        self._comboboxes = []

def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = Diags()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
