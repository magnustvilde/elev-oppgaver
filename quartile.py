from pylab import quantile as q

numbers = [1,4,6,9,2,5,6,2,2,5,6,1,0,0,2,5,6,3,4,3]

q1 = q(numbers,1/4)
q2= q(numbers,2/4)
q3 = q(numbers,3/4)

print(f'Q(1): {q1}')
print(f'Q(2): {q2}')
print(f'Q(3): {q3}')