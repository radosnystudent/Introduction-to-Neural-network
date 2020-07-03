from math import pow, log
import math
from random import random, randint

temperature = 1.0


def calculateCVector(z: list) -> list:
    """
    Function calculate vector based on given input vector
    @param: (list of floats) - list contains 0.0 and 1.0, size = 20
    @return: (list of floats) - calculated vector (list)
    """
    cVector = [[None for _ in range(20)] for _ in range(20)]
    for i in range(20):
        for j in range(20):
            if i != j:
                cVector[i][j] = (z[i] - 0.5)*(z[j] - 0.5)
            else:
                cVector[i][j] = 0.0
    return cVector


def calculateNextVector(prevVector: list, cVector: list) -> list:
    """
    Boltzman
    @param: (list of floats) - previous vector from this function (first can be randomly generated)
    @param: (list of floats) - cVecotr (calculated in function calculateCVector)
    @return: (list of floats) - calculated vector (list)
    """
    def calculateTheta(vector: list) -> float:
        """
        function calculate Theta
        @param: (list of floats) vector 
        @return: (float) calculated number
        """
        theta = 0.0
        for value in vector:
            theta += value
        return theta

    result = list()
    f_value = None

    for i in range(20):

        u_value = 0.0
        for j in range(20):
            w = 2*cVector[i][j]
            u_value += w * prevVector[j]
        u_value -= calculateTheta(cVector[i])

        f_value = (lambda u: 1.0 /
                   (1.0 + pow(math.e, -1.0 * (u / temperature))))(u_value)

        if f_value > randint(0, 10) * 1.0:
            result.append(1.0)
        else:
            result.append(0.0)
    return result


def decodeResult(vector: list) -> str:
    """
    Function coding vector of 0.0 and 1.0 to _ and *
    @param: (list) - vector of 0.0 and 1.0
    @return: (str) - coded vector of numbers
    """
    string = f''

    for ind, value in enumerate(vector):
        if value == 0.0:
            string += '_ '
        else:
            string += '* '
        if ind in [3, 7, 11, 15, 19]:
            string += '\n'
    #string += '\n'
    return string


z = [0.0 if i < 10 else 1.0 for i in range(20)]

cVector = calculateCVector(z)
xVector = [randint(0, 1) * 1.0 for _ in range(20)]
print(decodeResult(xVector))

xVector = calculateNextVector(xVector, cVector)
print(f'temperatura: {temperature}\n')
print(decodeResult(xVector))
