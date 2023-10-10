# car can walk 1, 2 or 3 m
# R(0) = 0
# R(1) = 1
# R(2) = 2
# R(3) = 4

def car(n):
    if n == 0 or n == 1 or n == 2 or n == 3:
        return n
    
    return car(n-1)+car(n-2)+car(n-3)


print(car(5))