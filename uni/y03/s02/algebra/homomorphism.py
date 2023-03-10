# Gets all values that g(1) can take, for g: Z/pZ -> Z/qZ
p = 6
q = 66
print([ x for x in range(q) if p * x % q == 0 and x == x**2 % q])


