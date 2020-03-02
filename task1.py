Year = int(input())
if Year % 4 != 0 or (Year % 400 != 0 and Year % 100 == 0):
    print("False")
else:
    print("True")
