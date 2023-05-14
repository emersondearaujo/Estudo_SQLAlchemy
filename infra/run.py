from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

data = repo.select()

print(data)
#Acesso ao repositorio de filmes e acessando o DBconnectionHandler como se fosse um select