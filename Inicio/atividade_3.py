# Neste exercício, você possui duas listas de Python. Cada lista representa os gastos do mês de dois amigos, João e Pedro. Cada valor na lista representa o gasto em uma das semanas do mês:

gastos_pedro = [325, 485, 1524, 874, 652, 214, 987, 321, 654, 789]
gastos_joao = [214, 874, 321, 987, 652, 485, 325, 789, 654, 1524]

# Seu objetivo é calcular a média de gastos de cada amigo e determinar quem gastou mais em média durante o mês. Para isso, você deve seguir os seguintes passos:

# 1. Calcular a média de gastos de Pedro.
media_pedro = sum(gastos_pedro) / len(gastos_pedro)

# 2. Calcular a média de gastos de João.
media_joao = sum(gastos_joao) / len(gastos_joao)

# 3. Comparar as médias e imprimir quem gastou mais em média.
if media_pedro > media_joao:
    print(f"Pedro gastou mais em média: R${media_pedro:.2f}")
elif media_joao > media_pedro:
    print(f"João gastou mais em média: R${media_joao:.2f}")
else:
    print("Ambos gastaram a mesma quantidade em média.")
    
    
