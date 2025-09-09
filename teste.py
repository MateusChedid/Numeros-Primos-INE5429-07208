import csv

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


if __name__ == "__main__":

    linear = LinearCongruentialGenerator(3**4096)
    xorshift = XorShiftGenerator(5)

    n_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    # n_bits = [40]


    # Abrindo arquivo CSV para escrita
    with open("1 - LCG.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        # Cabeçalho
        writer.writerow(["Algorithm", "n_bits_max", "n_bits", "Index", "Random_Number"])

        print("LCG")
        for n in n_bits:
            for i in range(10):
                random_number = linear.algorithm(n)
                writer.writerow(["LCG", n, random_number.bit_length(), i, random_number])

    with open("2 - XORSHIFT.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        # Cabeçalho
        writer.writerow(["Algorithm", "n_bits_max", "n_bits", "Index", "Random_Number"])
        print("XORSHIFT")
        for n in n_bits:
            for i in range(10):
                random_number = xorshift.algorithm(n)
                writer.writerow(["XORSHIFT", n, random_number.bit_length(), i, random_number])

    print("CSVs gerados ")
