from cp import  ContaPoupanca
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    conta_popanca = ContaPoupanca(100,123487,500)
    print(conta_popanca.saldo)
    print(conta_popanca.agencia)
    print(conta_popanca.numero)
    conta_popanca.depositar('123')
    conta_popanca.sacar('123')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
