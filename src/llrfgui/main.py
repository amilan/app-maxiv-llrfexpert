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

# Standard library imports
import os
# import sys
import importlib

# 3rd party imports
from taurus.qt.qtgui.taurusgui import TaurusGui
from taurus.qt.qtgui.application import TaurusApplication

from taurus.qt import Qt

# Local imports
from dialog import get_model

# Constants
EXPERT_GUI_NAME = 'llrfExpertGUI'
USER_GUI_NAME = 'llrfGUI'
ORGANIZATION = 'MAXIV'
PERIOD_ARG = '--taurus-polling-period='
PERIOD = 500
CONSOLE = False

__all__ = ['run']
__author__ = 'antmil'
__docformat__ = 'restructuredtext'


def configure_pythonpath():
    """
    Extend the pythonpath adding the llrfgui path.

    This method extends the pythonpath with the path where the module
    llrfgui is installed. This is extrange, but at this moment it's needed
    in order to be able to import the module panels from the taurusgui.
    Probably this method will be removed in the future if another (better)
    way is found.
    """
    from distutils.sysconfig import get_python_lib
    module_path = get_python_lib()
    panels_path = module_path
    sys.path.extend([panels_path])


def create_app_name(section, is_expert):
    if is_expert:
        app_name = EXPERT_GUI_NAME + '_' + section
    else:
        app_name = USER_GUI_NAME + '_' + section
    return app_name


def create_application(name, parser):
    """
    Create the application and return an (application, taurusgui) tuple.

    :return: Tuple compose by a TaurusApplication and a TaurusGUI
    :rtype: tuple
    """
    app = TaurusApplication(app_name=name, cmd_line_parser=parser)
    app.setOrganizationName(ORGANIZATION)
    gui = TaurusGui()
    return app, gui


def hide_toolbars(gui):
    """
    Hide unnecessary toolbars.

    :param TaurusGui gui: TaurusGUI to hide toolbars
    """
    gui.jorgsBar.hide()
    gui.statusBar().hide()
    gui.setLockView(False)


def set_polling_period(period):
    for arg in sys.argv:
        if arg.startswith(PERIOD_ARG):
            break
    else:
        sys.argv.append(PERIOD_ARG+str(period))


# def apply_panels(gui):
#     section, loops, diags = get_model()
#     create_panels(gui, section, loops, diags)


def create_panels(splashscreen, gui, section, loops_device, diags_device,
                  is_expert, transmitter1, transmitter2,
                  llrf_device=None, llrfdiags_device=None):
    """Create panels and set application name."""
    models_dict_expert = {
        'AutoStartUp': loops_device,
        'AutoTuning': loops_device,
        'Conditioning': loops_device,
        'Diagdc': loops_device,
        'Diags': [loops_device, diags_device],
        'Fdl': [loops_device, diags_device],
        'Fpgaclock': [loops_device, diags_device],
        'FpgaVersion': [loops_device, diags_device],
        'InterlockLevel': diags_device,
        'IqLoopsSettings': loops_device,
        'ItckInDiags': diags_device,
        'ItckInputDisable': diags_device,
        'ItckOutDiag': diags_device,
        'ItckOutDisable': diags_device,
        'Landau': diags_device,
        'LandauDiag': diags_device,
        'ManualTuning': loops_device,
        'Ramping': loops_device,
        'RampingDiag': loops_device,
        'Start': [loops_device, diags_device],
        'TuningDiag': loops_device,
        'Vcxo': loops_device,
        'PolarDiag': loops_device,
        'FIM': diags_device,
        "RFtransmitter_1": transmitter1,
        "RFtransmitter_2": transmitter2
    }

    models_dict_user = {
        'AutoTuningSimple': loops_device,
        'ItckOutDiagSimple': diags_device,
        'ManualTuningSimple': loops_device,
        'LlrfSimple': [llrf_device, llrfdiags_device]
    }

    if is_expert:
        models_dict = models_dict_expert
    else:
        models_dict = models_dict_user

    for name in models_dict.keys():
        msg = 'PROCESSING ' + name
        # print 'PROCESSING', name
        splashscreen.showMessage(msg)
        if name.startswith("RFtransmitter"):
            widget_instance = get_class_object("rftransmittergui", "LlRfTransmitterWidget")
        else:
            module_name = 'llrfgui.widgets.' + name.lower()
            widget_instance = get_class_object(module_name, name)
        gui.createPanel(widget_instance, name, floating=False, permanent=True)
        model = models_dict[name]
        if name.startswith("RFtransmitter"):
            gui.getPanel(name).widget().setModel(model)
        else:
            gui.getPanel(name).widget().setModel(model, section)


def get_class_object(module_name, class_name):
    mod = importlib.import_module(module_name)
    klass = getattr(mod, class_name)()
    return klass


def load_settings(gui, is_expert):
    if is_expert:
        ini_filename = '/default.ini'
    else:
        ini_filename = '/default_user.ini'

    default_ini = os.path.abspath(os.path.dirname(__file__)) + ini_filename
    gui.loadSettings(factorySettingsFileName=default_ini)


def run(period=PERIOD):
    """Run LLRF expert GUI."""
    import taurus.core.util.argparse as argparse
    parser = argparse.get_taurus_parser()
    parser.set_usage("%prog [-e, --expert]")
    description_message = "Graphical User Interface to control a LLRF system."
    parser.set_description(description_message)
    parser.add_option('-e', '--expert', action='store_true',
                      help="Launch the GUI in expert mode")

    parser.add_option('-r', '--rf_room', type=str,
                      help="""RF Room to be controlled.
                              \nAvailable options:
                              \n  RF-ROOM-1,RF-ROOM-2,RF-ROOM-3, RF-LAB
                           """)

    parser, options, args = argparse.init_taurus_args(parser=parser)

    # set_polling_period(period)

    import taurus
    taurus.Manager().changeDefaultPollingPeriod(period)
    configure_pythonpath()

    if options.expert:
        models = get_model(options.expert, options.rf_room)
        section, loops, diags, rftrans1, rftrans2 = models
        llrf = None
        llrfdiags = None
    else:
        models = get_model(options.expert, options.rf_room)
        section, loops, diags, llrf, llrfdiags, rftrans1, rftrans2 = models

    app_name = create_app_name(section, options.expert)
    app, gui = create_application(app_name, parser=parser)

    splashLogo = os.path.join(os.path.dirname(__file__),
                              'images/maxivlogo.png')
    splashscreen = Qt.QSplashScreen(Qt.QPixmap(splashLogo))
    splashscreen.show()
    app.processEvents()

    hide_toolbars(gui)

    splashscreen.showMessage('Creating panels')
    create_panels(
        splashscreen=splashscreen,
        gui=gui,
        section=section,
        loops_device=loops,
        diags_device=diags,
        is_expert=options.expert,
        transmitter1=rftrans1,
        transmitter2=rftrans2,
        llrf_device=llrf,
        llrfdiags_device=llrfdiags)
    splashscreen.showMessage('Loading settings')
    load_settings(gui, options.expert)

    gui.show()
    splashscreen.finish(gui)
    sys.exit(app.exec_())


if __name__ == '__main__':
    import sys

    EXPERT_MODE = '--expert'
    TEST_MODE = '-rtest'

    sys.argv.append(EXPERT_MODE)
    sys.argv.append(TEST_MODE)

    run()
