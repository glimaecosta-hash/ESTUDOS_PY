palavras = ["banana", "abacaxi", "laranja", "uva", "morango"]

maior_palavra = palavras[0]
menor_palavra = palavras[0]

for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra
    elif len(palavra) < len(menor_palavra):
        menor_palavra = palavra

print("Maior palavra:", maior_palavra)
print("Menor palavra:", menor_palavra)