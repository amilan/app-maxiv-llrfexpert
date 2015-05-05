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
                (self.ui.tauValueLabel_IcavRef, "Diag_IRef"),
                (self.ui.tauValueLabel_IcavVolt, "Diag_IcavLoops"),
                (self.ui.tauValueLabel_IFwTet1Loop, "Diag_IFwTet1Loops"),
                (self.ui.tauValueLabel_IFwTet2Loop, "Diag_IFwTet2Loops"),
                (self.ui.tauValueLabel_IFwCircInLoop, "Diag_IFwCircInLoops"),
                (self.ui.tauValueLabel_IFwCavLoop, "Diag_IFwCavLoops"),
                (self.ui.tauValueLabel_ILoopInput, "Diag_IloopinputSlowpiIq"),
                (self.ui.tauValueLabel_IerrorP, "Diag_Ierror"),
                (self.ui.tauValueLabel_IerrorA, "Diag_Ierroraccum"),
                (self.ui.tauValueLabel_IcrtlA, "Diag_Icontrol"),
                (self.ui.tauValueLabel_IcrtlAc1, "Diag_Icontrol1"),
                (self.ui.tauValueLabel_IcrtlAc2, "Diag_Icontrol2"),
                (self.ui.tauValueLabel_IMOA, "Diag_Imo"),
                # Q attributes
                (self.ui.tauValueLabel_QcavRef, "Diag_Qref"),
                (self.ui.tauValueLabel_QcavVolt, "Diag_QcavLoops"),
                (self.ui.tauValueLabel_QFwTet1Loop, "Diag_QFwTet1Loops"),
                (self.ui.tauValueLabel_QFwTet2Loop, "Diag_QFwTet2Loops"),
                (self.ui.tauValueLabel_QFwCircInLoop, "Diag_QFwCircInLoops"),
                (self.ui.tauValueLabel_QFwCavLoop, "Diag_QFwCavLoops"),
                (self.ui.tauValueLabel_QLoopInput, "Diag_QloopinputSlowpiIq"),
                (self.ui.tauValueLabel_QerrorP, "Diag_Qerror"),
                (self.ui.tauValueLabel_QerrorA, "Diag_Qerroraccum"),
                (self.ui.tauValueLabel_QctrlA, "Diag_Qcontrol"),
                (self.ui.tauValueLabel_QctrlAc1, "Diag_Qcontrol1"),
                (self.ui.tauValueLabel_QctrlAc2, "Diag_Qcontrol2"),
                (self.ui.tauValueLabel_QMOA, "Diag_Qmo"),
                # Amp attributes
                (self.ui.tauValueLabel_ampcavRef, "Diag_Ampref"),
                (self.ui.tauValueLabel_ampCavVolt, "Diag_AmpcavLoops"),
                (self.ui.tauValueLabel_ampFwTet1Loop, "Diag_AmpFwTet1Loops"),
                (self.ui.tauValueLabel_ampFwTet2Loop, "Diag_AmpFwTet2Loops"),
                (self.ui.tauValueLabel_ampFwCircInLoop, "Diag_AmpFwCircInLoops"),
                (self.ui.tauValueLabel_ampFwCavLoop, "Diag_AmpFwCavLoops"),
                (self.ui.tauValueLabel_ampLoopInput, "Diag_AmploopinputSlowpiIq"),
                (self.ui.tauValueLabel_amperrorP, "Diag_Amperror"),
                (self.ui.tauValueLabel_amperrorA, "Diag_Amperroraccum"),
                (self.ui.tauValueLabel_ampctrlA, "Diag_Ampcontrol"),
                (self.ui.tauValueLabel_ampctrlAc1, "Diag_Ampcontrol1"),
                (self.ui.tauValueLabel_ampctrlAc2, "Diag_Ampcontrol2"),
                (self.ui.tauValueLabel_ampMOA, "Diag_Ampmo"),
                # # Phase attributes
                (self.ui.tauValueLabel_phasecavRef, "Diag_Phref"),
                (self.ui.tauValueLabel_phasecavVolt, "Diag_PhcavLoops"),
                (self.ui.tauValueLabel_phaseFwTet1Loop, "Diag_PhFwTet1Loops"),
                (self.ui.tauValueLabel_phaseFwTet2Loop, "Diag_PhFwTet2Loops"),
                (self.ui.tauValueLabel_phaseFwCircInLoop, "Diag_PhFwCircInLoops"),
                (self.ui.tauValueLabel_phaseFwCavLoop, "Diag_PhFwCavLoops"),
                (self.ui.tauValueLabel_phaseLoopInput, "Diag_PhloopinputSlowpiIq"),
                (self.ui.tauValueLabel_phaseerrorP, "Diag_Pherror"),
                (self.ui.tauValueLabel_phaseerrorA, "Diag_Pherroraccum"),
                (self.ui.tauValueLabel_phasectrlA, "Diag_Phcontrol"),
                (self.ui.tauValueLabel_phasectrlAc1, "Diag_Phcontrol1"),
                (self.ui.tauValueLabel_phasectrlAc2, "Diag_Phcontrol2"),
                (self.ui.tauValueLabel_phaseMOA, "Diag_Phmo"),
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

