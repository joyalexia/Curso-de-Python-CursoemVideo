dias = int(input('Por quantos dias alugados? '))
km = float(input('Quantos km foram percorridos? '))

total = (km * 0.15) + (dias * 60)

print(f'O total a pagar é de R${total:.2f}')