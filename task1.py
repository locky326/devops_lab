Year = int(input())
print( Year % 4 == 0 or (Year % 400 == 0 and 0 != Year % 100))
