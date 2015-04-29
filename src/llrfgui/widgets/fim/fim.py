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
            (self.ui.taurusValueCheckBox, 'DisitckRvTet1Dacsoffloopsstby'),
            (self.ui.taurusValueCheckBox_1, 'DisitckRvTet1Pindiodeswitch'),
            (self.ui.taurusValueCheckBox_2, 'DisitckRvTet1Fdltrg'),
            (self.ui.taurusValueCheckBox_3, 'DisitckRvTet1Plctxoff'),
            (self.ui.taurusValueCheckBox_4, 'DisitckRvTet1Mps'),
            (self.ui.taurusValueCheckBox_5, 'DisitckRvTet1Diag'),

            (self.ui.taurusValueCheckBox_6, 'DisitckRvTet2Dacsoffloopsstby'),
            (self.ui.taurusValueCheckBox_7, 'DisitckRvTet2Pindiodeswitch'),
            (self.ui.taurusValueCheckBox_8, 'DisitckRvTet2Fdltrg'),
            (self.ui.taurusValueCheckBox_9, 'DisitckRvTet2Plctxoff'),
            (self.ui.taurusValueCheckBox_10, 'DisitckRvTet2Mps'),
            (self.ui.taurusValueCheckBox_11, 'DisitckRvTet2Diag'),

            (self.ui.taurusValueCheckBox_12, 'DisitckRvCircDacsoffloopsstby'),
            (self.ui.taurusValueCheckBox_13, 'DisitckRvCircPindiodeswitch'),
            (self.ui.taurusValueCheckBox_14, 'DisitckRvCircFdltrg'),
            (self.ui.taurusValueCheckBox_15, 'DisitckRvCircPlctxoff'),
            (self.ui.taurusValueCheckBox_16, 'DisitckRvCircMps'),
            (self.ui.taurusValueCheckBox_17, 'DisitckRvCircDiag'),

            (self.ui.taurusValueCheckBox_18, 'DisitckFwLoadDacsoffloopsstby'),
            (self.ui.taurusValueCheckBox_19, 'DisitckFwLoadPindiodeswitch'),
            (self.ui.taurusValueCheckBox_20, 'DisitckFwLoadFdltrg'),
            (self.ui.taurusValueCheckBox_21, 'DisitckFwLoadPlctxoff'),
            (self.ui.taurusValueCheckBox_22, 'DisitckFwLoadMps'),
            (self.ui.taurusValueCheckBox_23, 'DisitckFwLoadDiag'),

            (self.ui.taurusValueCheckBox_24, 'DisitckFwHybLoadDacsoffloopsstby'),
            (self.ui.taurusValueCheckBox_25, 'DisitckFwHybLoadPindiodeswitch'),
            (self.ui.taurusValueCheckBox_26, 'DisitckFwHybLoadFdltrg'),
            (self.ui.taurusValueCheckBox_27, 'DisitckFwHybLoadPlctxoff'),
            (self.ui.taurusValueCheckBox_28, 'DisitckFwHybLoadMps'),
            (self.ui.taurusValueCheckBox_29, 'DisitckFwHybLoadDiag'),

            (self.ui.taurusValueCheckBox_30, 'DisitckRvCavDacsoffloopsstby'),
            (self.ui.taurusValueCheckBox_31, 'DisitckRvCavPindiodeswitch'),
            (self.ui.taurusValueCheckBox_32, 'DisitckRvCavFdltrg'),
            (self.ui.taurusValueCheckBox_33, 'DisitckRvCavPlctxoff'),
            (self.ui.taurusValueCheckBox_34, 'DisitckRvCavMps'),
            (self.ui.taurusValueCheckBox_35, 'DisitckRvCavDiag'),

            (self.ui.taurusValueCheckBox_36, 'DisitckArcsDacsoffloopsstby'),
            (self.ui.taurusValueCheckBox_37, 'DisitckArcsPindiodeswitch'),
            (self.ui.taurusValueCheckBox_38, 'DisitckArcsFdltrg'),
            (self.ui.taurusValueCheckBox_39, 'DisitckArcsPlctxoff'),
            (self.ui.taurusValueCheckBox_40, 'DisitckArcsMps'),
            (self.ui.taurusValueCheckBox_41, 'DisitckArcsDiag'),

            (self.ui.taurusValueCheckBox_42, 'DisitckVacuumDacsoffloopsstby'),
            (self.ui.taurusValueCheckBox_43, 'DisitckVacuumPindiodeswitch'),
            (self.ui.taurusValueCheckBox_44, 'DisitckVacuumFdltrg'),
            (self.ui.taurusValueCheckBox_45, 'DisitckVacuumPlctxoff'),
            (self.ui.taurusValueCheckBox_46, 'DisitckVacuumMps'),
            (self.ui.taurusValueCheckBox_47, 'DisitckVacuumDiag'),

            (self.ui.taurusValueCheckBox_48, 'DisitckManualInterlockDacsoffloopsstby'),
            (self.ui.taurusValueCheckBox_49, 'DisitckManualInterlockPindiodeswitch'),
            (self.ui.taurusValueCheckBox_50, 'DisitckManualInterlockFdltrg'),
            (self.ui.taurusValueCheckBox_51, 'DisitckManualInterlockPlctxoff'),
            (self.ui.taurusValueCheckBox_52, 'DisitckManualInterlockMps'),
            (self.ui.taurusValueCheckBox_53, 'DisitckManualInterlockDiag'),

            (self.ui.taurusValueCheckBox_54, 'DisitckPlungerEndSwitchesUPDacsoffloopsstby'),
            (self.ui.taurusValueCheckBox_55, 'DisitckPlungerEndSwitchesUPPindiodeswitch'),
            (self.ui.taurusValueCheckBox_56, 'DisitckPlungerEndSwitchesUPFdltrg'),
            (self.ui.taurusValueCheckBox_57, 'DisitckPlungerEndSwitchesUPPlctxoff'),
            (self.ui.taurusValueCheckBox_58, 'DisitckPlungerEndSwitchesUPMps'),
            (self.ui.taurusValueCheckBox_59, 'DisitckPlungerEndSwitchesUPDiag'),

            (self.ui.taurusValueCheckBox_60, 'DisitckPlungerEndSwitchesDownDacsoffloopsstby'),
            (self.ui.taurusValueCheckBox_61, 'DisitckPlungerEndSwitchesDownPindiodeswitch'),
            (self.ui.taurusValueCheckBox_62, 'DisitckPlungerEndSwitchesDownFdltrg'),
            (self.ui.taurusValueCheckBox_63, 'DisitckPlungerEndSwitchesDownPlctxoff'),
            (self.ui.taurusValueCheckBox_64, 'DisitckPlungerEndSwitchesDownMps'),
            (self.ui.taurusValueCheckBox_65, 'DisitckPlungerEndSwitchesDownDiag'),

            (self.ui.taurusValueCheckBox_66, 'DisitckMpsDacsoffloopsstby'),
            (self.ui.taurusValueCheckBox_67, 'DisitckMpsPindiodeswitch'),
            (self.ui.taurusValueCheckBox_68, 'DisitckMpsFdltrg'),
            (self.ui.taurusValueCheckBox_69, 'DisitckMpsPlctxoff'),
            (self.ui.taurusValueCheckBox_70, 'DisitckMpsMps'),
            (self.ui.taurusValueCheckBox_71, 'DisitckMpsDiag')
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
