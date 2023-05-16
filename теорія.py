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
        raise TypeError(f"sorry,we can't work with{type(val_1)}, на тркба str")
    else:
        return val_1
a = "1234"
cheker(a)