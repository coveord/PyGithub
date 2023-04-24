from typing import Any, Dict

from github.GithubObject import NonCompletableGithubObject

class AdvancedSecurity(NonCompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def status(self) -> str: ...
