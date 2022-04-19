import Funcoes_jogos

def jogar():
    '''Fase 02 finalizada'''
    Funcoes_jogos.welcome_to_forca()
    
    palavra_secreta = Funcoes_jogos.loading_secret_word()
    
    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas,"\n")
   
    enforcou = False
    acertou = False
    erros = 0
    
    while(not enforcou and not acertou):
        
        chute = Funcoes_jogos.guess()
        
        if(chute==palavra_secreta):
    
           Funcoes_jogos.right_word(palavra_secreta)
           acertou =True
             
        else:     
            if(chute in palavra_secreta):
                
                Funcoes_jogos.guess_verification(letras_acertadas,chute,palavra_secreta)
                         
            else:
                erros += 1
                Funcoes_jogos.mistake_message(erros)
        
            enforcou = erros == 7
            acertou = "_" not in letras_acertadas
            print(letras_acertadas,"\n")

    if(acertou):
      
        Funcoes_jogos.winner_message()
        
    if(enforcou):
        Funcoes_jogos.enforcou(palavra_secreta)
        
    print("\nFim do jogo")

if(__name__ == "__main__"):
    jogar()