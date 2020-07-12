from math import pow

# stała c i epsilon
c_const: float = 0.01
eps_const: float = 0.0000001


def derivativeFirstX(vector: list) -> float:
    return (lambda vector: 4 * vector[0] - 2 * vector[1] - 2)(vector)


def derivativeFirstY(vector: list) -> float:
    return (lambda vector: 2 * vector[1] - 2 * vector[0])(vector)


def derivativeSecondX(vector: list) -> float:
    return (lambda vector: 2 * pow(vector[0], 3) - pow(vector[0], 2) - vector[0])(vector)


def derivativeSecondY(vector: list) -> float:
    return (lambda vector: 2 * vector[1] - 2)(vector)


def calculateMax(inputVec: list, newVector: list) -> float:
    maxVart = 0.0
    for i, value in enumerate(newVector):
        if (newMax := abs(value - inputVec[i]) > maxVart):
            maxVart = newMax
    return maxVart


def gradient(inputVec: list, functionNumber: int) -> str:
    """
    Funkcja przyjmuje dwa argumenty:
    wejscie:
        inputVec - wektor poczatkowy
        functionNumber - numer funkcji, ktorej minimum chcemy szukac (1 lub 2)
    wyjscie:
        wypisanie wartosci funkcji
    """

    newVector: list = [0.0, 0.0]

    while True:
        localVec: list = inputVec[:]  # tworzenie kopii wektora

        if functionNumber == 1:
            """
            obliczanie wartosci jesli badamy pierwsza funkcje
            stała c przemnożona przez pochodna dla x1 funkcji pierwszej
            """
            newVector[0] = inputVec[0] - c_const * derivativeFirstX(inputVec)
            """
            stała c przemnożona przez pochodna dla x2 funkcji pierwszej
            """
            newVector[1] = inputVec[1] - c_const * derivativeFirstY(inputVec)

        elif functionNumber == 2:
            """
            obliczanie wartosci jesli badamy druga funkcje
            stała c przemnożona przez pochodna dla x1 funkcji drugiej
            """
            newVector[0] = inputVec[0] - c_const * derivativeSecondX(inputVec)
            """
            stała c przemnożona przez pochodna dla x2 funkcji drugiej
            """
            newVector[1] = inputVec[1] - c_const * derivativeSecondY(inputVec)

        inputVec: list = localVec

        # obliczenie wartosci max potrzebnej do sprawdzenia warunku stopu
        # sprawdzenie warunku stopu, jeśli spełniony to wypisujemy wynik
        if calculateMax(inputVec, newVector) < eps_const:
            if functionNumber == 1:
                return (
                    f"Dla parametrów: x1 = {newVector[0]}, x2 = {newVector[1]},"
                    + f"funkcja F1 ma wartość: {round(2*pow(newVector[0],2) + pow(newVector[1],2) - 2*newVector[0]*newVector[1] - 2*newVector[1] + 1,4) + 0}"
                )
            elif functionNumber == 2:
                return (
                    f"Dla parametrów: x1 = {newVector[0]}, x2 = {newVector[1]},"
                    + f"funkcja F2 ma wartość: {round(pow(newVector[0],4)/2 - pow(newVector[0],3)/3 - pow(newVector[0],2)/2 + pow(newVector[1],2) - 2*newVector[1] + 1, 4) + 0}"
                )

        inputVec = newVector


if __name__ == "__main__":
    print(f"stała c: {c_const}, stała epsilon: {eps_const}")
    print(gradient([3.0, 5.0], 1))  # minimum lokalne funkcji 1
    print(gradient([1.0, 1.0], 1))  # minimum globalne funkcji 1
    print(gradient([-0.5, 1.0], 2))  # minimum lokalne funkcji 2
    print(gradient([1.0, 1.0], 2))  # minimum globalne funkcji 2
