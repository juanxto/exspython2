v = float(input("Insira o valor do produto: R$"))
d = 12 * v
d /= 100
p = v - d
print(f'O valor do produto com o desconto de 12% é de: R${p:.2f}')