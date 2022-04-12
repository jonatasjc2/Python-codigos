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
          
def mistake_message(mistakes):
    print("\nNúmero de erros cometidos: {}. Se atingir 6 erros estará enforcado\n".format(mistakes))
        
    
def enforcou(word):
    print("\nVocê perdeu!!A palavra era {}.".format(word))
    
def right_word(word):
     print("\nParabéns a palavra é esta:",word)
     