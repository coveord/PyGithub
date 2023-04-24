from typing import Any, Dict

from github.GithubObject import NonCompletableGithubObject

class SecretScanningPushProtection(NonCompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def status(self) -> str: ...
