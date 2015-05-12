#!/usr/bin/env python

###############################################################################
#     Base llrf Widget is a base class that will be used by all the LLRF
#     widgets.
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
Base class widget to be inherit by all the llrf widgets.
"""

__all__ = ['BaseLLRFWidget']

__author__ = "amilan"

__docformat__ = 'restructuredtext'


from taurus.external.qt import Qt
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.commons import *
from llrfgui.utils.decorators import alert_problems


#@UILoadable(with_ui='ui')
class BaseLLRFWidget(Qt.QWidget):
    """
    Base class to be used by any other LLRF widget.
    It provides the basic interface.
    """
    def __init__(self, parent=None):
        Qt.QWidget.__init__(self, parent)
        #self.loadUi()

    @alert_problems
    def setModel(self, model):
        '''
            Set the model of the widget. This method could be overwritten
            if needed due to a different model (i.e. widgets with a list of
            devices as model)

            :param str model: Model to be set.
        '''
        self._device_name = model
        self._set_comboboxes()
        self._create_attributes_lists()
        self._connect_all_attributes()
        self.connect_with_devices()
        self.connect_signals()

    @alert_problems
    def connect_with_devices(self):
        '''This method creates the tango device proxys. 
            To be overwritten if needed.
        '''
        pass
        #self._device_proxy = PyTango.DeviceProxy(self._device_name)

    @alert_problems
    def connect_signals(self):
        '''
            Method to connect QT signals with methods. By default is
            void, and it should be implemented by the widget itself.
        '''
        pass

    @alert_problems
    def _set_comboboxes(self):
        '''
            Method to set comboboxes models. By default is
            void, and it should be implemented by the widget itself.
        '''
        pass

    @alert_problems
    def _connect_all_attributes(self):
        '''
            Private method in charge of connect a list of tango attributes with
            their correspondent widget.
        '''
        for attribute in self._attributes:
            self.connect_attribute(attribute[0], attribute[1])

        for attribute in self._attributes_readback:
            self.connect_attribute(attribute[0], attribute[1])

        for combobox in self._comboboxes:
            self.connect_combobox(combobox[0], combobox[1])

    @alert_problems
    def connect_attribute(self, widget, attribute):
        '''
            Method to connect a single tango attribute with a widget.
        '''
        attribute = self._device_name + '/' + attribute
        widget.setModel(attribute)

    @alert_problems
    def connect_combobox(self, widget, attribute):
        '''
            Method to connect a single combobox with its tango attribute
        '''
        attribute = self._device_name + '/' + attribute
        widget.setModelName(attribute)

    @alert_problems
    def _create_attributes_lists(self):
        '''
            Create empty lists for the tango attributes that will be connected
            to the internal widgets.
        '''
        self._attributes = []

        self._attributes_readback = []

        self._comboboxes = []

def main():
    import sys
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = BaseLLRFWidget()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
