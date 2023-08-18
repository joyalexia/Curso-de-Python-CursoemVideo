preco = float(input('Digite o preço do produto: '))
desconto = preco - (preco * 5 / 100)

print(f'O produto de R${preco:.2f}, na promoção com desconto de 5% passa a custar {desconto:.2f}R$')