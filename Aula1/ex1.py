def f1(n):
    n+=1
    print("f1: ---------------------------------")
    print("n\tResult\t\t#Iter")
    r = 0
    it = 0
    for i in range(1, n):
        print(str(i-1) + "\t" + str(r) + "\t\t" + str(it))
        r += i
        it += 1
    print()
    return r

def f2(n):
    print("f2: ---------------------------------")
    print("n\tResult\t\t#Iter")
    r = 0
    it = 0
    for i in range(1, n):
        for j in range(1, n):
            r += i
            it+=1
        print(str(i-1) + "\t" + str(r) + "\t\t" + str(it))
    print()
    return r

def f3(n):
    n+=1
    print("f3: ---------------------------------")
    print("n\tResult\t\t#Iter")
    r = 0
    it = 0
    for i in range(1, n):
        for j in range(i, n):
            r+=1
            it+=1
        print(str(i-1) + "\t" + str(r) + "\t\t" + str(it))
    print()
    return r

def f4(n):
    n+=1
    print("f4: ---------------------------------")
    print("n\tResult\t\t#Iter")
    r = 0
    it = 0
    for i in range(1, n):
        for j in range(1, i):
            r+=j
            it+=1
        print(str(i-1) + "\t" + str(r) + "\t\t" + str(it))
    print()
    return r

x = int(input("select a number: \n"))
print()

f1(x)
f2(x)
f3(x)
f4(x)