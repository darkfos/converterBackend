from enum import Enum
from typing import Final


class AuthEnum(Enum):
    CREATE: Final[str] = "create"
    UPDATE: Final[str] = "update"
    DECODE: Final[str] = "decode"

    # Decode
    ACCESS: Final[str] = "access"
    REFRESH: Final[str] = "refresh"
