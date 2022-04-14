import random
import Funcoes_jogos

def jogar():
    
    Funcoes_jogos.welcome_to_guess_game() 

    numero_secreto = random.randrange(1,101)
    pontos = 1000
    total_de_tentativas = Funcoes_jogos.dificulty_guess_game()  

    for rodada in range(1, total_de_tentativas + 1):
        print("\nTentativa {} de {}".format(rodada, total_de_tentativas))
        
        chute = Funcoes_jogos.guess_number()

        if(chute < 1 or chute > 100):
            print("\nVocê deve digitar um número entre 1 e 100!")
            continue
        
        acertou = chute == numero_secreto

        if(acertou):
            print("\nVocê acertou e fez {} pontos!".format(pontos))
            break
        else:
            maior   = chute > numero_secreto
            menor   = chute < numero_secreto
            Funcoes_jogos.mensagem_de_erro(maior,menor)
            
            pontos = Funcoes_jogos.contagem_de_pontos(pontos,numero_secreto,chute)
    
    Funcoes_jogos.mensagem_final_do_jogo(acertou,numero_secreto)

if(__name__ == "__main__"):
    jogar()