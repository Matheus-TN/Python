n=0
for x in range(int(input("Insira a qntde de problemas: "))):
    s = input("Enter 0 or 1: ")
    n = n+1 if(s=="110")or(s=="101")or(s=="011")or(s=="111") else n
print(n)