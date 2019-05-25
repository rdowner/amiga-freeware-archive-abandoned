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
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from afa_import.fish_disk import FishDisk

def test_fish_disk_import():
    "Tests the ability to scan a GoldFish directory and import the metadata"
    fishdisk = FishDisk(980, os.path.join(os.path.dirname(__file__), 'd980'))

    assert len(fishdisk.artifacts) == 3
    artifact = fishdisk.artifacts[0]
    assert artifact.records['name'] == 'APipe-Handler'
    artifact = fishdisk.artifacts[1]
    assert artifact.records['name'] == 'HWGRCS'
    artifact = fishdisk.artifacts[2]
    assert artifact.records['name'] == 'Disk980-Overhead'

def test_fish_disk_generate_metadata():
    "Tests generating the metadata record"
    fishdisk = FishDisk(980, os.path.join(os.path.dirname(__file__), 'd980'))

    metadata = fishdisk.generate_metadata()
    assert metadata['volume_id'] == 'libraries/fish/disks/980'
    assert metadata['volume_number'] == 980
    assert metadata['name'] == "Amiga Library Disk 980"
    assert metadata['alternative_name'] == "Fish Disk 980"
    assert metadata['description'] == "This is disk 980 in Fred Fish's Amiga Library Disk collection."
    artifacts = metadata['artifacts']
    artifact = fishdisk.artifacts[0]
    assert artifact.records['name'] == 'APipe-Handler'
    artifact = fishdisk.artifacts[1]
    assert artifact.records['name'] == 'HWGRCS'
    artifact = fishdisk.artifacts[2]
    assert artifact.records['name'] == 'Disk980-Overhead'

def test_fish_disk_infer_disk_number():
    "Tests that the disk number can be correctly inferred from the pathname"

    fishdisk = FishDisk.frompath(os.path.join(os.path.dirname(__file__), 'd980'))
    metadata = fishdisk.generate_metadata()
    assert metadata['volume_id'] == 'libraries/fish/disks/980'
    assert metadata['volume_number'] == 980

def test_fish_disk_s3_metadata_key():
    "Tests the the metadata is placed in the correct location in the S3 metadata bucket"

    fishdisk = FishDisk.frompath(os.path.join(os.path.dirname(__file__), 'd980'))
    assert fishdisk.metadata_s3_key() == 'libraries/fish/disks/980.json'
