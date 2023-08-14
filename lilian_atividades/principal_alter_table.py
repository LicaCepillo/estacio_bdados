import sqlite3 as conector

conexao = None
cursor = None

try:
    conexao = conector.connect("lilian_atividades\meu_banco.db")
    conexao.execute ("PRAGMA foreign_keys = on")
    cursor = conexao.cursor()

    comando = '''ALTER TABLE Populacao
                ADD populacao INTEGER DEFAULT 0 NOT NULL;'''
    cursor.execute(comando)

    conexao.commit()

except conector.OperationalError as erro:
    print("Erro Operacional", erro)
except conector.DatabaseError as erro:
    print("Erro de Banco de Dados", erro)
