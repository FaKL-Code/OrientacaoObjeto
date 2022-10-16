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
                    
    def __saque_permitido(self, valor):
        return valor <= (self.__saldo + self.__limite)
    
    def sacar(self, valor):
        if self.__saque_permitido(valor):
            self.__saldo -= valor
        else: 
            print("Saldo insuficiente")
      
    def tranferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
     
    @property    
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def numero(self):
        return self.__numero
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
        
    @staticmethod
    def cod_banco(self):
        return "001"