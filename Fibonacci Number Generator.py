N = int(input("Enter N: "))

def fib_gen(n):
    a, b = 0, 1
    if n > 0:
      for _ in range(n):
          yield a
          a, b = b, a + b
    else:
      for _ in range(-n):
          yield -a
          a, b = -b, -a - b

print (list(fib_gen(N)))