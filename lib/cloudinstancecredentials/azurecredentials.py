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

import ast
from cloudinstancecredentials import utils
from cloudinstancecredentials.instancemetadata import InstanceMetadata


def detect_framework():
    try:
        curl_command = utils.command_run(
            [
                'curl',
                '-s',
                '-H',
                'Metadata:true',
                (
                  'http://169.254.169.254'
                  '/metadata/instance/compute/azEnvironment?'
                  'api-version=2019-06-01&format=text'
                )
            ]
        )
        return (curl_command.returncode == 0)
    except Exception:
        return False


class AzureInstanceMetadata(InstanceMetadata):
    def username(self):
        return self._get_instance_name()

    def password(self):
        return self._get_subscription_id()

    # private methods

    def _get_instance_metadata(self):
        curl_command = utils.command_run(
            [
                'curl',
                '-H',
                'Metadata:true',
                (
                  'http://169.254.169.254/metadata/instance?'
                  'api-version=2019-06-01'
                )
            ]
        )
        return ast.literal_eval(curl_command.output)

    def _get_instance_name(self):
        return self.metadata['compute']['name']

    def _get_subscription_id(self):
        return self.metadata['compute']['subscriptionId']
