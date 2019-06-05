# Copyright 2019 Richard Downer
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import boto3
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from cliff.command import Command


class Search(Command):
    """Send a search query to ElasticSearch"""

    def get_parser(self, prog_name):
        parser = super(Search, self).get_parser(prog_name)
        parser.add_argument('-p', '--profile', metavar='PROFILE_NAME', type=str, nargs=1, help='Name of the profile from the AWS credentials file')
        parser.add_argument('-s', '--search-endpoint', metavar='HOSTNAME', type=str, nargs=1, help='Hostname of the ElasticSearch endpoint')
        parser.add_argument('query', metavar='QUERY', type=str, nargs='+', help='ElasticSearch query')
        return parser

    def take_action(self, parsed_args):
        log = logging.getLogger(__name__)
        if parsed_args.profile:
            session = boto3.session.Session(profile_name=parsed_args.profile[0])
        else:
            session = boto3.session.Session()

        if parsed_args.search_endpoint:
            search_endpoint = parsed_args.search_endpoint[0]
            region = 'us-east-2'
            service = 'es'
            credentials = session.get_credentials()
            awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service)

            es = Elasticsearch(
                hosts = [{'host': search_endpoint, 'port': 443}],
                http_auth = awsauth,
                use_ssl = True,
                verify_certs = True,
                connection_class = RequestsHttpConnection
            )
        else:
            es = None

        log.info("{}".format(es.search(index='amiga-freeware', q=parsed_args.query[0])))
