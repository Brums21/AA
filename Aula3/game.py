import random as rand

def play_game():
    guess = rand.randint(1, 100)

    max = 100
    min = 1
    num_att = 0
    while (True):
        attempt = rand.randint(min,max)
        num_att += 1
        if guess == attempt:
            return num_att
        elif guess < attempt:
            max = attempt
            continue
        else:
            min = attempt
            continue

lista = [10**(i+1) for i in range(5)]
print(lista)
for n in lista:
    print("Simulation: playing the higher-lower game " + str(n) + " times ")
    print("The interval of values is [1, 100]")
    dict = {} #initialize the dictionary 
    for i in range(n):
        num_attempts = play_game()
        if num_attempts not in dict.keys():
            dict.update({num_attempts : 1})
        else:
            dict[num_attempts] += 1 

    lista = list(dict.keys())
    lista.sort()
    mydict = {i: dict[i] for i in lista}
    for key in mydict.keys():
        txt = "\t {} attempts: \t {:10} - {:>.2f}%".format(key, dict[key], (dict[key]/n)*100)
        print(txt)
