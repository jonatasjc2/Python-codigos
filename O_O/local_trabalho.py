from Modelo import Filme
from Modelo import Serie
from Modelo import Playlist

vingadores = Filme('vingadores - guerra Infinita',2018,'160')
tmep = Filme('todo mundo em pânico',1999,'100')

atlanta = Serie('Atlanta',2018, 2)
demolidor = Serie('demolidor',2016,2)


tmep.dar_like()
tmep.dar_like()
tmep.dar_like()

demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta,demolidor,tmep]
playlist_fim_de_semana = Playlist('fim de semana adoidado',filmes_e_series)

print("\n",playlist_fim_de_semana.nome,":\n")

print("Tamanho do playlist: {}\n".format(len(playlist_fim_de_semana)))

contador = 0
    while contador< len(playlist_fim_de_semana):
    print("\n{}".format(playlist_fim_de_semana[contador]))
    contador += 1

    
print("\nComo é que é, está ou não está?'\n{}".format(demolidor in playlist_fim_de_semana))
