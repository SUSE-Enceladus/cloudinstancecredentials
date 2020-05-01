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
        instance_name = self.metadata.get('compute').get('name')
        if instance_name:
            return instance_name

        self.log.error('No instance name in metadata')
        raise KeyError('instanceName')

    def _get_subscription_id(self):
        subscription_id = self.metadata.get('compute').get('subscriptionId')
        if subscription_id:
            return subscription_id

        self.log.error('No subscription ID in metadata')
        raise KeyError('instanceName')
