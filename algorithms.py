import random

class LinearCongruentialGenerator:
    def __init__(self, seed):
        self.seed = seed

    def algorithm(self, n_bits):
        a = 7**89
        c = 22
        m = 1 << n_bits

        x = self.seed
        self.seed = (a * x + c) % m
        return self.seed



class XorShiftGenerator:
    def __init__(self, seed):
        self.seed = seed

    def algorithm(self, n_bits):
        mask = (1 << n_bits) - 1  

        x = self.seed & mask
        x ^= (x << 13) & mask
        x ^= (x >> 17) & mask
        x ^= (x << 5) & mask
        self.seed = x & mask

        return self.seed


class MillerRabin:
    def __init__(self, n, k=5):
        """
        n: número a ser testado
        k: número de iterações do teste, mais iterações = maior confiabilidade
        """
        self.n = n
        self.k = k

    def is_prime(self):
        n = self.n
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False

        # Escrevendo n-1 como 2^r * d
        d = n - 1
        r = 0
        while d % 2 == 0:
            d //= 2
            r += 1

        # Testes de Miller-Rabin
        for _ in range(self.k):
            a = random.randrange(2, n - 1)
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True