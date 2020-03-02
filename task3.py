def lin(s):
    l = []
    if s.find('=') != -1:
        l.append('=')
        ss = s.split('=')
    else:
        print('ERROR')
        exit()
    if ss[0].find('-') != -1:
        l.append('-')
        sss = ss[0].split('-')
    elif ss[0].find('+') != -1:
        l.append('+')
        sss = ss[0].split('+')
    elif ss[0].find('*') != -1:
        l.append('*')
        sss = ss[0].split('*')
    elif ss[0].find('/') != -1:
        l.append('/')
        sss = ss[0].split('/')
    else:
        print('ERROR')
        exit()
    sss.append(ss[1])
    for i in sss:
        if i.isdigit():
            l.append(int(i))
        else:
            print('ERROR')
            exit()
    return l


oper = lin(input())

if len(oper) != 5:
    print("ERROR")
elif oper[0] != "=":
    print("ERROR")
elif oper[1] == "*":
    if oper[2] * oper[3] == oper[4]:
        print("YES")
    else:
        print("NO")
elif oper[1] == "/":
    if oper[2] / oper[3] == oper[4]:
        print("YES")
    else:
        print("NO")
elif oper[1] == "+":
    if oper[2] + oper[3] == oper[4]:
        print("YES")
    else:
        print("NO")
elif oper[1] == "-":
    if oper[2] - oper[3] == oper[4]:
        print("YES")
    else:
        print("NO")
else:
    print("ERROR")
