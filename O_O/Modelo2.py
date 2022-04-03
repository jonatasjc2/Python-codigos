class Funcionario:
    def __init__(self, nome):
        self.nome = nome
    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self):
        print('Mostrando cursos')

class Alura(Funcionario):
    def mostrar_tarefas(self):
       ''' print('Fez muita coisa, Alurete!')'''

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')
        
class Hipster:
    def __str__(self):
        return ("Hipster,  {}".format(self.nome))       
        
class Junior(Alura):
    pass

class Pleno(Alura, Caelum,Hipster):
    pass


        
jose = Junior('Joseeee')
jose.busca_perguntas_sem_resposta()

luan = Pleno('Otavio')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
luan.mostrar_tarefas()
print(luan)
