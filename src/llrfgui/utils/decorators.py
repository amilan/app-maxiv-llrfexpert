#!/usr/bin/env python

###############################################################################
#     Set of decorators used for the LLRF Expert GUI.
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
This module contains a set of decorators used for the LLRF Expert GUI.
"""

__all__ = ['alert_problems']

__author__ = "amilan"

__docformat__ = 'restructuredtext'

import PyTango
import traceback
import sys

from functools import wraps

from PyQt4 import QtGui

def alert_problems(meth):
    '''
        If an error happens during the execution of the method decorated by
        this decorator it will show a QMessageBox with an error message.
    '''
    @wraps(meth)
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

