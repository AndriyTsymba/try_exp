# практична
#2
class InvalidPassworld(Exception):
    def __int__(self, passworld):
        self.passwold = passworld
def valide_passworld(passworld):
    if len(passworld) < 8:
        raise InvalidPassworld(passworld)
try:
    passworld = input("Ведіть пароль")
    valide_passworld(passworld)
    print("пароль ведененно")
except InvalidPassworld as e:
    print(f"Неправильний пароль {e.passwold}, мінімум 8 значеннь")
class InvalidPasswordError(Exception):
 def __init__(self, password):
    self.password = password
def validate_password(password):
    german_chars = ['ä', 'ö', 'ü', 'ß']
    if german_chars in password:
            raise InvalidPasswordError(password)
try:
    password = input('Введіть пароль: ')
    validate_password(password)
    print('Пароль веденено правильно')
except InvalidPasswordError as e:
        print(f'Неправильний пароль: {e.password}')
