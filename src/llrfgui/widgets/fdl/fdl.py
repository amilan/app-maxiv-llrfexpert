#!/usr/bin/env python

###############################################################################
#     FDL is a widget used for the LLRF Expert GUI.
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

"""FDL is a widget used for the LLRF Expert GUI."""

# from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable

# from llrfgui.utils.commons import *
# from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget

__all__ = ['Fdl']
__author__ = "amilan"
__docformat__ = 'restructuredtext'


@UILoadable(with_ui='_ui')
class Fdl(BaseLLRFWidget):
    """Widget to control the Fast Data Logger."""

    def __init__(self, parent=None):
        """Class initialization."""
        config_file = self._get_config_file_name(__file__)
        BaseLLRFWidget.__init__(self, config_file, parent)
        self.loadUi()

    # @alert_problems
    # def setModel(self, model):
    #     self._device_name = model
    #     self._set_comboboxes()
    #     self._create_attributes_lists()
    #     self._connect_all_attributes()

    # @alert_problems
    # def _set_comboboxes(self):
    #     pass

    # @alert_problems
    # def _connect_all_attributes(self):
    #     for attribute in self._attributes:
    #         self.connect_attribute(attribute[0], attribute[1])

    #     for combobox in self._comboboxes:
    #         self.connect_combobox(combobox[0], combobox[1])

    # @alert_problems
    # def connect_attribute(self, widget, attribute):
    #     widget.setModel(attribute)

    # @alert_problems
    # def connect_combobox(self, widget, attribute):
    #     widget.setModelName(attribute)

    # @alert_problems
    # def _create_attributes_lists(self):
    #     self._attributes = [
    #                         ]

    #     self._comboboxes = [
    #                         ]


def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ['ws/rf/pynutaq_1', 'ws/rf/pynutaqdiags_1']
    panel = Fdl()
    panel.setModel(model)
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
