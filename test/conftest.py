import pytest
import aiosqlite
from typing import Final


URL_DB: Final[str] = "testdb.db"

@pytest.fixture(autouse=True, scope="session")
async def work_db() -> None:
    yield
    connection = await aiosqlite.connect(database=URL_DB)
    await connection.execute("DROP TABLE IF EXISTS users")
    await connection.execute("DROP TABLE IF EXISTS usertype")
    await connection.execute("DROP TABLE IF EXISTS history")
    await connection.close()


@pytest.fixture(scope="session")
async def engine() -> aiosqlite.Connection:
    connection = aiosqlite.connect(database=URL_DB)
    async with connection as conn:
        yield conn