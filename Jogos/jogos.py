import Funcoes_jogos

def escolhe_jogo():
    
    Funcoes_jogos.welcome()

    jogo = int(input("(1) Forca (2) Adivinhação\nQual jogo? "))

    Funcoes_jogos.the_chosen_game(jogo)

if(__name__ == "__main__"):
    escolhe_jogo()
