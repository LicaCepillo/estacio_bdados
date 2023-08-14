import sqlite3 as conector
from principal_molelo import Marca
from principal_molelo import Veiculo

conexao = conector.connect("lilian_atividades/banco_dados_exemplo2.db")
cursor = conexao.cursor()


# Inserção de dados da tabela Marca
comando1 = '''INSERT INTO Marca (nome, sigla) VALUES (:nome, :sigla);'''
marca1 = Marca("Marca A", "MA")
cursor.execute(comando1, vars(marca1))
marca1.id = cursor.lastrowid


marca2 = Marca("Marca B", "MB")
cursor.execute(comando1, vars(marca2))
marca2.id = cursor.lastrowid



# Inserção de dados na tabela Veiculos
comando2 = '''INSERT INTO Veiculo
                VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca);'''
veiculo1 = Veiculo("AAABBB1", 2001, "Prata", 1.0, 10080088809, marca2.id)
veiculo2 = Veiculo("BAABBB2", 2002, "Preto", 1.4, 30080088809, marca2.id)
veiculo3 = Veiculo("CAABBB3", 2003, "Branco", 1.6, 20080088809, marca2.id)
veiculo4 = Veiculo("DAABBB4", 2004, "Azul", 2.0, 40080088809, marca2.id)

cursor.execute(comando2, vars(veiculo1))
cursor.execute(comando2, vars(veiculo2))
cursor.execute(comando2, vars(veiculo3))
cursor.execute(comando2, vars(veiculo4))
conexao.commit()

