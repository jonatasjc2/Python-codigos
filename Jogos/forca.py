import random

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

        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        
        if(chute==palavra_secreta):
            
            print("\nParabéns a palavra é esta:",palavra_secreta,".Você ganhou\n")
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
                print("\nCuidado, você cometeu ",erros," erros meu amigo, se atingir 6 erros estará enforcado\n")
                 
            enforcou = erros == 6
            acertou = "_" not in letras_acertadas
            print(letras_acertadas)


    if(acertou):
        print("Você ganhou!!\n")
    else:
        print("Você perdeu!!\n")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
