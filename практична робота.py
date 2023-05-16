# практична
#3
class InvalidFileFormatError (Exception):
    def __init__(self, f):
        self.f = f
#FilleNotFoundError
#UnsupportedFormatError - коли немає розширення .txt

def read_file(f):
    try:
        with open(f, "r") as file:
            content = file.read()
            print("Вміст файлу:", content)
    except IOError:
        raise InvalidFileFormatError(f)

try:
    read_file(input("Введіть назву файлу: "))
except InvalidFileFormatError as e:
    print(f'Невірний формат файлу {e.f}'
          f'підтримуються тільки текстові файли')
