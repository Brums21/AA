def exp_bt(a,b):
    #brute force
    if b == 0:
        return 1, 0
    
    res, mult = exp_bt(a, b-1)

    return a*res, mult+1

def exp_dq(a,b):
    #divide and conquer
    if b == 0:
        return 1, 0

    if b == 1:
        return a, 0
    
    res1, mult1 = exp_dq(a, b//2)
    res2, mult2 = exp_dq(a, (b+1)//2)

    return res1*res2, mult+1

def exp_decq(a,b):
    #decrease and conquer
    if b == 0:
        return 1, 0

    if b%2 == 0: #b is even
        res, mult1 = exp_decq(a, b//2)
        return res*res, mult1+1
    else:        #b is odd
        res, mult2 = exp_decq(a, (b-1)//2)
        return res*res*a, mult2+2

print("BRUTE FORCE: \n")
print("n\t\t2**n\t\t#Mults")
print("-----------------------------------------")
for a in range(21):
    res, mult = exp_bt(2, a)
    print(str(a) + "\t\t" + str(res) + "\t\t" + str(mult))
    
print()
print()
print("DIVIDE AND CONQUER: \n")
print("n\t\t2**n\t\t#Mults")
print("-----------------------------------------")
for a in range(20):
    res, mult = exp_dq(2, a)
    print(str(a) + "\t\t" + str(res) + "\t\t" + str(mult))

print()
print()
print("DECREASE AND CONQUER: \n")
print("n\t\t2**n\t\t#Mults")
print("-----------------------------------------")
for a in range(20):
    res, mult = exp_decq(2, a)
    print(str(a) + "\t\t" + str(res) + "\t\t" + str(mult))