#!/usr/bin/env python

###############################################################################
#     Vcxodialog is a widget used for the LLRF Expert GUI.
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
Vcxodialog is a widget used for the LLRF Expert GUI.
"""

__all__ = ['VCXODialog']

__author__ = "amilan"

__docformat__ = 'restructuredtext'

import PyTango

from PyQt4 import QtCore, QtGui, Qt, Qwt5
from taurus.qt.qtgui.util.ui import UILoadable

from llrfgui.utils.decorators import alert_problems

#from ui_vcxoDialog import Ui_VCXODialog

@UILoadable(with_ui='ui')
class VCXODialog(QtGui.QDialog):
    def __init__(self, param=None, parent=None):
        """Initialize the VCXODialog 
        """
        
        QtGui.QDialog.__init__(self, parent)
        self.loadUi()
        
        #self.ui = Ui_VCXODialog()
        #self.ui.setupUi(self)
        
        self.device = param
        self.dp = PyTango.DeviceProxy(self.device)
        
        self.connectAttributes()
        
        self.fillComboBoxes()
        
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.sendWord)
    
    @alert_problems
    def connectAttributes(self):
        """Method to connect all the attributes
        """
        
        self.ui.taurusValueLineEdit.setModel(self.device + "/MDivider")
        self.ui.taurusValueLineEdit_3.setModel(self.device + "/NDivider")
        self.ui.taurusValueLineEdit_4.setModel(self.device + "/MuxSel")
        self.ui.taurusValueComboBox.setModelName(self.device + "/Mux0Divider")
        self.ui.taurusValueComboBox_2.setModelName(self.device + "/Mux1Divider")
        self.ui.taurusValueComboBox_3.setModelName(self.device + "/Mux2Divider")
        self.ui.taurusValueComboBox_4.setModelName(self.device + "/Mux3Divider")
        self.ui.taurusValueComboBox_5.setModelName(self.device + "/Mux4Divider")
        self.ui.taurusValueComboBox_6.setModelName(self.device + "/CPDirection")
        
        self.ui.taurusLabel.setModel(self.device + "/MDivider")
        self.ui.taurusLabel_3.setModel(self.device + "/NDivider")
        self.ui.taurusLabel_4.setModel(self.device + "/MuxSel")
        self.ui.taurusLabel_5.setModel(self.device + "/Mux0Divider")
        self.ui.taurusLabel_6.setModel(self.device + "/Mux1Divider")
        self.ui.taurusLabel_7.setModel(self.device + "/Mux2Divider")
        self.ui.taurusLabel_8.setModel(self.device + "/Mux3Divider")
        self.ui.taurusLabel_9.setModel(self.device + "/Mux4Divider")
        self.ui.taurusLabel_2.setModel(self.device + "/CPDirection")
        
    @alert_problems
    def sendWord(self):
        """Method to send the word to VCXO
            It must write an 1 in the corresponding attribute,
            and after this, write a 0.
        """
        self.dp['SendWord'] = True
        self.dp['SendWord'] = False
    
    @alert_problems
    def fillComboBoxes(self):
        """Method to fill the comboBoxes
        """
        options = [
            ['1', 1],
            ['2', 2],
            ['4', 4],
            ['8', 8],
            ['16', 16]
        ]

        booleanOptions = [
            ['OFF', 0],
            ['ON', 1]
        ]
        self.ui.taurusValueComboBox.addValueNames(options)
        self.ui.taurusValueComboBox_2.addValueNames(options)
        self.ui.taurusValueComboBox_3.addValueNames(options)
        self.ui.taurusValueComboBox_4.addValueNames(options)
        self.ui.taurusValueComboBox_5.addValueNames(options)
        self.ui.taurusValueComboBox_6.addValueNames(booleanOptions)
 
