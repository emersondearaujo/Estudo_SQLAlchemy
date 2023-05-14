from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

#mysql = linguagem que vai ser utilizado
#pymysql = driver que será utilizado
#root = usuario do mysql

#Configurações
engine = create_engine('mysql+pymysql://root:123456@localhost:3308/cinema')
Base = declarative_base()
Session = sessionmaker(bind=engine)
#Solicitação de sessão baseado nas conexões do BD
session = Session()

#Entidades
class Filmes(Base):
    __tablename__ = "filmes"

    titulo = Column(String, primary_key = True)
    genero = Column(String, nullable= False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
      return f"Filme (titulo={self.titulo}, ano={self.ano})"

#SQL comandos

#Insert

data_isert = Filmes(titulo = "teste2", genero = "Acao", ano = 2022)
#Estanciamento do objeto das classes para relacionar aos registros do banco de dados
session.add(data_isert)
session.commit()

#Delete
session.query(Filmes).filter(Filmes.titulo=="teste1").delete()
session.commit()

#Update
session.query(Filmes).filter(Filmes.genero == "Drama").update({ "ano": 2000})
session.commit()

#Select
data = session.query(Filmes).all()
print(data)
print(data[0].titulo)
#Comunicação do banco de dados a partir das entidades

session.close()
#Solicitação da chamada da sessão após fazer os processos
