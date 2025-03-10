def calcula_gorjeta():
    print("Calculadora de Gorjeta")
    print("-------------------------")

    conta = float(input("Informe o valor da conta: R$ "))
    taxa_gorjeta = int(input("Informe a taxa de gorjeta (em %): "))

    gorjeta = (conta / 100) * taxa_gorjeta
    total = conta + gorjeta

    print(f"Valor da conta: R$ {conta:.2f}")
    print(f"Taxa de gorjeta: {taxa_gorjeta}%")
    print(f"Gorjeta: R$ {gorjeta:.2f}")
    print(f"Total: R$ {total:.2f}")

calcula_gorjeta()