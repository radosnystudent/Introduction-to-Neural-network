from math import pow, log
import math
from random import random, randint

temperature = 1.0


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
    @param: (list of floats) - previous vector from this function (first can be randomly generated)
    @param: (list of floats) - cVecotr (calculated in function calculateCVector)
    @return: (list of floats) - calculated vector (list)
    """

    result = list()
    f_value = None

    for i in range(20):

        u_value = 0.0
        for j in range(20):
            w = 2*cVector[i][j]
            u_value += w * prevVector[j]
        u_value -= sum(cVector[i])  # calculate Theta

        f_value = (lambda u: 1.0 /
                   (1.0 + pow(math.e, -1.0 * (u / temperature))))(u_value)

        if f_value > randint(0, 10) * 1.0:
            result.append(1.0)
        else:
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

    z = [0.0 if i < 10 else 1.0 for i in range(20)]

    cVector = generateCVector(z)
    xVector = [randint(0, 1) * 1.0 for _ in range(20)]
    print(f'początkowy: {decodeResult(xVector)}\n')

    for _ in range(10):
        xVector = calculateNextVector(xVector, cVector)
        print(decodeResult(xVector))
        print(f'temperatura: {temperature}\n')
