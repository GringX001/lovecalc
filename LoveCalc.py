import os, subprocess

def somarNumero(numero: int):
    numero = list(str(numero))
    number = ""

    calculando = True
    while calculando:
        if not numero:
            calculando = False
            break

        if len(numero) == 1:
            number += numero[0]
            calculando = False
            break

        number += str(int(numero[0]) + int(numero[-1]))
        numero.pop(0)
        numero.pop()

    return int(number)

def finish_game():
    response = input("Testar outros nomes? Y/n - ")

    if not response or response == "y" or response == "Y":
        main_game()

def main_game():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

    print("Love Calc ❤️\n")
    nomeA = input("Digite um nome: ").lower()
    nomeB = input("Digite outro nome: ").lower()
    nomes = list(nomeA + nomeB)

    number = ""

    for i in range(len(nomes)):
        if nomes[i] == None:
            continue

        letter = nomes[i]
        nomes[i] = None
        count = 1

        for j in range(len(nomes)):
            if nomes[j] == None:
                continue

            if nomes[j] == letter:
                nomes[j] = None
                count += 1

        number += str(count)

    number = int(number)
    print("")

    while number > 99:
        print(number)
        number = somarNumero(number)

        if number <= 99:
            print(number)

    print(f"\nA compatibilidade amorosa entre {nomeA} e {nomeB} é de {number}% ❤️\n")
    finish_game()

main_game()