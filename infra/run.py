from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

repo.insert('Teste', 'comedia', 2023)
repo.delete('teste2')

data = repo.select()

print(data)
#Acesso ao repositorio de filmes e acessando o DBconnectionHandler como se fosse um select
