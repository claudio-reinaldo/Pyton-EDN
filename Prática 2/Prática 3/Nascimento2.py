from datetime import datetime

def calcular_dias_de_nascimento():
    ano_de_nascimento = int(input("Digite o seu ano de nascimento: "))
    
    data_de_nascimento = datetime(ano_de_nascimento)
    data_atual = datetime.now()

    diferenca_de_dias = (data_atual - data_de_nascimento).days

    print(f"Você tem {diferenca_de_dias} dias de vida.")

calcular_dias_de_nascimento()