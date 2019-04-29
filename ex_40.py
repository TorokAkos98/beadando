import numpy as np

def fixdeterminans(n):
    good = 0
    while good < n:
        matrix = np.random.randint(0,20,(2,2))
        det = (matrix[0][0]*matrix[1][1]) - (matrix[0][1]*matrix[1][0])
        if det > 10 and det < 20:
            print(matrix)
            print("Determinánsa=",det)
            print("\n")
            good = good+1
            continue

try:
    n = int(input("Hány darab mátrixot szeretnél? "))
    fixdeterminans(n)
except ValueError:
    print("Hibás bevitel!")
