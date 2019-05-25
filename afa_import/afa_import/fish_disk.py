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

import os.path
import re
from afa_import.product_info import ProductInfo

class FishDisk:

    @classmethod
    def frompath(cls, path):
        if os.sep == '\\':
            p = re.compile(r'(.*\\)?d(\d{3,4})')
        else:
            p = re.compile(r'(.*' + os.sep + r')?d(\d{3,4})')
        m = p.match(path)
        if m == None:
            raise Exception('Unable to extract disk number from path: ' + path)
        return FishDisk(int(m.group(2)), path)

    def __init__(self, disknumber, path):
        "Initialise FishDisk by scanning a directory of .pi files"

        self.disknumber = disknumber
        self.path = path
        self.artifacts = []
        overhead = None
        for fn in os.listdir(path):
            if fn[-3:] == '.pi':
                pi = ProductInfo.loadfile(disknumber, os.path.join(path, fn))
                if pi.records['name'] == "Disk{}-Overhead".format(disknumber):
                    overhead = pi
                else:
                    self.artifacts.append(pi)
        
        if overhead != None:
            self.artifacts.append(overhead)
    
    def metadata_s3_key(self):
        return 'libraries/fish/disks/{}.json'.format(self.disknumber)

    def generate_metadata(self):
        metadata = {
            "volume_id": 'libraries/fish/disks/{}'.format(self.disknumber),
            "volume_number": self.disknumber,
            "name": 'Amiga Library Disk {}'.format(self.disknumber),
            "alternative_name": 'Fish Disk {}'.format(self.disknumber),
            "description": "This is disk {} in Fred Fish's Amiga Library Disk collection.".format(self.disknumber),
            "artifacts": self.artifacts
        }
        return metadata
    
    def to_dict(self):
        d = {}
        metadata = self.generate_metadata()
        for k in ('volume_id', 'volume_number', 'name', 'alternative_name', 'description'):
            d[k] = metadata[k]
        d['artifacts'] = list(map(lambda i: i.records, metadata['artifacts']))
        return d
