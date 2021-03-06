#!/usr/bin/env python

###########################################################################
#     LLRF expert Graphical User Interface.
#
#     Copyright (C) 2015  MAX IV Laboratory, Lund Sweden.
#
#     This is free software; you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation; either version 3 of the License, or
#     (at your option) any later version.
#
#     This software is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program; if not, see <http://www.gnu.org/licenses/>.
###########################################################################

"""
Common definitions for the main GUI.

The most important definition here is the :py:data:`sections_dict` which
collects the relationship between device servers and sections.
"""

__all__ = ['sections_dict', 'sections_dict_tests', 'extra_attributes_dict']
__author__ = 'antmil'
__docformat__ = 'restructuredtext'

# Old nutaq equipment

# Solaris nutaq equipment

# Constants definition
RF1_POTENTIOMETER_A = 'R3-316S2/RF/RF-01/Potentiometer01'
RF1_POTENTIOMETER_B = 'R3-317S2/RF/RF-01/Potentiometer01'
RF1_LANDAU = 'R3-313S2/RF/RF-03/Potentiometer01'

RF2_POTENTIOMETER_A = 'R3-318S2/RF/RF-01/Potentiometer01'
RF2_POTENTIOMETER_B = 'R3-319S2/RF/RF-01/Potentiometer01'
RF2_LANDAU = 'R3-314S2/RF/RF-03/Potentiometer01'

RF3_POTENTIOMETER_A = 'R3-320S2/RF/RF-01/Potentiometer01',
RF3_POTENTIOMETER_B = 'R3-301S2/RF/RF-01/Potentiometer01',
RF3_LANDAU = 'R3-315S2/RF/RF-03/Potentiometer01'

RF1_POTENTIOMETER_A = 'R1-D1105S/RF/RF-01/Potentiometer03',
RF1_POTENTIOMETER_B = 'R1-D1105S/RF/RF-01/Potentiometer03',
RF1_LANDAU = 'R1-D1105S/RF/RF-01/Potentiometer03'

# F_R1_D1105S_RF_RF301_POT01_R, 3
# F_R1_D1105S_RF_RF302_POT01_R, 3

LANDAU_A_POTENTIOMETER = 'R3-313S2/RF/RF-03/Potentiometer01'
LANDAU_B_POTENTIOMETER = 'R3-314S2/RF/RF-03/Potentiometer01'
POTENTIOMETER_A_test = 'test/fakedevice/1/output1'
POTENTIOMETER_B_test = 'test/fakedevice/fake-02/R3-A1'

