
import sqlite3 as conector

conexao = conector.connect("lilian_atividades\meu_banco.db")
cursor = conexao.cursor()

comando = '''DROP TABLE Municipio; '''
cursor.execute (comando)

#comando = '''DROP TABLE Populacao; '''
#cursor.execute (comando)

#comando = '''DROP TABLE Dengue; '''
#cursor.execute (comando)
