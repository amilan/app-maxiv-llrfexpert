#!/usr/bin/env python

from setuptools import setup

setup(name = "taurusgui-llrfexpert",
      version = "1.3.0",
      description = "Taurus GUI for Low Level RF expert users.",
      author = "Antonio Milan Otero",
      author_email = "antonio.milan_otero@maxlab.lu.se",
      license = "GPLv3",
      url = "http://www.maxlab.lu.se",
      package_dir = {'':'src'},
      packages = ['llrfGUI'],
      #install_requires = ['python-taurus'],
      scripts = ['scripts/llrfGUI']
     )

