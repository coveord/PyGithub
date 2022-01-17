from typing import Any, Dict, List, Union

from github.CheckRun import CheckRun
from github.CheckSuite import CheckSuite
from github.CommitCombinedStatus import CommitCombinedStatus
from github.CommitComment import CommitComment
from github.CommitStats import CommitStats
from github.CommitStatus import CommitStatus
from github.File import File
from github.GitCommit import GitCommit
from github.GithubObject import CompletableGithubObject, _NotSetType
from github.NamedUser import NamedUser
from github.PaginatedList import PaginatedList
from github.PullRequest import PullRequest

class Commit(CompletableGithubObject):
    def __repr__(self) -> str: ...
    @property
    def _identity(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def author(self) -> NamedUser: ...
    @property
    def comments_url(self) -> str: ...
    @property
    def commit(self) -> GitCommit: ...
    @property
    def committer(self) -> NamedUser: ...
    def create_comment(
        self,
        body: str,
        line: Union[int, _NotSetType] = ...,
        path: Union[_NotSetType, str] = ...,
        position: Union[int, _NotSetType] = ...,
    ) -> CommitComment: ...
    def create_status(
        self,
        state: str,
        target_url: Union[_NotSetType, str] = ...,
        description: Union[_NotSetType, str] = ...,
        context: Union[_NotSetType, str] = ...,
    ) -> CommitStatus: ...
    @property
    def files(self) -> List[File]: ...
    def get_check_suites(
        self,
        app_id: Union[_NotSetType, int]=...,
        check_name: Union[_NotSetType, str]=...,
    ) -> PaginatedList[CheckSuite]: ...
    def get_combined_status(self) -> CommitCombinedStatus: ...
    def get_comments(self) -> PaginatedList[CommitComment]: ...
    def get_statuses(self) -> PaginatedList[CommitStatus]: ...
    def get_pulls(self) -> PaginatedList[PullRequest]: ...
    def get_check_runs(
        self,
        check_name: Union[_NotSetType, str] = ...,
        status: Union[_NotSetType, str] = ...,
        filter: Union[_NotSetType, str] = ...,
    ) -> PaginatedList[CheckRun]: ...
    @property
    def html_url(self) -> str: ...
    @property
    def parents(self) -> List[Commit]: ...
    @property
    def sha(self) -> str: ...
    @property
    def stats(self) -> CommitStats: ...
    @property
    def url(self) -> str: ...
