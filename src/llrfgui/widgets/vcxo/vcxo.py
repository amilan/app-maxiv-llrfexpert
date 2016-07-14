#!/usr/bin/env python

###############################################################################
#     Vcxo is a widget used for the LLRF Expert GUI.
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

"""Vcxo is a widget used for the LLRF Expert GUI."""

from taurus.external.qt import Qt, QtCore, QtGui
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget

__all__ = ['Vcxo']
__author__ = "amilan"
__docformat__ = 'restructuredtext'


@UILoadable(with_ui='ui')
class Vcxo(BaseLLRFWidget):
    """Widget to control the VCXO."""

    def __init__(self, parent=None):
        """Class initialization."""
        config_file = self._get_config_file_name(__file__)
        BaseLLRFWidget.__init__(self, config_file, parent)
        self.loadUi()

    @alert_problems
    def connect_signals(self):
        """Implementation of connect_signals method."""
        QtCore.QObject.connect(self.ui.pushButton_VCXO,
                               QtCore.SIGNAL("clicked()"),
                               self.open_VCXO)

    @alert_problems
    def open_VCXO(self):
        """Open VCXO dialog."""
        # from VCXODialog import VCXODialog
        from llrfgui.widgets.vcxodialog import VCXODialog
        vcxo = VCXODialog(self._device_name)
        # vcxo = VCXODialog(self._device_name_diag)
        vcxo.exec_()
        vcxo = None


def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = 'ws/rf/pynutaq_1'
    panel = Vcxo()
    panel.setModel(model)
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
