from aiosqlite import Connection
import pytest


@pytest.mark.asyncio
async def test_create_table_user_type(engine: Connection):
    await engine.execute(sql="""
    CREATE TABLE IF NOT EXISTS UserType (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_type VARCHAR(120) UNIQUE);
    """)
    await engine.execute(sql="""
    INSERT INTO UserType (name_type) VALUES ('user'), ('admin')
    ON CONFLICT DO NOTHING
    """)

    req = await engine.execute("SELECT * from usertype")
    assert len(await req.fetchall()) == 2, "Таблица тип пользователя не была создана"


@pytest.mark.asyncio
async def test_create_table_user(engine: Connection):
    await engine.execute(sql="""
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_user_type INTEGER,
    email VARCHAR(200) UNIQUE,
    username VARCHAR(125),
    hashed_password BYTEA,
    avatar TEXT,
    FOREIGN KEY (id_user_type) REFERENCES UserType (id) ON DELETE CASCADE
    );
    """)


@pytest.mark.asyncio
async def test_create_table_history(engine: Connection):
    await engine.execute(sql="""
    CREATE TABLE IF NOT EXISTS History (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_operation VARCHAR(255),
    date_operation DATE
    );
    """)