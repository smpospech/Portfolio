# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries
import math
import numpy as np


class Dft:
    def __init__(self):
        pass

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""
        rows = matrix.shape[0]
        cols = matrix.shape[1]
        result = np.zeros(matrix.shape, dtype=complex)
        N = 15

        for i in range(0, rows):
            for j in range(0, cols):
                u, v = 0, 0
                if(u <= 14 and v <= 14):
                    result[i][j] = (math.cos(((2 * math.pi) / N) * (u*i + v*j)) - 1j * math.sin(((2 * math.pi) / N) * (u*i + v*j)))
                    u+=1
                    v+=1

        return result

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        You can implement the inverse transform formula with or without the normalizing factor.
        Both formulas are accepted.
        takes as input:
        matrix: a 2d matrix (DFT) usually complex
        returns a complex matrix representing the inverse fourier transform"""
        rows = matrix.shape[0]
        cols = matrix.shape[1]
        result = np.zeros(matrix.shape, dtype=complex)
        N = 15

        for i in range(0, rows):
            for j in range(0, cols):
                u, v = 0, 0
                if (u <= 14 and v <= 14):
                    result[i][j] = (math.cos(((2 * math.pi) / N) * (u * i + v * j)) + 1j * math.sin(((2 * math.pi) / N) * (u * i + v * j)))
                    u+=1
                    v+=1

        return result

    def magnitude(self, matrix):
        """Computes the magnitude of the input matrix (iDFT)
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the complex matrix"""
        rows = matrix.shape[0]
        cols = matrix.shape[1]

        magMat = np.zeros(matrix.shape, dtype=complex)

        for u in range(rows):
            for v in range(cols):
                if(matrix[u][v] < 0):
                    magMat = matrix[u][v] * -1
                else:
                    magMat = matrix[u][v] * 1

        return magMat