from typing import List

from xpypi.files.file_repo import FileRepository
from xpypi.packages.package import Package
from xpypi.packages.package_repo import PackageRepository


class Application:
    """
    Main PyPi application.
    """

    def __init__(self, package_repo: PackageRepository, file_repo: FileRepository):
        self._package_repo = package_repo
        self._file_repo = file_repo

    def list_packages(self) -> List[str]:
        return self._package_repo.list_packages()

    def list_package_versions(self, package_name: str) -> List[str]:
        return self._package_repo.list_package_versions(package_name)

    def get_package(self, package_name: str, package_version: str) -> Package:
        return self._package_repo.get_package(package_name, package_version)

    
