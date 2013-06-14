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

import PyTango
import traceback
import sys,time

from PyQt4 import QtCore, QtGui, Qt, Qwt5
from ui_OVRLoops import Ui_Form

def alert_problems(meth):
    def _alert_problems(self, *args, **kws):
        try:
            return meth(self, *args, **kws)
        except PyTango.DevFailed:
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            traceback.print_exc()
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            exectype, value = sys.exc_info()[:2]
            error_str = 'Error in comunications with device server!'
            QtGui.QMessageBox.critical(self, 'LLRF', error_str)
        except Exception, e:
            print ''
            traceback.print_exc()
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            error_str = 'Unexpected error!'
            QtGui.QMessageBox.critical(self,'LLRF', error_str)
            
    return _alert_problems

class OVRLoops(QtGui.QDialog):
    def __init__(self,model=None, param=None, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        if model is not None:
            self.setModel(model)
        
    def setModel(self,device):
        self.device = PyTango.DeviceProxy(device)
        
        self.attrList = ['OVRAdc1',
                         'OVRAdc2',
                         'OVRAdc3',
                         'OVRAdc4',
                         'OVRAdc5',
                         'OVRAdc6',
                         'OVRAdc7',
                         'OVRAdc8'
                        ]
        self.widgetList = [self.ui.taurusBoolLed,
                           self.ui.taurusBoolLed_2,
                           self.ui.taurusBoolLed_3,
                           self.ui.taurusBoolLed_4, 
                           self.ui.taurusBoolLed_5,
                           self.ui.taurusBoolLed_6,
                           self.ui.taurusBoolLed_7,
                           self.ui.taurusBoolLed_8
                          ]
                          
        for i in range(len(self.widgetList)):
            self.connectAttributes(self.widgetList[i],self.attrList[i])
        
    def connectAttributes(self,widget,attr):
        widget.setModel(attr)


def main():
    
    app = QtGui.QApplication(sys.argv)
    widget = OVRLoops('WS/RF/Lyrtech-01')
    widget.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
