import Funcoes_jogos

def pull_the_game():
    game = int(input("(1) Forca (2) Adivinhação\nQual jogo? "))
    return game
    
def escolhe_jogo():
    
    Funcoes_jogos.welcome()    
    jogo = pull_the_game()
    Funcoes_jogos.the_chosen_game(jogo)
        
        
if(__name__ == "__main__"):
    escolhe_jogo()


