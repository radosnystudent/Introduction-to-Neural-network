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

# rozmmiar wektorów
N: float = 20

def generateCVector(z: list) -> list:
    """
    wektor początkowy
    """

    return [
        [0.0 if i == j else (z[i] - 0.5) * (z[j] - 0.5) for j in range(N)]
        for i in range(N)
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
    return sum([wVector[row][j] * prevVector[j] for j in range(N)]) - thetaVector[row]


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

    for i in range(N):
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

    temperatures: list = [0.1, 1.5, 4.0, 20.0]
    temperatureIndex = 0

    z: list = [0.0 if i < 10 else 1.0 for i in range(N)]

    cVector: list = generateCVector(z)
    xVector: list = [randint(0, 1) * 1.0 for _ in range(N)]

    wVector: list = calculateW(cVector)
    thetaVector: list = calculateTheta(cVector)
    print(f"początkowy: {decodeResult(xVector)}\n")

    for i in range(N):
        xVector: list = calculateNextVector(xVector, wVector, thetaVector, temperatures[temperatureIndex])
        if i % 5 == 0:
            print(f'temperatura: {temperatures[temperatureIndex]}')
            if temperatureIndex + 1 < len(temperatures):
                temperatureIndex += 1
        print(decodeResult(xVector))
