# Implementação de dois geradores de números pseudoaleatórios em Python:

# 1) Linear Congruential Generator (LCG)
# 2) XorShift

class LinearCongruentialGenerator:
    def __init__(self, seed=2**27):

        # Define a semente inicial do gerador.
        self.seed = seed

    def algorithm(self, n_bits):

        #Executa uma iteração do algoritmo LCG para gerar o próximo número
        #pseudoaleatório com base na semente atual.
  
        # Parâmetros do LCG 
        a = 33690453   # multiplicador
        c = 1013904223   # incremento
        m = 2**n_bits   # módulo (determina o intervalo e o período máximo)

        # Obtém a semente atual
        x = self.seed

        # Fórmula do LCG:
        # Xi+1 = (a * Xi + c) mod m
        self.seed = (a * x + c) % m

        # Retorna o novo valor gerado
        return self.seed


class XorShiftGenerator:
    def __init__(self, seed=2**27):
        # Define a semente inicial para o gerador XorShift
        self.seed = seed

    def algorithm(self, n_bits):
   
        #Executa uma iteração do algoritmo XorShift para gerar o próximo número
        #pseudoaleatório com base na semente atual.

        # Cria uma máscara para limitar o resultado ao tamanho desejado em bits
        mask = (2**n_bits) - 1

        # Garante que o valor inicial esteja dentro do intervalo da máscara
        x = self.seed & mask

        # Aplica as transformações do algoritmo XorShift:
        # Bit shifts combinados com operações XOR
        x ^= (x << 13) & mask
        x ^= (x >> 17) & mask
        x ^= (x << 5) & mask

        # Atualiza a semente com o novo valor limitado
        self.seed = x & mask

        return self.seed
