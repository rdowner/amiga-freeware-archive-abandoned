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
from cliff.command import Command
from afa_import.fish_disk import FishDisk

class GoldFish(Command):
    "Imports from a GoldFish CD-ROM"

    def get_parser(self, prog_name):
        parser = super(GoldFish, self).get_parser(prog_name)
        parser.add_argument('-p', '--profile', metavar='PROFILE_NAME', type=str, nargs=1, help='Name of the profile from the AWS credentials file')
        parser.add_argument('-a', '--artifact-bucket', metavar='BUCKET', type=str, nargs=1, help='Name of the S3 bucket for artifacts')
        parser.add_argument('-m', '--metadata-bucket', metavar='BUCKET', type=str, nargs=1, help='Name of the S3 bucket for metadata')
        parser.add_argument('directory', metavar='DIR', type=str, nargs='+', help='Directory containing a GoldFish disk')
        return parser

    def take_action(self, parsed_args):
        log = logging.getLogger(__name__)
        session = boto3.session.Session(profile_name=parsed_args.profile[0])
        s3 = session.resource('s3')
        metadata_bucket = parsed_args.metadata_bucket[0]
        artifact_bucket = parsed_args.artifact_bucket[0]

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
