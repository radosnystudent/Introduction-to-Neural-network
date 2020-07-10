from math import pow, log, exp
from random import random, randint


'''
Im mniejsza jest temperatura tym bardziej maszyna Boltzmanna dąży do sieci Hopfielda,
a dla wysokich temperatur maszyna Boltzmana jest procesem Markowa.

T - temperatura
1) dla T >> 0 maszyna Boltzmana działa losowo
2) dla niewielkich T Maszyna Boltzmana działa według sieci Hopfielda:
1.0 , gdy u(t) > 0
0.0 , gdy u(t) < 0
'''


def generateCVector(z: list) -> list:
    """
    wektor początkowy
    """

    return [
        [0.0 if i == j else (z[i] - 0.5) * (z[j] - 0.5) for j in range(20)]
        for i in range(20)
    ]


def calculateTheta(cVector: list) -> list:
    """
    obliczanie parametru theta
    """
    return [sum(row) for row in cVector]


def calculateW(cVector: list) -> list:
    """
    liczenie macierzy wag
    """
    return [[2 * value for value in row] for row in cVector]


def calculateUvalue(
    prevVector: list, row: int, wVector: list, thetaVector: list
) -> float:
    """
    wartosc u - suma (wektor wag razy stan) - wartosc theta
    """
    return sum([wVector[row][j] * prevVector[j] for j in range(20)]) - thetaVector[row]


def calculateF(u: float, temperature: float) -> float:
    """
    wartosc F dla argumentów u i temperatury
    """
    return (lambda u: 1.0 / (1.0 + exp(-u / temperature)))(u)


def calculateNextVector(
    prevVector: list, wVector: list, thetaVector: list, temperature: float
) -> list:
    """
    generowanie nastepnego stanu maszyny boltzmana
    """

    result: list = list()

    for i in range(20):
        # jeśli temperatura jest większa od 1.0, MB działa losowo,
        # w przypadku gdy jest mniejsza od 1.0 działa według sieci Hopfielda

        if (
            calculateF(
                calculateUvalue(prevVector, i, wVector, thetaVector), temperature
            ) >= random()
        ):
            result.append(1.0)
        else:
            result.append(0.0)

    return result


def decodeResult(vector: list) -> str:
    """
    kodowanie wektora do znaków: 0.0 ->  i 1.0 -> ■
    """

    return " ".join(["\u25A1" if value != 1.0 else "\u25A0" for value in vector])


if __name__ == "__main__":

    temperature: float = 0.1

    z: list = [0.0 if i < 10 else 1.0 for i in range(20)]

    cVector: list = generateCVector(z)
    xVector: list = [randint(0, 1) * 1.0 for _ in range(20)]

    wVector: list = calculateW(cVector)
    thetaVector: list = calculateTheta(cVector)
    print(f"początkowy: {decodeResult(xVector)}\n")

    for _ in range(10):
        xVector: list = calculateNextVector(xVector, wVector, thetaVector, temperature)
        print(decodeResult(xVector))
