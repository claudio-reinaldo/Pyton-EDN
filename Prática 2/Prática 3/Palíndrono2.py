def verificar_palindromo():
    frase = input("Digite uma frase: ")
    frase = frase.replace(" ", "").lower()  # remove espaços e converte para minúsculas
    if frase == frase[::-1]:
        print("Sim")
    else:
        print("Não")

verificar_palindromo()