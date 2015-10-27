#!/usr/bin/env python

###############################################################################
#     LlrfSimple is a widget used for the LLRF Expert GUI.
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
LlrfSimple is a widget used for the LLRF Expert GUI.
"""

__all__ = ['LlrfSimple']

__author__ = "amilan"

__docformat__ = 'restructuredtext'

from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.commons import *
from llrfgui.utils.decorators import alert_problems
from llrfgui.widgets.basellrfwidget import BaseLLRFWidget


@UILoadable(with_ui='ui')
class LlrfSimple(BaseLLRFWidget):

    def __init__(self, parent=None):
        config_file = self._get_config_file_name(__file__)
        BaseLLRFWidget.__init__(self, config_file, parent)
        self.loadUi()
  #
  #   @alert_problems
  #   def setModel(self, model):
  #       self._device_name = model[0]
  #       self._device_diag_name = model[1]
  #       self._set_comboboxes()
  #       self._create_attributes_lists()
  #       self._connect_all_attributes()
  #
  # #  @alert_problems
  # #  def _set_comboboxes(self):
  # #      pass
  #
  # #  @alert_problems
  # #  def _connect_all_attributes(self):
  # #      for attribute in self._attributes:
  # #          self.connect_attribute(attribute[0], attribute[1])
  #
  # #      for attribute in self._attributes_readback:
  # #          self.connect_attribute(attribute[0], attribute[1])
  #
  # #      for combobox in self._comboboxes:
  # #          self.connect_combobox(combobox[0], combobox[1])
  #
  #   @alert_problems
  #   def connect_attribute(self, widget, attribute):
  #       #attribute = self._device_name + '/' + attribute
  #       widget.setModel(attribute)
  #
  #   @alert_problems
  #   def connect_combobox(self, widget, attribute):
  #       # attribute = self._device_name + '/' + attribute
  #       widget.setModelName(attribute)
  #
  #   @alert_problems
  #   def _create_attributes_lists(self):
  #       self._attributes = [
  #       ]
  #
  #       self._attributes_readback = [
  #           (self.ui.tauValueLabel_Source, self._device_name + "/FPGAClockSourceA"),
  #           (self.ui.tauValueLabel_Locked_2, self._device_name + "/FPGALockedA"),
  #           (self.ui.tauValueLabel_Source_3, self._device_diag_name + "/FPGAClockSourceA"),
  #           (self.ui.tauValueLabel_Locked_4, self._device_diag_name + "/FPGALockedA"),
  #       ]
  #
  #       self._comboboxes = []

def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ['ws/rf/llrf-1', 'ws/rf/llrfdiags_1']
    panel = LlrfSimple()
    panel.setModel(model)
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()