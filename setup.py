#!/usr/bin/env python

###############################################################################
#     LLRF expert graphical user interface.
#
#     Copyright (C) 2013  MAX IV Laboratory, Lund Sweden.
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


from setuptools import setup, find_packages

def main():

    name = "taurusgui-llrfexpert"

    version = "1.4.1"

    description = "Taurus GUI for Low Level RF expert users."

    author = "Antonio Milan Otero"

    author_email = "antonio.milan_otero@maxlab.lu.se"

    license = "GPLv3"

    url = "http://www.maxlab.lu.se"

    package_dir = {'': 'src'}

    packages = find_packages('src')

    scripts = ['scripts/ctllrfgui']

    data_files = [('~/.config/MAXIV', ['config/llrfExpertGUI.ini'])]

    setup(
        name=name,
        version=version,
        description=description,
        author=author,
        author_email=author_email,
        license=license,
        url=url,
        package_dir=package_dir,
        packages=packages,
        scripts=scripts,
        data_files=data_files
    )

if __name__ == "__main__":
    main()
