import random
def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************\n")
    
    
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
    
    print(letras_acertadas,"\n")

    while(not enforcou  and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        
        
        if(chute==palavra_secreta):
            
            print("\nParabéns a palavra é esta:",palavra_secreta,".\nVocê ganhou!!")
            break
            
        else:   
            if(chute in palavra_secreta):
                index = 0
                for letra in palavra_secreta:
                    if(chute == letra):
                        letras_acertadas[index] = letra
                    index += 1
                    
            else:
                total_de_tentativas = 6
                erros += 1
                print("\nTentativa {} de {}\n".format(erros, total_de_tentativas))
    
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas,"\n")


    if(acertou):
        print("\nVocê ganhou!!")
    if(enforcou):
        print("\nVocê perdeu!!\nA palavra era {}.".format(palavra_secreta))
    print("\nFim do jogo")

if(__name__ == "__main__"):
    jogar()
