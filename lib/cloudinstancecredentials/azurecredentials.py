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

from azuremetadata import azuremetadata
from cloudinstancecredentials.instancemetadata import InstanceMetadata


class AzureInstanceMetadata(InstanceMetadata):
    def username(self):
        return self._get_instance_name()

    def password(self):
        return self._get_subscription_id()

    # private methods

    def _get_instance_metadata(self):
        meta = azuremetadata.AzureMetadata(api_version='2019-08-15')
        return meta.get_instance_data()

    def _get_instance_name(self):
        return self.metadata['compute']['name']

    def _get_subscription_id(self):
        return self.metadata['compute']['subscriptionId']
