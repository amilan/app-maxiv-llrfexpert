#!/usr/bin/env python

###############################################################################
#     Ramping is a widget used for the LLRF Expert GUI.
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

"""Ramping is a widget used for the LLRF Expert GUI."""

import PyTango

from taurus.external.qt import Qt, QtCore
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget

__all__ = ['Ramping']
__author__ = "amilan"
__docformat__ = 'restructuredtext'


@UILoadable(with_ui='ui')
class Ramping(BaseLLRFWidget):
    """Widget to control the ramping of the LLRF."""

    def __init__(self, parent=None):
        """Class initialization."""
        config_file = self._get_config_file_name(__file__)
        BaseLLRFWidget.__init__(self, config_file, parent)
        self.loadUi()

    @alert_problems
    def connect_with_devices(self):
        """Create the tango device proxys."""
        self._device_proxy = PyTango.DeviceProxy(self._device_name)

    @alert_problems
    def connect_signals(self):
        """Implementation of the connect_signals method."""
        QtCore.QObject.connect(self.ui.pushButton_rampingA,
                               QtCore.SIGNAL("clicked()"),
                               self.reset_ramping_up_A)
        QtCore.QObject.connect(self.ui.pushButton_rampingA_2,
                               QtCore.SIGNAL("clicked()"),
                               self.reset_ramping_down_A)
        QtCore.QObject.connect(self.ui.pushButton_writeSlopesA,
                               QtCore.SIGNAL("clicked()"),
                               self.write_slopes_A)

        QtCore.QObject.connect(self.ui.pushButton_rampingB,
                               QtCore.SIGNAL("clicked()"),
                               self.reset_ramping_up_B)
        QtCore.QObject.connect(self.ui.pushButton_rampingB_3,
                               QtCore.SIGNAL("clicked()"),
                               self.reset_ramping_down_B)
        QtCore.QObject.connect(self.ui.pushButton_writeSlopesB,
                               QtCore.SIGNAL("clicked()"),
                               self.write_slopes_B)

    @alert_problems
    def reset_ramping_up_A(self):
        """Ramping up reset for cavity A."""
        self._device_proxy['RampUpA'] = True
        self._device_proxy['RampUpA'] = False

    @alert_problems
    def reset_ramping_down_A(self):
        """Ramping down reset for cavity B."""
        self._device_proxy['RampDownA'] = True
        self._device_proxy['RampDownA'] = False

    @alert_problems
    def write_slopes_A(self):
        """Write slopes for cavity A."""
        self._device_proxy.WriteSlopesA()

    @alert_problems
    def reset_ramping_up_B(self):
        """Ramping up reset for cavity B."""
        self._device_proxy['RampUpB'] = True
        self._device_proxy['RampUpB'] = False

    @alert_problems
    def reset_ramping_down_B(self):
        """"Ramping down reset for caviyt B."""
        self._device_proxy['RampDownB'] = True
        self._device_proxy['RampDownB'] = False

    @alert_problems
    def write_slopes_B(self):
        """Write slopes for cavity B."""
        self._device_proxy.WriteSlopesB()


def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = 'ws/rf/pynutaq_1'
    panel = Ramping()
    panel.setModel(model)
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
