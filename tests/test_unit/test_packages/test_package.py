from unittest import TestCase

from xpypi.files.file import File
from xpypi.packages.package import Package


class PackageTest(TestCase):

    def setUp(self):
        self.name = "package_name"
        self.version = "1.0.0"

        self.package = Package(self.name, self.version)

    def test_name(self):
        self.assertEqual(self.name, self.package.name)

    def test_version(self):
        self.assertEqual(self.version, self.package.version)

    def test_files(self):
        self.assertSetEqual(set(), self.package.files)

    def test_insert_file(self):
        self.package.insert_file(File('file_name.txt', b'file_contents'))

        self.assertSetEqual({File('file_name.txt', b'file_contents')}, self.package.files)
