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
 
'''
def 

def

def 

def

'''