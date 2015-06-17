#!/usr/bin/env python

###############################################################################
#     PolarDiag is a widget used for the LLRF Expert GUI.
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
PolarDiag is a widget used for the LLRF Expert GUI.
"""

__all__ = ['PolarDiag']

__author__ = "amilan"

__docformat__ = 'restructuredtext'

from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.commons import *
from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget


@UILoadable(with_ui='ui')
class PolarDiag(BaseLLRFWidget):

    def __init__(self, parent=None):
        BaseLLRFWidget.__init__(self, parent)
        self.loadUi()

    @alert_problems
    def _create_attributes_lists(self):
        self._attributes = []

        self._attributes_readback = [
                # I attributes
                (self.ui.tauValueLabel_IcavRef, "Diag_IRefA"),
                (self.ui.tauValueLabel_IcavVolt, "Diag_IcavLoopsA"),
                (self.ui.tauValueLabel_IFwTet1Loop, "Diag_IFwTet1LoopsA"),
                (self.ui.tauValueLabel_IFwTet2Loop, "Diag_IFwTet2LoopsA"),
                (self.ui.tauValueLabel_IFwCircInLoop, "Diag_IFwCircInLoopsA"),
                (self.ui.tauValueLabel_IFwCavLoop, "Diag_IFwCavLoopsA"),
                (self.ui.tauValueLabel_ILoopInput, "Diag_IpolarForAmplitudeLoopA"),
                (self.ui.tauValueLabel_IPhLoopInput, "Diag_IpolarForPhaseLoopA"),
                (self.ui.tauValueLabel_IcrtlA, "Diag_IcontrolA"),
                (self.ui.tauValueLabel_IcrtlAc1, "Diag_Icontrol1A"),
                (self.ui.tauValueLabel_IcrtlAc2, "Diag_Icontrol2A"),
                # Q attributes
                (self.ui.tauValueLabel_QcavRef, "Diag_QrefA"),
                (self.ui.tauValueLabel_QcavVolt, "Diag_QcavLoopsA"),
                (self.ui.tauValueLabel_QFwTet1Loop, "Diag_QFwTet1LoopsA"),
                (self.ui.tauValueLabel_QFwTet2Loop, "Diag_QFwTet2LoopsA"),
                (self.ui.tauValueLabel_QFwCircInLoop, "Diag_QFwCircInLoopsA"),
                (self.ui.tauValueLabel_QFwCavLoop, "Diag_QFwCavLoopsA"),
                (self.ui.tauValueLabel_QLoopInput, "Diag_QpolarForAmplitudeLoopA"),
                (self.ui.tauValueLabel_QPhLoopInput, "Diag_QpolarForPhaseLoopA"),
                (self.ui.tauValueLabel_QctrlA, "Diag_QcontrolA"),
                (self.ui.tauValueLabel_QctrlAc1, "Diag_Qcontrol1A"),
                (self.ui.tauValueLabel_QctrlAc2, "Diag_Qcontrol2A"),
                # Amp attributes
                (self.ui.tauValueLabel_ampcavRef, "Diag_AmprefA"),
                (self.ui.tauValueLabel_ampCavVolt, "Diag_AmpcavLoopsA"),
                (self.ui.tauValueLabel_ampFwTet1Loop, "Diag_AmpFwTet1LoopsA"),
                (self.ui.tauValueLabel_ampFwTet2Loop, "Diag_AmpFwTet2LoopsA"),
                (self.ui.tauValueLabel_ampFwCircInLoop, "Diag_AmpFwCircInLoopsA"),
                (self.ui.tauValueLabel_ampFwCavLoop, "Diag_AmpFwCavLoopsA"),
                (self.ui.tauValueLabel_ampLoopInput, "Diag_AmpInputOfAmpLoopA"),
                (self.ui.tauValueLabel_ampPhLoopInput, "Diag_AmpInputOfAmpLoopA"),
                (self.ui.tauValueLabel_ampLoopError, "Diag_AmpLoopErrorA"),
                (self.ui.tauValueLabel_ampctrlA, "Diag_AmpcontrolA"),
                (self.ui.tauValueLabel_ampctrlAc1, "Diag_Ampcontrol1A"),
                (self.ui.tauValueLabel_ampctrlAc2, "Diag_Ampcontrol2A"),
                (self.ui.tauValueLabel_ampLoopErrorAccum, "Diag_AmpLoopErrorAccumA"),
                # # Phase attributes
                (self.ui.tauValueLabel_phasecavRef, "Diag_PhrefA"),
                (self.ui.tauValueLabel_phasecavVolt, "Diag_PhcavLoopsA"),
                (self.ui.tauValueLabel_phaseFwTet1Loop, "Diag_PhFwTet1LoopsA"),
                (self.ui.tauValueLabel_phaseFwTet2Loop, "Diag_PhFwTet2LoopsA"),
                (self.ui.tauValueLabel_phaseFwCircInLoop, "Diag_PhFwCircInLoopsA"),
                (self.ui.tauValueLabel_phaseFwCavLoop, "Diag_PhFwCavLoopsA"),
                (self.ui.tauValueLabel_phaseLoopInput, "Diag_PhaseInputOfAmpLoopA"),
                (self.ui.tauValueLabel_phasePhLoopInput, "Diag_PhInputOfPhaseLoopA"),
                (self.ui.tauValueLabel_phaseLoopError, "Diag_PhLoopErrorA"),
                (self.ui.tauValueLabel_phasectrlA, "Diag_PhcontrolA"),
                (self.ui.tauValueLabel_phasectrlAc1, "Diag_Phcontrol1A"),
                (self.ui.tauValueLabel_phasectrlAc2, "Diag_Phcontrol2A"),
                (self.ui.tauValueLabel_phaseLoopErrorAccum, "Diag_PhLoopErrorAccumA"),
        ]

        self._comboboxes = []

def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = PolarDiag()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

