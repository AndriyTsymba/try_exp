# теорія
try:
    print("start coded")
    print(error)
    print("end code")
except:
    print("no prodlems")
print("any code..")
#2
def cheker(val_1):
    if type(val_1) != str:
        raise TypeError(f"sorry,we can't work with{type(val_1)}, на треба str")
    else:
        return val_1
a = "1234"
cheker(a)
#3
class BuildingHouseErorr(Exception):
    def __str__(self):
        return "Щось не те  багото матеріалу"
def cheker_material_built(amount,limit):
    if amount > limit:
        return "Достатньо матеріалів"
    else:
       raise BuildingHouseErorr()
print(cheker_material_built(123,567))
