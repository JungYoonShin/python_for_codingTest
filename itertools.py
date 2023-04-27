#순열(순서o)
from itertools import permutations
data = ['a', 'b', 'c']
result = list(permutations(data, 3)) 

#조합(순서x)
from itertools import combinations
data = ['a', 'b', 'c']
result = list(combinations(data, 2))

#순열(순서o, 중복o)
from itertools import product
data = ['a', 'b', 'c']
result = list(product(data, repeat=2))
