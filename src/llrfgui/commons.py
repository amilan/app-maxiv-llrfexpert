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

"""Common definitions for the main GUI.
   The most important definition here is the :py:data:`sections_dict` which collects the
   relationship between device servers and sections.
"""

__all__ = ['sections_dict']

__author__ = 'antmil'

__docformat__ = 'restructuredtext'

# Old nutaq equipment

# Solaris nutaq equipment

# This will be substitude by an autodiscovery method ... soon ...
sections_dict = {
    #'rflab_old': {
    #    'loops': 'ws/rf/pynutaq-1',
    #    'diags': 'ws/rf/pynutaq-2'
    #},
    #'rflab_new': {
    #    'loops': 'ws/rf/pynutaq-3',
    #    'diags': 'ws/rf/pynutaq-4'
    #},
    'amilan_tests': {
        'loops': 'ws/rf/pynutaq_1',
        'diags': 'ws/rf/pynutaqdiags_1'
    },
    'R3-A100111CAB03': {
        'loops': 'R3-A100111CAB03/RF/NUTAQ-01',
        'diags': 'R3-A100111CAB03/RF/NUTAQDIAGS-01'
    },
    'R3-A101711CAB03': {
        'loops': 'R3-A101711CAB03/RF/NUTAQ-01',
        'diags': 'R3-A101711CAB03/RF/NUTAQDIAGS-01'
    },
    'R3-A101911CAB03': {
        'loops': 'R3-A101911CAB03/RF/NUTAQ-01',
        'diags': 'R3-A101911CAB03/RF/NUTAQDIAGS-01'
    },
}
