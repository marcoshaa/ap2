import sqlite3
from sqlite3 import Error

class banco_db:

    def __init__(self,banco =None):
        self.conn = None
        self.cursor = None

        if banco:
            self.open(banco)
    
    def open(self,banco):
        try:
            self.conn= sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            print("Conexão Criada")
        except sqlite3.Error as e:
            print("Conexão nao Estabelecida")

#__________________CRIA O BANCO CASO NAO TENHA NO PROJETO________________#

    def criar_tabela(self):#cria tabela, se ja tiver a tabela ela ignora esse comando
        cur = self.cursor
        cur.execute("""
        CREATE TABLE cadastro (
        nome TEXT NOT NULL,
        login TEXT NOT NULL,
        senha TEXT NOT NULL,
        nivel INTEGER NOT NULL,
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT);""")

#__________________FUNÇÃO CRIADA PARA FAZER INSERT INTO NO BANCO_______________#

    def inserir_dados(self,query):
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()
        
#_____________________FUNÇÃO CRIADA PARA FAZER SELECT NO BANCO____________________#

    def pegar_dados(self,query):
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall

#_______________________FUNÇÃO CRIADA PARA PEGAR APENAS O CAMPO NIVEL DO BANCO____________#

    def pegarNivel(self,query):
        cur = self.cursor
        cur.execute(query)
        
#___________DESCOMENTE E EXECUTE O COD. PARA GERAR MAIS BANCOS CASO QUEIRA_____________________________#  

#db = banco_db("X.db") #SUBISTITUIR O X PELO NOME DO NOVA BANCO.
#db.criar_tabela()