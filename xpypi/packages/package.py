from xpypi.files.file import File


class Package:
    """
    Class representing a Python package (containing a name, a version, and a collection of files).
    """

    def __init__(self, name: str, version: str):
        self._name = name
        self._version = version

        self._files = set()

    @property
    def name(self) -> str:
        return self._name

    @property
    def version(self) -> str:
        return self._version

    def insert_file(self, new_file: File):
        self._files.add(new_file)
