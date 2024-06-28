import math
from pymodbus.client import ModbusTcpClient

class Tanque:
    def __init__(self, diametro, altura, nivel_maximo, cliente, esclavo,sensorLevel):
        self.diametro = diametro
        self.altura = altura
        self.nivel_maximo = nivel_maximo
        self.litros_actual = 0
        self.nivel_actual = 0
        self.client = cliente
        self.esclavo = esclavo
        self.sensorLevel=sensorLevel
 

    def llenar(self):
        for v in self.valvulas:
            if (v.status == True) and (v.tipo != "Entrada"):
                v.cerrar(0)
            if (v.status == False) and (v.tipo == "Entrada"):
                v.abrir(1000)
        print("Llenado Tanque ...")
        while self.litros_actual < self.nivel_maximo:
            self.update()  
            print( self.medirLitros(), "L")

    def vaciar(self):
        for v in self.valvulas:
            if (v.tipo == "Entrada"):
                v.cerrar()
            if (v.tipo == "Salida"):
                v.abrir()
        print("Vaciando Tanque ...")     
        while self.litros_actual > 0:               
                self.update()  
                print( self.medirLitros(), "L")             
    
    def medirLitros(self):
        lectura = self.client.read_input_registers(self.sensorLevel, 1, self.esclavo)  
        return lectura.registers[0]
    
    def medirNivel(self, nivel_cm):
        radio = self.diametro / 2
        altura_litros = (math.pi * radio**2 * nivel_cm) / 1000
        return altura_litros
    
class TanqueConValvulas(Tanque):
    def __init__(self, diametro, altura, nivel_maximo, cliente, esclavo,sensorLevel, valvulas):
        self.valvulas = valvulas
        self.esclavo = esclavo  # Agrega esclavo como atributo
 
        super().__init__(diametro, altura, nivel_maximo, cliente, esclavo,sensorLevel) 

    def abrir_valvula(self,valvula):
        self.valvulas[valvula-1].abrir(1000)

    def cerrar_valvula(self,valvula):
        self.valvulas[valvula-1].cerrar(0)

    def update(self):
        for v in self.valvulas:
            if v.status == True:
                if v.tipo == "Entrada":
                    self.litros_actual = self.medirLitros() 
                else:
                    if self.litros_actual > 0:
                        self.litros_actual = self.medirLitros()
        if self.litros_actual < 0:
            self.litros_actual = 0
        if self.litros_actual > self.nivel_maximo:
            self.litros_actual = self.nivel_maximo    
                        


class Valvula():
    def __init__(self,tipo,caudal,Direccion,cliente,esclavo):
        self.tipo = tipo
        self.caudal = caudal
        self.status = False #False = Cerrada y True = Abierta
        self.caudalActual = 0 
        self.Direccion=Direccion 
        self.client=cliente
        self.esclavo=esclavo

    def abrir(self,nivel):
        self.status = True 
        self.client.write_register(self.Direccion, nivel, self.esclavo)
        
    def cerrar(self,nivel):
        self.status = False 
        self.client.write_register(self.Direccion, nivel, self.esclavo) 