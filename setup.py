#!/usr/bin/env python
"""Setup module for cloudinstancecredentials"""

# Copyright (c) 2020 SUSE LLC
#
# This file is part of cloudinstancecredentials.
#
# cloudinstancecredentials is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# cloudinstancecredentials is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with cloudinstancecredentials. If not, see
# <http://www.gnu.org/licenses/>.

import sys

try:
    import setuptools
except ImportError:
    sys.stderr.write('Python setuptools required, please install.')
    sys.exit(1)

version = open('lib/cloudinstancecredentials/VERSION').read().strip()

with open('requirements.txt') as req_file:
    requirements = req_file.read().splitlines()

with open('requirements-dev.txt') as req_file:
    dev_requirements = req_file.read().splitlines()[2:]

if __name__ == '__main__':
    setuptools.setup(
        name='cloudinstancecredentials',
        description=(
            'Command-line tools to set auth credentials on a '
            'public cloud instance'
        ),
        long_description=open('README.md').read(),
        long_description_content_type="text/markdown",
        url='https://github.com/SUSE-Enceladus/cloudinstancecredentials',
        license='GPLv3+',
        install_requires=requirements,
        extras_require={
            'dev': dev_requirements
        },
        author='SUSE Public Cloud Team',
        author_email='public-cloud-dev@susecloud.net',
        version=version,
        packages=setuptools.find_packages('lib'),
        package_data={'cloudinstancecredentials': ['VERSION']},
        package_dir={
            '': 'lib',
        },
        scripts=[
            'set-http-basic-credentials',
            'cloudinstancecredentials-config'
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Natural Language :: English',
            'Environment :: Console',
            'License :: OSI Approved :: '
            'GNU General Public License v3 or later (GPLv3+)',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
        ]
    )
