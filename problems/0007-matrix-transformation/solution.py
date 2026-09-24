import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

	A, T, S = np.array(A), np.array(T), np.array(S)

	for M in (T, S):
		det = np.linalg.det(M)
		if len(M) != len(M[1]) or det == 0:
			return -1 

	transformed_matrix = np.linalg.inv(T) @ A @ S

	return transformed_matrix