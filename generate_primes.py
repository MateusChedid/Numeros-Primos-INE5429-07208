import csv
import time
import algorithms


        
if __name__ == "__main__":

    linear = algorithms.LinearCongruentialGenerator(3**4096)
    xorshift = algorithms.XorShiftGenerator(3**4096)

    n_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

    with open("csvs/Primes/1 - LCG.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(["Algorithm", "n_bits_max", "n_bits", "Random_Number"])
        print("LCG")

        lcg_n_bits_dict = {}
        for n in n_bits:
            avg = 0
            tries = 0
            primo = False
            start = time.perf_counter()
            while not primo:
                random_number = linear.algorithm(n)
                primo = algorithms.MillerRabin(random_number).is_prime()
                tries += 1
            end = time.perf_counter()
            total_time = end - start
            avg = total_time / tries
            writer.writerow(["LCG", n, random_number.bit_length(), random_number])
            lcg_n_bits_dict.update({n: f'{avg*1000}'})
            print(f"n_bits: {n}, avg time: {avg*1000} ms, total time: {total_time*1000} ms, tries: {tries}")



    with open("csvs/Primes/2 - XORSHIFT.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(["Algorithm", "n_bits_max", "n_bits", "Random_Number"])
        print("XORSHIFT")

        xor_n_bits_dict = {}
        for n in n_bits:
            avg = 0
            tries = 0
            primo = False
            start = time.perf_counter()
            while not primo:
                random_number = xorshift.algorithm(n)
                primo = algorithms.MillerRabin(random_number).is_prime()
                tries += 1
            end = time.perf_counter()
            total_time = end - start
            avg = total_time / tries
            writer.writerow(["XORSHIFT", n, random_number.bit_length(), random_number])
            xor_n_bits_dict.update({n: f'{avg*1000}'})
            print(f"n_bits: {n}, avg time: {avg*1000} ms, total time: {total_time*1000} ms, tries: {tries}")
        
    print("CSVs gerados ")


    with open("csvs/Primes/3 - COMPARISON.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Algorithm", "Tamanho do Número", "Tempo para gerar"])
        for n in n_bits:
            writer.writerow(["LCG", n, lcg_n_bits_dict[n]])
        for n in n_bits:
            writer.writerow(["XORSHIFT", n, xor_n_bits_dict[n]])
