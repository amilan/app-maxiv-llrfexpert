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
    def _create_attributes_lists(self):
        self._attributes = []

        self._attributes_readback = [
            # I signals
            (self.ui.tauValueLabel_ICavVolt, "Diag_IcavLoops"),
            (self.ui.tauValueLabel_IFwCavVolt, "Diag_IFwCavLoops"),
            (self.ui.tauValueLabel_IRvcavVolt, "Diag_Irvcav"),
            (self.ui.tauValueLabel_IFwTet1_3, "Diag_IFwTet1"),
            (self.ui.tauValueLabel_IFwTet2_3, "Diag_IFwTet2"),
            (self.ui.tauValueLabel_IRvTet1_3, "Diag_Irvtet1"),
            (self.ui.tauValueLabel_IRvTet2_3, "Diag_Irvtet2"),
            (self.ui.tauValueLabel_IFwCirc_3, "Diags_IFwCircInLoops"),
            (self.ui.tauValueLabel_IRvCirc_3, "Diag_Irvcirc"),
            (self.ui.tauValueLabel_IFwLoad_3, "Diag_Ifwload"),
            (self.ui.tauValueLabel_IFwHybLoad_3, "Diag_Ifwhybload"),
            (self.ui.tauValueLabel_IMO_5, "Diag_Imo"),
            (self.ui.tauValueLabel_Landau, "Diag_Ilandau"),
            # Q signals
            (self.ui.tauValueLabel_QCavVolt, "Diag_QcavLoops"),
            (self.ui.tauValueLabel_QFwCavVolt_5, "Diag_QFwCavLoops"),
            (self.ui.tauValueLabel_QRvCavVolt_3, "Diag_Qrvcav"),
            (self.ui.tauValueLabel_QFwTet1_3, "Diag_QFwTet1"),
            (self.ui.tauValueLabel_QFwTet2_3, "Diag_QFwTet2"),
            (self.ui.tauValueLabel_QRvTet1_3, "Diag_Qrvtet1"),
            (self.ui.tauValueLabel_QRvTet2_3, "Diag_Qrvtet2"),
            (self.ui.tauValueLabel_QFwCirc_3, "Diags_QFwCircInLoops"),
            (self.ui.tauValueLabel_QRvCirc_3, "Diag_Qrvcirc"),
            (self.ui.tauValueLabel_QFwLoad_3, "Diag_Qfwload"),
            (self.ui.tauValueLabel_QFwHybLoad_3, "Diag_Qfwhybload"),
            (self.ui.tauValueLabel_QMO_5, "Diag_Qmo"),
            (self.ui.tauValueLabel_QMO_6, "Diag_Qlandau"),
            # Amp signals
            (self.ui.tauValueLabel_ampFwCavVolt_6, "Diag_AmpCavLoops"),
            (self.ui.tauValueLabel_ampFwCavVolt_5, "Diag_AmpFwCavLoops"),
            (self.ui.tauValueLabel_ampRvCavVolt_3, "Diag_AmpRvcav"),
            (self.ui.tauValueLabel_ampFwTet1_3, "Diag_AmpFwTet1"),
            (self.ui.tauValueLabel_ampFwTet2_3, "Diag_AmpFwTet2"),
            (self.ui.tauValueLabel_ampRvTet1_3, "Diag_AmpRvtet1"),
            (self.ui.tauValueLabel_ampRvTet2_3, "Diag_AmpRvtet2"),
            (self.ui.tauValueLabel_ampFwCirc_3, "Diags_AmpFwCircInLoops"),
            (self.ui.tauValueLabel_ampRvCirc_3, "Diag_AmpRvcirc"),
            (self.ui.tauValueLabel_ampFwLoad_3, "Diag_AmpFwload"),
            (self.ui.tauValueLabel_ampFwHybLoad_3, "Diag_AmpFwhybload"),
            (self.ui.tauValueLabel_ampMO_5, "Diag_AmpMo"),
            (self.ui.tauValueLabel_ampMO_6, "Diag_AmpLandau"),
            # Amp signals
            (self.ui.tauValueLabel_phaseFwCavVolt_6, "Diag_PhCavLoops"),
            (self.ui.tauValueLabel_phaseFwCavVolt_5, "Diag_PhFwCavLoops"),
            (self.ui.tauValueLabel_phaseRvCavVolt_3, "Diag_PhRvcav"),
            (self.ui.tauValueLabel_phaseFwTet1_3, "Diag_PhFwTet1"),
            (self.ui.tauValueLabel_phaseFwTet2_3, "Diag_PhFwTet2"),
            (self.ui.tauValueLabel_phaseRvTet1_3, "Diag_PhRvtet1"),
            (self.ui.tauValueLabel_phaseRvTet2_3, "Diag_PhRvtet2"),
            (self.ui.tauValueLabel_phaseFwCirc_3, "Diags_PhFwCircInLoops"),
            (self.ui.tauValueLabel_phaseRvCirc_3, "Diag_PhRvcirc"),
            (self.ui.tauValueLabel_phaseFwLoad_3, "Diag_PhFwload"),
            (self.ui.tauValueLabel_phaseFwHybLoad_3, "Diag_PhFwhybload"),
            (self.ui.tauValueLabel_phaseMO_5, "Diag_PhMo"),
            (self.ui.tauValueLabel_phaseMO_6, "Diag_PhLandau"),
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
