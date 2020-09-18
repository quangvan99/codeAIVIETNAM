from functools import reduce
import math

# e = 1 + 1/1! + 1/2! + ...
n = 40
# e = 1 + reduce((lambda x,y:x + 1/math.factorial(y)), range(n))
e = sum([1/math.factorial(i) for i in range(n)])
print(e)