#!/usr/bin/env python

#############################################################################
##
## Copyright (C) 2004-2005 Trolltech AS. All rights reserved.
##
## This file is part of the example classes of the Qt Toolkit.
##
## This file may be used under the terms of the GNU General Public
## License version 2.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
## http://www.trolltech.com/products/qt/opensource.html
##
## If you are unsure which license is appropriate for your use, please
## review the following information:
## http://www.trolltech.com/products/qt/licensing.html or contact the
## sales department at sales@trolltech.com.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
#############################################################################

from PyQt4 import QtCore, QtGui
import traceback

import PyTango

from llrfGUI.oldVersion.ui_vcxoDialog import Ui_VCXODialog


def alert_problems(meth):
    def _alert_problems(self, *args, **kws):
        try:
            return meth(self, *args, **kws)
        except PyTango.DevFailed:
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            traceback.print_exc()
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            exctype, value = sys.exc_info()[:2]
            error_str = 'Error in the communication with a device server!'
            QtGui.QMessageBox.critical(self, 'VCXO', error_str)
        except Exception, e:
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            traceback.print_exc()
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            error_str = 'Unexpected error !'
            QtGui.QMessageBox.critical(self, 'VCXO', error_str)
    return _alert_problems

class VCXODialog(QtGui.QDialog):
    def __init__(self, param=None, parent=None):
        """Initialize the VCXODialog 
        """
        
        QtGui.QDialog.__init__(self, parent)
        
        self.ui = Ui_VCXODialog()
        self.ui.setupUi(self)
        
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
                    ['1',1],
                    ['2',2],
                    ['4',4],
                    ['8',8],
                    ['16',16]
            ]
            
        booleanOptions = [
                    ['OFF',0],
                    ['ON',1]
            ]
        self.ui.taurusValueComboBox.addValueNames(options)
        self.ui.taurusValueComboBox_2.addValueNames(options)
        self.ui.taurusValueComboBox_3.addValueNames(options)
        self.ui.taurusValueComboBox_4.addValueNames(options)
        self.ui.taurusValueComboBox_5.addValueNames(options)
        self.ui.taurusValueComboBox_6.addValueNames(booleanOptions)
        
        
        
        