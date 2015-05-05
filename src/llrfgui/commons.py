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

"""Main module to run the Low Level Radio Frequency expert taurus GUI."""

__all__ = ['sections_dict']

__author__ = 'antmil'

__docformat__ = 'restructuredtext'

# Old nutaq equipment

# Solaris nutaq equipment

sections_dict = {
    'rflab_old': {
        'loops': 'ws/rf/pynutaq-1',
        'diags': 'ws/rf/pynutaq-2'
    },
    'rflab_new': {
        'loops': 'ws/rf/pynutaq-3',
        'diags': 'ws/rf/pynutaq-4'
    },
}