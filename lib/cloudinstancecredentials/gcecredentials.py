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

from gcemetadata import gcemetadata

from cloudinstancecredentials.instancemetadata import InstanceMetadata


class GceInstanceMetadata(InstanceMetadata):
    def username(self):
        return self._get_instance_id()

    def password(self):
        return self._get_instance_name()

    # private methods

    def _get_instance_metadata(self):
        """Set the category to query"""
        meta = gcemetadata.GCEMetadata()
        meta.set_data_category('instance/')
        return meta

    def _get_instance_id(self):
        """The instance ID from the IID"""
        instance_id = self.metadata.get('id')
        if instance_id:
            return instance_id

        self.log.error('No instance id in metadata')
        raise KeyError('id')

    def _get_instance_name(self):
        """The name of this instance"""
        instance_name = self.metadata.get('name')
        if instance_name:
            return instance_name

        self.log.error('No key found in metadata')
        raise KeyError('name')
