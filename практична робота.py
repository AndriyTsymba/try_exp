# практична
class InvaLidUserNameError(Exception):
    def __int__(self,username):
        self.username = username
def register_user(username):
    if len(username) <5:
        raise InvaLidUserNameError(username)
    else:
        print("Все зареєстровано")
try:
    username = input("Ведіть імя корстувача")
    register_user(username)
except InvaLidUserNameError as e:
        print(f"Неправильне ім'я користувача{e.username}","мінімум символів")
class InvalidSimvolsError(Exception):
    def __init__(self,username):
        self.username = username
def register_user(usermane):
    invalide_simvols = ["!","@","#","%","&","*"]
    for i in invalide_simvols:
        if i in usermane:
            raise InvaLidUserNameError(username)
try:
    register_user("jagdgys!@jfgd")
except InvaLidUserNameError as e:
    print(f"ведено не правильно ім'я{e.username},треба без символів")

