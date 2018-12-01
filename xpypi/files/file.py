class File:
    """
    A file inside a package.
    """

    def __init__(self, name: str, contents: bytes):
        self._name = name
        self._contents = contents

    @property
    def name(self) -> str:
        return self._name

    @property
    def contents(self) -> bytes:
        return self._contents

    def __hash__(self):
        return hash((self._name, self._contents))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
