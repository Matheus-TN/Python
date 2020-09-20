for x in range((int(input("Insira a quantidade de palavras: ")))):
    s = input("Insira as palavras: ")
    print(s[0]+str(len(s)-2)+s[-1]) if len(s)>10 else print(s)