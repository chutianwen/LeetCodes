import numpy as np
from collections import Counter
p = np.random.randint(1, 11, (10,))
p = np.array([10, 1, 1, 1, 1, 1, 1, 1, 1, 1])
p = p.astype(np.float32)
print(p)
p /= np.sum(p)
print(p)

# pick two based on the probablity
# [p(0), p(1), ... p(9)]
pick = np.random.choice(p.size, 30, p=p)
pick += 1
print(pick)
cnts = Counter(pick)
cnts_sorted = sorted(cnts, key=cnts.get, reverse=True)
print(cnts)