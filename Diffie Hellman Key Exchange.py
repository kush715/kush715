import random
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def primitive_root(p):
    primitive_roots = []
    for i in range(2, p):
        if is_prime(i):
            s = set()
            for j in range(1, p):
                s.add(pow(i, j, p))
            if len(s) == p - 1:
                primitive_roots.append(i)
    return primitive_roots
def diffie_hellman(p, g):
    a = random.randint(2, p - 1)
    b = random.randint(2, p - 1)
    A = pow(g, a, p)
    B = pow(g, b, p)
    K1 = pow(B, a, p)
    K2 = pow(A, b, p)
    return K1, K2
p = 23  # Example prime number
g = primitive_root(p)[0]  # Example primitive root modulo p
K1, K2 = diffie_hellman(p, g)
print("Shared secret key for Alice:", K1)
print("Shared secret key for Bob:", K2)
