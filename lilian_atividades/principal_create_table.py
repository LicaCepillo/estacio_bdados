import sqlite3 as conector

conexao = None
cursor = None

try:
    conexao = conector.connect("lilian_atividades\meu_banco.db")
   
    cursor = conexao.cursor()

    #comando = '''DROP TABLE Populacao; '''
    #cursor.execute (comando)

    
    comando1 = '''CREATE TABLE Municipio(
                codigo INTEGER NOT NULL,
                nome VARCHAR(31) NOT NULL,
                PRIMARY KEY(codigo)
                );'''
    cursor.execute(comando1)

    comando2 = '''CREATE TABLE Populacao (
                codigo INTEGER NOT NULL,
                ano INTEGER NOT NULL,
                populacao INTEGER NOT NULL,
                PRIMARY KEY(codigo, ano),
                FOREIGN KEY(codigo) REFERENCES Municipio(codigo)
                );'''
    cursor.execute(comando2)

    comando3 = '''CREATE TABLE Dengue (
                codigo INTEGER NOT NULL,
                ano INTEGER NOT NULL,
                casos INTEGER NOT NULL,
                PRIMARY KEY(codigo, ano),
                FOREIGN KEY(codigo) REFERENCES Municipio(codigo)
                );'''
    cursor.execute(comando3)

    conexao.commit()

except conector.OperationalError as erro:
    print("Erro Operacional", erro)
except conector.DatabaseError as erro:
    print("Erro de Banco de Dados", erro)
