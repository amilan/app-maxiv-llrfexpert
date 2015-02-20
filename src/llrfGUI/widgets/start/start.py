#!/usr/bin/env python

###############################################################################
##     Start is a widget used for the LLRF Expert GUI.
##
##     Copyright (C) 2013  Max IV Laboratory, Lund Sweden
##
##     This program is free software: you can redistribute it and/or modify
##     it under the terms of the GNU General Public License as published by
##     the Free Software Foundation, either version 3 of the License, or
##     (at your option) any later version.
##
##     This program is distributed in the hope that it will be useful,
##     but WITHOUT ANY WARRANTY; without even the implied warranty of
##     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##     GNU General Public License for more details.
##
##     You should have received a copy of the GNU General Public License
##     along with this program.  If not, see [http://www.gnu.org/licenses/].
###############################################################################

__author__ = "amilan"

from start import * 
from widgets.basellrfwidget import BaseLLRFWidget

from taurus.external.qt import Qt, QtCore, QtGui
from taurus.qt.qtgui.util.ui import UILoadable
from taurus.qt.qtgui.display import TaurusStateLed
from utils.tih import *
from utils.decorators import alert_problems

#from PyQt4 import QtCore, QtGui
import PyTango

@UILoadable(with_ui='ui')
class Start(BaseLLRFWidget):

    def __init__(self, parent=None):
        BaseLLRFWidget.__init__(self, parent)
        self.loadUi()
        self.create_state_leds()

    @alert_problems
    def create_state_leds(self):
        """Method for creating an state led in toolbar
        """
        self.ui.label_state1 = QtGui.QLabel()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.label_state1.sizePolicy().hasHeightForWidth())
        self.ui.label_state1.setSizePolicy(sizePolicy)
        self.ui.label_state1.setText("Loops:")
        #self.label_state1.setMinimumSize(QtCore.QSize(175, 20))
        #self.label_state1.setMaximumSize(QtCore.QSize(93, 20))
        #font = QtGui.QFont()
        #font.setPointSize(8)
        #self.label_state1.setFont(font)
       
        self.ui.label_state2 = QtGui.QLabel()
        sizePolicy2 = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ui.label_state2.sizePolicy().hasHeightForWidth())
        self.ui.label_state2.setSizePolicy(sizePolicy2)
        self.ui.label_state2.setText("Diag:")
        #self.label_state2.setMinimumSize(QtCore.QSize(175, 20))
        #self.label_state2.setMaximumSize(QtCore.QSize(93, 20))
        #font = QtGui.QFont()
        #font.setPointSize(8)
        #self.label_state2.setFont(font)
        
        self.ui.lyrtechStatus1 = TaurusStateLed()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.lyrtechStatus1.sizePolicy().hasHeightForWidth())
        
        self.ui.lyrtechStatus2 = TaurusStateLed()
        sizePolicy2 = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ui.lyrtechStatus2.sizePolicy().hasHeightForWidth())

        self.ui.gridLayout.addWidget(self.ui.label_state1, 0, 2, 1, 1)
        self.ui.gridLayout.addWidget(self.ui.lyrtechStatus1, 0, 3, 1, 1)
        self.ui.gridLayout.addWidget(self.ui.label_state2, 0, 4, 1, 1)
        self.ui.gridLayout.addWidget(self.ui.lyrtechStatus2, 0, 5, 1, 1)

    @alert_problems
    def setModel(self, model):
        self._device_name = model[0]
        self._device_diag_name = model[1]
        self._set_comboboxes()
        self._create_attributes_lists()
        self._connect_all_attributes()
        self.connect_with_devices()
        self.connect_signals()

    @alert_problems
    def connect_with_devices(self):
        """This method creates the tango device proxys. """
        self._device_proxy = PyTango.DeviceProxy(self._device_name)
        self._device_diag_proxy = PyTango.DeviceProxy(self._device_diag_name)

    @alert_problems
    def connect_signals(self):
        QtCore.QObject.connect(self.ui.pushButton,
                               QtCore.SIGNAL("clicked()"),
                               self.start_dev)
        QtCore.QObject.connect(self.ui.pushButton,
                               QtCore.SIGNAL("clicked()"),
                               self.stop_dev)

    @alert_problems
    def start_dev(self):
        """Methos to start running the lyrtech DS
        """
        self._device_proxy.start()
        self._device_diag_proxy.start()
    
    @alert_problems
    def stop_dev(self):
        """Method to stop running the lyrtech DS
        """
        self._device_proxy.stop()
        self._device_diag_proxy.stop()

   # @alert_problems
   # def _set_comboboxes(self):
   #     pass

   # @alert_problems
   # def _connect_all_attributes(self):
   #     for attribute in self._attributes:
   #         self.connect_attribute(attribute[0], attribute[1])

   #     for attribute in self._attributes_readback:
   #         self.connect_attribute(attribute[0], attribute[1])

   #     for combobox in self._comboboxes:
   #         self.connect_combobox(combobox[0], combobox[1])

    @alert_problems
    def connect_attribute(self, widget, attribute):
        #attribute = self._device_name + '/' + attribute
        widget.setModel(attribute)

    @alert_problems
    def connect_combobox(self, widget, attribute):
        #attribute = self._device_name + '/' + attribute
        widget.setModelName(attribute)

    @alert_problems
    def _create_attributes_lists(self):
        self._attributes = []

        self._attributes_readback = [
            (self.ui.lyrtechStatus1, self._device_name + "/state"),
            (self.ui.lyrtechStatus2, self._device_diag_name + "/state"),
        ]

        self._comboboxes = []

def main():
    from taurus.qt.qtgui.application import TaurusApplication

    app = TaurusApplication()
    model = ''
    panel = Start()
    panel.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
