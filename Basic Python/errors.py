if True
    print("Missing colon")  # SyntaxError

def func():
    print("Improper indentation")  # IndentationError

print(undeclared_variable)  # NameError

print(5 + "string")  # TypeError

int("abc")  # ValueError

lst = [1, 2, 3]
print(lst[5])  # IndexError

d = {"a": 1}
print(d["b"])  # KeyError

lst = [1, 2, 3]
lst.appended(4)  # AttributeError

print(10 / 0)  # ZeroDivisionError

import non_existent_module  # ModuleNotFoundError

open("non_existent_file.txt")  # FileNotFoundError

raise RuntimeError("This is a runtime error")  # RuntimeError

