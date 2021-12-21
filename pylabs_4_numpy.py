import numpy as np

# 1
a=np.sum(np.arange(0,100))
print(a)

# 2
x=int(input('сумма ряда до числа:'))
b=np.sum(np.arange(0,x))
print(b)

# 3
sredn_100 = np.mean(np.random.random(100))
print(sredn_100)
