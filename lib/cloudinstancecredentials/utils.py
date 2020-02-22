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

import subprocess
from collections import namedtuple
import os


def command_run(command, custom_env=None, raise_on_error=True):
    command_type = namedtuple(
        'command', ['output', 'error', 'returncode']
    )
    environment = os.environ
    if custom_env:
        environment = custom_env

    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=environment
        )
    except Exception as issue:
        print(
            '{0}: {1}: {2}'.format(command[0], type(issue).__name__, issue)
        )
        raise Exception(
            '{0}: {1}: {2}'.format(command[0], type(issue).__name__, issue)
        )
    output, error = process.communicate()
    if process.returncode != 0 and not error:
        error = bytes(b'(no output on stderr)')
    if process.returncode != 0 and not output:
        output = bytes(b'(no output on stdout)')
    if process.returncode != 0 and raise_on_error:
        print(
            'EXEC: Failed with stderr: {0}, stdout: {1}'.format(
                error.decode(), output.decode()
            )
        )
        raise Exception(
            '{0}: stderr: {1}, stdout: {2}'.format(
                command[0], error.decode(), output.decode()
            )
        )
    return command_type(
        output=output.decode(),
        error=error.decode(),
        returncode=process.returncode
    )
