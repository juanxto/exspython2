seg = int(input('Digite os segundos: '))

horas = seg // 3600
minutos = (seg % 3600) // 60
segundos = seg % 60

print(f'São {horas} horas, {minutos} minutos e {segundos} segundos')
