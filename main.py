import secrets
import string



def generate_password(size: int):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(size))
    return password
size = int(input('Enter size of password: '))





print(f"Твой новый пароль: {generate_password(size)}")