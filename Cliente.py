from pessoa import Pessoa
from Conta import Conta

class Cliente(Pessoa):

    def __init__(self, nome, idade, conta: Conta):
        super().__init__(nome, idade)
        self.conta = conta




