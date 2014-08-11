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

import sys, time
import PyTango
import traceback

from PyQt4 import QtCore, QtGui, Qt, Qwt5
from ui_llrf import Ui_LLRF
from tih import *
from taurus.qt.qtgui.display import TaurusStateLed

time.sleep(1.0)

#ScrollabeArea
class ScrollableArea:
    def __init__(self, parent, frame):
        self.sa = QtGui.QScrollArea(parent.ui.centralwidget)
        frame.setParent(None)
        self.sa.setWidget(frame)
        self.sa.setFrameStyle(QtGui.QFrame.NoFrame)
        self.sa.setWidgetResizable(True)
        parent.ui.centralwidget.layout().setSpacing(0)
        parent.ui.centralwidget.layout().setMargin(0)
        parent.ui.centralwidget.layout().addWidget(self.sa)
        
        
def alert_problems(meth):
    def _alert_problems(self, *args, **kws):
        try:
            return meth(self, *args, **kws)
        except PyTango.DevFailed:
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            traceback.print_exc()
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            exctype, value = sys.exc_info()[:2]
            #str_aux = 'PyTango.DevFailed in ' + meth.__name__ + ':\n'
            #for error in value:
                #str_aux += '-----------\n'
                #str_aux += "reason\t" + error.reason + "\n"
                #str_aux += "description\t" + error.desc + "\n"
                #str_aux += "origin\t" + err.origin + "\n"
            error_str = 'Error in the communication with a device server!'
            QtGui.QMessageBox.critical(self, 'LLRF', error_str)
        except Exception, e:
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            traceback.print_exc()
            print '~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-'
            #str_aux = 'Exception in ' + meth.__name__ + ':\n'
            #str_aux += str(e)+'\n'
            error_str = 'Unexpected error !'
            QtGui.QMessageBox.critical(self, 'LLRF', error_str)
    return _alert_problems

