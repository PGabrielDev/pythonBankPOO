from Conta import  Conta


class ContaCorrente(Conta):

    def __init__(self,agencia, numero, saldo=0, limite=400):
        super().__init__(agencia,numero,saldo)
        self.limite = limite

    def sacar(self, valor):
        if not self._validacao(valor):
            return
        if not self.__is_saque_negativo(float(valor)):
            return
        self.saldo -= float(valor)
        print(f'O saque foi Realizado novo saldo: {self.saldo}')


    def __is_saque_negativo(self, valor):
        if (self.saldo - valor) < self.limite * -1:
            print("Saldo insuficiente para realizar o saldo")
            return False
        return True
