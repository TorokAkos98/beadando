abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","+"]

try:
    n = int(input("Adj meg egy számot(1-26): "))
    if n>26 or n<1:
        print("Hibás bevitel!")
        exit()
except ValueError:
    print("Hibás bevitel!")
    exit()

usedletters = abc[0:n+1]
usedletters = usedletters[::-1]

for i in range(1,n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i):
        print(usedletters[j],end=" ")
    for i in range(i,0,-1):
        print(usedletters[i],end=" ")
    print("\n")

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i):
        print(usedletters[j],end=" ")
    for i in range(i,0,-1):
        print(usedletters[i],end=" ")
    print("\n")
