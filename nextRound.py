n = input("n participantes: ")
k = input("k score: ")
n1 = n.split(" ")
k1 = k.split(" ")
a = k1[int(n1[-1])]
count = 0
for i in k1:
    count = count+1 if((a < i) or(a==i)) else count
print(count)