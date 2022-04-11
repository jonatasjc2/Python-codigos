import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************\n")

    print("(1) Forca (2) Adivinhação\n")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("\nJogando forca\n")
        forca.jogar()
    elif(jogo == 2):
        print("\nJogando adivinhação\n")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()
