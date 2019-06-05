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

import os
import logging
import json
import boto3
from elasticsearch import Elasticsearch, RequestsHttpConnection, helpers
from requests_aws4auth import AWS4Auth
from cliff.command import Command
from afa_import.fish_disk import FishDisk

class GoldFish(Command):
    "Imports from a GoldFish CD-ROM"

    def get_parser(self, prog_name):
        parser = super(GoldFish, self).get_parser(prog_name)
        parser.add_argument('-p', '--profile', metavar='PROFILE_NAME', type=str, nargs=1, help='Name of the profile from the AWS credentials file')
        parser.add_argument('-a', '--artifact-bucket', metavar='BUCKET', type=str, nargs=1, help='Name of the S3 bucket for artifacts')
        parser.add_argument('-m', '--metadata-bucket', metavar='BUCKET', type=str, nargs=1, help='Name of the S3 bucket for metadata')
        parser.add_argument('-s', '--search-endpoint', metavar='HOSTNAME', type=str, nargs=1, help='Hostname of the ElasticSearch endpoint')
        parser.add_argument('directory', metavar='DIR', type=str, nargs='+', help='Directory containing a GoldFish disk')
        return parser

    def take_action(self, parsed_args):
        log = logging.getLogger(__name__)
        if parsed_args.profile:
            session = boto3.session.Session(profile_name=parsed_args.profile[0])
        else:
            session = boto3.session.Session()
        s3 = session.resource('s3')

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
            search_endpoint = None
            es = None

        metadata_bucket = parsed_args.metadata_bucket[0] if parsed_args.metadata_bucket else None
        artifact_bucket = parsed_args.artifact_bucket[0] if parsed_args.artifact_bucket else None

        es_actions = []
        for dir in parsed_args.directory:
            fd = FishDisk.frompath(dir)
            metadata = fd.to_dict()
            log.info("Importing '{}'".format(metadata['name']))

            if metadata_bucket:
                log.info("Uploading metadata to s3://{}/{}".format(metadata_bucket, fd.metadata_s3_key()))
                obj = s3.Object(metadata_bucket, fd.metadata_s3_key())
                obj.put(Body=json.dumps(metadata))

            if artifact_bucket:
                for a in metadata['artifacts']:
                    log.info("Uploading artifact to s3://{}/{}".format(artifact_bucket, a['artifact_id']))
                    obj = s3.Object(artifact_bucket, a['artifact_id'])
                    obj.put(Body=open(os.path.join(dir, a['filename']), 'rb'))

            if search_endpoint:
                for a in fd.artifacts:
                    log.info("Generating search index entry for {}".format(a.records['artifact_id']))
                    action = {
                        "_index": "amiga-freeware",
                        "_type": "amiga-freeware",
                        "_id": a.records['artifact_id'],
                        "_source": a.search_index_entry()
                    }
                    es_actions.append(action)

        helpers.bulk(es, es_actions)
