x = 0
for n in range(int(input("Int value: "))):
    a = input("++ or --: ")
    if a == ("x++") or a == ("++x"):    x+=1
    elif a == ("x--") or a == ("--x"):  x-=1
    else: print("Invalid input")
print(x)

