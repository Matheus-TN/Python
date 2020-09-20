a = input("Enter the first string: ").lower()
b = input("Enter the second string: ").lower()
if len(a) == len(b):
    if a>b: print(1)
    elif a==b: print(0)
    else: print(-1)
elif a>b: print(1)
else: print(-1)
