from ntpath import join


cookies = ['user_id=11357', 'user_group_id=11', 'user_permissions="1,24"']
solz = 'Ezm9hsTwmgeU5rEx29C3gQBfWUdZA6'
import hashlib


def sing_cookie(cookie: list[str], sol: str) -> str:
    array = cookie[:]
    array.sort()
    array.append(sol)
    print(array)
    return(hashlib.sha256(";".join(array).encode())).hexdigest()



print(sing_cookie(cookie=cookies, sol=solz))