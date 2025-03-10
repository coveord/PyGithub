############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Thomas Cooper <coopernetes@proton.me>                         #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

from __future__ import annotations

from typing import Any

import github.DependabotAlert
import github.Repository
from github.GithubObject import Attribute, NotSet


class OrganizationDependabotAlert(github.DependabotAlert.DependabotAlert):
    """
    This class represents a Dependabot alert on an organization.

    The reference can be found here
    https://docs.github.com/en/rest/dependabot/alerts#list-dependabot-alerts-for-an-organization

    The OpenAPI schema can be found at
    - /components/schemas/dependabot-alert-with-repository

    """

    def _initAttributes(self) -> None:
        super()._initAttributes()
        self._repository: Attribute[github.Repository.Repository] = NotSet

    @property
    def repository(self) -> github.Repository.Repository:
        return self._repository.value

    def _useAttributes(self, attributes: dict[str, Any]) -> None:
        super()._useAttributes(attributes)
        if "repository" in attributes:
            self._repository = self._makeClassAttribute(github.Repository.Repository, attributes["repository"])
