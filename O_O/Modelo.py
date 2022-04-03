class Programa:

   def __init__(self,nome,ano):
       self._nome = nome.title()
       self.ano = ano
       self._likes = 0
       
   ''' O property é uma maneira simplificada de retornar um atributo de um objeto(self), 
   em outras palavras @property faz a função de get.likes. O @property faz com que uma 
   determinada função seja aquela que invoca o atributo de um determinado objeto(self).'''
   @property
   def likes(self):
       return self._likes
       
   def dar_like (self):
        self._likes += 1

   @property
   def nome(self):
       return self._nome
   
   ''  'O @nome.setter define como pode-se valorar o atributo nome.'''     
   @nome.setter 
   def nome (self, novo_nome):
       self._nome = novo_nome.title()
        
   '''dandar atribuity'''
   def __str__(self):
       return( "{} - {} - {} likes".format(self._nome,self.ano,self._likes))
   

class Filme(Programa):
    
   def __init__(self,nome,ano,duracao):
       
       '''dunder method. Aqui temos a invocação da classe mãe, ou seja, a classe Programa
       super().__init__(nome, ano) é a mesma coisa de: 
   def __init__(self,nome,ano):
       self._nome = nome.title()
       self.ano = ano
       Todos os métodos são herdados da classe mãe'''
       
       super().__init__(nome,ano)
       self.duracao = duracao
   
   def __str__(self):
       return( "{} - {} - {} min - {} likes".format(self._nome,self.ano,self.duracao,self._likes))
    
  

class Serie(Programa):
    
    def __init__(self,nome,ano,temporadas):
        
        super().__init__(nome,ano)
        self.temporadas = temporadas
        
    def __str__(self):
        return("{} - {} - {} temporadas - {} likes".format(self._nome,self.ano,self.temporadas,self._likes))
        
 
class Playlist:
    
    def __init__(self,nome,programas):
        
        self._nome = nome.title()
        self._programas = programas
    
    '''esse dunder method faz com que a casse Playlist seja um interavel'''
    def __getitem__(self,item):
        return self._programas[item]
    

    
     
    def __len__(self):
        return len(self._programas)
        
       
       
    @property    
    def nome(self):
        return self._nome
        
    @nome.setter
    def nome(self, new_name):
        self._nome = new_name.title()
        
    
        
       