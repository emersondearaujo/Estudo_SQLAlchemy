from infra.configs.connection import DBconnectionHandler
from infra.entities.filmes import Filmes

# Criando o acesso de tudo que contém no DBconnectionHandler para acessos dos elementos selfie
class FilmesRepository:
    def select(self):
        with DBconnectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data

    def insert(self, titulo, genero, ano):
        with DBconnectionHandler() as db:
            data_isert = Filmes(titulo=titulo, genero=genero, ano=ano)
            db.session.add(data_isert)
            db.session.commit()

    def delete(self, titulo):
        with DBconnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
            db.session.commit()


def update(self, titulo, ano):
    with DBconnectionHandler() as db:
        db.session.query(Filmes).filter(Filmes.titulo == titulo).update({"ano": ano})
        db.session.commit()
