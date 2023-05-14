from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBconnectionHandler:
    #Criação do método construtor

    def __init__(self) -> None:
        self.__connection_String = 'mysql+pymysql://root:123456@localhost:3308/cinema'
#Para quando inicar o instanciamento do objeto
        self.__engine = self.__create_database_engine()
        self.session = None

#Metodo privado para criação da engine
    def __create_database_engine(self):
        engine = create_engine(self.__connection_String)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

#retorno do contexto selfie e criação de secção
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()