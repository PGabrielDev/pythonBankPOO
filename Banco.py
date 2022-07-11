from Cliente import Cliente
from Conta import  Conta


class Banco:
    def __init__(self):
        self._contas = []
        self._clientes = []
        self._agencias = ['001','002','003']


    def inserir_conta(self, conta):
        self._contas.append(conta)

    def inserir_cliente(self, cliente):
        self._clientes.append(cliente)

    def autenticar(self, cliente:Cliente):
        if cliente  not in self._clientes:
            print('Cliente nao faz parte do banco')
            return False

        if cliente.conta.agencia not in self._agencias:
            print('Agencia não faz parte deste banco')
            return False

        if cliente.conta not in self._contas:
            print('Conta do não faz parte do banco')
            return False
        return True




