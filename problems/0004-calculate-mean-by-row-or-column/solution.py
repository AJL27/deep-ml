import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	

	output = []

	if mode == 'row':
		for i in matrix:
			output.append(sum(i)/len(i))
		return output

	elif mode == 'column':
		matrix = np.array(matrix)
		for i in matrix.T:
			output.append(sum(i)/len(i))
		return output

	
	else:
		return []
	
	return means
		