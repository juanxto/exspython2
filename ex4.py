reais = float(input('Quantos reais você tem? R$'))
cotDol = float(input('Qual a cotação do dólar hoje: R$'))
dol = reais / cotDol
print(f'Os seus R${reais:.2f} equivalem a ${dol:.2f}')