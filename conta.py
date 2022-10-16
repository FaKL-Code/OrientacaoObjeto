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
            
    def tranferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        
    def get_saldo(self):
        return self.__saldo
    
    def get_limite(self):
        return self.__limite
    
    def get_titular(self):
        return self.__titular
    
    def get_numero(self):
        return self.__numero
    
    def set_saldo(self, saldo):
        self.__saldo = saldo
    
    def set_limite(self, limite):
        self.__limite = limite