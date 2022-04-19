import random
import forca
import adivinhacao 

'''aqui começa as funções do jogo da forca'''

def loading_file_animais():
    arquivo = open("animais.txt","r")
    animais = []
    
    for linha in arquivo:
        linha = linha.strip()
        animais.append(linha)
     
    arquivo.close()
    
    numero_aleatorio = random.randrange(0,len(animais))
    
    secret_word = animais[numero_aleatorio].upper()
    return secret_word

def loading_file_paises():
    arquivo = open("paises.txt","r")
    paises = []
    
    for linha in arquivo:
        linha = linha.strip()
        paises.append(linha)
     
    arquivo.close()
    
    numero_aleatorio = random.randrange(0,len(paises))
    
    secret_word = paises[numero_aleatorio].upper()
    return secret_word

def loading_file_frutas():
    arquivo = open("frutas.txt","r")
    frutas = []
    
    for linha in arquivo:
        linha = linha.strip()
        frutas.append(linha)
     
    arquivo.close()
    
    numero_aleatorio = random.randrange(0,len(frutas))
    
    palavra_secreta = frutas[numero_aleatorio].upper()
    return palavra_secreta

def welcome_to_forca():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def pull_the_options():
    print("\nEscolha o assunto que te interessa\n")
    print("(1) Frutas\n(2) Paises\n(3) Animais\n")
    options = (input("\nQual é a sua escolha: "))
    options = int(options)
    return options

def loading_secret_word():  
    options = pull_the_options()
    
    while (options >= 0):
        
        if(options == 1):
            secret_word = loading_file_frutas()
            break
        
        elif(options == 2):
            secret_word = loading_file_paises()
            break
        
        elif(options == 3):
            secret_word = loading_file_animais()
            break
        else:
            print("\nPreste atenção!Você deve escolher uma alternativa valida\n")
            options = pull_the_options()
            continue
    return secret_word

def guess():
    entrada_de_dado = input("\nQual letra ou palavra, se você quer arriscar um chute? ")
    entrada_de_dado = entrada_de_dado.strip().upper()
    return entrada_de_dado
    

def guess_verification(vector,guess,word): 
    index = 0
    for letter in word:
        if(guess == letter):
            vector[index] = letter
        index += 1    
          
        
def winner_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    
def enforcou(word):
    print("\nVocê perdeu!!A palavra era {}.".format(word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    
def right_word(word):
    print("\nParabéns a palavra é esta:",word)
    
def mistake_message(erros):
    print("\nNúmero de erros cometidos: {}. Se atingir 7 erros estará enforcado\n".format(erros)) 
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
        
'''Aqui começa as funções do jogos.py'''

def the_chosen_game(game):
    if(game == 1):
        print("\nJogando forca\n")
        forca.jogar()
    elif(game == 2):
        print("\nJogando adivinhação\n")
        adivinhacao.jogar()
        
def welcome():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************\n")

'''Aqui começa as funções do jogo adivinhação'''
    
def mensagem_final_do_jogo(acertou,numero_secreto):
    if(acertou):
        pass
    else:
        print("A número secreto era: {}\nFim do jogo".format(numero_secreto))

def contagem_de_pontos(points,secret_number,guess_number): 
    pontos_perdidos = abs(secret_number - guess_number)
    points = points - pontos_perdidos
    return points

def mensagem_de_erro(maior,menor):
    if(maior):
        print("\nVocê errou! O seu chute foi maior do que o número secreto.\n")
    elif(menor):
        print("\nVocê errou! O seu chute foi menor do que o número secreto.\n")
    
def welcome_to_guess_game():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************\n")

def guess_number(): 
    chute_str = input("Digite um número entre 1 e 100: ")
    print("\nVocê digitou " , chute_str)
    chute = int(chute_str)
    return chute    
    


def dificulty_guess_game():    
    tentativas = 0
    print("Qual nível de dificuldade?\n")
    print("(1) Fácil\n(2) Médio\n(3) Difícil")
    options = (input("Defina o nível: "))
    options = int(options)
    if(options == 1):
        tentativas = 20
    elif(options == 2):
        tentativas = 10
    else:
        tentativas = 5
        
    return tentativas   
