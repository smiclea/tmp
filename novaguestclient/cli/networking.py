# Copyright (c) 2017 Cloudbase Solutions Srl
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Command-line interface sub-commands related to endpoints.
"""

import argparse
import json

from cliff import command
from cliff import lister
from cliff import show

from novaguestclient import exceptions
from novaguestclient.cli import formatter



class Networking(command.Command):
    """validates an edpoint's connection"""

    def get_parser(self, prog_name):
        parser = super(Networking, self).get_parser(prog_name)
        parser.add_argument('instance_id', help='The instance id')
        return parser

    def take_action(self, args):
        networking = self.app.client_manager.guestagent.networking
        valid, message = networking.apply_networking(args.instance_id)
        if not valid:
            raise exceptions.EndpointConnectionValidationFailed(message)
