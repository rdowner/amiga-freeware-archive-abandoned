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
from afa_import.product_info import ProductInfo

def test_pi_parse_string():
    testdata = """# This file contains product information that can be used by
# KingFisher 2.0 and other similar tools.

.name
PolyFit
.type
Graphing
.short
"Method of least squares" line fitting
.description
A program to fit straight lines, polynomes and exponentional curves to sets
of points.  Can fit to polynomes of degree of 16 and lower.  Calculated
coefficients can be printed and saved.  A graph of the points and curve can
be shown (in any screen resolution), printed and saved as an IFF file.
Supports localization.  Binary only.
.version
1.21
.date
1994.02.05
.author
Camiel Rouweler
.requirements
Requires OS 2.0+
.distribution
Freeware
.address
Weldam 2
5655 JG Eindhoven
Netherlands
.docs
READMEFIRST
PolyFit.guide
.described-by
Fred Fish (fnf@fishpond.cygnus.com)
.submittal
Submitted on disk directly by the author.
.contents
PolyFit		A program to fit straight lines, polynomes and exponentional
		curves to sets of points.  Can fit to polynomes of degree of
		16 and lower.  Calculated coefficients can be printed and saved.
		A graph of the points and curve can be shown (in any screen
		resolution), printed and saved as an IFF file.  Supports
		localization.  Version 1.21, OS2.0 and higher, freeware,
		binary only.
		Author: Camiel Rouweler
"""
    pi = ProductInfo(1000, 'PolyFit.lha', testdata)
    assert_pi_match(pi.records)

def test_pi_parse_file():
    pi = ProductInfo.loadfile(1000, os.path.join(os.path.dirname(__file__), 'PolyFit.lha.pi'))
    assert_pi_match(pi.records)

def assert_pi_match(parsed):
    assert parsed["name"] == "PolyFit"
    assert parsed["type"] == "Graphing"
    assert parsed["short"] == '"Method of least squares" line fitting'
    assert parsed["description"] == ("A program to fit straight lines, polynomes and exponentional curves to sets\n" +
        "of points.  Can fit to polynomes of degree of 16 and lower.  Calculated\n" +
        "coefficients can be printed and saved.  A graph of the points and curve can\n" +
        "be shown (in any screen resolution), printed and saved as an IFF file.\n" +
        "Supports localization.  Binary only.")
    assert parsed["version"] == "1.21"
    assert parsed["date"] == "1994.02.05"
    assert parsed["author"] == "Camiel Rouweler"
    assert parsed["requirements"] == "Requires OS 2.0+"
    assert parsed["distribution"] == "Freeware"
    assert parsed["address"] == "Weldam 2\n5655 JG Eindhoven\nNetherlands"
    assert parsed["docs"] == "READMEFIRST\nPolyFit.guide"
    assert parsed["described-by"] == "Fred Fish (fnf@fishpond.cygnus.com)"
    assert parsed["submittal"] == "Submitted on disk directly by the author."
    assert parsed["contents"] == """PolyFit		A program to fit straight lines, polynomes and exponentional
		curves to sets of points.  Can fit to polynomes of degree of
		16 and lower.  Calculated coefficients can be printed and saved.
		A graph of the points and curve can be shown (in any screen
		resolution), printed and saved as an IFF file.  Supports
		localization.  Version 1.21, OS2.0 and higher, freeware,
		binary only.
		Author: Camiel Rouweler"""

def test_pi_parse_latin1_not_ascii_file():
    "Assert that files with characters in the Latin-1 range are correctly converted to unicode"
    pi = ProductInfo.loadfile(158, os.path.join(os.path.dirname(__file__), 'MSDOS.lha.pi'))
    assert pi.records["author"] == "Frank Wübbeling "

def test_pi_to_search_index_entry():
    "Assert correct generation of search index entries"
    pi = ProductInfo.loadfile(1000, os.path.join(os.path.dirname(__file__), 'PolyFit.lha.pi'))
    parsed = pi.records
    search = pi.search_index_entry()
    assert search["object-type"] == "artifact"
    assert search["object-link"] == "libraries/fish/disks/1000#PolyFit"
    assert search["filename"] == "PolyFit.lha"
    assert search["content-type"] == "application/x-lha"
    assert search["name"] == "PolyFit"
    assert search["fish-type"] == "Graphing"
    assert search["short"] == '"Method of least squares" line fitting'
    assert search["description"] == ("A program to fit straight lines, polynomes and exponentional curves to sets\n" +
        "of points.  Can fit to polynomes of degree of 16 and lower.  Calculated\n" +
        "coefficients can be printed and saved.  A graph of the points and curve can\n" +
        "be shown (in any screen resolution), printed and saved as an IFF file.\n" +
        "Supports localization.  Binary only.")
    assert search["version"] == "1.21"
    assert search["date"] == "1994.02.05"
    assert search["author"] == "Camiel Rouweler"
    assert search["distribution"] == "Freeware"
    assert search["address"] == "Weldam 2\n5655 JG Eindhoven\nNetherlands"
    assert search["contents"] == """PolyFit		A program to fit straight lines, polynomes and exponentional
		curves to sets of points.  Can fit to polynomes of degree of
		16 and lower.  Calculated coefficients can be printed and saved.
		A graph of the points and curve can be shown (in any screen
		resolution), printed and saved as an IFF file.  Supports
		localization.  Version 1.21, OS2.0 and higher, freeware,
		binary only.
		Author: Camiel Rouweler"""