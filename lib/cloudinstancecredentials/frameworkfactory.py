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


def get_metadata(logger):
    try:
        from cloudinstancecredentials import azurecredentials

        return azurecredentials.AzureInstanceMetadata(logger)
    except Exception:
        pass
    try:
        from cloudinstancecredentials import ec2credentials

        return ec2credentials.Ec2InstanceMetadata(logger)
    except Exception:
        return None
