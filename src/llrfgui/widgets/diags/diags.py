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
            (self.ui.tauValueLabel_ICavVolt, self._device_name + "/Diag_IcavLoopsA"),
            (self.ui.tauValueLabel_IFwCavVolt_5, self._device_name + "/Diag_IFwCavLoopsA"),
            (self.ui.tauValueLabel_IRvCavVolt_3, self._device_diag + "/Diag_IrvcavA"),
            (self.ui.tauValueLabel_IFwTet1_3, self._device_name + "/Diag_IFwTet1LoopsA"),
            (self.ui.tauValueLabel_IFwTet2_3, self._device_name + "/Diag_IFwTet2LoopsA"),
            (self.ui.tauValueLabel_IRvTet1_3, self._device_diag + "/Diag_Irvtet1A"),
            (self.ui.tauValueLabel_IRvTet2_3, self._device_diag + "/Diag_Irvtet2A"),
            (self.ui.tauValueLabel_IFwCirc_3, self._device_name + "/Diag_IFwCircInLoopsA"),
            (self.ui.tauValueLabel_IRvCirc_3, self._device_diag + "/Diag_IrvcircA"),
            (self.ui.tauValueLabel_IFwLoad_3, self._device_diag + "/Diag_IfwloadA"),
            (self.ui.tauValueLabel_IFwHybLoad_3, self._device_diag + "/Diag_IfwhybloadA"),
            (self.ui.tauValueLabel_IMO_5, self._device_diag + "/Diag_ImoA"),
            (self.ui.tauValueLabel_Landau, self._device_diag + "/Diag_IlandauA"),
            # Q signals
            (self.ui.tauValueLabel_QCavVolt, self._device_name + "/Diag_QcavLoopsA"),
            (self.ui.tauValueLabel_QFwCavVolt_5, self._device_name + "/Diag_QFwCavLoopsA"),
            (self.ui.tauValueLabel_QRvCavVolt_3, self._device_diag + "/Diag_QrvcavA"),
            (self.ui.tauValueLabel_QFwTet1_3, self._device_name + "/Diag_QFwTet1LoopsA"),
            (self.ui.tauValueLabel_QFwTet2_3, self._device_name + "/Diag_QFwTet2LoopsA"),
            (self.ui.tauValueLabel_QRvTet1_3, self._device_diag + "/Diag_Qrvtet1A"),
            (self.ui.tauValueLabel_QRvTet2_3, self._device_diag + "/Diag_Qrvtet2A"),
            (self.ui.tauValueLabel_QFwCirc_3, self._device_name + "/Diag_QFwCircInLoopsA"),
            (self.ui.tauValueLabel_QRvCirc_3, self._device_diag + "/Diag_Qrvcirca"),
            (self.ui.tauValueLabel_QFwLoad_3, self._device_diag + "/Diag_QfwloadA"),
            (self.ui.tauValueLabel_QFwHybLoad_3, self._device_diag + "/Diag_QfwhybloadA"),
            (self.ui.tauValueLabel_QMO_5, self._device_diag + "/Diag_QmoA"),
            (self.ui.tauValueLabel_QMO_6, self._device_diag + "/Diag_QlandauA"),
            # Amp signals
            (self.ui.tauValueLabel_ampFwCavVolt_6, self._device_name + "/Diag_AmpCavLoopsA"),
            (self.ui.tauValueLabel_ampFwCavVolt_5, self._device_name + "/Diag_AmpFwCavLoopsA"),
            (self.ui.tauValueLabel_ampRvCavVolt_3, self._device_diag + "/Diag_AmpRvcavA"),
            (self.ui.tauValueLabel_ampFwTet1_3, self._device_name + "/Diag_AmpFwTet1LoopsA"),
            (self.ui.tauValueLabel_ampFwTet2_3, self._device_name + "/Diag_AmpFwTet2LoopsA"),
            (self.ui.tauValueLabel_ampRvTet1_3, self._device_diag + "/Diag_AmpRvtet1A"),
            (self.ui.tauValueLabel_ampRvTet2_3, self._device_diag + "/Diag_AmpRvtet2A"),
            (self.ui.tauValueLabel_ampFwCirc_3, self._device_name + "/Diag_AmpFwCircInLoopsA"),
            (self.ui.tauValueLabel_ampRvCirc_3, self._device_diag + "/Diag_AmpRvcircA"),
            (self.ui.tauValueLabel_ampFwLoad_3, self._device_diag + "/Diag_AmpFwloadA"),
            (self.ui.tauValueLabel_ampFwHybLoad_3, self._device_diag + "/Diag_AmpFwhybloadA"),
            (self.ui.tauValueLabel_ampMO_5, self._device_diag + "/Diag_AmpMoA"),
            (self.ui.tauValueLabel_ampMO_6, self._device_diag + "/Diag_AmpLandauA"),
            # Amp signals
            (self.ui.tauValueLabel_phaseFwCavVolt_6, self._device_name + "/Diag_PhCavLoopsA"),
            (self.ui.tauValueLabel_phaseFwCavVolt_5, self._device_name + "/Diag_PhFwCavLoopsA"),
            (self.ui.tauValueLabel_phaseRvCavVolt_3, self._device_diag + "/Diag_PhRvcavA"),
            (self.ui.tauValueLabel_phaseFwTet1_3, self._device_name + "/Diag_PhFwTet1LoopsA"),
            (self.ui.tauValueLabel_phaseFwTet2_3, self._device_name + "/Diag_PhFwTet2LoopsA"),
            (self.ui.tauValueLabel_phaseRvTet1_3, self._device_diag + "/Diag_PhRvtet1A"),
            (self.ui.tauValueLabel_phaseRvTet2_3, self._device_diag + "/Diag_PhRvtet2A"),
            (self.ui.tauValueLabel_phaseFwCirc_3, self._device_name + "/Diag_PhFwCircInLoopsA"),
            (self.ui.tauValueLabel_phaseRvCirc_3, self._device_diag + "/Diag_PhRvcircA"),
            (self.ui.tauValueLabel_phaseFwLoad_3, self._device_diag + "/Diag_PhFwloadA"),
            (self.ui.tauValueLabel_phaseFwHybLoad_3, self._device_diag + "/Diag_PhFwhybloadA"),
            (self.ui.tauValueLabel_phaseMO_5, self._device_diag + "/Diag_PhMoA"),
            (self.ui.tauValueLabel_phaseMO_6, self._device_diag + "/Diag_PhLandauA"),
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
