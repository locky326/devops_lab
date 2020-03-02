List1 = input().split()
List2 = input().split()
Out = list(set(List1) & set(List2))
Out.sort()
for i in Out:
    print(i, end=' ')
