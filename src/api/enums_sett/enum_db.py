from enum import Enum
from typing import Final


class UserRole(Enum):
    USER_ROLE: Final[int] = 1
    ADMIN_ROLE: Final[int] = 2