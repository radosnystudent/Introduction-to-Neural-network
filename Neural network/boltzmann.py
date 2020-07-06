from math import pow, log
import math
from random import random, randint, getrandbits

temperature: float = 1.0


def generateCVector(z: list) -> list:
    """
    Function generate vector based on given input vector
    @param: (list of floats) - list contains 0.0 and 1.0, size = 20
    @return: (list of floats) - generated vector (list)
    """

    return [[0.0 if i != j else (z[i] - 0.5)*(z[j] - 0.5) for j in range(20)] for i in range(20)]


def calculateNextVector(prevVector: list, cVector: list) -> list:
    """
    Boltzman
    @param: (list of floats) - previous vector from this function (first can be randomly generated); size = 20
    @param: (list of floats) - cVecotr (generated in function generateCVector); size = 20
    @return: (list of floats) - calculated vector (list); size = 20
    """

    result: list = list()
    f_value: any = None

    for i in range(20):

        u_value = 0.0

        # obliczanie wag, potrzebnych do wyliczenia wartości u
        for j in range(20):
            w = 2*cVector[i][j]
            u_value += w * prevVector[j]
        # odjęcie wartości progowej, która jest sumą wartości wektora C[i]
        u_value -= sum(cVector[i])

        # obliczenie wartości funkcji f dla argumentu u
        f_value = (lambda u: 1.0 /
                   (1.0 + math.exp(u / temperature)))(u_value)

        # jeśli temperatura jest większa od 1.0, MB działa losowo,
        # w przypadku gdy jest mniejsza od 1.0 działa według sieci Hopfielda

        if temperature >= 1.0:
            if f_value > randint(0, 10) * 1.0:
                result.append(1.0)
            else:
                result.append(0.0)
        else:
            if u_value > 0.0:
                result.append(1.0)
            elif u_value < 0.0:
                result.append(0.0)
    return result


def decodeResult(vector: list) -> str:
    """
    Function coding 0.0 to  and 1.0 to ■
    @param: (list) - vector of 0.0 and 1.0
    @return: (str) - coded vector of numbers
    """

    return ' '.join([u"\u25A1" if value == 0.0 else u"\u25A0" for value in vector])


if __name__ == '__main__':

    z: list = [0.0 if i < 10 else 1.0 for i in range(20)]

    cVector = generateCVector(z)
    xVector: list = [randint(0, 1) * 1.0 for _ in range(20)]
    print(f'początkowy: {decodeResult(xVector)}\n')

    for _ in range(10):
        temperature = randint(1, 50) / 10
        xVector = calculateNextVector(xVector, cVector)
        print(decodeResult(xVector))
        print(f'temperatura: {temperature}\n')
