Dia = input().split()
a = []


def Test(arg):
    z = 0
    for i in arg:
        if (i != '0' and int(arg) % int(i) == 0):
            z += 1
        else:
            return "0"
    if z == len(arg):
        return arg
    else:
        return "0"


j = int(Dia[0])
while j <= int(Dia[1]):
    if Test(str(j)) != "0":
        a.append(j)
    j += 1
print(a)
