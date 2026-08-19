caixas = 1250
supor_caixas = 12

caminhao = caixas // supor_caixas

sobra = caixas % supor_caixas

print(f"O número de caminhões necessários é: {caminhao}")
print(f"A quantidade de caixas que sobram é: {sobra}")