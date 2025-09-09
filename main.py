class RandomNumberGenerator:

    def __init__(self, seed):
        self.seed = seed

    def lcg(self, n_bits):

        a=1664525675676356575
        c=10139042356735633458623 

        m = 1 << n_bits

        x = self.seed
        self.seed = (a * x + c) % m

        return self.seed
    
    def xorshift(self, n_bits):

        mask = (1 << n_bits) - 1  

        x = self.seed & mask
        x ^= (x << 34) & mask
        x ^= (x >> 167) & mask
        x ^= (x << 56) & mask
        self.seed = x & mask

        return self.seed


if __name__ == "__main__":

    seed = 21412413123
    print(seed.bit_length())
    rng = RandomNumberGenerator(seed)
    r = int(input("LCG(1) XOR(2): "))

    n_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

    if r == 1:
        print("LCG")
        # LCG loop
        for n in n_bits:
            print(f"n_bits: {n}")
            for i in range(10):
                random_number = rng.lcg(n)
                print(f"{i} -> {str(random_number)[:5]}..., size: {random_number.bit_length()}")
            print('\n')
    else:
        print("XORSHIFT")
        # Xorshift loop
        for n in n_bits:
            print(f"n_bits: {n}")
            for i in range(10):
                random_number = rng.xorshift(n)
                print(f"{i} -> {str(random_number)[:5]}..., size: {random_number.bit_length()}")
                # print(f"{i} -> {random_number}, size: {random_number.bit_length()}")
            print('\n')
