import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

	n1 = [len(a[1])]
	n2 = [len(b)]

	if n1 != n2:
		return -1

	matrix_a = np.array(a)
	matrix_b = np.array(b)

	return matrix_a @ matrix_b