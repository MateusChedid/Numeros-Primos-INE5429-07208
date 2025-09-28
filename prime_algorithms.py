import random
import math

class MillerRabin:
    def __init__(self, n, rounds=5):
        self.n = n
        self.rounds = rounds

    #Passo 1
    def find_k_m(self):
        #n-1 = 2^k * m
        n1 = self.n - 1
        k = 1
        m = n1 // 2**k
        while m % 2 == 0:
            k += 1
            m = n1 // 2**k
        return k, int(m)
    
    #Passo 2
    def chosen_a(self):
        return random.randint(2, self.n - 2)
    
    #Passo 3
    def is_prime(self):
        if self.n < 2:
            return False
        if self.n in [2, 3]:
            return True
        if self.n % 2 == 0:
            return False
        
        k, m = self.find_k_m()

        for _ in range(self.rounds):
            a = self.chosen_a()
            b = pow(a, m, self.n)
            if b == 1 or b == self.n - 1:
                continue
            for _ in range(k - 1):
                b = pow(b, 2, self.n)
                if b == self.n - 1:
                    break
            else:
                return False
        return True  

class Fermat:
    def __init__(self, n, k=5):
        """
        n: número a ser testado
        k: número de iterações (mais = maior confiabilidade)
        """
        self.n = n
        self.k = k

    def is_prime(self):
        n = self.n

        # Casos triviais
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False

        # Teste de Fermat
        for _ in range(self.k):
            a = random.randrange(2, n - 1)
            # se não for coprimo, já é composto
            if math.gcd(a, n) != 1:
                return False
            if pow(a, n - 1, n) != 1:
                return False  # não satisfaz o teorema de Fermat → composto

        return True  # provavelmente primo