from enum import Enum
from typing import Final, List


class APIRoutersData(Enum):

    # API V1
    API_V1_PREFIX: Final[str] = "/api/v1"
    API_V1_TAGS: Final[List[str]] = ["API/V1"]

    # Auth
    AUTH_PREFIX: Final[str] = "/auth"
    AUTH_TAGS: Final[list[str]] = ["Auth"]

    # User
    USER_ROUTER_PREFIX: Final[str] = "/user"
    USER_ROUTER_TAGS: Final[List[str]] = ["User"]

    # UserType
    USER_TYPE_ROUTER_PREFIX: Final[str] = "/user_type"
    USER_TYPE_ROUTER_TAGS: Final[List[str]] = ["User Type"]

    # History
    HISTORY_ROUTER_PREFIX: Final[str] = "/history"
    HISTORY_ROUTER_TAGS: Final[List[str]] = ["History"]
