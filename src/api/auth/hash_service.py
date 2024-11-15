import bcrypt


class HashService:

    @classmethod
    async def hash_password(cls, password):
        return bcrypt.hashpw(password=password.encode("utf-8"), salt=bcrypt.gensalt())

    @classmethod
    async def verify_password(cls, password, old_password):
        return bcrypt.checkpw(password=password, hashed_password=old_password)