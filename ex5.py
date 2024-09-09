vb = int(input('Insira a quantidade de votos em branco: '))
vn = int(input('Insira a quantidade de votos nulos: '))
vv = int(input('Insira a quantidade de votos validos: '))
vt = vv + vn + vb
pvv = (vv / vt) * 100
pvn = (vn/ vt) * 100
pvb = (vb/ vt) * 100

print(f'A porcentagem de votos validos é {pvv}%\n'
      f'A porcentagem de votos nulos é {pvn}%\n'
      f'A porcentagem de votos em branco é {pvb}%')