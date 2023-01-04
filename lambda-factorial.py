import math


test = lambda number: 'exponential wins' if (2**number > math.factorial(number)) else 'factorial wins'
print(test(400))
print(math.factorial(400))
