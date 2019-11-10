#
# MIT License
#
# Copyright (c) 2019 Keisuke Sehara
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

"""tests the schemata in the 'schema' directory."""

import unittest
import json
import sys
from pathlib import Path

import jsonschema as js
import jsonref as jr

DEFAULT_SCHEMA_DIR = Path("schema")
DEFAULT_TESTS_DIR  = Path("schema_tests")

def resolve_file_uri(path):
    if not path.is_absolute():
        import os
        path = Path(os.getcwd()) / path
    return path.as_uri()

def is_special_part(item):
    for chr in ('/', '\\', '.'):
        if chr in item:
            return True
    return False

def file_stem(path):
    stem = path.stem
    try:
        return stem[:stem.index('.')]
    except:
        return stem

def as_test_name(path):
    path = Path(path)
    valid_parts = [item for item in path.parent.parts if not is_special_part(item)][1:]
    valid_parts.append(file_stem(path))
    return '_'.join(valid_parts)

class TestContext:
    def __init__(self, datafile, schemafile):
        self.datafile   = Path(datafile)
        self.schemafile = Path(schemafile)

        if not self.datafile.exists():
            raise FileNotFoundError(f"JSON file not found: {datafile}")
        if not self.schemafile.exists():
            raise FileNotFoundError(f"schema file not found: {schemafile}")

        with open(schemafile, 'r') as src:
            self.schema     = json.load(src)
            self.resolver   = js.RefResolver(resolve_file_uri(self.schemafile), self.schema)
        with open(datafile, 'r') as src:
            self.dataroot   = jr.JsonRef.replace_refs(json.load(src),
                            base_uri=resolve_file_uri(self.datafile))

    def validate(self, elem):
        js.validate(elem, self.schema, resolver=self.resolver)

test_format = """
class testclass_{test_name}(unittest.TestCase):
    def setUp(self):
        self.context = TestContext({testfile}, {schemafile})

    def test_valid(self):
        for i, elem in enumerate(self.context.dataroot['valid']):
            with self.subTest(i=i):
                self.context.validate(elem)

    def test_invalid(self):
        for i, elem in enumerate(self.context.dataroot['invalid']):
            with self.subTest(i=i):
                with self.assertRaises(js.exceptions.ValidationError):
                    self.context.validate(elem)
"""

def _generate_test_case(schemafile, testfile):
    test_name = as_test_name(schemafile)
    exec(test_format.format(test_name=test_name,
                            testfile=repr(str(testfile)),
                            schemafile=repr(str(schemafile))), globals(), globals())

def parse_tests(schemadir=None, testsdir=None):
    schemadir = Path(DEFAULT_SCHEMA_DIR if schemadir is None else schemadir)
    testsdir  = Path(DEFAULT_TESTS_DIR if testsdir is None else testsdir)
    for testfile in testsdir.iterdir():
        schemafile = schemadir / testfile.name
        if not schemafile.exists():
            print(f"*** no corresponding schema file for: {testfile}", file=sys.stderr)
            continue
        if testfile.is_file():
            if testfile.suffix == '.json':
                print(f"adding test for: {schemafile}", file=sys.stderr)
                _generate_test_case(schemafile, testfile)
        elif testfile.is_dir():
            parse_tests(schemadir=schemafile, testsdir=testfile)

if __name__ == '__main__':
    parse_tests()
    unittest.main()
