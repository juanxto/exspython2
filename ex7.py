cf = float(input('Digite o custo de fabrica de um carro: R$'))
pd = (28 * cf) / 100
pi = (45 * cf) / 100
cc = cf + pd + pi
print(f'O custo ao consumidor é R${cc:.2f}')