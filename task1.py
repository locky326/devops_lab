Year = int(input())
print(not((Year % 4 != 0) or (Year % 400 != 0 and Year % 100 == 0)))
