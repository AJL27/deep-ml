import numpy as np
import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	matrix = np.array(matrix)

	trace = matrix[0][0] + matrix[1][1]
	det = matrix[0][0] * matrix[1][1] - matrix[0][1]*matrix[1][0]


	eigenvalues = []

	eigenvalues.append(trace/2 + math.sqrt((trace**2)/4 - det))
	eigenvalues.append(trace/2 - math.sqrt((trace**2)/4 - det))

	return eigenvalues
