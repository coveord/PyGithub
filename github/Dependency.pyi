from typing import Any, Dict

from github.GithubObject import NonCompletableGithubObject
from github.Package import Package

class Dependency(NonCompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def package(self) -> Package: ...
    @property
    def manifest_path(self) -> str: ...
    @property
    def scope(self) -> str: ...