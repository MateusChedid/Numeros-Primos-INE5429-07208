import prime_algorithms

pseudo_primos = [
    341, 561, 645, 1105, 1387, 1729, 1905, 2047, 2465, 2701,
    2821, 3277, 4033, 4681, 5461, 6601, 7957, 8321, 8481, 8911,
    10261, 10585, 11305, 12801, 13741, 13747, 13981, 14491, 15709, 15841,
    16705, 18721, 18705, 19951, 20005, 20341, 21601, 22901, 23377, 25761,
    29341, 30121, 30889, 31621, 31685, 33153, 34945, 35333, 39865, 41041
]

for num in pseudo_primos:
    if prime_algorithms.Fermat(num,5).is_prime() and not prime_algorithms.MillerRabin(num,10).is_prime():
        print(f"For Fermat, {num} is probably a prime number, but for Miller-Rabin, it is not.")
    elif not prime_algorithms.Fermat(num,5).is_prime() and prime_algorithms.MillerRabin(num,10).is_prime():
        print(f"For Miller-Rabin, {num} is probably a prime number, but for Fermat, it is not.")
