import bcrypt


class Password:
    @staticmethod
    def crypt_pass(password: str) -> bytes:
        hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return hash

    @staticmethod
    def check_pass(password: str, hash: bytes) -> bool:
        return bcrypt.checkpw(password.encode(), hash)
