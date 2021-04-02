from classes.conta_poupanca import ContaPoupanca
from classes.conta_corrente import ContaCorrente


cp = ContaPoupanca(111, 222, 0)
cp.depositar(10)
cp.sacar(5)
cp.sacar(5)
cp.sacar(1)

print('*' * 30)

cc = ContaCorrente(agencia=1111, conta=3333, saldo=0, limite=500)
cc.depositar(100)
cc.sacar(250)
cc.sacar(500)
cc.depositar(1000)