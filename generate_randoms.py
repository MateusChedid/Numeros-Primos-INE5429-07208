import csv
import time
import algorithms


        
if __name__ == "__main__":

    linear = algorithms.LinearCongruentialGenerator(3**4096)
    xorshift = algorithms.XorShiftGenerator(3**4096)

    random_linear_numbers = []
    random_xor_numbers = []

    n_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

    with open("csvs/Randoms/1 - LCG.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(["Algorithm", "n_bits_max", "n_bits", "Index", "Random_Number"])
        print("LCG")

        lcg_n_bits_dict = {}
        quantity = 1500
        for n in n_bits:
            avg = 0
            for i in range(quantity):
                start = time.perf_counter()
                random_number = linear.algorithm(n)
                end = time.perf_counter()
                avg += (end - start)
                writer.writerow(["LCG", n, random_number.bit_length(), i, random_number])
                random_linear_numbers.append(random_number)

            lcg_n_bits_dict.update({n: f'{(avg/quantity)*1000}'})

            print(f"n_bits: {n}, avg time: {(avg/quantity)*1000} ms")

    with open("csvs/Randoms/2 - XORSHIFT.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(["Algorithm", "n_bits_max", "n_bits", "Index", "Random_Number"])
        print("XORSHIFT")

        xor_n_bits_dict = {}
        
        quantity = 1500
        for n in n_bits:
            avg = 0
            for i in range(quantity):
                start = time.perf_counter()
                random_number = xorshift.algorithm(n)
                end = time.perf_counter()
                avg += (end - start)
                writer.writerow(["XORSHIFT", n, random_number.bit_length(), i, random_number])
                random_xor_numbers.append(random_number)

            xor_n_bits_dict.update({n: f'{(avg/quantity)*1000}'})

            print(f"n_bits: {n}, avg time: {(avg/quantity)*1000} ms")
    print("CSVs gerados ")


    with open("csvs/Randoms/3 - COMPARISON.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Algorithm", "Tamanho do Número", "Tempo para gerar"])
        for n in lcg_n_bits_dict:
            writer.writerow(["LCG", n, lcg_n_bits_dict[n]])
        for n in xor_n_bits_dict:
            writer.writerow(["XORSHIFT", n, xor_n_bits_dict[n]])
