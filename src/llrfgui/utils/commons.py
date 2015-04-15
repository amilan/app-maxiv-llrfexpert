#!/usr/bin/env python

###############################################################################
#     Common definitions for the widgets in the llrf expert gui
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
Common definitions for the widgets in the llrf expert gui
"""

__author__ = "amilan"

__docformat__ = 'restructuredtext'

# LAB devices
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

# Definition of possible values for comboBoxes
CQ = [ 
    ['1st Quadrant [0]', 0],
    ['2nd Quadrant [1]', 1],
    ['3rd Quadrant [2]', 2],
    ['4th Quadrant [3]', 3],
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
    ['50 Hz [0]', 0],
    ['100 Hz [1]', 1],
    ['200 Hz [2]', 2],
    ['400 Hz [3]', 3],
    ['600 Hz [4]', 4],
    ['800 Hz [5]', 5],
    ['1 kHz [6]', 6],
    ['2 KHz [7]', 7],
]

CCMDSTART = [
    ['Not RF [0]', 0],
    ['RF Detected [1]', 1],
    ['Tuning Cavity [2]', 2],
    ['Closing Loops [3]', 3],
    ['Increasing Power [4]', 4],
    ['Ready DC Power [5]', 5],
    ['Ready Ramping [6]', 6],
    ['Loops Saturated [7]', 7],
]

# CCMDSTART = [
#     ['Minimum Drive [0]', 0],
#     ['Min Drive & Tuning [1]', 1],
#     ['Cav Tuned [2]', 2],
#     ['Min Volt & Close Loops [3]', 3],
#     ['Voltage Increase [4]', 4],
#     ['DC mode [5]', 5],
#     ['Ramping mode [6]', 6],
#     ['Loops Diagnostics [7]', 7],
# ]

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
    ['onboard', 'onboard'],
    ['external_front', 'external_front'],
    ['onboard_divided', 'onboard_divided'],
    ['reserved', 'reserved'],
    ['fpdp_receive', 'fpdp_receive'],
    ['rapid_channel', 'rapid_channel'],
    ['dif_receive', 'dif_receive'],
    ['reserved_error', 'reserved_error'],
]

CEN = [
    ['Enable','Enable'],
    ['Disable','Disable']
]

# CCS = [
#    ['onboard', 0],
#    ['external_front', 1],
#    ['onboard_divided', 2],
#    ['reserved', 3],
#    ['fpdp_receive', 4],
#    ['rapid_channel', 5],
#    ['dif_receive', 6],
#    ['reserved_error', 7],
# ]

CPIR = [
    ['0,1', 0],
    ['0.2', 1],
    ['0.5', 2],
    ['1', 3],
    ['2', 4],
    ['5', 5],
    ['10', 6],
    ['Inmediatly apply', 7],
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
