"""
Exercicio com Abstração, Herença, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e 
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que 
possa sacar/depositar nessa conta. Contas correntes tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente Tem conta (Agregação de classe ContaCorrente ou ContaPoupança)
Criar classes ContaPoupança e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas tem agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter método sacar abstrato (Abstração e 
    Polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas de seguinte maneira:
    Banco tem contas e clientes (Agregação)
    *Checar se a agência é daquele banco
    *Checar se o Cliente é daquele banco
    *Checar se a conta é daquele banco
Só será possivel sacar se passar na autenticação do banco (descrita acima)
"""

from classes.banco import Banco
from classes.contacorrente import ContaCorrente
from classes.contapoupanca import ContaPoupanca
from classes.cliente import Cliente


cc = ContaCorrente('12', '159357')
danilo = Cliente("Danilo", 27, cc)
nu = Banco()
nu.add_cliente(danilo)
nu.add_conta(cc)
if nu.valida(cc, danilo, cc.agencia):
    danilo.conta.depositar(2500.00)
    danilo.conta.sacar(1685.69)
    