class llrfGUI(QtGui.QMainWindow):
    def __init__(self, param=None, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        
        ##Get Graphical information ///////////////////////////////////////////
        self.ui = Ui_LLRF()
        self.ui.setupUi(self)
        
        ## Restore settings ///////////////////////////////////////////////////
        settings = QtCore.QSettings()
        self.restoreState(settings.value("MainWindow/State").toByteArray())
        
        ## Create the leds for state //////////////////////////////////////////
        self.createStateLeds()
        
        ## Create custom widgets //////////////////////////////////////////////
        #self.createCustomWidgets()
        
        ## Initialize lists ///////////////////////////////////////////////////
        self.connectedAttributeWidgets = []  ##For saving and restore attribute
                                             ##values. Still not needed. 
        
        ## Fill the values of the comboBoxes //////////////////////////////////
        self.fillComboBoxes()
        
        ## Connect the signals ////////////////////////////////////////////////
        self.connectSignals()
        
        ## Connect attributes /////////////////////////////////////////////////
        if param == None:
            self.sector = 'LAB'
        else:
            self.sector = param
        self.connectAllAtributes()
        
        ## Make the GUI scrollable ////////////////////////////////////////////
        ##Not needed since it's in ui file
        ##self.ui.scroll = ScrollableArea(self, self.ui.frame)
        
        
    @alert_problems
    def connectAllAtributes(self):
        """Depending on the choose sector, it initialize the deviceproxys and 
           it connects all the attributes.
        """
        
        if self.sector == 'LAB':
            self.device = MAIN_DEVICE_LAB
            self.deviceDiag = DIAG_DEVICE_LAB
            #self.devicePLC = PLC_DEVICE_LAB
            self.deviceAlarm = ALARM_DEVICE_LAB
            self.alarmDevice = ALARM_DEVICE_LAB
            
        ## Set the title depending on the sector //////////////////////////////
        self.setWindowTitle('LLRF Expert GUI %s' %(self.sector))
        
        ## Connect with all the devices involved //////////////////////////////
        self.connectWithDevices()
        
        ## Create the lists with attributes to connect ////////////////////////
        self.createLists()
        
        ## Connect all the attributes /////////////////////////////////////////
        for i,attr in enumerate(self._attrList):
            self.connectAttribute(attr[0], attr[1])
            
        for i,attr in enumerate(self._attrDiagList):
            self.connectAttributeDiag(attr[0], attr[1])
            
        for i,attr in enumerate(self._comboList):
            self.connectComboBoxAttributes(attr[0],attr[1])
            
    @alert_problems
    def fillComboBoxes(self):
        """This method will add the values to the comboBoxes
        """
        ## Main Parameters A //////////////////////////////////////////////////
        self.ui.comboBox_voltInc.addValueNames(CV)
        self.ui.comboBox_quad.addValueNames(CQ)
        self.ui.comboBox_lookRef.addValueNames(CB)
        self.ui.comboBox_loopEn.addValueNames(CB)
        self.ui.comboBox_phaseShiftEn.addValueNames(CB)
        self.ui.comboBox_DACsGainEn.addValueNames(CB)
        self.ui.comboBox_GainTetA1En.addValueNames(CB)
        self.ui.comboBox_autoConditioningEnable.addValueNames(CB)
        self.ui.comboBox_loopInputA.addValueNames(CB)
        
        ## Main Parameters B //////////////////////////////////////////////////
        self.ui.comboBox_voltInc_3.addValueNames(CV)
        self.ui.comboBox_quad_2.addValueNames(CQ)
        self.ui.comboBox_lookRef_2.addValueNames(CB)
        self.ui.comboBox_loopEn_2.addValueNames(CB)
        self.ui.comboBox_phaseShiftEn_3.addValueNames(CB)
        self.ui.comboBox_DACsGainEn_2.addValueNames(CB)
        self.ui.comboBox_GainTetB1En.addValueNames(CB)
        self.ui.comboBox_autoConditioningEnable_2.addValueNames(CB)
        self.ui.comboBox_loopInputB.addValueNames(CB)
        
        ## Conditioning A /////////////////////////////////////////////////////
        self.ui.comboBox_pulseMode.addValueNames(CB)
        self.ui.comboBox_voltInc_2.addValueNames(CV)

        ## Conditioning B /////////////////////////////////////////////////////
        self.ui.comboBox_pulseMode_3.addValueNames(CB)
        self.ui.comboBox_voltInc_6.addValueNames(CV)
        
        ## Tuning Loop A //////////////////////////////////////////////////////
        self.ui.comboBox_tuningEn.addValueNames(CB)
        self.ui.comboBox_tuningPosEn.addValueNames(CB)
        self.ui.comboBox_tuningFreq.addValueNames(CC)
        self.ui.comboBox_tuningTrgEnA.addValueNames(CFS)
        self.ui.comboBox_tuningFFEnA.addValueNames(CB)
        self.ui.comboBox_tuningFilterEnA.addValueNames(CB)
        
        ## Tuning Loop B //////////////////////////////////////////////////////
        self.ui.comboBox_tuningEn_2.addValueNames(CB)
        self.ui.comboBox_tuningPosEn_2.addValueNames(CB)
        self.ui.comboBox_tuningFreq_2.addValueNames(CC)
        self.ui.comboBox_tuningTrgEnB.addValueNames(CFS)
        self.ui.comboBox_tuningFFEnB.addValueNames(CB)
        self.ui.comboBox_tuningFilterEnB.addValueNames(CB)
        
        ## Manual Tuning A ////////////////////////////////////////////////////
        self.ui.comboBox_moveUp.addValueNames(CB)
        self.ui.comboBox_movePlg.addValueNames(CB)
        self.ui.comboBox_freqPulses.addValueNames(CC)
        
        ## Manual Tuning A ////////////////////////////////////////////////////
        self.ui.comboBox_moveUp_2.addValueNames(CB)
        self.ui.comboBox_movePlg_2.addValueNames(CB)
        self.ui.comboBox_freqPulses_2.addValueNames(CC)
        
        ## FPGA Clock source //////////////////////////////////////////////////
        self.ui.tauValueComboBox_clockSource.addValueNames(CCS)
        self.ui.tauValueComboBox_clockSource_3.addValueNames(CCS)
        
        ##Interlocks inputs disable comboboxes ///////////////////////////////
        self.ui.comboBox_RvTet1DisA.addValueNames(CEN)
        self.ui.comboBox_RvTet2DisA.addValueNames(CEN)
        self.ui.comboBox_RvCircDisA.addValueNames(CEN)
        self.ui.comboBox_FwLoadDisA.addValueNames(CEN)
        self.ui.comboBox_FwHybLoadDisA.addValueNames(CEN)
        self.ui.comboBox_RvCavDisA.addValueNames(CEN)
        self.ui.comboBox_ManualITCKDisA.addValueNames(CEN)
        self.ui.comboBox_ArcsDisA.addValueNames(CEN)
        self.ui.comboBox_VacuumDisA.addValueNames(CEN)
        self.ui.comboBox_ExtDisA.addValueNames(CEN)
        self.ui.comboBox_ExtITCKDisB_2.addValueNames(CEN)
        self.ui.comboBox_ExtITCKDisB_3.addValueNames(CEN)
        
        self.ui.comboBox_RvTet1DisB.addValueNames(CEN)
        self.ui.comboBox_RvTet2DisB.addValueNames(CEN)
        self.ui.comboBox_RvCircDisB.addValueNames(CEN)
        self.ui.comboBox_FwLoadDisB.addValueNames(CEN)
        self.ui.comboBox_FwHybLoadDisB.addValueNames(CEN)
        self.ui.comboBox_RvCavDisB.addValueNames(CEN)
        self.ui.comboBox_ManualITCKDisB.addValueNames(CEN)
        self.ui.comboBox_ArcsDisB.addValueNames(CEN)
        self.ui.comboBox_VacuumDisB.addValueNames(CEN)
        self.ui.comboBox_ExtITCKDisB.addValueNames(CEN)
        self.ui.comboBox_ExtDisA_2.addValueNames(CEN)
        self.ui.comboBox_ExtDisA_3.addValueNames(CEN)
        
        #Interlocks output disable comboboxes//////////////////////////////////
        self.ui.comboBox_DACsOffDisA.addValueNames(CEN)
        self.ui.comboBox_PINSwitchDisA.addValueNames(CEN)
        self.ui.comboBox_triggerFDLLoopsDisA.addValueNames(CEN)
        self.ui.comboBox_triggerFDLDiagDisA.addValueNames(CEN)
        self.ui.comboBox_outputPLCDisA.addValueNames(CEN)
        self.ui.comboBox_outputUpLevelDisA.addValueNames(CEN)
        
        self.ui.comboBox_DACsOffDisB.addValueNames(CEN)
        self.ui.comboBox_PINSwitchDisB.addValueNames(CEN)
        self.ui.comboBox_triggerFDLLoopsDisB.addValueNames(CEN)
        self.ui.comboBox_triggerFDLDiagDisB.addValueNames(CEN)
        self.ui.comboBox_outputPLCDisB.addValueNames(CEN)
        self.ui.comboBox_outputUpLevelDisB.addValueNames(CEN)
        
        #Ramping comboboxes////////////////////////////////////////////////////
        self.ui.comboBox_rampingEnA.addValueNames(CB)
        self.ui.comboBox_rampingEnB.addValueNames(CB)
        
        self.ui.comboBox_phaseIncRate.addValueNames(CPIR)
        self.ui.comboBox_phaseIncRate_2.addValueNames(CPIR)
        
        #Automatic startup/////////////////////////////////////////////////////
        self.ui.comboBox_autoStartUpA.addValueNames(CB)
        self.ui.comboBox_CommandStartA.addValueNames(CCMDSTART)
        self.ui.comboBox_autoStartUpB.addValueNames(CB)
        self.ui.comboBox_CommandStartB.addValueNames(CCMDSTART)
        
        #Landau ///////////////////////////////////////////////////////////////
        self.ui.comboBox_moveUp_3.addValueNames(CB)
        self.ui.comboBox_movePlg_3.addValueNames(CB)
        self.ui.comboBox_tuningEn_3.addValueNames(CB)
        self.ui.comboBox_tuningPosEn_3.addValueNames(CB)
        
        #FDL //////////////////////////////////////////////////////////////////
        self.ui.taurusValueComboBox_chSrA.addValueNames(CFDL)
        self.ui.taurusValueComboBox_chSrDA.addValueNames(CFDLDIAG)
        self.ui.taurusValueComboBox_chSrB.addValueNames(CFDL)
        self.ui.taurusValueComboBox_chSrDB.addValueNames(CFDLDIAG)
        
        
    @alert_problems
    def connectSignals(self):
        QtCore.QObject.connect(self.ui.actionStart, QtCore.SIGNAL("triggered()"), self.startDev)
        QtCore.QObject.connect(self.ui.actionStop, QtCore.SIGNAL("triggered()"), self.stopDev)
        QtCore.QObject.connect(self.ui.actionQuit, QtCore.SIGNAL("triggered()"), self.actionQuit)
        
        QtCore.QObject.connect(self.ui.pushButton_rTU, QtCore.SIGNAL("clicked()"), self.tuningResetA)
        QtCore.QObject.connect(self.ui.pushButton_rTU_2, QtCore.SIGNAL("clicked()"), self.tuningResetB)
        QtCore.QObject.connect(self.ui.pushButton_rTU_3, QtCore.SIGNAL("clicked()"), self.landauReset)
        
        QtCore.QObject.connect(self.ui.pushButton_VCXO, QtCore.SIGNAL("clicked()"), self.openVCXO)
        
        QtCore.QObject.connect(self.ui.pushButton_resetITCKA, QtCore.SIGNAL("clicked()"), self.resetITCKA)
        QtCore.QObject.connect(self.ui.pushButton_resetITCKB, QtCore.SIGNAL("clicked()"), self.resetITCKB)
        
        QtCore.QObject.connect(self.ui.pushButton_SWITCKA, QtCore.SIGNAL("clicked()"), self.resetManualITCKA)
        QtCore.QObject.connect(self.ui.pushButton_SWITCKB, QtCore.SIGNAL("clicked()"), self.resetManualITCKB)
        
        QtCore.QObject.connect(self.ui.pushButton_rampingA, QtCore.SIGNAL("clicked()"), self.resetRampingUpA)
        QtCore.QObject.connect(self.ui.pushButton_rampingA_2, QtCore.SIGNAL("clicked()"), self.resetRampingDownA)
        QtCore.QObject.connect(self.ui.pushButton_rampingB, QtCore.SIGNAL("clicked()"), self.resetRampingUpB)
        QtCore.QObject.connect(self.ui.pushButton_rampingB_3, QtCore.SIGNAL("clicked()"), self.resetRampingDownB)
        
        QtCore.QObject.connect(self.ui.pushButton_writeSlopesA, QtCore.SIGNAL("clicked()"), self.writeSlopesA)
        QtCore.QObject.connect(self.ui.pushButton_writeSlopesB, QtCore.SIGNAL("clicked()"), self.writeSlopesB)
        
        QtCore.QObject.connect(self.ui.pushButton_OVRLoops, QtCore.SIGNAL("clicked()"), self.openOVRLoops)
        QtCore.QObject.connect(self.ui.pushButton_OVRDiag, QtCore.SIGNAL("clicked()"), self.openOVRDiag)
        
        # Interlocks input disable
        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.enableAllInterlocksA)
        QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL("clicked()"), self.disableAllInterlocksA)
        QtCore.QObject.connect(self.ui.pushButton_5, QtCore.SIGNAL("clicked()"), self.enableAllInterlocksB)
        QtCore.QObject.connect(self.ui.pushButton_6, QtCore.SIGNAL("clicked()"), self.disableAllInterlocksB)

        # PLC buttons
        QtCore.QObject.connect(self.ui.pushButton_startPump, QtCore.SIGNAL("clicked()"), self.startPump)
        QtCore.QObject.connect(self.ui.pushButton_stopPump, QtCore.SIGNAL("clicked()"), self.stopPump)
        QtCore.QObject.connect(self.ui.pushButton_enableHF, QtCore.SIGNAL("clicked()"), self.enableHF)
        QtCore.QObject.connect(self.ui.pushButton_disableHF, QtCore.SIGNAL("clicked()"), self.disableHF)
        QtCore.QObject.connect(self.ui.pushButton_resetAlarm, QtCore.SIGNAL("clicked()"), self.resetAlarm)
        
        # FDL buttons
        QtCore.QObject.connect(self.ui.pushButton_FDLStartLoops, QtCore.SIGNAL("clicked()"), self.fdlStart)
        QtCore.QObject.connect(self.ui.pushButton_FDLStopLoops, QtCore.SIGNAL("clicked()"), self.fdlStop)

        QtCore.QObject.connect(self.ui.pushButton_FDLStartDiag, QtCore.SIGNAL("clicked()"), self.fdlStartDiag)
        QtCore.QObject.connect(self.ui.pushButton_FDLStopDiag, QtCore.SIGNAL("clicked()"), self.fdlStopDiag)
        
        QtCore.QObject.connect(self.ui.pushButton_FDLSWTrgLoops, QtCore.SIGNAL("clicked()"), self.fdlSWTriggerLoops)
        QtCore.QObject.connect(self.ui.pushButton_FDLSWTrgDiag, QtCore.SIGNAL("clicked()"), self.fdlSWTriggerDiag)
        
        QtCore.QObject.connect(self.ui.pushButton_FDLLoopsPath, QtCore.SIGNAL("clicked()"), self.setFDLLoopsPath)
        QtCore.QObject.connect(self.ui.pushButton_FDLDiagPath, QtCore.SIGNAL("clicked()"), self.setFDLDiagPath)
        
    @alert_problems
    def setFDLLoopsPath(self):
        path = QtGui.QFileDialog.getExistingDirectory(self, self.tr("Path to save FDL Data"))
        self.dp['FDLDataFilePath'] = path
        
    @alert_problems
    def setFDLDiagPath(self):
        path = QtGui.QFileDialog.getExistingDirectory(self, self.tr("Path to save FDL Data"))
        self.dpDiag['FDLDataFilePath'] = path
        
    @alert_problems
    def fdlSWTriggerLoops(self):
        self.dp.FDLSWTrigger()
        
    @alert_problems
    def fdlSWTriggerDiag(self):
        self.dpDiag.FDLSWTrigger()
    
    @alert_problems
    def fdlStart(self):
        self.dp['FDLStart'] = 1

    @alert_problems
    def fdlStop(self):
        self.dp['FDLStart'] = 0

    @alert_problems
    def fdlStartDiag(self):
        self.dpDiag['FDLStart'] = 1

    @alert_problems
    def fdlStopDiag(self):
        self.dpDiag['FDLStart'] = 0

    @alert_problems
    def startPump(self):
        #self.dpPLC['TANGO_COM'] = PLC_CMD_START_PUMP
        #self.devicePLC['TANGO_COM'] = PLC_CMD_START_PUMP
        #@TODO: Remove this method for plc and the whole widget
        pass
        
    @alert_problems
    def stopPump(self):
        #self.dpPLC['TANGO_COM'] = PLC_CMD_STOP_PUMP
        #self.devicePLC['TANGO_COM'] = PLC_CMD_STOP_PUMP
        #@TODO: Remove this method for plc and the whole widget
        pass
        
    @alert_problems
    def enableHF(self):
        #self.dpPLC['TANGO_COM'] = PLC_CMD_ENABLE_HF
        #self.devicePLC['TANGO_COM'] = PLC_CMD_ENABLE_HF
        #@TODO: Remove this method for plc and the whole widget
        pass

    @alert_problems
    def disableHF(self):
        #self.dpPLC['TANGO_COM'] = PLC_CMD_DISABLE_HF
        #self.devicePLC['TANGO_COM'] = PLC_CMD_DISABLE_HF
        #@TODO: Remove this method for plc and the whole widget
        pass
    
    @alert_problems
    def resetAlarm(self):
        #self.dpPLC['TANGO_COM'] = PLC_CMD_RESET_ALARM
        #self.devicePLC['TANGO_COM'] = PLC_CMD_RESET_ALARM
        #@TODO: Remove this method for plc and the whole widget
        pass
    
    @alert_problems
    def openVCXO(self):
        from VCXODialog import VCXODialog
        vcxo = VCXODialog(self.device)
        #vcxo = VCXODialog(self.deviceDiag)
        vcxo.exec_()
        vcxo = None
        
    @alert_problems
    def openOVRLoops(self):
        from OVRLoops import OVRLoops
        vcxo = OVRLoops(self.device)
        vcxo.exec_()
        vcxo = None
        
    @alert_problems
    def openOVRDiag(self):
        from OVRDiag import OVRDiag
        vcxo = OVRDiag(self.deviceDiag)
        vcxo.exec_()
        vcxo = None
        
    @alert_problems
    def writeSlopesA(self):
        self.dp.WriteSlopesA()
        
    @alert_problems
    def writeSlopesB(self):
        self.dp.WriteSlopesB()
    
    @alert_problems
    def resetRampingUpA(self):
        self.dp['RampUpA'] = True
        self.dp['RampUpA'] = False
        
    @alert_problems
    def resetRampingDownA(self):
        self.dp['RampDownA'] = True
        self.dp['RampDownA'] = False
        
    @alert_problems
    def resetRampingUpB(self):
        self.dp['RampUpB'] = True
        self.dp['RampUpB'] = False
        
    @alert_problems
    def resetRampingDownB(self):
        self.dp['RampDownB'] = True
        self.dp['RampDownB'] = False
    
    
    @alert_problems
    def tuningResetA(self):
        self.dp['TuningResetA'] = True
        self.dp['TuningResetA'] = False
        
    @alert_problems
    def tuningResetB(self):
        self.dp['TuningResetB'] = True
        self.dp['TuningResetB'] = False
        
    @alert_problems
    def landauReset(self):
        self.dp['LandauTuningReset'] = True
        self.dp['LandauTuningReset'] = False
        
    @alert_problems
    def resetITCKA(self):
        self.dpDiag.resetITCKA()
        
    @alert_problems
    def resetITCKB(self):
        self.dpDiag.resetITCKB()
        
    @alert_problems
    def resetManualITCKA(self):
        self.dpDiag.resetManualITCKA()
        
    @alert_problems
    def resetManualITCKB(self):
        self.dpDiag.resetManualITCKB()
    
    @alert_problems
    def startDev(self):
        """Methos to start running the lyrtech DS
        """
        self.dp.start()
        self.dpDiag.start()
    
    @alert_problems
    def stopDev(self):
        """Method to stop running the lyrtech DS
        """
        self.dp.stop()
        self.dpDiag.stop()
    
    @alert_problems
    def actionQuit(self):
        """Method to close de application
        """
        self.close()
        
    @alert_problems
    def enableAllInterlocksA(self):
        attrs_to_enable = [ "RvTet1DisA",
                            "RvTet2DisA",
                            "RvCircDisA",
                            "FwLoadDisA",
                            "FwHybLoadDisA",
                            "RvCavDisA",
                            "ManualITCKDisA",
                            "ArcsDisA",
                            "VacuumDisA",
                            "ExtITCKDisA",
                            "PlungerEndSwitchUpDisA",
                            "PlungerEndSwitchDownDisA"
                            ]
        for att in attrs_to_enable:
            self.dpDiag[att] = 'Enable'

    @alert_problems
    def disableAllInterlocksA(self):
        attrs_to_disable = [ "RvTet1DisA",
                             "RvTet2DisA",
                             "RvCircDisA",
                             "FwLoadDisA",
                             "FwHybLoadDisA",
                             "RvCavDisA",
                             "ManualITCKDisA",
                             "ArcsDisA",
                             "VacuumDisA",
                             "ExtITCKDisA",
                             "PlungerEndSwitchUpDisA",
                             "PlungerEndSwitchDownDisA"
                            ]
        for att in attrs_to_disable:
            self.dpDiag[att] = 'Disable'

    @alert_problems
    def enableAllInterlocksB(self):
        attrs_to_enable = [ "RvTet1DisB",
                            "RvTet2DisB",
                            "RvCircDisB",
                            "FwLoadDisB",
                            "FwHybLoadDisB",
                            "RvCavDisB",
                            "ManualITCKDisB",
                            "ArcsDisB",
                            "VacuumDisB",
                            "ExtITCKDisB",
                            "PlungerEndSwitchUpDisB",
                            "PlungerEndSwitchDownDisB"
                            ]
        for att in attrs_to_enable:
            self.dpDiag[att] = 'Enable'


    @alert_problems
    def disableAllInterlocksB(self):
        attrs_to_disable = [ "RvTet1DisB",
                             "RvTet2DisB",
                             "RvCircDisB",
                             "FwLoadDisB",
                             "FwHybLoadDisB",
                             "RvCavDisB",
                             "ManualITCKDisB",
                             "ArcsDisB",
                             "VacuumDisB",
                             "ExtITCKDisB",
                             "PlungerEndSwitchUpDisB",
                             "PlungerEndSwitchDownDisB"
                            ]
        for att in attrs_to_disable:
            self.dpDiag[att] = 'Disable'

    @alert_problems
    def closeEvent(self, event):
        """Method for saving settings and ask for close the app.
        """
        settings = QtCore.QSettings()
        settings.setValue("MainWindow/State", QtCore.QVariant(self.saveState()))
        
        reply = QtGui.QMessageBox.question(self, 'llrfGUI', 'Are you sure to quit?', 
                                                  QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, 
                                                  QtGui.QMessageBox.No )
                                                  
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    @alert_problems
    def connectWithDevices(self):
        """This method creates the tango device proxys. """
        
        self.dp = PyTango.DeviceProxy(self.device)
        self.dpDiag = PyTango.DeviceProxy(self.deviceDiag)
    
    @alert_problems
    def connectAttribute(self, widget, attr):
        """This method connects the GUI with the corresponding tango attributes
        """
        widget.setModel(attr)
        self.connectedAttributeWidgets += [widget]
    
    @alert_problems
    def connectComboBoxAttributes(self, widget, attr):
        """This method connects the comboBoxes with the corresponding attribute
        """
        widget.setModelName(attr)
        self.connectedAttributeWidgets += [widget]
    
    @alert_problems
    def connectAttributeDiag(self, widget, attr):
        """This method connects the GUI with the corresponding tango attributes
           used for diagnostics
        """
        widget.setModel(attr)
        
    @alert_problems
    def createStateLeds(self):
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
        
        self.ui.toolBar.addWidget(self.ui.label_state1)
        self.ui.toolBar.addWidget(self.ui.lyrtechStatus1)
        self.ui.toolBar.addWidget(self.ui.label_state2)
        self.ui.toolBar.addWidget(self.ui.lyrtechStatus2)
        
        
    @alert_problems
    def createCustomWidgets(self):
        from alarmwidget import AlarmWidget
        self.alarmWidget = AlarmWidget()
        
        font = QtGui.QFont()
        font.setPointSize(8)
        self.alarmWidget.setFont(font)
        
        layout = QtGui.QVBoxLayout(self.ui.groupBox_alarmHistory)
        layout.addWidget(self.alarmWidget)
        
    @alert_problems
    def createLists(self):
        """This method will create the needed lists with the info for setting 
            models
        """
        ## Readable attributes ////////////////////////////////////////////////
        self._attrDiagList = [
                
                (self.ui.lyrtechStatus1, self.device + "/state"),
                (self.ui.lyrtechStatus2, self.deviceDiag + "/state"),
                
                (self.ui.tauValueLabel_cavVolt_2, self.device + "/AmpRefInA"),
                (self.ui.tauValueLabel_cavPhase_2, self.device + "/PhaseRefInA"),
                
                (self.ui.tauValueLabel_ampRefMinA, self.device + "/AmpRefMinA"),
                (self.ui.tauValueLabel_phaseRefMinA, self.device + "/PhaseRefMinA"),
                
                (self.ui.tauValueLabel_voltInc, self.device + "/VoltageRateIncreaseA"),
                (self.ui.tauValueLabel_PILimit_2, self.device + "/PILimitA"),
                (self.ui.tauValueLabel_ki_2, self.device + "/KiA"),
                (self.ui.tauValueLabel_kp_2, self.device + "/KpA"),
                (self.ui.tauValueLabel_quad, self.device + "/QuadrantSelectionA"),
                (self.ui.tauValueLabel_lookRef, self.device + "/LookRefA"),
                (self.ui.tauValueLabel_lookEn, self.device + "/LoopEnableA"),
                (self.ui.tauValueLabel_phaseShiftEn, self.device + "/ADCsPhaseShiftEnableA"),
                (self.ui.tauValueLabel_phaseShift_2, self.device + "/PhaseShiftCavA"),
                (self.ui.tauValueLabel_phaseShift_4, self.device + "/PhaseShiftDACA1"),
                (self.ui.tauValueLabel_phaseShift_6, self.device + "/PhaseShiftDACA2"),
                (self.ui.tauValueLabel_DACsGainEn, self.device + "/DACsPhaseShiftEnableA"),
                (self.ui.tauValueLabel_Tetrode1AEn, self.device + "/GainTetrodeEnableA"),
                (self.ui.tauValueLabel_Tetrode1A, self.device + "/GainTetrodeA1"),
                (self.ui.tauValueLabel_Tetrode2A, self.device + "/GainTetrodeA2"),
                (self.ui.tauValueLabel_loopInputA, self.device + "/LoopInputA"),
                
                (self.ui.tauValueLabel_cavVolt_3, self.device + "/AmpRefInB"),
                (self.ui.tauValueLabel_cavPhase_3, self.device + "/PhaseRefInB"),
                
                (self.ui.tauValueLabel_ampRefMinB, self.device + "/AmpRefMinB"),
                (self.ui.tauValueLabel_phaseRefMinB, self.device + "/PhaseRefMinB"),
                
                (self.ui.tauValueLabel_voltInc_3, self.device + "/VoltageRateIncreaseB"),
                (self.ui.tauValueLabel_PILimit_3, self.device + "/PILimitB"),
                (self.ui.tauValueLabel_ki_3, self.device + "/KiB"),
                (self.ui.tauValueLabel_kp_3, self.device + "/KpB"),
                (self.ui.tauValueLabel_quad_2, self.device + "/QuadrantSelectionB"),
                (self.ui.tauValueLabel_lookRef_2, self.device + "/LookRefB"),
                (self.ui.tauValueLabel_lookEn_2, self.device + "/LoopEnableB"),
                (self.ui.tauValueLabel_phaseShiftEn_3, self.device + "/ADCsPhaseShiftEnableB"),
                (self.ui.tauValueLabel_phaseShift_3, self.device + "/PhaseShiftCavB"),
                (self.ui.tauValueLabel_phaseShift_5, self.device + "/PhaseShiftDACB1"),
                (self.ui.tauValueLabel_phaseShift_7, self.device + "/PhaseShiftDACB2"),
                (self.ui.tauValueLabel_DACsGainEn_2, self.device + "/DACsPhaseShiftEnableB"),
                (self.ui.tauValueLabel_Tetrode1BEn, self.device + "/GainTetrodeEnableB"),
                (self.ui.tauValueLabel_Tetrode1B, self.device + "/GainTetrodeB1"),
                (self.ui.tauValueLabel_Tetrode2B, self.device + "/GainTetrodeB2"),
                (self.ui.tauValueLabel_loopInputB, self.device + "/LoopInputB"),
                
                (self.ui.tauValueLabel_autoConditioningEnable, self.device + "/AutoConditioningEnableA"),
                (self.ui.tauValueLabel_pulseMode, self.device + "/PulseModeEnableA"),
                (self.ui.tauValueLabel_dutyCycle_2, self.device + "/ConditioningDutyCicleA"),
                (self.ui.tauValueLabel_cavVolt_4, self.device + "/CavityVoltA"),
                (self.ui.tauValueLabel_voltInc_2, self.device + "/VoltageRateIncreaseB"),
                
                (self.ui.tauValueLabel_autoConditioningEnable_2, self.device + "/AutoConditioningEnableB"),
                (self.ui.tauValueLabel_pulseMode_3, self.device + "/PulseModeEnableB"),
                (self.ui.tauValueLabel_dutyCycle_4, self.device + "/ConditioningDutyCicleB"),
                (self.ui.tauValueLabel_cavVolt_7, self.device + "/CavityVoltB"),
                (self.ui.tauValueLabel_voltInc_6, self.device + "/VoltageRateIncreaseB"),
                
                (self.ui.tauValueLabel_numberPulses_2, self.device + "/NumStepsA"),
                (self.ui.tauValueLabel_moveUp, self.device + "/MoveUpA"),
                (self.ui.tauValueLabel_movePlg1, self.device + "/MoveA"),
                (self.ui.tauValueLabel_freqPulses, self.device + "/PulsesFrequencyA"),
                
                (self.ui.tauValueLabel_numberPulses_3, self.device + "/NumStepsB"),
                (self.ui.tauValueLabel_moveUp_2, self.device + "/MoveUpB"),
                (self.ui.tauValueLabel_movePlg1_2, self.device + "/MoveB"),
                (self.ui.tauValueLabel_freqPulses_2, self.device + "/PulsesFrequencyB"),
                
                (self.ui.tauValueLabel_Source, self.device + "/FPGAClockSource"),
                (self.ui.tauValueLabel_Locked_2, self.device + "/FPGALocked"),
                
                (self.ui.tauValueLabel_Power, self.device + "/VCXOPowered"),
                (self.ui.tauValueLabel_Ref, self.device + "/VCXORef"),
                (self.ui.tauValueLabel_Locked, self.device + "/VCXOLocked"),
                
                (self.ui.tauValueLabel_IcavRef, self.device + "/IRefDiagA"),
                (self.ui.tauValueLabel_IcavVolt, self.device + "/ICavA"),
                (self.ui.tauValueLabel_IerrorP, self.device + "/IErrorA"),
                (self.ui.tauValueLabel_IerrorA, self.device + "/IErrorAccumA"),
                (self.ui.tauValueLabel_IcrtlA, self.device + "/IControlA"),
                (self.ui.tauValueLabel_IcrtlAc, self.device + "/IControl1A"),
                (self.ui.tauValueLabel_IcrtlAc2, self.device + "/IControl2A"),
                (self.ui.tauValueLabel_QcavRef, self.device + "/QRefDiagA"),
                (self.ui.tauValueLabel_QcavVolt, self.device + "/QCavA"),
                (self.ui.tauValueLabel_QerrorP, self.device + "/QErrorA"),
                (self.ui.tauValueLabel_QerrorA, self.device + "/QErrorAccumA"),
                (self.ui.tauValueLabel_QctrlA, self.device + "/QControlA"),
                (self.ui.tauValueLabel_QctrlAc, self.device + "/QControl1A"),
                (self.ui.tauValueLabel_QctrlAc2, self.device + "/QControl2A"),
                (self.ui.tauValueLabel_ampCavRef, self.device + "/AmpRefDiagA"),
                (self.ui.tauValueLabel_ampCavVolt, self.device + "/AmpCavA"),
                (self.ui.tauValueLabel_ampErrorP, self.device + "/AmpErrorA"),
                (self.ui.tauValueLabel_ampErrorA, self.device + "/AmpErrorAccumA"),
                (self.ui.tauValueLabel_ampCtrlA, self.device + "/AmpControlA"),
                (self.ui.tauValueLabel_ampCtrlAc, self.device + "/AmpControl1A"),
                (self.ui.tauValueLabel_ampCtrlAc2, self.device + "/AmpControl2A"),
                (self.ui.tauValueLabel_phaseCavRef, self.device + "/PhRefDiagA"),
                (self.ui.tauValueLabel_phaseCavVolt, self.device + "/PhCavA"),
                (self.ui.tauValueLabel_phaseErrorP, self.device + "/PhErrorA"),
                (self.ui.tauValueLabel_phaseErrorA, self.device + "/PhErrorAccumA"),
                (self.ui.tauValueLabel_PhCrtlA, self.device + "/PhControlA"),
                (self.ui.tauValueLabel_phaseCtrlAc, self.device + "/PhControl1A"),
                (self.ui.tauValueLabel_phaseCtrlAc_2, self.device + "/PhControl2A"),
                
                (self.ui.tauValueLabel_IcavRef_2, self.device + "/IRefDiagB"),
                (self.ui.tauValueLabel_IcavVolt_2, self.device + "/ICavB"),
                (self.ui.tauValueLabel_IerrorP_2, self.device + "/IErrorB"),
                (self.ui.tauValueLabel_IerrorA_2, self.device + "/IErrorAccumB"),
                (self.ui.tauValueLabel_IctrlA_2, self.device + "/IControlB"),
                (self.ui.tauValueLabel_IcrtlAc_4, self.device + "/IControl1B"),
                (self.ui.tauValueLabel_IcrtlAc_8, self.device + "/IControl2B"),
                (self.ui.tauValueLabel_QcavRef_2, self.device + "/QRefDiagB"),
                (self.ui.tauValueLabel_QcavVolt_2, self.device + "/QCavB"),
                (self.ui.tauValueLabel_QerrorP_2, self.device + "/QErrorB"),
                (self.ui.tauValueLabel_QerrorA_2, self.device + "/QErrorAccumB"),
                (self.ui.tauValueLabel_QCtrlA_3, self.device + "/QControlB"),
                (self.ui.tauValueLabel_QctrlAc_4, self.device + "/QControl1B"),
                (self.ui.tauValueLabel_QctrlAc_8, self.device + "/QControl2B"),
                (self.ui.tauValueLabel_ampCavRef_2, self.device + "/AmpRefDiagB"),
                (self.ui.tauValueLabel_ampCavVolt_2, self.device + "/AmpCavB"),
                (self.ui.tauValueLabel_ampErrorP_2, self.device + "/AmpErrorB"),
                (self.ui.tauValueLabel_ampErrorA_2, self.device + "/AmpErrorAccumB"),
                (self.ui.tauValueLabel_ampCtrlA_2, self.device + "/AmpControlB"),
                (self.ui.tauValueLabel_ampCtrlAc_4, self.device + "/AmpControl1B"),
                (self.ui.tauValueLabel_ampCtrlAc_8, self.device + "/AmpControl2B"),
                (self.ui.tauValueLabel_phaseCavRef_2, self.device + "/PhRefDiagB"),
                (self.ui.tauValueLabel_phaseCavVolt_2, self.device + "/PhCavB"),
                (self.ui.tauValueLabel_phaseErrorP_2, self.device + "/PhErrorB"),
                (self.ui.tauValueLabel_phaseErrorA_2, self.device + "/PhErrorAccumB"),
                (self.ui.tauValueLabel_phaseCtrlA_5, self.device + "/PhControlB"),
                (self.ui.tauValueLabel_phaseCtrlAc_4, self.device + "/PhControl1B"),
                (self.ui.tauValueLabel_phaseCtrlAc_8, self.device + "/PhControl2B"),
                
                (self.ui.tauValueLabel_rTuningD, self.device + "/AngCavFwA"),
                (self.ui.tauValueLabel_rFwAmp, self.device + "/AngFwA"),
                (self.ui.tauValueLabel_rCavVolt, self.device + "/AngCavLA"),
                (self.ui.tauValueLabel_rPlung1Pos, "tango://srvv0-tangohost-0:10000/m2sr/llrf/cav2/voltage"),
                
                (self.ui.tauValueLabel_rTuningD_2, self.device + "/AngCavFwB"),
                (self.ui.tauValueLabel_rFwAmp_2, self.device + "/AngFwB"),
                (self.ui.tauValueLabel_rCavVolt_2, self.device + "/AngCavLB"),
                (self.ui.tauValueLabel_rPlung1Pos_2, "tango://srvv0-tangohost-0:10000/m2sr/llrf/cav3/voltage"),
                
                (self.ui.tauValueLabel_IFwTet1, self.device + "/IFwTet1A"),
                (self.ui.tauValueLabel_QFwTet1, self.device + "/QFwTet1A"),
                (self.ui.tauValueLabel_ampFwTet1, self.device + "/AmpFwTet1A"),
                (self.ui.tauValueLabel_phaseFwTet1, self.device + "/PhFwTet1A"),
                
                (self.ui.tauValueLabel_IFwTet2, self.device + "/IFwTet2A"),
                (self.ui.tauValueLabel_QFwTet2, self.device + "/QFwTet2A"),
                (self.ui.tauValueLabel_ampFwTet2, self.device + "/AmpFwTet2A"),
                (self.ui.tauValueLabel_phaseFwTet2, self.device + "/PhFwTet2A"),
                
                (self.ui.tauValueLabel_IFwTet1_2, self.device + "/IFwTet1B"),
                (self.ui.tauValueLabel_QFwTet1_2, self.device + "/QFwTet1B"),
                (self.ui.tauValueLabel_ampFwTet1_2, self.device + "/AmpFwTet1B"),
                (self.ui.tauValueLabel_phaseFwTet1_2, self.device + "/PhFwTet1B"),
                
                (self.ui.tauValueLabel_IFwTet2_2, self.device + "/IFwTet2B"),
                (self.ui.tauValueLabel_QFwTet2_2, self.device + "/QFwTet2B"),
                (self.ui.tauValueLabel_ampFwTet2_2, self.device + "/AmpFwTet2B"),
                (self.ui.tauValueLabel_phaseFwTet2_2, self.device + "/PhFwTet2B"),
                
                (self.ui.tauValueLabel_IFwCavVolt, self.device + "/IFwA"),
                (self.ui.tauValueLabel_QFwCavVolt, self.device + "/QFwA"),
                (self.ui.tauValueLabel_ampFwCavVolt, self.device + "/AmpFwA"),
                (self.ui.tauValueLabel_phaseFwCavVolt, self.device + "/PhFwA"),
                
                (self.ui.tauValueLabel_IFwCavVolt_2, self.device + "/IFwB"),
                (self.ui.tauValueLabel_QFwCavVolt_2, self.device + "/QFwB"),
                (self.ui.tauValueLabel_ampFwCavVolt_2, self.device + "/AmpFwB"),
                (self.ui.tauValueLabel_phaseFwCavVolt_2, self.device + "/PhFwB"),
                
                (self.ui.tauValueLabel_filterStage, self.device + "/FilterStagesA"),
                (self.ui.tauValueLabel_samplesAv, self.device + "/NumSamplesAverageA"),
                
                (self.ui.tauValueLabel_filterStage_2, self.device + "/FilterStagesB"),
                (self.ui.tauValueLabel_samplesAv_2, self.device + "/NumSamplesAverageB"),
                
                (self.ui.tauValueLabel_tuningEn, self.device + "/TuningEnableA"),
                (self.ui.tauValueLabel_tuningPosEn, self.device + "/TuningPosEnA"),
                (self.ui.tauValueLabel_tuningFreq, self.device + "/PulsesFrequencyA"),
                (self.ui.tauValueLabel_marginUp, self.device + "/MarginUpA"),
                (self.ui.tauValueLabel_marginLow, self.device + "/MarginLowA"),
                (self.ui.tauValueLabel_forwardMin_2, self.device + "/FwMinA"),
                (self.ui.tauValueLabel_tuningDelayA, self.device + "/TuningDelayA"),
                (self.ui.tauValueLabel_tuningTrgEnA, self.device + "/TuningTriggerEnableA"),
                (self.ui.tauValueLabel_tuningFFEnA, self.device + "/TuningFFA"),
                (self.ui.tauValueLabel_tuningFFStepsA, self.device + "/TuningFFStepsA"),
                (self.ui.tauValueLabel_tuningFilterEnA, self.device + "/TuningFilterEnableA"),
                
                (self.ui.tauValueLabel_tuningEn_2, self.device + "/TuningEnableB"),
                (self.ui.tauValueLabel_tuningPosEn_2, self.device + "/TuningPosEnB"),
                (self.ui.tauValueLabel_tuningFreq_2, self.device + "/PulsesFrequencyB"),
                (self.ui.tauValueLabel_marginUp_2, self.device + "/MarginUpB"),
                (self.ui.tauValueLabel_marginLow_2, self.device + "/MarginLowB"),
                (self.ui.tauValueLabel_forwardMin_3, self.device + "/FwMinB"),
                (self.ui.tauValueLabel_tuningDelayB, self.device + "/TuningDelayB"),
                (self.ui.tauValueLabel_tuningTrgEnB, self.device + "/TuningTriggerEnableB"),
                (self.ui.tauValueLabel_tuningFFEnB, self.device + "/TuningFFB"),
                (self.ui.tauValueLabel_tuningFFStepsB, self.device + "/TuningFFStepsB"),
                (self.ui.tauValueLabel_tuningFilterEnB, self.device + "/TuningFilterEnableB"),
                
                (self.ui.tauValueLabel_tuningOffset, self.device + "/PhaseOffsetA"),
                (self.ui.tauValueLabel_tuningOffset_2, self.device + "/PhaseOffsetB"),
                
                (self.ui.tauValueLabel_IMOA, self.device + "/IMOA"),
                (self.ui.tauValueLabel_QMOA, self.device + "/QMOA"),
                (self.ui.tauValueLabel_AmpMOA, self.device + "/AmpMOA"),
                (self.ui.tauValueLabel_PhMOA, self.device + "/PhMOA"),
                
                (self.ui.tauValueLabel_IMOB, self.device + "/IMOB"),
                (self.ui.tauValueLabel_QMOB, self.device + "/QMOB"),
                (self.ui.tauValueLabel_AmpMOB, self.device + "/AmpMOB"),
                (self.ui.tauValueLabel_PhMOB, self.device + "/PhMOB"),
                
                
                ##from LyrtechDiag ////////////////////////////////////////////
                (self.ui.tauValueLabel_Source_3, self.deviceDiag + "/FPGAClockSource"),
                (self.ui.tauValueLabel_Locked_4, self.deviceDiag + "/FPGALocked"),
                
                (self.ui.tauValueLabel_IRvCavVolt, self.deviceDiag + "/IRvCavA"),
                (self.ui.tauValueLabel_QRvCavVolt, self.deviceDiag+ "/QRvCavA"),
                (self.ui.tauValueLabel_ampRvCavVolt, self.deviceDiag + "/AmpRvCavA"),
                (self.ui.tauValueLabel_phaseRvCavVolt, self.deviceDiag + "/PhRvCavA"),
                
                (self.ui.tauValueLabel_IRvCavVolt_2, self.deviceDiag + "/IRvCavB"),
                (self.ui.tauValueLabel_QRvCavVolt_2, self.deviceDiag+ "/QRvCavB"),
                (self.ui.tauValueLabel_ampRvCavVolt_2, self.deviceDiag + "/AmpRvCavB"),
                (self.ui.tauValueLabel_phaseRvCavVolt_2, self.deviceDiag + "/PhRvCavB"),
                
                (self.ui.tauValueLabel_IRvTet1, self.deviceDiag + "/IRvTet1A"),
                (self.ui.tauValueLabel_QRvTet1, self.deviceDiag+ "/QRvTet1A"),
                (self.ui.tauValueLabel_ampRvTet1, self.deviceDiag + "/AmpRvTet1A"),
                (self.ui.tauValueLabel_phaseRvTet1, self.deviceDiag + "/PhRvTet1A"),
                
                (self.ui.tauValueLabel_IRvTet2, self.deviceDiag + "/IRvTet2A"),
                (self.ui.tauValueLabel_QRvTet2, self.deviceDiag + "/QRvTet2A"),
                (self.ui.tauValueLabel_ampRvTet2, self.deviceDiag + "/AmpRvTet2A"),
                (self.ui.tauValueLabel_phaseRvTet2, self.deviceDiag + "/PhRvTet2A"),
                
                (self.ui.tauValueLabel_IRvTet1_2, self.deviceDiag + "/IRvTet1B"),
                (self.ui.tauValueLabel_QRvTet1_2, self.deviceDiag + "/QRvTet1B"),
                (self.ui.tauValueLabel_ampRvTet1_2, self.deviceDiag + "/AmpRvTet1B"),
                (self.ui.tauValueLabel_phaseRvTet1_2, self.deviceDiag + "/PhRvTet1B"),
                
                (self.ui.tauValueLabel_IRvTet2_2, self.deviceDiag + "/IRvTet2B"),
                (self.ui.tauValueLabel_QRvTet2_2, self.deviceDiag + "/QRvTet2B"),
                (self.ui.tauValueLabel_ampRvTet2_2, self.deviceDiag + "/AmpRvTet2B"),
                (self.ui.tauValueLabel_phaseRvTet2_2, self.deviceDiag + "/PhRvTet2B"),
                
                (self.ui.tauValueLabel_IFwCirc, self.deviceDiag + "/IFwCircA"),
                (self.ui.tauValueLabel_QFwCirc, self.deviceDiag + "/QFwCircA"),
                (self.ui.tauValueLabel_ampFwCirc, self.deviceDiag + "/AmpFwCircA"),
                (self.ui.tauValueLabel_phaseFwCirc, self.deviceDiag + "/PhFwCircA"),
                
                (self.ui.tauValueLabel_IFwCirc_2, self.deviceDiag + "/IFwCircB"),
                (self.ui.tauValueLabel_QFwCirc_2, self.deviceDiag + "/QFwCircB"),
                (self.ui.tauValueLabel_ampFwCirc_2, self.deviceDiag + "/AmpFwCircB"),
                (self.ui.tauValueLabel_phaseFwCirc_2, self.deviceDiag + "/PhFwCircB"),
                
                (self.ui.tauValueLabel_IRvCirc, self.deviceDiag + "/IRvCircA"),
                (self.ui.tauValueLabel_QRvCirc, self.deviceDiag + "/QRvCircA"),
                (self.ui.tauValueLabel_ampRvCirc, self.deviceDiag + "/AmpRvCircA"),
                (self.ui.tauValueLabel_phaseRvCirc, self.deviceDiag + "/PhRvCircA"),
                
                (self.ui.tauValueLabel_IRvCirc_2, self.deviceDiag + "/IRvCircB"),
                (self.ui.tauValueLabel_QRvCirc_2, self.deviceDiag + "/QRvCircB"),
                (self.ui.tauValueLabel_ampRvCirc_2, self.deviceDiag + "/AmpRvCircB"),
                (self.ui.tauValueLabel_phaseRvCirc_2, self.deviceDiag + "/PhRvCircB"),
                
                (self.ui.tauValueLabel_IFwLoad, self.deviceDiag + "/IFwLoadA"),
                (self.ui.tauValueLabel_QFwLoad, self.deviceDiag + "/QFwLoadA"),
                (self.ui.tauValueLabel_ampFwLoad, self.deviceDiag + "/AmpFwLoadA"),
                (self.ui.tauValueLabel_phaseFwLoad, self.deviceDiag + "/PhFwLoadA"),
                
                (self.ui.tauValueLabel_IFwLoad_2, self.deviceDiag + "/IFwLoadB"),
                (self.ui.tauValueLabel_QFwLoad_2, self.deviceDiag + "/QFwLoadB"),
                (self.ui.tauValueLabel_ampFwLoad_2, self.deviceDiag + "/AmpFwLoadB"),
                (self.ui.tauValueLabel_phaseFwLoad_2, self.deviceDiag + "/PhFwLoadB"),

                (self.ui.tauValueLabel_IFwHybLoad, self.deviceDiag + "/IFwHybLoadA"),
                (self.ui.tauValueLabel_QFwHybLoad, self.deviceDiag + "/QFwHybLoadA"),
                (self.ui.tauValueLabel_ampFwHybLoad, self.deviceDiag + "/AmpFwHybLoadA"),
                (self.ui.tauValueLabel_phaseFwHybLoad, self.deviceDiag + "/PhFwHybLoadA"),
                
                (self.ui.tauValueLabel_IFwHybLoad_2, self.deviceDiag + "/IFwHybLoadB"),
                (self.ui.tauValueLabel_QFwHybLoad_2, self.deviceDiag + "/QFwHybLoadB"),
                (self.ui.tauValueLabel_ampFwHybLoad_2, self.deviceDiag + "/AmpFwHybLoadB"),
                (self.ui.tauValueLabel_phaseFwHybLoad_2, self.deviceDiag + "/PhFwHybLoadB"), 
                
                (self.ui.tauValueLabel_IMO, self.deviceDiag + "/IMO"),
                (self.ui.tauValueLabel_QMO, self.deviceDiag + "/QMO"),
                (self.ui.tauValueLabel_ampMO, self.deviceDiag + "/AmpMO"),
                (self.ui.tauValueLabel_phaseMO, self.deviceDiag + "/PhMO"),
                
                (self.ui.tauValueLabel_IMO_2, self.deviceDiag + "/ILandau"),
                (self.ui.tauValueLabel_QMO_2, self.deviceDiag + "/QLandau"),
                (self.ui.tauValueLabel_ampMO_2, self.deviceDiag + "/AmpLandau"),
                (self.ui.tauValueLabel_phaseMO_2, self.deviceDiag + "/PhLandau"),
                
                #Interlocks levels
                (self.ui.tauValueLabel_RvTet1A, self.deviceDiag + "/RvTet1A"),
                (self.ui.tauValueLabel_RvTet2A, self.deviceDiag + "/RvTet2A"),
                (self.ui.tauValueLabel_RvCircA, self.deviceDiag + "/RvCircA"),
                (self.ui.tauValueLabel_FwLoadA, self.deviceDiag + "/FwLoadA"),
                (self.ui.tauValueLabel_FwHybLoadA, self.deviceDiag + "/FwHybLoadA"),
                (self.ui.tauValueLabel_RvCavA, self.deviceDiag + "/RvCavA"),
                
                (self.ui.tauValueLabel_RvTet1B, self.deviceDiag + "/RvTet1B"),
                (self.ui.tauValueLabel_RvTet2B, self.deviceDiag + "/RvTet2B"),
                (self.ui.tauValueLabel_RvCircB, self.deviceDiag + "/RvCircB"),
                (self.ui.tauValueLabel_FwLoadB, self.deviceDiag + "/FwLoadB"),
                (self.ui.tauValueLabel_FwHybLoadB, self.deviceDiag + "/FwHybLoadB"),
                (self.ui.tauValueLabel_RvCavB, self.deviceDiag + "/RvCavB"),
                
                (self.ui.taurusBoolLed_23, self.device + "/Vacuum1A"),
                (self.ui.taurusBoolLed_24, self.device + "/Vacuum2A"),
                (self.ui.taurusBoolLed_25, self.device + "/Vacuum1B"),
                (self.ui.taurusBoolLed_26, self.device + "/Vacuum2B"),
                
                #Automatic Tuning
                (self.ui.taurusBoolLed_31, self.device + "/TuningOnDiagA"),
                (self.ui.taurusBoolLed_32, self.device + "/FreqUpA"),
                (self.ui.taurusBoolLed_34, self.device + "/TuningOnDiagB"),
                (self.ui.taurusBoolLed_33, self.device + "/FreqUpB"),
                
                #Manual Tuning
                (self.ui.taurusBoolLed_27, self.device + "/ManualTuningOnA"),
                (self.ui.taurusBoolLed_28, self.device + "/ManualFreqUpA"),
                (self.ui.taurusBoolLed_30, self.device + "/ManualTuningOnB"),
                (self.ui.taurusBoolLed_29, self.device + "/ManualFreqUpB"),
                
                #OVR
                (self.ui.taurusBoolLed_35, self.alarmDevice + "/ManualTuningOnB"),
                (self.ui.taurusBoolLed_26, self.alarmDevice + "/ManualFreqUpB"),
                
                #Interlock inputs disable
                (self.ui.tauValueLabel_RvTet1DisA, self.deviceDiag + "/RvTet1DisA"),
                (self.ui.tauValueLabel_RvTet2DisA, self.deviceDiag + "/RvTet2DisA"),
                (self.ui.tauValueLabel_RvCircDisA, self.deviceDiag + "/RvCircDisA"),
                (self.ui.tauValueLabel_FwLoadDisA, self.deviceDiag + "/FwLoadDisA"),
                (self.ui.tauValueLabel_FwHybLoadDisA, self.deviceDiag + "/FwHybLoadDisA"),
                (self.ui.tauValueLabel_RvCavDisA, self.deviceDiag + "/RvCavDisA"),
                (self.ui.tauValueLabel_ManualITCKDisA, self.deviceDiag + "/ManualITCKDisA"),
                (self.ui.tauValueLabel_ArcsDisA, self.deviceDiag + "/ArcsDisA"),
                (self.ui.tauValueLabel_VacuumDisA, self.deviceDiag + "/VacuumDisA"),
                (self.ui.tauValueLabel_ExtITCKDisA, self.deviceDiag + "/ExtITCKDisA"),
                (self.ui.tauValueLabel_ExtITCKDisB_2, self.deviceDiag + "/PlungerEndSwitchUpDisA"),
                (self.ui.tauValueLabel_ExtITCKDisB_3, self.deviceDiag + "/PlungerEndSwitchDownDisA"),
                
                (self.ui.tauValueLabel_RvTet1DisB, self.deviceDiag + "/RvTet1DisB"),
                (self.ui.tauValueLabel_RvTet2DisB, self.deviceDiag + "/RvTet2DisB"),
                (self.ui.tauValueLabel_RvCircDisB, self.deviceDiag + "/RvCircDisB"),
                (self.ui.tauValueLabel_FwLoadDisB, self.deviceDiag + "/FwLoadDisB"),
                (self.ui.tauValueLabel_FwHybLoadDisB, self.deviceDiag + "/FwHybLoadDisB"),
                (self.ui.tauValueLabel_RvCavDisB, self.deviceDiag + "/RvCavDisB"),
                (self.ui.tauValueLabel_ManualITCKDisB, self.deviceDiag + "/ManualITCKDisB"),
                (self.ui.tauValueLabel_ArcsDisB, self.deviceDiag + "/ArcsDisB"),
                (self.ui.tauValueLabel_VacuumDisB, self.deviceDiag + "/VacuumDisB"),
                (self.ui.tauValueLabel_ExtITCKDisB, self.deviceDiag + "/ExtITCKDisB"),
                (self.ui.tauValueLabel_ExtITCKDisA_2, self.deviceDiag + "/PlungerEndSwitchUpDisB"),
                (self.ui.tauValueLabel_ExtITCKDisA_3, self.deviceDiag + "/PlungerEndSwitchDownDisB"),
                
                #Interlock outputs disable
                (self.ui.tauValueLabel_DACsOffDisA, self.deviceDiag + "/DACsOffDisA"),
                (self.ui.tauValueLabel_PINSwitchDisA, self.deviceDiag + "/PinSwitchDisA"),
                (self.ui.tauValueLabel_triggerFDLLoopsDisA, self.deviceDiag + "/TriggerFDLDisA"),
                (self.ui.tauValueLabel_triggerFDLDiagDisA, self.deviceDiag + "/TriggerDiagFDLDisA"),
                (self.ui.tauValueLabel_outputPLCDisA, self.deviceDiag + "/OutputPLCDisA"),
                (self.ui.tauValueLabel_outputUpLevelDisA, self.deviceDiag + "/OutputUpperLevelDisA"),
                
                (self.ui.tauValueLabel_DACsOffDisB, self.deviceDiag + "/DACsOffDisB"),
                (self.ui.tauValueLabel_PINSwitchDisB, self.deviceDiag + "/PinSwitchDisB"),
                (self.ui.tauValueLabel_triggerFDLLoopsDisB, self.deviceDiag + "/TriggerFDLDisB"),
                (self.ui.tauValueLabel_triggerFDLDiagDisB, self.deviceDiag + "/TriggerDiagFDLDisB"),
                (self.ui.tauValueLabel_outputPLCDisB, self.deviceDiag + "/OutputPLCDisB"),
                (self.ui.tauValueLabel_outputUpLevelDisB, self.deviceDiag + "/OutputUpperLevelDisB"),
                
                #Interlock inputs diagnostics
                (self.ui.taurusBoolLed, self.deviceDiag + "/RvTet1DiagA"),
                (self.ui.taurusBoolLed_2, self.deviceDiag + "/RvTet2DiagA"),
                (self.ui.taurusBoolLed_3, self.deviceDiag + "/RvCircDiagA"),
                (self.ui.taurusBoolLed_4, self.deviceDiag + "/FwLoadDiagA"),
                (self.ui.taurusBoolLed_5, self.deviceDiag + "/FwHybLoadDiagA"),
                (self.ui.taurusBoolLed_6, self.deviceDiag + "/RvCavDiagA"),
                (self.ui.taurusBoolLed_7, self.deviceDiag + "/ManualITCKDiagA"),
                (self.ui.taurusBoolLed_8, self.deviceDiag + "/ArcsDiagA"),
                (self.ui.taurusBoolLed_9, self.deviceDiag + "/VacuumDiagA"),
                (self.ui.taurusBoolLed_10, self.deviceDiag + "/ExternalITCKDiagA"),
                (self.ui.taurusBoolLed_41, self.deviceDiag + "/PlungerEndSwitchUpDiagA"),
                (self.ui.taurusBoolLed_43, self.deviceDiag + "/PlungerEndSwitchDownDiagA"),
                
                (self.ui.taurusBoolLed_11, self.deviceDiag + "/RvTet1DiagB"),
                (self.ui.taurusBoolLed_12, self.deviceDiag + "/RvTet2DiagB"),
                (self.ui.taurusBoolLed_13, self.deviceDiag + "/RvCircDiagB"),
                (self.ui.taurusBoolLed_14, self.deviceDiag + "/FwLoadDiagB"),
                (self.ui.taurusBoolLed_15, self.deviceDiag + "/FwHybLoadDiagB"),
                (self.ui.taurusBoolLed_16, self.deviceDiag + "/RvCavDiagB"),
                (self.ui.taurusBoolLed_17, self.deviceDiag + "/ManualITCKDiagB"),
                (self.ui.taurusBoolLed_18, self.deviceDiag + "/ArcsDiagB"),
                (self.ui.taurusBoolLed_19, self.deviceDiag + "/VacuumDiagB"),
                (self.ui.taurusBoolLed_20, self.deviceDiag + "/ExternalITCKDiagB"),
                (self.ui.taurusBoolLed_42, self.deviceDiag + "/PlungerEndSwitchUpDiagB"),
                (self.ui.taurusBoolLed_44, self.deviceDiag + "/PlungerEndSwitchDownDiagB"),
                (self.ui.tauValueLabel_itckTimestamp, self.deviceDiag + "/ITCKTimestampA"),
                (self.ui.tauValueLabel_itckTimestamp_2, self.deviceDiag + "/ITCKTimestampB"),
                
                #Interlock outpus diagnostics
                (self.ui.taurusBoolLed_21, self.deviceDiag + "/DACsOffDiagA"),
                (self.ui.taurusBoolLed_22, self.deviceDiag + "/PinSwitchDiagA"),
                (self.ui.taurusBoolLed_45, self.deviceDiag + "/TriggerFDLDiagA"),
                (self.ui.taurusBoolLed_46, self.deviceDiag + "/TriggerDiagFDLDiagA"),
                (self.ui.taurusBoolLed_47, self.deviceDiag + "/OutputPLCDiagA"),
                (self.ui.taurusBoolLed_48, self.deviceDiag + "/OutputUpperLevelDiagA"),
                
                
                (self.ui.taurusBoolLed_49, self.deviceDiag + "/DACsOffDiagB"),
                (self.ui.taurusBoolLed_50, self.deviceDiag + "/PinSwitchDiagB"),
                (self.ui.taurusBoolLed_51, self.deviceDiag + "/TriggerFDLDiagB"),
                (self.ui.taurusBoolLed_52, self.deviceDiag + "/TriggerDiagFDLDiagB"),
                (self.ui.taurusBoolLed_53, self.deviceDiag + "/OutputPLCDiagB"),
                (self.ui.taurusBoolLed_54, self.deviceDiag + "/OutputUpperLevelDiagB"),
                
                #Ramping readings
                (self.ui.tauValueLabel_RampingEnA, self.device + "/RampingEnA"),
                (self.ui.tauValueLabel_timeRampUpA, self.device + "/TimeRampUpA"),
                (self.ui.tauValueLabel_timeRampDownA, self.device + "/TimeRampDownA"),
                (self.ui.tauValueLabel_ampRampInitA, self.device + "/AmpRampInitA"),
                (self.ui.tauValueLabel_ampRampEndA, self.device + "/AmpRampEndA"),
                (self.ui.tauValueLabel_phaseRampInitA, self.device + "/PhaseRampInitA"),
                (self.ui.tauValueLabel_phaseRampEndA, self.device + "/PhaseRampEndA"),
                
                (self.ui.tauValueLabel_IRampInitA, self.device + "/IRampInitA"),
                (self.ui.tauValueLabel_QRampInitA, self.device + "/QRampInitA"),
                (self.ui.tauValueLabel_IRampEndA, self.device + "/IRampEndA"),
                (self.ui.tauValueLabel_QRampEndA, self.device + "/QRampEndA"),
                (self.ui.tauValueLabel_AmpSlopeRampUpA, self.device + "/AmpSlopeRampUpA"),
                (self.ui.tauValueLabel_PhaseSlopeRampUpA, self.device + "/PhaseSlopeRampUpA"),
                (self.ui.tauValueLabel_AmpSlopeRampDownA, self.device + "/AmpSlopeRampDownA"),
                (self.ui.tauValueLabel_PhaseSlopeRampDownA, self.device + "/PhaseSlopeRampDownA"),
                
                (self.ui.tauValueLabel_RampingEnB, self.device + "/RampingEnB"),
                (self.ui.tauValueLabel_timeRampUpB, self.device + "/TimeRampUpB"),
                (self.ui.tauValueLabel_timeRampDownB, self.device + "/TimeRampDownB"),
                (self.ui.tauValueLabel_ampRampInitB, self.device + "/AmpRampInitB"),
                (self.ui.tauValueLabel_ampRampEndB, self.device + "/AmpRampEndB"),
                (self.ui.tauValueLabel_phaseRampInitB, self.device + "/PhaseRampInitB"),
                (self.ui.tauValueLabel_phaseRampEndB, self.device + "/PhaseRampEndB"),
                
                (self.ui.tauValueLabel_IRampInitB, self.device + "/IRampInitB"),
                (self.ui.tauValueLabel_QRampInitB, self.device + "/QRampInitB"),
                (self.ui.tauValueLabel_IRampEndB, self.device + "/IRampEndB"),
                (self.ui.tauValueLabel_QRampEndB, self.device + "/QRampEndB"),
                (self.ui.tauValueLabel_AmpSlopeRampUpB, self.device + "/AmpSlopeRampUpB"),
                (self.ui.tauValueLabel_PhaseSlopeRampUpB, self.device + "/PhaseSlopeRampUpB"),
                (self.ui.tauValueLabel_AmpSlopeRampDownB, self.device + "/AmpSlopeRampDownB"),
                (self.ui.tauValueLabel_PhaseSlopeRampDownB, self.device + "/PhaseSlopeRampDownB"),
                
                (self.ui.tauValueLabel_phaseIncRate, self.device + "/PhaseIncreaseRateA"),
                (self.ui.tauValueLabel_phaseIncRate_2, self.device + "/PhaseIncreaseRateB"),
                
                #Automatic startup/////////////////////////////////////////////
                (self.ui.tauValueLabel_autoStartUpA, self.device + "/AutoStartUpEnA"),
                (self.ui.tauValueLabel_CommandStartA, self.device + "/CommandStartA"),
                
                (self.ui.tauValueLabel_autoStartUpB, self.device + "/AutoStartUpEnB"),
                (self.ui.tauValueLabel_CommandStartB, self.device + "/CommandStartB"),
                
                (self.ui.tauValueLabel_StateStartA, self.device + "/StateStartA"),
                (self.ui.tauValueLabel_StateStartB, self.device + "/StateStartB"),
                
                #Ramping State/////////////////////////////////////////////////
                (self.ui.tauValueLabel_RampingStateA, self.device + "/RampingStateA"),
                (self.ui.tauValueLabel_RampingStateB, self.device + "/RampingStateB"),
                
                ##Vesions /////////////////////////////////////////////////////
                (self.ui.tauValueLabel_loopVersion, self.device + "/VersionDate"),
                (self.ui.tauValueLabel_diagVersion, self.deviceDiag + "/VersionDate"),
                
                ##Landau //////////////////////////////////////////////////////
                (self.ui.tauValueLabel_tuningEn_3, self.deviceDiag + "/LandauTuningEnable"),
                (self.ui.tauValueLabel_moveUp_3, self.deviceDiag + "/MoveLandauUp"),
                (self.ui.tauValueLabel_movePlg1_3, self.deviceDiag + "/MoveLandauPLG"),
                (self.ui.tauValueLabel_tuningOffset_3, self.deviceDiag + "/LandauPhaseOffset"),
                (self.ui.tauValueLabel_marginUp_3, self.deviceDiag + "/LandauMarginUp"),
                (self.ui.tauValueLabel_marginLow_3, self.deviceDiag + "/LandauMarginLow"),
                (self.ui.tauValueLabel_forwardMin_4, self.deviceDiag + "/MinLandauAmplitude"),
                (self.ui.tauValueLabel_tuningPosEn_3, self.deviceDiag + "/LandauPositiveEn"),
                (self.ui.tauValueLabel_numberPulses_4, self.deviceDiag + "/NumSteps"),
                (self.ui.taurusBoolLed_37, self.deviceDiag + "/PlungerMvMTDiagA"),
                (self.ui.taurusBoolLed_38, self.deviceDiag + "/PlungerMvUpMTDiagA"),
                (self.ui.taurusBoolLed_39, self.deviceDiag + "/PlungerMvATDiagA"),
                (self.ui.taurusBoolLed_40, self.deviceDiag + "/PlungerMvUpATDiagA"),
                
                #(self.ui., self.deviceDiag + "DephaseMOLandauA")
                #(self.ui., self.deviceDiag + "DephaseMOLandauB")
                
                #PLC ///////////////////////////////////////////////
                #(self.ui.taurusLabel_airTemp, self.devicePLC + "/AIR_TEMP_HPC_1"),
                #(self.ui.taurusLabel_vacPressure, self.devicePLC + "/M2COND_VAC_C1_SCALE"),
                #(self.ui.taurusLabel_watTempReturn, self.devicePLC + "/TEMP_RET_PUMP"),
                #(self.ui.taurusLabel_watTempOConductor, self.devicePLC + "/TEMP_SLINGA_SC"),
                #(self.ui.taurusLabel_watTempLoop, self.devicePLC + "/TEMP_STUBB_SC"),
                #(self.ui.taurusLed_pumpOn, self.devicePLC + "/FLODE_OK"),
                #(self.ui.taurusLed_hfOn, self.devicePLC + "/HF_ENABLE_ON"),
                #(self.ui.taurusLed_airTemp, self.devicePLC + "/A_AIR_TEMP_HPC_1_50"),
                #(self.ui.taurusLed_fanError, self.devicePLC + "/A_FAN_ERROR"),
                #(self.ui.taurusLed_cavTemp, self.devicePLC + "/A_CAV_90G"),
                #(self.ui.taurusLed_vacPumpControlUnit, self.devicePLC + "/A_VAC_INT_FROM_RFCAB_1"),
                #(self.ui.taurusLed_watCircFlowBody, self.devicePLC + "/A_CIRK_WATER_FL1"),
                #(self.ui.taurusLed_watCircFlowLoad, self.devicePLC + "/A_CIRK_WATER_FL2"),
                #(self.ui.taurusLed_watHighReturnTemp, self.devicePLC + "/A_HIGH_TEMP_RETURN"),
                #(self.ui.taurusLed_watLowPressure, self.devicePLC + "/A_LOW_PRESSURE"),
                #(self.ui.taurusLed_watPumpLowFlow, self.devicePLC + "/A_TIM_CAV_OFF_FLOW"),
                
                #PyAlarm widget////////////////////////////////////////////////
                #(self.alarmWidget, self.deviceAlarm),
                
                #FDL //////////////////////////////////////////////////////////
                (self.ui.taurusLed_3, self.device + "/FDLTriggerState"),
                (self.ui.taurusLed_4, self.deviceDiag + "/FDLTriggerState"),
                (self.ui.taurusLabel_bufferSize, self.device + "/FDLDataBufferSize"),
                (self.ui.taurusLabel_buffersizeD, self.deviceDiag + "/FDLDataBufferSize"),
                (self.ui.taurusLabel_trgDelay, self.device + "/FDLTriggerDelay"),
                (self.ui.taurusLabel_trgDelayD, self.deviceDiag + "/FDLTriggerDelay"),
                (self.ui.taurusLabel_chSrA, self.device + "/FDLChannelSourceA"),
                (self.ui.taurusLabel_chSrDA, self.deviceDiag + "/FDLChannelSourceA"),
                (self.ui.taurusLabel_chSrB, self.device + "/FDLChannelSourceB"),
                (self.ui.taurusLabel_chSrDB, self.deviceDiag + "/FDLChannelSourceB"),
                
                #//////////////////////////////////////////////////////////////
                (self.ui.tauValueLabel_gainola, self.device + "/GainOLA"),
                (self.ui.tauValueLabel_gainolb, self.device + "/GainOLB"),
                (self.ui.tauValueLabel_phaseShift_11, self.device + "/PhaseShiftFwTet1A"),
                (self.ui.tauValueLabel_phaseShift_10, self.device + "/PhaseShiftFwTet1B"),
                
                (self.ui.tauValueLabel_FwTet1Loop, self.device + "/IFwTet1ALoop"),
                (self.ui.tauValueLabel_FwTet1Loop_2, self.device + "/QFwTet1ALoop"),
                (self.ui.tauValueLabel_FwTet1Loop_3, self.device + "/AmpFwTet1ALoop"),
                (self.ui.tauValueLabel_FwTet1Loop_4, self.device + "/PhFwTet1ALoop"),
                (self.ui.tauValueLabel_FwTet1Loop_5, self.device + "/IFwTet1BLoop"),
                (self.ui.tauValueLabel_FwTet1Loop_6, self.device + "/QFwTet1BLoop"),
                (self.ui.tauValueLabel_FwTet1Loop_7, self.device + "/AmpFwTet1BLoop"),
                (self.ui.tauValueLabel_FwTet1Loop_8, self.device + "/PhFwTet1BLoop"),
                
            ]
        
        ## Writtable attributes ///////////////////////////////////////////////
        self._attrList = [
                #in the old version where this
                #(self.ui.lineEdit_cavVolt, self.device + "/CavityVoltA"),
                #(self.ui.lineEdit_cavPhase, self.device + "/CavityPhaseA"),
                (self.ui.lineEdit_cavVolt, self.device + "/AmpRefInA"),
                (self.ui.lineEdit_cavPhase, self.device + "/PhaseRefInA"),
                
                (self.ui.lineEdit_ampRefMinA, self.device + "/AmpRefMinA"),
                (self.ui.lineEdit_phaseRefMinA, self.device + "/PhaseRefMinA"),
                
                (self.ui.lineEdit_PILimit, self.device + "/PILimitA"),
                (self.ui.lineEdit_ki, self.device + "/KiA"),
                (self.ui.lineEdit_kp, self.device + "/KpA"),
                
                (self.ui.lineEdit_phaseShift, self.device + "/PhaseShiftCavA"),
                (self.ui.lineEdit_phaseShift_3, self.device + "/PhaseShiftDACA1"),
                (self.ui.lineEdit_phaseShift_5, self.device + "/PhaseShiftDACA2"),
                
                (self.ui.lineEdit_Tetrode1A, self.device + "/GainTetrodeA1"),
                (self.ui.lineEdit_Tetrode2A, self.device + "/GainTetrodeA2"),
                
                (self.ui.lineEdit_cavVolt_2, self.device + "/AmpRefInB"),
                (self.ui.lineEdit_cavPhase_2, self.device + "/PhaseRefInB"),
                
                (self.ui.lineEdit_ampRefMinB, self.device + "/AmpRefMinB"),
                (self.ui.lineEdit_phaseRefMinB, self.device + "/PhaseRefMinB"),
                
                (self.ui.lineEdit_PILimit_2, self.device + "/PILimitB"),
                (self.ui.lineEdit_ki_2, self.device + "/KiB"),
                (self.ui.lineEdit_kp_2, self.device + "/KpB"),
                
                (self.ui.lineEdit_phaseShift_2, self.device + "/PhaseShiftCavB"),
                (self.ui.lineEdit_phaseShift_4, self.device + "/PhaseShiftDACB1"),
                (self.ui.lineEdit_phaseShift_6, self.device + "/PhaseShiftDACB2"),
                
                (self.ui.lineEdit_Tetrode1A, self.device + "/GainTetrodeB1"),
                (self.ui.lineEdit_Tetrode2B, self.device + "/GainTetrodeB2"),
                
                (self.ui.lineEdit_dutyCycle, self.device + "/ConditioningDutyCicleA"),
                (self.ui.lineEdit_cavVolt_3, self.device + "/CavityVoltA"),
                
                (self.ui.lineEdit_dutyCycle_3, self.device + "/ConditioningDutyCicleB"),
                (self.ui.lineEdit_cavVolt_6, self.device + "/CavityVoltB"),
                
                (self.ui.lineEdit_numberPulses, self.device + "/NumStepsA"),
                
                (self.ui.lineEdit_numberPulses_2, self.device + "/NumStepsB"),
                
                (self.ui.lineEdit_marginUp_2, self.device + "/MarginUpA"),
                (self.ui.lineEdit_marginLow_2, self.device + "/MarginLowA"),
                (self.ui.lineEdit_forwardMin, self.device + "/FwMinA"),
                
                (self.ui.lineEdit_tuningDelayA, self.device + "/TuningDelayA"),
                (self.ui.lineEdit_tuningFFStepsA, self.device + "/TuningFFStepsA"),
                (self.ui.lineEdit_tuningDelayB, self.device + "/TuningDelayB"),
                (self.ui.lineEdit_tuningFFStepsB, self.device + "/TuningFFStepsB"),
                
                (self.ui.lineEdit_marginUp_3, self.device + "/MarginUpB"),
                (self.ui.lineEdit_marginLow_3, self.device + "/MarginLowB"),
                (self.ui.lineEdit_forwardMin_2, self.device + "/FwMinB"),
                
                (self.ui.lineEdit_filterStage, self.device + "/FilterStagesA"),
                (self.ui.lineEdit_samplesAv, self.device + "/NumSamplesAverageA"),
                
                (self.ui.lineEdit_filterStage_2, self.device + "/FilterStagesB"),
                (self.ui.lineEdit_samplesAv_2, self.device + "/NumSamplesAverageB"),
                
                (self.ui.lineEdit_tuningOffset, self.device + "/PhaseOffsetA"),
                (self.ui.lineEdit_tuningOffset_2, self.device + "/PhaseOffsetB"),
                
                #Fast Interlocks
                (self.ui.lineEdit_RvTet1A, self.deviceDiag + "/RvTet1A"),
                (self.ui.lineEdit_RvTet2A, self.deviceDiag + "/RvTet2A"),
                (self.ui.lineEdit_RvCircA, self.deviceDiag + "/RvCircA"),
                (self.ui.lineEdit_FwLoadA, self.deviceDiag + "/FwLoadA"),
                (self.ui.lineEdit_FwHybLoadA, self.deviceDiag + "/FwHybLoadA"),
                (self.ui.lineEdit_RvCavA, self.deviceDiag + "/RvCavA"),
                
                (self.ui.lineEdit_RvTet1B, self.deviceDiag + "/RvTet1B"),
                (self.ui.lineEdit_RvTet2B, self.deviceDiag + "/RvTet2B"),
                (self.ui.lineEdit_RvCircB, self.deviceDiag + "/RvCircB"),
                (self.ui.lineEdit_FwLoadB, self.deviceDiag + "/FwLoadB"),
                (self.ui.lineEdit_FwHybLoadB, self.deviceDiag + "/FwHybLoadB"),
                (self.ui.lineEdit_RvCavB, self.deviceDiag + "/RvCavB"),
                
                #Interlock Inputs Diagnostics
                (self.ui.taurusWheelEdit, self.deviceDiag + "/ITCKNumber"),
                
                #Ramping inputs
                (self.ui.lineEdit_timeRampUpA, self.device + "/TimeRampUpA"),
                (self.ui.lineEdit_timeRampDownA, self.device + "/TimeRampDownA"),
                (self.ui.lineEdit_ampRampInitA, self.device + "/AmpRampInitA"),
                (self.ui.lineEdit_ampRampEndA, self.device + "/AmpRampEndA"),
                (self.ui.lineEdit_phaseRampInitA, self.device + "/PhaseRampInitA"),
                (self.ui.lineEdit_phaseRampEndA, self.device + "/PhaseRampEndA"),
                
                (self.ui.lineEdit_timeRampUpB, self.device + "/TimeRampUpB"),
                (self.ui.lineEdit_timeRampDownB, self.device + "/TimeRampDownB"),
                (self.ui.lineEdit_ampRampInitB, self.device + "/AmpRampInitB"),
                (self.ui.lineEdit_ampRampEndB, self.device + "/AmpRampEndB"),
                (self.ui.lineEdit_phaseRampInitB, self.device + "/PhaseRampInitB"),
                (self.ui.lineEdit_phaseRampEndB, self.device + "/PhaseRampEndB"),
                
                #FDL //////////////////////////////////////////////////////////
                (self.ui.taurusValueLineEdit_bufferSize, self.device + "/FDLDataBufferSize"),
                (self.ui.taurusValueLineEdit_bufferSizeD, self.deviceDiag + "/FDLDataBufferSize"),
                (self.ui.taurusValueLineEdit_trgDelay, self.device + "/FDLTriggerDelay"),
                (self.ui.taurusValueLineEdit_trgDelayD, self.deviceDiag + "/FDLTriggerDelay"),
                
                #//////////////////////////////////////////////////////////////
                (self.ui.lineEdit_gainola, self.device + "/GainOLA"),
                (self.ui.lineEdit_gainolb, self.device + "/GainOLB"),
                (self.ui.lineEdit_phaseShift_10, self.device + "/PhaseShiftFwTet1A"),
                (self.ui.lineEdit_phaseShift_9, self.device + "/PhaseShiftFwTet1B"),
            ]
            
        self._comboList = [
                
                (self.ui.comboBox_voltInc, self.device + "/VoltageRateIncreaseA"),
                
                (self.ui.comboBox_quad, self.device + "/QuadrantSelectionA"),
                (self.ui.comboBox_lookRef, self.device + "/LookRefA"),
                (self.ui.comboBox_loopEn, self.device + "/LoopEnableA"),
                (self.ui.comboBox_phaseShiftEn, self.device + "/ADCsPhaseShiftEnableA"),
                (self.ui.comboBox_DACsGainEn, self.device + "/DACsPhaseShiftEnableA"),
                (self.ui.comboBox_GainTetA1En, self.device + "/GainTetrodeEnableA"),
                (self.ui.comboBox_loopInputA, self.device + "/LoopInputA"),
                
                (self.ui.comboBox_voltInc_3, self.device + "/VoltageRateIncreaseB"),
                (self.ui.comboBox_quad_2, self.device + "/QuadrantSelectionB"),
                (self.ui.comboBox_lookRef_2, self.device + "/LookRefB"),
                (self.ui.comboBox_loopEn_2, self.device + "/LoopEnableB"),
                (self.ui.comboBox_phaseShiftEn_3, self.device + "/ADCsPhaseShiftEnableB"),
                (self.ui.comboBox_GainTetB1En, self.device + "/GainTetrodeEnableB"),
                (self.ui.comboBox_loopInputB, self.device + "/LoopInputB"),
                
                (self.ui.comboBox_DACsGainEn_2, self.device + "/DACsPhaseShiftEnableB"),
                (self.ui.comboBox_pulseMode, self.device + "/PulseModeEnableA"),
                (self.ui.comboBox_voltInc_2, self.device + "/VoltageRateIncreaseA"),
                
                (self.ui.comboBox_pulseMode_3, self.device + "/PulseModeEnableB"),
                
                (self.ui.comboBox_autoConditioningEnable, self.device + "/AutoConditioningEnableA"),
                (self.ui.comboBox_autoConditioningEnable_2, self.device + "/AutoConditioningEnableB"),
                
                (self.ui.comboBox_voltInc_6, self.device + "/VoltageRateIncreaseB"),
                (self.ui.comboBox_moveUp, self.device + "/MoveUpA"),
                (self.ui.comboBox_movePlg, self.device + "/MoveA"),
                (self.ui.comboBox_freqPulses, self.device + "/PulsesFrequencyA"),
                (self.ui.comboBox_moveUp_2, self.device + "/MoveUpB"),
                (self.ui.comboBox_movePlg_2, self.device + "/MoveB"),
                (self.ui.comboBox_freqPulses_2, self.device + "/PulsesFrequencyB"),
                (self.ui.comboBox_tuningEn, self.device + "/TuningEnableA"),
                (self.ui.comboBox_tuningPosEn, self.device + "/TuningPosEnA"),
                (self.ui.comboBox_tuningFreq, self.device + "/PulsesFrequencyA"),
                (self.ui.comboBox_tuningEn_2, self.device + "/TuningEnableB"),
                (self.ui.comboBox_tuningPosEn_2, self.device + "/TuningPosEnB"),
                (self.ui.comboBox_tuningFreq_2, self.device + "/PulsesFrequencyB"),
                (self.ui.tauValueComboBox_clockSource, self.device + "/FPGAClockSource"),
                (self.ui.comboBox_tuningTrgEnA, self.device + "/TuningTriggerEnableA"),
                (self.ui.comboBox_tuningFFEnA, self.device + "/TuningFFA"),
                (self.ui.comboBox_tuningFilterEnA, self.device + "/TuningFilterEnableA"),
                (self.ui.comboBox_tuningTrgEnB, self.device + "/TuningTriggerEnableB"),
                (self.ui.comboBox_tuningFFEnB, self.device + "/TuningFFB"),
                (self.ui.comboBox_tuningFilterEnB, self.device + "/TuningFilterEnableB"),
                
                #Interlocks inputs disable comboboxes
                (self.ui.tauValueComboBox_clockSource_3, self.deviceDiag + "/FPGAClockSource"),
                (self.ui.comboBox_RvTet1DisA, self.deviceDiag + "/RvTet1DisA"),
                (self.ui.comboBox_RvTet2DisA, self.deviceDiag + "/RvTet2DisA"),
                (self.ui.comboBox_RvCircDisA, self.deviceDiag + "/RvCircDisA"),
                (self.ui.comboBox_FwLoadDisA, self.deviceDiag + "/FwLoadDisA"),
                (self.ui.comboBox_FwHybLoadDisA, self.deviceDiag + "/FwHybLoadDisA"),
                (self.ui.comboBox_RvCavDisA, self.deviceDiag + "/RvCavDisA"),
                (self.ui.comboBox_ManualITCKDisA, self.deviceDiag + "/ManualITCKDisA"),
                (self.ui.comboBox_ArcsDisA, self.deviceDiag + "/ArcsDisA"),
                (self.ui.comboBox_VacuumDisA, self.deviceDiag + "/VacuumDisA"),
                (self.ui.comboBox_ExtDisA, self.deviceDiag + "/ExtITCKDisA"),
                (self.ui.comboBox_ExtITCKDisB_2, self.deviceDiag + "/PlungerEndSwitchUpDisA"),
                (self.ui.comboBox_ExtITCKDisB_3, self.deviceDiag + "/PlungerEndSwitchDownDisA"),
                
                (self.ui.comboBox_RvTet1DisB, self.deviceDiag + "/RvTet1DisB"),
                (self.ui.comboBox_RvTet2DisB, self.deviceDiag + "/RvTet2DisB"),
                (self.ui.comboBox_RvCircDisB, self.deviceDiag + "/RvCircDisB"),
                (self.ui.comboBox_FwLoadDisB, self.deviceDiag + "/FwLoadDisB"),
                (self.ui.comboBox_FwHybLoadDisB, self.deviceDiag + "/FwHybLoadDisB"),
                (self.ui.comboBox_RvCavDisB, self.deviceDiag + "/RvCavDisB"),
                (self.ui.comboBox_ManualITCKDisB, self.deviceDiag + "/ManualITCKDisB"),
                (self.ui.comboBox_ArcsDisB, self.deviceDiag + "/ArcsDisB"),
                (self.ui.comboBox_VacuumDisB, self.deviceDiag + "/VacuumDisB"),
                (self.ui.comboBox_ExtITCKDisB, self.deviceDiag + "/ExtITCKDisB"),
                (self.ui.comboBox_ExtDisA_2, self.deviceDiag + "/PlungerEndSwitchUpDisB"),
                (self.ui.comboBox_ExtDisA_3, self.deviceDiag + "/PlungerEndSwitchDownDisB"),
                
                #Interlocks output disable comboboxes
                (self.ui.comboBox_DACsOffDisA, self.deviceDiag + "/DACsOffDisA"),
                (self.ui.comboBox_PINSwitchDisA, self.deviceDiag + "/PinSwitchDisA"),
                (self.ui.comboBox_triggerFDLLoopsDisA, self.deviceDiag + "/TriggerFDLDisA"),
                (self.ui.comboBox_triggerFDLDiagDisA, self.deviceDiag + "/TriggerDiagFDLDisA"),
                (self.ui.comboBox_outputPLCDisA, self.deviceDiag + "/OutputPLCDisA"),
                (self.ui.comboBox_outputUpLevelDisA, self.deviceDiag + "/OutputUpperLevelDisA"),
                
                (self.ui.comboBox_DACsOffDisB, self.deviceDiag + "/DACsOffDisB"),
                (self.ui.comboBox_PINSwitchDisB, self.deviceDiag + "/PinSwitchDisB"),
                (self.ui.comboBox_triggerFDLLoopsDisB, self.deviceDiag + "/TriggerFDLDisB"),
                (self.ui.comboBox_triggerFDLDiagDisB, self.deviceDiag + "/TriggerDiagFDLDisB"),
                (self.ui.comboBox_outputPLCDisB, self.deviceDiag + "/OutputPLCDisB"),
                (self.ui.comboBox_outputUpLevelDisB, self.deviceDiag + "/OutputUpperLevelDisB"),
                
                #Ramping comboboxes
                (self.ui.comboBox_rampingEnA, self.device + "/RampingEnA"),
                (self.ui.comboBox_rampingEnB, self.device + "/RampingEnB"),
                
                (self.ui.comboBox_phaseIncRate, self.device + "/PhaseIncreaseRateA"),
                (self.ui.comboBox_phaseIncRate_2, self.device + "/PhaseIncreaseRateB"),
                
                #Automatic startup/////////////////////////////////////////////
                (self.ui.comboBox_autoStartUpA, self.device + "/AutoStartUpEnA"),
                (self.ui.comboBox_CommandStartA, self.device + "/CommandStartA"),
                
                (self.ui.comboBox_autoStartUpB, self.device + "/AutoStartUpEnB"),
                (self.ui.comboBox_CommandStartB, self.device + "/CommandStartB"),
                
                #Landau ///////////////////////////////////////////////////////
                (self.ui.comboBox_moveUp_3, self.deviceDiag + "/MoveLandauUp"),
                (self.ui.comboBox_movePlg_3, self.deviceDiag + "/MoveLandauPLG"),
                (self.ui.comboBox_tuningEn_3, self.deviceDiag + "/LandauTuningEnable"),
                (self.ui.comboBox_tuningPosEn_3, self.deviceDiag + "/LandauPositiveEn"),
                
                (self.ui.taurusValueComboBox_chSrA, self.device + "/FDLChannelSourceA"),
                (self.ui.taurusValueComboBox_chSrDA, self.deviceDiag + "/FDLChannelSourceA"),
                (self.ui.taurusValueComboBox_chSrB, self.device + "/FDLChannelSourceB"),
                (self.ui.taurusValueComboBox_chSrDB, self.deviceDiag + "/FDLChannelSourceB")
                
            ]
    
    
def main():
    app = QtGui.QApplication(sys.argv)
    
    total_args = len(sys.argv)
    sectorSelected = []
    
    wnd = llrfGUI()
    wnd.show()
    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()


