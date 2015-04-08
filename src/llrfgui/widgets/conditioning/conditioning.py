#!/usr/bin/env python

###############################################################################
#     Conditioning is a widget used for the LLRF Expert GUI.
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
Conditioning is a widget used for the LLRF Expert GUI.
"""

__all__ = ['Conditioning']

__author__ = "amilan"

__docformat__ = 'restructuredtext'


from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.commons import *
from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget


@UILoadable(with_ui='ui')
class Conditioning(BaseLLRFWidget):

    def __init__(self, parent=None):
        BaseLLRFWidget.__init__(self, parent)
        self.loadUi()

    @alert_problems
    def _set_comboboxes(self):
        self.ui.comboBox_autoConditioningEnable.addValueNames(CB)
        self.ui.comboBox_pulseMode.addValueNames(CB)

    @alert_problems
    def _create_attributes_lists(self):
        self._attributes = [
            (self.ui.lineEdit_dutyCycle, "ConditioningDutyCicleA"),
        ]

        self._attributes_readback = [
            (self.ui.tauValueLabel_autoConditioningEnable, "AutoConditioningEnableA"),
            (self.ui.tauValueLabel_pulseMode, "PulseModeEnableA"),
            (self.ui.tauValueLabel_dutyCycle_2, "ConditioningDutyCicleA"),
            (self.ui.taurusBoolLed_23, "Diag_Vaccum1"),
            (self.ui.taurusBoolLed_24, "Diag_Vaccum2"),
            ]

        self._comboboxes = [
            (self.ui.comboBox_autoConditioningEnable, "AutoConditioningEnableA"),
            (self.ui.comboBox_pulseMode, "PulseModeEnableA"),
        ]

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
