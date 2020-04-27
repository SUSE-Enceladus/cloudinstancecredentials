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

import json

import ec2metadata

from cloudinstancecredentials.instancemetadata import InstanceMetadata


class Ec2InstanceMetadata(InstanceMetadata):
    def username(self):
        return self._get_instance_id()

    def password(self):
        return self._get_account_id()

    # private methods

    def _get_instance_identity_doc(self):
        """Retrive and cache the instance identity document (IID)"""
        meta = ec2metadata.EC2Metadata()
        meta.setAPIVersion('latest')
        self.iid = json.loads(meta.get('document'))

    def _get_instance_id(self):
        """The instance ID from the IID"""
        return self.iid.get('instanceId')

    def _get_account_id(self):
        """The account ID of the owner of this instance, shown as 
           'Owner' in the UI"""
        return self.iid.get('accountId')
        
