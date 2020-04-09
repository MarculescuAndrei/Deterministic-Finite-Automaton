f = open("Source.txt", 'r')

poz = f.readline()
poz = poz[:-1]

Final = f.readline().split()
L = f.readline().split()

Adjacency = {}

while L:
    if L[0] not in Adjacency.keys():
        Adjacency[L[0]] = [(L[1], L[2])]
    else:
        Adjacency[L[0]].append((L[1], L[2]))
    L = f.readline().split()

Word = input("The word is: ")
Counter = 0

if Word == '':
    if poz in Final:
        print("The word is valid")
    else:
        print("The word is invalid")
else:
    for j in Word:
        Counter += 1
        Found = False
        if poz not in Adjacency.keys():
            print("The word is invalid")

            break
        else:
            for Arc in Adjacency[poz]:
                if j == Arc[1]:
                    poz = Arc[0]
                    Found = True
                    break
            if Found == False:
                print("The word is invalid")
                break
            elif j == Word[-1] and Counter > len(Word) - 1 and poz in Final:
                print("The word is valid")
                break
            elif j == Word[-1] and Counter > len(Word) - 1 and poz not in Final:
                print("The word is invalid")
                break
print(Adjacency)
f.close()
