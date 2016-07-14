#!/usr/bin/env python

###############################################################################
#     Start is a widget used for the LLRF Expert GUI.
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

"""Start is a widget used for the LLRF Expert GUI."""

import PyTango

from taurus.external.qt import Qt, QtCore, QtGui
from taurus.qt.qtgui.util.ui import UILoadable
from taurus.qt.qtgui.display import TaurusStateLed

# from llrfgui.utils.commons import *
from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget

__all__ = ['Start']
__author__ = "amilan"
__docformat__ = 'restructuredtext'

# from PyQt4 import QtCore, QtGui


@UILoadable(with_ui='ui')
class Start(BaseLLRFWidget):
    """Widget to start the devices."""

    def __init__(self, parent=None):
        """Class initialization."""
        config_file = self._get_config_file_name(__file__)
        BaseLLRFWidget.__init__(self, config_file, parent)
        self.loadUi()
        self.create_state_leds()

    @alert_problems
    def create_state_leds(self):
        """Method for creating an state led in toolbar."""
        self.ui.label_state1 = QtGui.QLabel()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
                                       QtGui.QSizePolicy.Fixed
                                       )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                        self.ui.label_state1.sizePolicy().hasHeightForWidth()
                        )
        self.ui.label_state1.setSizePolicy(sizePolicy)
        self.ui.label_state1.setText("Loops:")
        # self.label_state1.setMinimumSize(QtCore.QSize(175, 20))
        # self.label_state1.setMaximumSize(QtCore.QSize(93, 20))
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # self.label_state1.setFont(font)

        self.ui.label_state2 = QtGui.QLabel()
        sizePolicy2 = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
                                        QtGui.QSizePolicy.Fixed
                                        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
                        self.ui.label_state2.sizePolicy().hasHeightForWidth()
                        )
        self.ui.label_state2.setSizePolicy(sizePolicy2)
        self.ui.label_state2.setText("Diag:")
        # self.label_state2.setMinimumSize(QtCore.QSize(175, 20))
        # self.label_state2.setMaximumSize(QtCore.QSize(93, 20))
        # font = QtGui.QFont()
        # font.setPointSize(8)
        # self.label_state2.setFont(font)

        self.ui.lyrtechStatus1 = TaurusStateLed()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
                                       QtGui.QSizePolicy.Fixed
                                       )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
                        self.ui.lyrtechStatus1.sizePolicy().hasHeightForWidth()
                        )

        self.ui.lyrtechStatus2 = TaurusStateLed()
        sizePolicy2 = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,
                                        QtGui.QSizePolicy.Fixed
                                        )
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
                        self.ui.lyrtechStatus2.sizePolicy().hasHeightForWidth()
                        )

        self.ui.gridLayout.addWidget(self.ui.label_state1, 0, 2, 1, 1)
        self.ui.gridLayout.addWidget(self.ui.lyrtechStatus1, 0, 3, 1, 1)
        self.ui.gridLayout.addWidget(self.ui.label_state2, 0, 4, 1, 1)
        self.ui.gridLayout.addWidget(self.ui.lyrtechStatus2, 0, 5, 1, 1)

    @alert_problems
    def connect_with_devices(self):
        """Create tango device proxys."""
        self._device_proxy = PyTango.DeviceProxy(self._device_name)
        self._device_diag_proxy = PyTango.DeviceProxy(self._device_diag)

    @alert_problems
    def connect_signals(self):
        """Implementation of the connect_signals method."""
        QtCore.QObject.connect(self.ui.pushButton,
                               QtCore.SIGNAL("clicked()"),
                               self.start_dev)
        QtCore.QObject.connect(self.ui.pushButton_2,
                               QtCore.SIGNAL("clicked()"),
                               self.stop_dev)

    @alert_problems
    def start_dev(self):
        """Start running the device servers."""
        # self._device_proxy.start()
        # self._device_diag_proxy.start()
        self._device_diag_proxy.init_hardware()
        self._device_proxy.init_hardware()

    @alert_problems
    def stop_dev(self):
        """Method to stop running the lyrtech DS."""
        self._device_proxy.stop()
        self._device_diag_proxy.stop()


def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ['ws/rf/pynutaq_1', 'ws/rf/pynutaqdiags_1']
    panel = Start()
    panel.setModel(model)
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
