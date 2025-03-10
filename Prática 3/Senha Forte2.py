def verifica_senha_forte():
    while True:
        senha = input("Digite uma senha (ou SAIR para encerrar): ")
        if senha.lower() == "sair":
            print("Programa encerrado")
            break
        if len(senha) < 8:
            print("Senha fraca: Deve ter no mínimo 8 caracteres")
            continue
        if not any(caractere.isdigit() for caractere in senha):
            print("Senha fraca: deve conter pelo menos um número")
            continue
        print("Senha forte e válida")
        break

verifica_senha_forte()
