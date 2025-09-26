import csv
import time
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
        # self.seed |= (1 << (n_bits - 1))
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

        # self.seed |= (1 << (n_bits - 1))
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



if __name__ == "__main__":

    linear = LinearCongruentialGenerator(3**4096)
    xorshift = XorShiftGenerator(3**4096)

    n_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    # n_bits = [40]


    # Abrindo arquivo CSV para escrita
    with open("1 - LCG.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        # Cabeçalho
        writer.writerow(["Algorithm", "n_bits_max", "n_bits", "Index", "Random_Number"])
        print("LCG")
        lcg_n_bits_dict = {}
        for n in n_bits:
            avg = 0
            for i in range(1):
                start = time.perf_counter()
                random_number = linear.algorithm(n)
                miller_rabin = MillerRabin(random_number)
                while not miller_rabin.is_prime():
                    random_number = linear.algorithm(n)
                    miller_rabin = MillerRabin(random_number)
                end = time.perf_counter()
                avg += (end - start)
                writer.writerow(["LCG", n, random_number.bit_length(), i, random_number])

            lcg_n_bits_dict.update({n: f'{(avg/10000)*1000:.2f}'})

            print(f"n_bits: {n}, avg time: {(avg/10000)*1000:.2f} ms")


    with open("2 - XORSHIFT.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        # Cabeçalho
        writer.writerow(["Algorithm", "n_bits_max", "n_bits", "Index", "Random_Number"])
        print("XORSHIFT")
        xor_n_bits_dict = {}
        for n in n_bits:
            avg = 0
            for i in range(10):
                start = time.perf_counter()
                random_number = xorshift.algorithm(n)
                miller_rabin = MillerRabin(random_number)
                while not miller_rabin.is_prime():
                    random_number = xorshift.algorithm(n)
                    miller_rabin = MillerRabin(random_number)
                end = time.perf_counter()
                avg += (end - start)
                writer.writerow(["XORSHIFT", n, random_number.bit_length(), i, random_number])
        
            xor_n_bits_dict.update({n: f'{(avg/100000)*1000:.2f}'})

            print(f"n_bits: {n}, avg time: {(avg/1000000)*1000:.2f} ms")
    print("CSVs gerados ")

    with open("3 - COMPARISON.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        # Cabeçalho
        writer.writerow(["Algorithm", "Tamanho do Número", "Tempo para gerar"])
        for n in n_bits:
            writer.writerow(["LCG", n, lcg_n_bits_dict[n]])
        for n in n_bits:
            writer.writerow(["XORSHIFT", n, xor_n_bits_dict[n]])
