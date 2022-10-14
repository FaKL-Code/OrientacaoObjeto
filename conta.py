class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
    def extrato(self):
        print("O saldo do titular {} é de {} reais".format(self.titular, self.saldo))
        
    def depositar(self, valor):
        self.saldo += valor
        
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else: 
            print("Saldo insuficiente")