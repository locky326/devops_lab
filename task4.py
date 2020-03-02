Com = []
a = int(input())

for i in range(a):
    res = input().split()
    if res[0] == "insert":
        Com.insert(int(res[1]), int(res[2]))
    elif res[0] == "print":
        print(Com)
    elif res[0] == "remove":
        Com.remove(int(res[1]))
    elif res[0] == "append":
        Com.append(int(res[1]))
    elif res[0] == "sort":
        Com.sort()
    elif res[0] == "pop":
        Com.pop()
    elif res[0] == "reverse":
        Com.reverse()
