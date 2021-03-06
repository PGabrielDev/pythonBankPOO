from Conta import Conta


class ContaPoupanca(Conta):

    def sacar(self, valor):
        if not self._validacao(valor):
            return
        if not self.__is_saque_negativo(float(valor)):
            return
        self.saldo -= float(valor)
        print(f'O saque foi Realizado novo saldo: {self.saldo}')


    def __is_saque_negativo(self, valor):
        if (self.saldo - valor) < 0:
            print("Saldo insuficiente para realizar o saque")
            return False
        return True

