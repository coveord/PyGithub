from typing import Any, Dict

from github.GithubObject import NonCompletableGithubObject
from github.NamedUser import NamedUser

class SecretScanningAlert(NonCompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def created_at(self) -> str: ...
    @property
    def html_url(self) -> str: ...
    @property
    def locations_url(self) -> str: ...
    @property
    def number(self) -> str: ...
    @property
    def push_protection_bypassed(self) -> str: ...
    @property
    def push_protection_bypassed_at(self) -> str: ...
    @property
    def push_protection_bypassed_by(self) -> NamedUser: ...
    @property
    def resolution(self) -> str: ...
    @property
    def resolution_comment(self) -> str: ...
    @property
    def resolved_at(self) -> str: ...
    @property
    def resolved_by(self) -> NamedUser: ...
    @property
    def secret(self) -> str: ...
    @property
    def secret_type(self) -> str: ...
    @property
    def secret_type_display_name(self) -> str: ...
    @property
    def state(self) -> str: ...
    @property
    def url(self) -> str: ...
