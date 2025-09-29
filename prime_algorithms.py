import random
import math

class MillerRabin:
    def __init__(self, n, rounds=5):
        self.n = n
        self.rounds = rounds

    # Passo 1: decompor n-1 na forma 2^k * m
    def find_k_m(self):

        #Decompõe n-1 em fatores de 2: n-1 = 2^k * m, com m ímpar.
        #Retorna:
        #    k (int): Expoente de 2.
        #    m (int): Parte ímpar da decomposição.

        n1 = self.n - 1
        k = 0
        m = n1
        while m % 2 == 0:
            k += 1
            m //= 2
        return k, m

    # Passo 2: escolha de uma base aleatória
    def chosen_a(self):

        #Escolhe uma base aleatória a no intervalo [2, n-2].
        return random.randint(2, self.n - 2)

    # Passo 3: execução do teste de Miller-Rabin
    def is_prime(self):
        # Casos triviais
        if self.n < 2:
            return False
        if self.n in [2, 3]:
            return True
        if self.n % 2 == 0:
            return False

        # Decomposição de n-1 = 2^k * m
        k, m = self.find_k_m()

        # Repetição do teste para várias bases aleatórias
        for _ in range(self.rounds):
            a = self.chosen_a()                # base aleatória
            b = pow(a, m, self.n)              # cálculo de a^m mod n

            # Condição 1: se b == 1 ou b == n-1, passa nessa rodada
            if b == 1 or b == self.n - 1:
                continue

            # Condição 2: verificar se existe algum r tal que a^(2^r*m) ≡ -1 (mod n)
            for _ in range(k - 1):
                b = pow(b, 2, self.n)          # elevar ao quadrado sucessivamente
                if b == self.n - 1:            # se encontrou n-1, passa
                    break
            else:
                # Se não achou 1 nem -1, n é definitivamente composto
                return False

        # Se passou em todas as rodadas, n é um provável primo
        return True


class Fermat:
    def __init__(self, n, rounds=5):
        self.n = n
        self.rounds = rounds

    def chosen_a(self):
        #Escolhe uma base aleatória a no intervalo [2, n-2].
        return random.randint(2, self.n - 2)

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
        for _ in range(self.rounds):
            a = self.chosen_a() 

            # se não for coprimo, já é composto
            if math.gcd(a, n) != 1:
                return False
            if pow(a, n - 1, n) != 1:
                return False  # não satisfaz o teorema de Fermat → composto

        return True  # provavelmente primo

        
