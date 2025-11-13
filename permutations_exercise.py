import math
import numpy as np

S = np.array([15, 24, np.array([])])

n = S.size
k = int(input("Please input the K value"))


permutations = math.factorial(n) / math.factorial(n-k)

print(permutations)