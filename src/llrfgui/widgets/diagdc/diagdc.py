#!/usr/bin/env python

###############################################################################
#     Diagdc is a widget used for the LLRF Expert GUI.
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
Diagdc is a widget used for the LLRF Expert GUI.
"""

__all__ = ['Diagdc']

__author__ = "amilan"

__docformat__ = 'restructuredtext'

from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.commons import *
from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget


@UILoadable(with_ui='ui')
class Diagdc(BaseLLRFWidget):

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
                # [?] ILoopInput?
                #(self.ui.tauValueLabel_ILoopInput, "Diag_IRef"),
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
                # [?] ILoopInput?
                #(self.ui.tauValueLabel_QLoopInput, "Diag_QRef"),
                (self.ui.tauValueLabel_QerrorP, "Diag_Qerror"),
                (self.ui.tauValueLabel_QerrorA, "Diag_Qerroraccum"),
                (self.ui.tauValueLabel_QctrlA, "Diag_Qcontrol"),
                (self.ui.tauValueLabel_QctrlAc1, "Diag_Qcontrol1"),
                (self.ui.tauValueLabel_QctrlAc2, "Diag_Qcontrol2"),
                (self.ui.tauValueLabel_QMOA, "Diag_Qmo"),
                # Amp attributes
                # (self.ui.tauValueLabel_ampcavRef, "Diag_Qref"),
                # (self.ui.tauValueLabel_ampcavVolt, "Diag_QcavLoops"),
                # (self.ui.tauValueLabel_ampFwTet1Loop, "Diag_QFwTet1Loops"),
                # (self.ui.tauValueLabel_ampFwTet2Loop, "Diag_QFwTet2Loops"),
                # (self.ui.tauValueLabel_ampFwCircInLoop, "Diag_QFwCircInLoops"),
                # (self.ui.tauValueLabel_ampFwCavLoop, "Diag_QFwCavLoops"),
                # # [?] ILoopInput?
                # #(self.ui.tauValueLabel_ampLoopInput, "Diag_QRef"),
                # (self.ui.tauValueLabel_amperrorP, "Diag_Qerror"),
                # (self.ui.tauValueLabel_amperrorA, "Diag_Qerroraccum"),
                # (self.ui.tauValueLabel_ampctrlA, "Diag_Qcontrol"),
                # (self.ui.tauValueLabel_ampctrlAc1, "Diag_Qcontrol1"),
                # (self.ui.tauValueLabel_ampctrlAc2, "Diag_Qcontrol2"),
                # (self.ui.tauValueLabel_ampMOA, "Diag_Qmo"),
                # # Phase attributes
                # (self.ui.tauValueLabel_phasecavRef, "Diag_Qref"),
                # (self.ui.tauValueLabel_phasecavVolt, "Diag_QcavLoops"),
                # (self.ui.tauValueLabel_phaseFwTet1Loop, "Diag_QFwTet1Loops"),
                # (self.ui.tauValueLabel_phaseFwTet2Loop, "Diag_QFwTet2Loops"),
                # (self.ui.tauValueLabel_phaseFwCircInLoop, "Diag_QFwCircInLoops"),
                # (self.ui.tauValueLabel_phaseFwCavLoop, "Diag_QFwCavLoops"),
                # # [?] ILoopInput?
                # #(self.ui.tauValueLabel_phaseLoopInput, "Diag_QRef"),
                # (self.ui.tauValueLabel_phaseerrorP, "Diag_Qerror"),
                # (self.ui.tauValueLabel_phaseerrorA, "Diag_Qerroraccum"),
                # (self.ui.tauValueLabel_phasectrlA, "Diag_Qcontrol"),
                # (self.ui.tauValueLabel_phasectrlAc1, "Diag_Qcontrol1"),
                # (self.ui.tauValueLabel_phasectrlAc2, "Diag_Qcontrol2"),
                # (self.ui.tauValueLabel_phaseMOA, "Diag_Qmo"),
        ]

        self._comboboxes = []

def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = Diagdc()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

