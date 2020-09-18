<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 16:33:34 2020

@author: Admin
"""
from functools import reduce

# x1 = (x0 + N/x0)/2

iterator = 20
N = 9

quadratic = reduce((lambda x,_: (x + N/x)/2.0), [N/2,*range(iterator)])
print(quadratic)
=======
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 16:33:34 2020

@author: Admin
"""
from functools import reduce

# x1 = (x0 + N/x0)/2

numIterator = 20
N = 9

quadratic = reduce((lambda x,_: (x + N/x)/2.0), [N/2,*range(numIterator)])
print(quadratic)
>>>>>>> b33c5c4e00ff8965739c1cc7a0ee310f5f713d8e
