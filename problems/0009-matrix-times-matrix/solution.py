import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    ma = len(a)
    na = len(a[0])

    mb = len(b)
    nb = len(b[0])

    if na != mb:
        return -1

    a = np.array(a)
    b = np.array(b)

    return a @ b



