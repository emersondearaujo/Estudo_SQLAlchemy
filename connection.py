from sqlalchemy import create_engine

#mysql = linguagem que vai ser utilizado
#pymysql = driver que será utilizado
#root = usuario do mysql
engine = create_engine('mysql+pymysql://root:123456@localhost:3308/cinema')

#Para execução do primeiro teste e realizar a impressão acima basta retirar o #(comentário da linha de código em Python)
#print(engine)

#A partir da conexão conseguimos usar o sql
conn = engine.connect()
response = conn.execute('SELECT * FROM filmes;')

#Para cada linha de resposta imprimir ela
for row in response:
    print(row)
    print(row.titulo)
