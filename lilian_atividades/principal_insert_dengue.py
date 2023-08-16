import sqlite3 as conector
from modelo import Dengue, Populacao, Municipio

  
conexao = None
cursor = None


    
conexao = conector.connect("lilian_atividades\meu_banco.db")
cursor = conexao.cursor()

with open("lilian_atividades/dengue_2018rj.csv") as arquivo:
        arquivo.readline () #descarta o cabeçalho
        for linha in arquivo:
            codigo, nome, casos_2018, casos_2019 = linha.strip().split(',')
            print(codigo, nome, casos_2018, casos_2019)

            comando= '''INSERT INTO Dengue VALUES (?,?,?);''' # parâmetros nomeados
            cursor.execute(comando, (codigo, 2018, casos_2018))
            cursor.execute(comando, (codigo, 2019, casos_2019))
conexao.commit()