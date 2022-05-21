class Biblioteca:
    def __init__(self,titulo,ano):
        self._titulo=titulo.title()
        self.ano=ano
        self._likes=0

    def dar_likes(self):
        self._likes+=1

    @property
    def titulo(self):
        return self._titulo

    @property
    def likes(self):
        return self._likes

    @titulo.setter
    def titulo(self,titulo):
        self._titulo=titulo

    def __str__(self):
        return (f'Nome:{self.titulo}{self.likes} Likes')

class Filme(Biblioteca):
    def __init__(self,titulo,ano,duracao):
        super().__init__(titulo,ano)
        self.duracao=duracao

    def __str__(self):
        return (f'Nome:{self.titulo} Ano: {self.ano} Duração: {self.duracao} {self.likes} Likes')

class Serie(Biblioteca):
    def __init__(self,titulo,ano,temporadas):
        super().__init__(titulo,ano)
        self.temporadas=temporadas

    def __str__(self):
        return (f'Nome:{self.titulo} Ano: {self.ano} Temporadas: {self.temporadas} {self.likes} Likes')

class Playlist():
    def __init__(self,nome,programa):
        self.nome = nome
        self._programa=programa

    def __getitem__(self, item):
        return self._programa[item]

    def __len__(self):
        return len(self._programa)

    @property
    def listagem(self):
        return self._programa

Demolidor=Serie('Demolidor',2018,2)
Demolidor.titulo='Demolidor2'
Tmep=Filme('Todo Mundo em Panico',1999,100)
Vingadores=Filme ("Vingadores",2022,160)
Atlanta=Serie("Atlanta",2017,2)


Atlanta.dar_likes()
Tmep.dar_likes()
Tmep.dar_likes()
Vingadores.dar_likes()
Vingadores.dar_likes()
Demolidor.dar_likes()
Demolidor.dar_likes()
Atlanta.dar_likes()
Atlanta.dar_likes()

Filmes_E_Series=[Vingadores,Atlanta,Demolidor,Tmep]

Lista_De_Fim_De_Semana=Playlist("Lista de Fim de Semana",Filmes_E_Series)

for Biblioteca in Lista_De_Fim_De_Semana:
    print(Biblioteca)

print(f'Tamanho da Playlist {len(Lista_De_Fim_De_Semana)}')

