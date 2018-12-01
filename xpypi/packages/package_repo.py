from abc import ABC, abstractmethod
from typing import List

from xpypi.packages.package import Package


class PackageRepository(ABC):
    """
    Interface for interacting with packages.
    """

    @abstractmethod
    def upsert_package(self, package: Package):
        """
        Insert or update a package.
        :param package: New or updated package that will be saved to the repository.
        :return: Void
        """
        pass

    @abstractmethod
    def get_package(self, name: str) -> Package:
        """
        Get the most up-to-date version of a package.
        :param name: Name of the package to get.
        :return: Package.
        """
        pass

    @abstractmethod
    def get_versioned_package(self, name: str, version: str) -> Package:
        """
        Get a specific version of a package.
        :param name: Name of the package to get.
        :param version: Version of the package to get.
        :return: Package
        """
        pass

    @abstractmethod
    def list_packages(self) -> List[str]:
        """
        List the names of all packages.
        :return: List of package names.
        """
        pass

    @abstractmethod
    def list_package_versions(self, name: str) -> List[str]:
        """
        List all the versions for a package.
        :param name: Package name.
        :return: List of package versions.
        """
        pass
