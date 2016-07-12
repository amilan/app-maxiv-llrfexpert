#!/usr/bin/env python

###############################################################################
#     ItckInDiags is a widget used for the LLRF Expert GUI.
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

"""ItckInDiags is a widget used for the LLRF Expert GUI."""

from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.widgets.basellrfwidget import BaseLLRFWidget

__all__ = ['ItckInDiags']
__author__ = "amilan"
__docformat__ = 'restructuredtext'


@UILoadable(with_ui='ui')
class ItckInDiags(BaseLLRFWidget):
    """Widget to setup interlocks parameters for the Diagnostics devices."""

    def __init__(self, parent=None):
        """Class initialization."""
        config_file = self._get_config_file_name(__file__)
        BaseLLRFWidget.__init__(self, config_file, parent)
        self.loadUi()


def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = 'ws/rf/pynutaqdiags_1'
    panel = ItckInDiags()
    panel.setModel(model)
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
