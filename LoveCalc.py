import os, subprocess, sys

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

        number += str(int(numero.pop(0)) + int(numero.pop()))

    return int(number)

def finish_game():
    while True:
        response = input("Testar outros nomes? Y/n - ").lower().strip()

        if not response or response == "y":
            main_game()
        elif response == "n":
            sys.exit()

def main_game():
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True)
    print("Love Calc ❤️\n")

    nomeA = None
    while not nomeA or not nomeA.isalpha():
        nomeA = input("Digite um nome: ").strip()

    nomeB = None
    while not nomeB or not nomeA.isalpha():
        nomeB = input("Digite outro nome: ").strip()

    nomes = list(nomeA.lower() + nomeB.lower())
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