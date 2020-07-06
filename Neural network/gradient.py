from math import pow

# stała c i eps
c_const: float = 0.01
eps_const: float = 0.0000001

# Funkcja przyjmuje dwa argumenty
# wejscie:
#   inputVec - wektor poczatkowy
#   functionNumber - numer funkcji, ktorej minimum chcemy szukac (1 lub 2)
# wyjscie:
#   wypisanie wartosci funkcji


def gradient(inputVec: list, functionNumber: int) -> str:
    """
    Function calculate gradient
    @param: (list) - function's arguments (size = 2)
    @param: (int) - 1 or 2, which function wanna calculate
    @return: (str) - string message with function value
    """

    newVector: list = [0.0, 0.0]

    while True:
        localVec = inputVec[:]  # tworzenie kopii wektora

        if functionNumber == 1: # obliczanie wartosci jesli badamy funkcje 1
            # stała c przemnożona przez pochodna dla x1 funkcji pierwszej
            newVector[0] = inputVec[0] - c_const * \
                (lambda vector: 4*vector[0] - 2*vector[1] - 2)(inputVec)
            # stała c przemnożona przez pochodna dla x2 funkcji pierwszej
            newVector[1] = inputVec[1] - c_const * \
                (lambda vector: 2*vector[1] - 2*vector[0])(inputVec)

        elif functionNumber == 2: # obliczanie wartosci jesli badamy funkcje 2        
            # stała c przemnożona przez pochodna dla x1 funkcji drugiej
            newVector[0] = inputVec[0] - c_const * (lambda vector: 2*pow(
                vector[0], 3) - pow(vector[0], 2) - vector[0])(inputVec)
            # stała c przemnożona przez pochodna dla x2 funkcji drugiej
            newVector[1] = inputVec[1] - c_const * \
                (lambda vector: 2*vector[1] - 2)(inputVec)

        inputVec = localVec

        # obliczenie wartosci max potrzebnej do sprawdzenia warunku stopu
        maxVart = 0.0
        for i, value in enumerate(newVector):
            if abs(value - inputVec[i]) > maxVart:
                maxVart = abs(value - inputVec[i])

        # sprawdzenie warunku stopu, jeśli spełniony to wypisujemy wynik w zależności która funkcje sprawdzalismy
        if maxVart < eps_const:
            if functionNumber == 1:
                return f'Dla parametrów: x1 = {newVector[0]}, x2 = {newVector[1]}, funkcja F1 ma wartość: {round(2*pow(newVector[0],2) + pow(newVector[1],2) - 2*newVector[0]*newVector[1] - 2*newVector[1] + 1,4)}'
            elif functionNumber == 2:
                return f'Dla parametrów: x1 = {newVector[0]}, x2 = {newVector[1]}, funkcja F2 ma wartość: {round(pow(newVector[0],4)/2 - pow(newVector[0],3)/3 - pow(newVector[0],2)/2 + pow(newVector[1],2) - 2*newVector[1] + 1, 4)}'

        inputVec = newVector


# print(gradient([ , ], 1)) # minimum lokalne funkcji 1 ... ?
print(gradient([1.0, 1.0], 1))  # minimum globalne funkcji 1
print(gradient([-0.5, 1.0], 2))  # minimum lokalne funkcji 2
print(gradient([1.0, 1.0], 2))  # minimum globalne funkcji 2
