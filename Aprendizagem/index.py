temperatuda = float(input("Digite a temperatura em Celsius: "))
temperadura_1 = 15
temperadura_2 = 25


if temperatuda < temperadura_1:
    print("Está frio.")
elif temperatuda >= temperadura_1 and temperatuda <= temperadura_2:
    print("Está agradável.")
else:
    print("Está calor.")
    
