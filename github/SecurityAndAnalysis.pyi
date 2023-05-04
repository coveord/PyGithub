from typing import Any, Dict

from github.AdvancedSecurity import AdvancedSecurity
from github.GithubObject import NonCompletableGithubObject
from github.SecretScanning import SecretScanning
from github.SecretScanningPushProtection import SecretScanningPushProtection

class SecurityAndAnalysis(NonCompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def advanced_security(self) -> AdvancedSecurity: ...
    @property
    def secret_scanning(self) -> SecretScanning: ...
    @property
    def secret_scanning_push_protection(self) -> SecretScanningPushProtection: ...
