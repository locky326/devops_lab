import re

inp = str(input())
oper = re.split('\D', inp)
symb = re.split('\d', inp)
symbol = list(filter(None, symb))

if len(oper) != 3:
    print("ERROR")
elif symbol[1] != "=":
    print("ERROR")
elif symbol[0] == "*":
    if (int(oper[0]) * int(oper[1])) == int(oper[2]):
        print("YES")
    else:
        print("NO")
elif symbol[0] == "/":
    if (int(oper[0]) / int(oper[1])) == int(oper[2]):
        print("YES")
    else:
        print("NO")
elif symbol[0] == "+":
    if (int(oper[0]) + int(oper[1])) == int(oper[2]):
        print("YES")
    else:
        print("NO")
elif symbol[0] == "-":
    if (int(oper[0]) - int(oper[1])) == int(oper[2]):
        print("YES")
    else:
        print("NO")
else:
    print("ERROR")