# This will be substitude by an autodiscovery method ... soon ...
sections_dict = {
    # 'rflab_old': {
    #    'loops': 'ws/rf/pynutaq-1',
    #    'diags': 'ws/rf/pynutaq-2'
    # },
    # 'rflab_new': {
    #    'loops': 'ws/rf/pynutaq-3',
    #    'diags': 'ws/rf/pynutaq-4'
    # },
    # 'amilan_tests': {
    #     'loops': 'ws/rf/pynutaq_1',
    #     'diags': 'ws/rf/pynutaqdiags_1',
    #     'llrf': 'ws/rf/llrf-1',
    #     'llrfdiags': 'ws/rf/llrfdiags-3'
    # },
    # 'R3-A100111CAB03': {
    #     'loops': 'R3-A100111CAB03/RF/NUTAQ-01',
    #     'diags': 'R3-A100111CAB03/RF/NUTAQDIAGS-01'
    # },
    # 'R3-A101711CAB03': {
    #     'loops': 'R3-A101711CAB03/RF/NUTAQ-01',
    #     'diags': 'R3-A101711CAB03/RF/NUTAQDIAGS-01'
    # },
    # 'R3-A101911CAB03': {
    #     'loops': 'R3-A101911CAB03/RF/NUTAQ-01',
    #     'diags': 'R3-A101911CAB03/RF/NUTAQDIAGS-01'
    # },
    'RF-ROOM-1': {
        'loops': 'R3-A101711CAB03/RF/NUTAQ-01',
        'diags': 'R3-A101711CAB03/RF/NUTAQDIAGS-01',
        'llrf': 'R3-A101711CAB03/RF/LLRF-01',
        'llrfdiags': 'R3-A101711CAB03/RF/LLRFDIAGS-01',
        'rftransmitter1': 'r3-a101711/rf/txa-01',
        'rftransmitter2': 'r3-a101711/rf/txa-51'
    },
    'RF-ROOM-2': {
        'loops': 'R3-A101911CAB03/RF/NUTAQ-01',
        'diags': 'R3-A101911CAB03/RF/NUTAQDIAGS-01',
        'llrf': 'R3-A101911CAB03/RF/LLRF-01',
        'llrfdiags': 'R3-A101911CAB03/RF/LLRFDIAGS-01',
        'rftransmitter1': 'r3-a101911/rf/txa-01',
        'rftransmitter2': 'r3-a101911/rf/txa-51'
    },
    'RF-ROOM-3': {
        'loops': 'R3-A100111CAB03/RF/NUTAQ-01',
        'diags': 'R3-A100111CAB03/RF/NUTAQDIAGS-01',
        'llrf': 'R3-A100111CAB03/RF/LLRF-01',
        'llrfdiags': 'R3-A100111CAB03/RF/LLRFDIAGS-01',
        'rftransmitter1': 'r3-a100111/rf/txa-01',
        'rftransmitter2': 'r3-a100111/rf/txa-51'
    },
    'R1': {
        'loops': 'R1-D100101CAB03/RF/Nutaq-01',
        'diags': 'R1-D100101CAB03/RF/NutaqDiags-01',
        'llrf': 'R1-D100101CAB03/RF/LLRF-01',
        'llrfdiags': 'R1-D100101CAB03/RF/LLRFDIAGS-01',
        'rftransmitter1': 'R1-D100101-RF-TXA-01',
        'rftransmitter2': 'R1-D100101-RF-TXA-02'
    },
    'RF-LAB': {
        'loops': 'rflab/llrf/nutaq_loops',
        'diags': 'rflab/llrf/nutaq_diags',
        'llrf': 'rflab/llrf/loops-01',
        'llrfdiags': 'rflab/llrf/diags-01',
        'rftransmitter1': '',
        'rftransmitter2': ''
    },
}

sections_dict_tests = {
    'test': {
        'loops': 'ws/rf/pynutaq_1',
        'diags': 'ws/rf/pynutaqdiags_1',
        'llrf': 'ws/rf/llrf-1',
        'llrfdiags': 'ws/rf/llrfdiags-3',
        'rftransmitter1': '',
        'rftransmitter2': ''
    }
}

extra_attributes_dict = {'RF-ROOM-1': {'POT_A': RF1_POTENTIOMETER_A,
                                       'POT_B': RF1_POTENTIOMETER_B,
                                       'LANDAU': RF1_LANDAU,
                                       },
                         'RF-ROOM-2': {'POT_A': RF2_POTENTIOMETER_A,
                                       'POT_B': RF2_POTENTIOMETER_B,
                                       'LANDAU': RF2_LANDAU,
                                       },
                         'RF-ROOM-3': {'POT_A': RF3_POTENTIOMETER_A,
                                       'POT_B': RF3_POTENTIOMETER_B,
                                       'LANDAU': RF3_LANDAU,
                                       },
                         'R1': {'POT_A': RF1_POTENTIOMETER_A,
                                'POT_B': RF1_POTENTIOMETER_B,
                                'LANDAU': RF1_LANDAU,
                                },
                         'RF-LAB': {'POT_A': '',
                                    'POT_B': '',
                                    'LANDAU': '',
                                    },
                         'test': {'POT_A': POTENTIOMETER_A_test,
                                  'POT_B': POTENTIOMETER_B_test,
                                  'LANDAU': POTENTIOMETER_A_test,
                                  }
                         }
