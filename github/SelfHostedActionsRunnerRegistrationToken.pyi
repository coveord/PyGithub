from datetime import datetime
from typing import Any, Dict

import github.GithubObject

class SelfHostedActionsRunnerRegistrationToken(github.GithubObject.NonCompletableGithubObject):
    @property
    def token(self) -> str: ...
    @property
    def expires_at(self) -> datetime: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
