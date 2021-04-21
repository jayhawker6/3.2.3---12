print("1 to 5 inclusive:")
print()
a = 1
while a != 6:
    print(a)
    a += 1
a = 10
print()
print("10 to 1 inclusive:")
print()
while a != 0:
    print(a)
    a -= 1
print()
print("Even numbers from 2 to 10 inclusive:")
print()
a = 2
while a != 12:
    print(a)
    a += 2
print()
print("Odd numbers from 9 down to 1 inclusive:")
print()
a = 9
while a > 0:
    if (a % 2) != 0:
        print(a)
    a -= 1