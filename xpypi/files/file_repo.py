from abc import ABC, abstractmethod

from xpypi.files.file import File


class FileRepository(ABC):
    """
    Interface for interacting with files.
    """

    @abstractmethod
    def save_file(self, file_obj: File):
        """
        Implement this method to save a file.
        :param file_obj: File that will be saved.
        :return: Void
        """
        pass

    @abstractmethod
    def get_file(self, file_name: str) -> File:
        """
        Implement this method to get a File by name.
        :param file_name: Name of the file.
        :return: File object.
        """
        pass
