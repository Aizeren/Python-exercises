import numpy as np

def pi(N):
  r = 1
  arrX = np.random.rand(N)
  arrY = np.random.rand(N)
  arrR = (arrX[:]**2 + arrY[:]**2) <= r**2
  N_circ = arrR.sum()
  return 4*N_circ/N

for n in [100, 1000, 10000, 100000, int(1e+6)]:
  print(pi(n))