#!/usr/bin/env python

###############################################################################
#     ItckOutDiagSimple is a widget used for the LLRF Expert GUI.
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
ItckOutDiagSimple is a widget used for the LLRF Expert GUI.
"""

__all__ = ['ItckOutDiagSimple']

__author__ = "amilan"

__docformat__ = 'restructuredtext'

import PyTango

from taurus.external.qt import Qt, QtCore
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget


@UILoadable(with_ui='ui')
class ItckOutDiagSimple(BaseLLRFWidget):

    def __init__(self, parent=None):
        config_file = self._get_config_file_name(__file__)
        BaseLLRFWidget.__init__(self, config_file, parent)
        self.loadUi()

    @alert_problems
    def connect_with_devices(self):
        """This method creates the tango device proxys. """
        self._device_proxy = PyTango.DeviceProxy(self._device_name)

    @alert_problems
    def connect_signals(self):
        QtCore.QObject.connect(self.ui.pushButton_resetITCKA,
                               QtCore.SIGNAL("clicked()"), self.resetITCKA)

        QtCore.QObject.connect(self.ui.pushButton_resetITCKB,
                               QtCore.SIGNAL("clicked()"), self.resetITCKB)

        QtCore.QObject.connect(self.ui.pushButton_stopItckA,
                               QtCore.SIGNAL("clicked()"), self.stopItckA)

        QtCore.QObject.connect(self.ui.pushButton_stopItckB,
                               QtCore.SIGNAL("clicked()"), self.stopItckB)

    @alert_problems
    def resetITCKA(self):
        self._device_proxy.reset_itckA()

    @alert_problems
    def resetITCKB(self):
        self._device_proxy.reset_itckB()

    @alert_problems
    def stopItckA(self):
        self._device_proxy.reset_manual_itckA()

    @alert_problems
    def stopItckB(self):
        self._device_proxy.reset_manual_itckB()

def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = 'ws/rf/llrfdiags_1'
    panel = ItckOutDiagSimple()
    panel.setModel(model)
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
