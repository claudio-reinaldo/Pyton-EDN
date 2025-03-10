def verificar_senha_forte(senha):
    # Verifica se a senha tem pelo menos 8 caracteres e 1 número
    return len(senha) >= 8 and any(char.isdigit() for char in senha)

while True:
    senha = input("Digite uma senha forte (mínimo 8 caracteres e pelo menos 1 número) ou 'sair' para encerrar: ")
    
    # Verifica se a entrada é uma string
    if not isinstance(senha, str):
        print("Erro: Entrada inválida. Por favor, digite uma string.")
        continue

    if senha.lower() == "sair":
        print("Encerrando...")
        break

    if verificar_senha_forte(senha):
        print("Senha validada com sucesso!")
        break
    else:
        # Mensagem de erro mais específica
        if len(senha) < 8:
            print("Senha fraca: Deve ter pelo menos 8 caracteres.")
        elif not any(char.isdigit() for char