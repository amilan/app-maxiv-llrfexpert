#!/usr/bin/env python

###############################################################################
#     Fim is a widget used for the LLRF Expert GUI.
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
Fim is a widget used for the LLRF Expert GUI.
"""

__all__ = ['FIM']

__author__ = "amilan"

__docformat__ = 'restructuredtext'


from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.commons import *
from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget


@UILoadable(with_ui='ui')
class FIM(BaseLLRFWidget):

    def __init__(self, parent=None):
        BaseLLRFWidget.__init__(self, parent)
        self.loadUi()

    @alert_problems
    def _create_attributes_lists(self):
        self._attributes = [
            (self.ui.taurusValueCheckBox, 'DisitckRvTet1DacsoffloopsstbyA'),
            (self.ui.taurusValueCheckBox_1, 'DisitckRvTet1PindiodeswitchA'),
            (self.ui.taurusValueCheckBox_2, 'DisitckRvTet1FdltrgA'),
            (self.ui.taurusValueCheckBox_3, 'DisitckRvTet1PlctxoffA'),
            (self.ui.taurusValueCheckBox_4, 'DisitckRvTet1MpsA'),
            (self.ui.taurusValueCheckBox_5, 'DisitckRvTet1DiagA'),

            (self.ui.taurusValueCheckBox_6, 'DisitckRvTet2DacsoffloopsstbyA'),
            (self.ui.taurusValueCheckBox_7, 'DisitckRvTet2PindiodeswitchA'),
            (self.ui.taurusValueCheckBox_8, 'DisitckRvTet2FdltrgA'),
            (self.ui.taurusValueCheckBox_9, 'DisitckRvTet2PlctxoffA'),
            (self.ui.taurusValueCheckBox_10, 'DisitckRvTet2MpsA'),
            (self.ui.taurusValueCheckBox_11, 'DisitckRvTet2DiagA'),

            (self.ui.taurusValueCheckBox_12, 'DisitckRvCircDacsoffloopsstbyA'),
            (self.ui.taurusValueCheckBox_13, 'DisitckRvCircPindiodeswitchA'),
            (self.ui.taurusValueCheckBox_14, 'DisitckRvCircFdltrgA'),
            (self.ui.taurusValueCheckBox_15, 'DisitckRvCircPlctxoffA'),
            (self.ui.taurusValueCheckBox_16, 'DisitckRvCircMpsA'),
            (self.ui.taurusValueCheckBox_17, 'DisitckRvCircDiagA'),

            (self.ui.taurusValueCheckBox_18, 'DisitckFwLoadDacsoffloopsstbyA'),
            (self.ui.taurusValueCheckBox_19, 'DisitckFwLoadPindiodeswitchA'),
            (self.ui.taurusValueCheckBox_20, 'DisitckFwLoadFdltrgA'),
            (self.ui.taurusValueCheckBox_21, 'DisitckFwLoadPlctxoffA'),
            (self.ui.taurusValueCheckBox_22, 'DisitckFwLoadMpsA'),
            (self.ui.taurusValueCheckBox_23, 'DisitckFwLoadDiagA'),

            (self.ui.taurusValueCheckBox_24, 'DisitckFwHybLoadDacsoffloopsstbyA'),
            (self.ui.taurusValueCheckBox_25, 'DisitckFwHybLoadPindiodeswitchA'),
            (self.ui.taurusValueCheckBox_26, 'DisitckFwHybLoadFdltrgA'),
            (self.ui.taurusValueCheckBox_27, 'DisitckFwHybLoadPlctxoffA'),
            (self.ui.taurusValueCheckBox_28, 'DisitckFwHybLoadMpsA'),
            (self.ui.taurusValueCheckBox_29, 'DisitckFwHybLoadDiagA'),

            (self.ui.taurusValueCheckBox_30, 'DisitckRvCavDacsoffloopsstbyA'),
            (self.ui.taurusValueCheckBox_31, 'DisitckRvCavPindiodeswitchA'),
            (self.ui.taurusValueCheckBox_32, 'DisitckRvCavFdltrgA'),
            (self.ui.taurusValueCheckBox_33, 'DisitckRvCavPlctxoffA'),
            (self.ui.taurusValueCheckBox_34, 'DisitckRvCavMpsA'),
            (self.ui.taurusValueCheckBox_35, 'DisitckRvCavDiagA'),

            (self.ui.taurusValueCheckBox_36, 'DisitckArcsDacsoffloopsstbyA'),
            (self.ui.taurusValueCheckBox_37, 'DisitckArcsPindiodeswitchA'),
            (self.ui.taurusValueCheckBox_38, 'DisitckArcsFdltrgA'),
            (self.ui.taurusValueCheckBox_39, 'DisitckArcsPlctxoffA'),
            (self.ui.taurusValueCheckBox_40, 'DisitckArcsMpsA'),
            (self.ui.taurusValueCheckBox_41, 'DisitckArcsDiagA'),

            (self.ui.taurusValueCheckBox_42, 'DisitckVacuumDacsoffloopsstbyA'),
            (self.ui.taurusValueCheckBox_43, 'DisitckVacuumPindiodeswitchA'),
            (self.ui.taurusValueCheckBox_44, 'DisitckVacuumFdltrgA'),
            (self.ui.taurusValueCheckBox_45, 'DisitckVacuumPlctxoffA'),
            (self.ui.taurusValueCheckBox_46, 'DisitckVacuumMpsA'),
            (self.ui.taurusValueCheckBox_47, 'DisitckVacuumDiagA'),

            (self.ui.taurusValueCheckBox_48, 'DisitckManualInterlockDacsoffloopsstbyA'),
            (self.ui.taurusValueCheckBox_49, 'DisitckManualInterlockPindiodeswitchA'),
            (self.ui.taurusValueCheckBox_50, 'DisitckManualInterlockFdltrgA'),
            (self.ui.taurusValueCheckBox_51, 'DisitckManualInterlockPlctxoffA'),
            (self.ui.taurusValueCheckBox_52, 'DisitckManualInterlockMpsA'),
            (self.ui.taurusValueCheckBox_53, 'DisitckManualInterlockDiagA'),

            (self.ui.taurusValueCheckBox_54, 'DisitckPlungerEndSwitchesUPDacsoffloopsstbyA'),
            (self.ui.taurusValueCheckBox_55, 'DisitckPlungerEndSwitchesUPPindiodeswitchA'),
            (self.ui.taurusValueCheckBox_56, 'DisitckPlungerEndSwitchesUPFdltrgA'),
            (self.ui.taurusValueCheckBox_57, 'DisitckPlungerEndSwitchesUPPlctxoffA'),
            (self.ui.taurusValueCheckBox_58, 'DisitckPlungerEndSwitchesUPMpsA'),
            (self.ui.taurusValueCheckBox_59, 'DisitckPlungerEndSwitchesUPDiagA'),

            (self.ui.taurusValueCheckBox_60, 'DisitckPlungerEndSwitchesDownDacsoffloopsstbyA'),
            (self.ui.taurusValueCheckBox_61, 'DisitckPlungerEndSwitchesDownPindiodeswitchA'),
            (self.ui.taurusValueCheckBox_62, 'DisitckPlungerEndSwitchesDownFdltrgA'),
            (self.ui.taurusValueCheckBox_63, 'DisitckPlungerEndSwitchesDownPlctxoffA'),
            (self.ui.taurusValueCheckBox_64, 'DisitckPlungerEndSwitchesDownMpsA'),
            (self.ui.taurusValueCheckBox_65, 'DisitckPlungerEndSwitchesDownDiagA'),

            (self.ui.taurusValueCheckBox_66, 'DisitckMpsDacsoffloopsstbyA'),
            (self.ui.taurusValueCheckBox_67, 'DisitckMpsPindiodeswitchA'),
            (self.ui.taurusValueCheckBox_68, 'DisitckMpsFdltrgA'),
            (self.ui.taurusValueCheckBox_69, 'DisitckMpsPlctxoffA'),
            (self.ui.taurusValueCheckBox_70, 'DisitckMpsMpsA'),
            (self.ui.taurusValueCheckBox_71, 'DisitckMpsDiagA')
        ]

        self._attributes_readback = []

        self._comboboxes = []

def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = Conditioning()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
