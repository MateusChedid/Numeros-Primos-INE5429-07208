def lcg(seed, a=1664525, c=1013904223, m=2**4096):
    next_numer = (a * seed + c) % m
    return next_numer


if __name__ == "__main__":

    seed = 123456789
    new_seed = lcg(seed)

    for i in range(1000):
        random_number = lcg(new_seed)
        new_seed = random_number
        print(f"{i}, size: {random_number.bit_length()}")
        
