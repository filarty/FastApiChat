import string

import bcrypt


class Password:
    @staticmethod
    def crypt_pass(password: str) -> bytes:
        hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return hash

    @staticmethod
    def check_pass(password: str, hash: bytes) -> bool:
        return bcrypt.checkpw(password.encode(), hash)

    @staticmethod
    def valid_pass(password: str) -> bool:
        result = [any([i.isupper() for i in password]),
                  any([i.islower() for i in password]),
                  any([i.isdigit() for i in password]),
                  all([i not in string.whitespace for i in password]),
                  any([i in string.punctuation for i in password])]
        return all(result)


if __name__ == "__main__":
    print(Password.valid_pass("ddawd12A" "$%@!a"))