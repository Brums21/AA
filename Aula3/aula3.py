#Brute-force comparison
def bf(lista):
    even = 0
    comp = 0
    for element in lista:
        if element%2 == 0:
            even += 1
        comp+=1
    return even, comp


lista = [2**a for a in range(10)]
#print(lista)
print("BRUTE FORCE: \n")
print("Elements\t\tCOMPS\t\t#Even-Values")
print("---------------------------------------------------------------")
for element in lista:
    list = [a for a in range(element)]
    even, comp = bf(list)
    print(str(len(list)) + "\t\t\t" + str(comp) + "\t\t" + str(even))

print()
print()
print()
print("Divide and conquer: \n")
print("Elements\t\tCOMPS\t\t#Even-Values")
print("---------------------------------------------------------------")
