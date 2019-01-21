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

class ProductInfo:

    def __init__(self, disknumber, filename, input):
        "Initialise ProductInfo from a string"

        lines = input.splitlines()
        # Drop everything before the `.name` record
        while len(lines) > 0 and lines[0] != ".name":
            del lines[0]
        
        # Split into list of records, with each record being a list of strings
        q = []
        w = []
        line_no = len(lines)
        while len(lines) > 0:
            tail = lines.pop()
            try:
                q.insert(0, tail)
                if len(tail) > 0 and tail[0] == '.':
                    w.insert(0, q)
                    q = []
                line_no -= 1
            except:
                raise Exception('Error parsing {} {} line {}: {}'.format(disknumber, filename, line_no, tail))
        
        # Convert that list into a dict    
        r = {
            'filename': filename,
            'disknumber': disknumber,
            'content-type': 'application/x-lha'
        }
        for e in w:
            key = e[0][1:]
            del e[0]
            value = '\n'.join(e)
            r[key] = value
        
        self.records = r

    @classmethod
    def loadfile(cls, disknumber, filename):
        fn, ext = os.path.splitext(os.path.basename(filename))
        with open(filename, 'r', encoding='iso-8859-1') as myfile:
            data=myfile.read()
        return cls(disknumber, fn, data)

    def search_index_entry(self):
        conv = {
            'object-type': 'artifact',
            'object-link': 'libraries/fish/disks/%d#%s' % (self.records['disknumber'], self.records.get('name', None)),
            'filename': self.records['filename'],
            'content-type': self.records['content-type'],
            'address': self.records.get('address', None),
            'aminet-dir': self.records.get('aminet-dir', None),
            'author': self.records.get('author', None),
            'contents': self.records.get('contents', None),
            'date': self.records.get('date', None),
            'description': self.records.get('description', None),
            'distribution': self.records.get('distribution', None),
            'email': self.records.get('email', None),
            'fullname': self.records.get('fullname', None),
            'name': self.records.get('name', None),
            'short': self.records.get('short', None),
            'fish-type': self.records.get('type', None),
            'version': self.records.get('version', None),
        }
        return {k: v for k, v in conv.items() if v is not None}
