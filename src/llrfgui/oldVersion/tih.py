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

## LAB devices ////////////////////////////////////////////////////////////////
MAIN_DEVICE_LAB = "ws/rf/lyrtech-01"
DIAG_DEVICE_LAB = "ws/rf/lyrtech-02"
PLC_DEVICE_LAB = "ws/plc/cav-cool-12"
ALARM_DEVICE_LAB = "ws/plc/alarm"

# PLC command codes
PLC_CMD_START_PUMP  = 1 << 0
PLC_CMD_STOP_PUMP   = 1 << 1
PLC_CMD_RESET_ALARM = 1 << 2
PLC_CMD_ENABLE_HF   = 1 << 3
PLC_CMD_DISABLE_HF  = 1 << 4

#Declaration of the possible values for comboBoxes#####################
CQ = [ 
        [ '1st Quadrant [0]', 0],
        [ '2nd Quadrant [1]', 1],
        [ '3rd Quadrant [2]', 2],
        [ '4th Quadrant [3]', 3],
    ]
        
CP = [
        ['[0,360]',0],
        ['[-90,270]',1],
        ['[-180,180]',2],
        ['[-270,90]',3],
    ]
        
CB = [
        ['OFF', 0],
        ['ON', 1],
    ]

CV = [ 
        ['0.01 mV/s [0]', 0],
        ['0.03 mV/s [1]', 1],
        ['0.1 mV/s [2]', 2],
        ['0.33 mV/s [3]', 3],
        ['1 mV/s [4]', 4],
        ['2 mV/s [5]', 5],
        ['4 mV/s [6]', 6],
        ['Immediatly apply [7]', 7],
    ]
        
CC = [ 
        [ '50 Hz [0]', 0],
        [ '100 Hz [1]', 1],
        [ '200 Hz [2]', 2],
        [ '400 Hz [3]', 3],
        [ '600 Hz [4]', 4],
        [ '800 Hz [5]', 5],
        [ '1 kHz [6]', 6],
        [ '2 KHz [7]', 7],
    ]

CCMDSTART = [
                ['Not RF', "Not RF"],
                ['RF Detected', "RF Detected"],
                ['Tuning Cavity', "Tuning Cavity"],
                ['Closing Loops', "Closing Loops"],
                ['Increasing Power', "Increasing Power"],
                ['Ready DC Power', "Ready DC Power"],
                ['Ready Ramping', "Ready Ramping"],
                ['Loops Saturated', "Loops Saturated"],
            ]

#CCMDSTART = [
                #['Minimum Drive [0]', 0],
                #['Min Drive & Tuning [1]', 1],
                #['Cav Tuned [2]', 2],
                #['Min Volt & Close Loops [3]', 3],
                #['Voltage Increase [4]', 4],
                #['DC mode [5]', 5],
                #['Ramping mode [6]', 6],
                #['Loops Diagnostics [7]', 7],
            #]

CMOVINGAVERAGE = [
                    ['1 [0]', 0],
                    ['2 [1]', 1],
                    ['4 [2]', 2],
                    ['8 [3]', 3],
                    ['16 [4]', 4],
                    ['32 [5]', 5],
                    ['64 [6]', 6],
                    ['128 [7]', 7],
                ]

CFS = [ 
        ['0', 0],
        ['1', 1],
        ['2', 2],
        ['3', 3],
      ]

CCS = [ 
        [ 'onboard' , 'onboard' ],
        [ 'external_front' , 'external_front'],
        [ 'onboard_divided' , 'onboard_divided'],
        [ 'reserved' ,'reserved'],
        [ 'fpdp_receive'  , 'fpdp_receive'],
        [ 'rapid_channel' , 'rapid_channel'],
        [ 'dif_receive' , 'dif_receive'],
        [ 'reserved_error' , 'reserved_error'],
    ]

CEN = [
        ['Enable','Enable'],
        ['Disable','Disable']
    ]

#CCS = [ 
#        [ 'onboard' , 0 ],
#        [ 'external_front' ,1],
#        [ 'onboard_divided' , 2],
#        [ 'reserved' , 3],
#        [ 'fpdp_receive'  , 4],
#        [ 'rapid_channel' , 5],
#        [ 'dif_receive' , 6],
#        [ 'reserved_error' , 7],
#    ]                                                                          

CPIR = [
        ['0,1',0],
        ['0.2',1],
        ['0.5',2],
        ['1',3],
        ['2',4],
        ['5',5],
        ['10',6],
        ['Inmediatly apply',7],
    ]

CFDL = [
        ['All signals', 1],
        ['IQCav', 2],
        ['I&QContr', 3],
        ['I&QCont1', 4],
        ['I&QCont2', 5],
        ['I&QError', 6],
        ['I&QErrorAccum', 7],
        ['I&QFwCav', 8],
        ['TuningDephase&CavPhase', 9],
        ['I&QRef', 10],
        ['AmpFw&PhFw', 11],
        ['I&QFwTet1', 12],
        ['I&QFwTet2', 13],
        ['I&QCavFilt', 14],
        ['I&QMO', 15],
        ['Amp&PhCav', 16],
    ]

CFDLDIAG = [
        ['All signals', 1],
        ['RvTet1', 2],
        ['RvTet2', 3],
        ['FwCircIn', 4],
        ['RvCircIr', 5],
        ['FwLoad', 6],
        ['FwHybLoad', 7],
        ['RvCav', 8],
        ['MO_landau', 9],
    ]
              
              