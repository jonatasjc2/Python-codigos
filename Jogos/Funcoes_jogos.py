import random 

def welcome_to_forca():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
def loading_secret_word():
    arquivo = open("palavras.txt","r")
    frutas = []
    
    for linha in arquivo:
        linha = linha.strip()
        frutas.append(linha)
     
    arquivo.close()
    
    numero_aleatorio = random.randrange(0,len(frutas))
    
    palavra_secreta = frutas[numero_aleatorio].upper()
    return palavra_secreta

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
     