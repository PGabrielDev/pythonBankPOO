from Banco import Banco
from cp import  ContaPoupanca
from Cliente import  Cliente as cli



if __name__ == '__main__':
    conta_popanca = ContaPoupanca('45',123487,500)

    cliente = cli('Guilherme',21,conta_popanca)
    banco = Banco()
    banco.inserir_conta(conta_popanca)
    banco.inserir_cliente(cliente)
    if banco.autenticar(cliente):
        cliente.conta.sacar(300)
    else:
        print('Cliente não autenticado')



