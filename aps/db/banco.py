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

    def criar_tabela(self):#cria tabela, se ja tiver a tabela ela ignora esse comando
        cur = self.cursor
        cur.execute("""
        CREATE TABLE cadastro (
        nome TEXT NOT NULL,
        login TEXT NOT NULL,
        senha TEXT NOT NULL,
        nivel INTEGER NOT NULL,
        Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT);""")

    def inserir_dados(self,query):
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()
        


    def pegar_dados(self,query):
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall

    def pegarNivel(self,query):
        cur = self.cursor
        cur.execute(query)
        
        

#db = banco_db("cadastro.db")
#db.criar_tabela()