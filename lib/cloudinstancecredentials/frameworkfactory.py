# Copyright 2020 SUSE LLC
#
# This file is part of cloudinstancecredentials
#
# cloudinstancecredentials is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cloudinstancecredentials is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# cloudinstancecredentials. If not, see <http://www.gnu.org/licenses/>.

from importlib import import_module
from cloudinstancecredentials.utils import command_run


def get_metadata(logger):
    frameworks = ['Azure', 'Ec2']
    try:
        for framework in frameworks:
            which_command = command_run(
                ['rpm', '-q', 'python3-{}metadata'.format(framework.lower())],
                raise_on_error=False
            )

            if (which_command.returncode == 0) and ('not installed' not
                                                    in which_command.output):
                framework_mod = import_module(
                    '{}credentials'.format(framework.lower())
                )
                framework_class = getattr(
                    framework_mod, '{}InstanceMetadata'.format(framework)
                )
                return framework_class(logger)
        logger.warning('Framework not supported.')
    except Exception as err:
        logger.error('CloudInstanceCredentials failed: {}'.format(err))
