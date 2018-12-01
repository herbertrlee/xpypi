from unittest import TestCase

from xpypi.files.file import File


class FileTest(TestCase):

    def setUp(self):
        self.file_name = "file.txt"
        self.file_contents = b'file_contents'

        self.file = File(self.file_name, self.file_contents)

    def test_name(self):
        self.assertEqual(self.file_name, self.file.name)

    def test_contents(self):
        self.assertEqual(self.file_contents, self.file.contents)

    def test_hash(self):
        expected_hash = hash((self.file_name, self.file_contents))

        self.assertEqual(expected_hash, self.file.__hash__())

    def test_eq(self):
        other_file = File(self.file_name, self.file_contents)
        self.assertEqual(other_file, self.file)
