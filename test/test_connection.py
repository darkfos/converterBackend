from aiosqlite import Connection
import pytest


@pytest.mark.asyncio
async def test_connection(engine: Connection) -> None:
    assert engine.is_alive() is True, "Не удалось подключиться к БД"
