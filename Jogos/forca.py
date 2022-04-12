import random
'''isto é um comentario'''
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")
    
    arquivo = open("palavras.txt","r")
    frutas = []
    
    for linha in arquivo:
        linha = linha.strip()
        frutas.append(linha)
     
    arquivo.close()
    
    numero_aleatorio = random.randrange(0,len(frutas))
    
    palavra_secreta = frutas[numero_aleatorio].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
   
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):
        
        chute = input("\nQual letra? ")
        chute = chute.strip().upper()
        
        if(chute==palavra_secreta):
            
            print("\nParabéns a palavra é esta:",palavra_secreta)
            acertou =True
             
        else:     
            if(chute in palavra_secreta):
                index = 0
                for letra in palavra_secreta:
                    if(chute == letra):
                        letras_acertadas[index] = letra
                    index += 1
                    
            else:
                erros += 1
                print("\nNúmero de erros cometidos: {}. Se atingir 6 erros estará enforcado\n".format(erros))
                 
            enforcou = erros == 6
            acertou = "_" not in letras_acertadas
            print(letras_acertadas,"\n")

    if(acertou):
        print("\nVocê ganhou!!\n")
    if(enforcou):
        print("\nVocê perdeu!!\nA palavra era {}.".format(palavra_secreta))
    print("\nFim do jogo")

if(__name__ == "__main__"):
    jogar()
