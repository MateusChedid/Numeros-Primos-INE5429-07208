import csv
import time
import random_algorithms
import prime_algorithms
import matplotlib.pyplot as plt
import os
import math

        
if __name__ == "__main__":

    def to_superscript_10(n):
        exponent = int(math.log10(n))
        sup = str(exponent).translate(str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹"))
        return f"10{sup}"

    def plot_histogram(data, num_iterations, bins=100, title="Histogram", save_path=None):
        max_val = max(data)
        data = [x / max_val for x in data]  # normaliza para 0–1

        plt.hist(data, bins=bins, edgecolor='black', color="darkblue", linewidth=0.25)
        plt.title(title)
        plt.xlabel("Normalized Numbers")
        plt.ylabel(f"Frequency over {to_superscript_10(num_iterations)} iterations")
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        if save_path:
            # Cria diretório se não existir
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            plt.savefig(f"{save_path}/{title}.png", dpi=300)  # dpi ajusta a resolução

        plt.close()  # Fecha a figura para não mostrar ou ocupar memória

    action = int(input("Escolha a ação:\n1 - Gerar apenas números aleatórios\n2 - Gerar números primos\nOpção: "))

    if action == 1:
        random_option = int(input("Escolha o gerador de números aleatórios:\n1 - LCG\n2 - XORSHIFT\n3- Ambos\nOpção: "))

    elif action == 2:
        random_option = int(input("A verificação de primo será feita com números gerados pelo:\n1 - LCG\n2 - XORSHIFT\nOpção: "))
        prime_option = int(input("Escolha o teste de primalidade:\n1 - Miller-Rabin\n2 - Fermat\n3- Ambos\nOpção: "))
        if random_option not in [1, 2] or prime_option not in [1, 2, 3]:
            print("Valor inválido")
            exit()
    else:
        print("Valor inválido")
        exit()

    n_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]
    quantity = 10**5

    if random_option == 1 or random_option == 3:
        linear = random_algorithms.LinearCongruentialGenerator(2**27)
        random_linear_numbers = []
        with open("csvs/main_csvs/Randoms/ 1 - LCG.csv", mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=";")
            writer.writerow(["Algorithm", "n_bits_max", "n_bits", "Index", "Random_Number"])
            print("LCG")

            lcg_n_bits_dict = {}

            for n in n_bits:
                avg = 0
                n_bits_list = []
                for i in range(quantity):

                    start = time.perf_counter()
                    random_number = linear.algorithm(n)
                    end = time.perf_counter()

                    avg += (end - start)
                    writer.writerow(["LCG", n, random_number.bit_length(), i, random_number])
                    random_linear_numbers.append(random_number)
                    n_bits_list.append(random_number)

                plot_histogram(n_bits_list, quantity, bins=100, title=f"LCG - n_bits={n}", save_path="csvs/main_csvs/Randoms/histograms")           
                lcg_n_bits_dict.update({n: f'{(avg/quantity)*1000:.5f}'})

                print(f"n_bits: {n}, avg time: {(avg/quantity)*1000:.5f} ms")

    if random_option == 2 or random_option == 3:
        xorshift = random_algorithms.XorShiftGenerator(2**27)
        random_xor_numbers = []
        with open("csvs/main_csvs/Randoms/ 2 - XORSHIFT.csv", mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=";")

            writer.writerow(["Algorithm", "n_bits_max", "n_bits", "Index", "Random_Number"])
            print("XORSHIFT")

            xor_n_bits_dict = {}
            
            for n in n_bits:
                avg = 0
                n_bits_list = []
                for i in range(quantity):

                    start = time.perf_counter()
                    random_number = xorshift.algorithm(n)
                    end = time.perf_counter()

                    avg += (end - start)
                    writer.writerow(["XORSHIFT", n, random_number.bit_length(), i, random_number])
                    random_xor_numbers.append(random_number)
                    n_bits_list.append(random_number)

                plot_histogram(n_bits_list, quantity, bins=100, title=f"XORSHIFT - n_bits={n}", save_path="csvs/main_csvs/Randoms/histograms")
                xor_n_bits_dict.update({n: f'{(avg/quantity)*1000:.5f}'})

                print(f"n_bits: {n}, avg time: {(avg/quantity)*1000:.5f} ms")

    print("CSVs gerados ")


    with open("csvs/main_csvs/Randoms/ 3 - COMPARISON.csv", mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=";")
        writer.writerow(["Algorithm", "Tamanho do Número", "Tempo para gerar"])
        if random_option == 1 or random_option == 3:
            for n in n_bits:
                writer.writerow(["LCG", n, f"{lcg_n_bits_dict[n]} ms"])
        if random_option == 2 or random_option == 3:
            for n in n_bits:
                writer.writerow(["XORSHIFT", n, xor_n_bits_dict[n]])


    if action == 2:
        #Primes
        if random_option == 1:
            random_number_list = random_linear_numbers
        elif random_option == 2:
            random_number_list = random_xor_numbers

        if prime_option == 1:
            alg_selected = "Miller-Rabin"
        elif prime_option == 2:
            alg_selected = "Fermat"
        elif prime_option == 3:
            alg_selected = "Miller-Rabin e Fermat"

        print(f"Identificando primos com números gerados pelo {alg_selected}")

        with open(f"csvs/main_csvs/Primes/ 1 - {alg_selected}.csv", mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file)

            writer.writerow(["Algorithm", "n_bits", "Prime_Number"])

            if prime_option in [1, 3]:
                miller_n_bits_dict = {}
                for random_number in random_number_list:
                    start = time.perf_counter()
                    primo = prime_algorithms.MillerRabin(random_number).is_prime()
                    end = time.perf_counter()
                    if primo:
                        total_time = end - start
                        writer.writerow(["Miller-Rabin", random_number.bit_length(), random_number])
                        miller_n_bits_dict.update({random_number: [random_number.bit_length(), f'{total_time*1000}']})
                        print(f"n_bits: {random_number.bit_length()}, time: {total_time*1000} ms")

            if prime_option in [2, 3]:
                fermat_n_bits_dict = {}
                for random_number in random_number_list:
                    start = time.perf_counter()
                    primo = prime_algorithms.Fermat(random_number).is_prime()
                    end = time.perf_counter()
                    if primo:
                        total_time = end - start
                        writer.writerow(["Fermat", random_number.bit_length(), random_number])
                        fermat_n_bits_dict.update({random_number: [random_number.bit_length(), f'{total_time*1000}']})
                        print(f"n_bits: {random_number.bit_length()}, time: {total_time*1000} ms")
                        

        
        print("CSVs gerados ")


        with open("csvs/main_csvs/Primes/ 2 - COMPARISON.csv", mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=";")
            writer.writerow(["Algorithm", "Tamanho do Número","Numero Primo gerado", "Tempo para gerar"])
            if prime_option in [1, 3]:
                for n in miller_n_bits_dict:
                    writer.writerow(["Miller-Rabin", miller_n_bits_dict[n][0], n, f"{miller_n_bits_dict[n][1]} ms"])
            if prime_option in [2, 3]:
                for n in fermat_n_bits_dict:
                    writer.writerow(["Fermat", fermat_n_bits_dict[n][0], n, f"{fermat_n_bits_dict[n][1]} ms"])


