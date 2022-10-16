class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
    def extrato(self):
        print("O saldo do titular {} é de {} reais".format(self.__titular, self.__saldo))
        
    def depositar(self, valor):
        self.__saldo += valor
        
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else: 
            print("Saldo insuficiente")