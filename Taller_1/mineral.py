import matplotlib.pyplot as plt

class Mineral:
    def __init__(self, nombre, dureza, rompimiento_por_fractura, color, composicion,  lustre, specific_gravity, sistema_cristalino):
        self.nombre = nombre
        self.dureza = dureza
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.color = color
        self.composicion = composicion
        self.lustre = lustre
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = specific_gravity

    def es_silicato(self):
        if 'Si' in self.composicion and 'O' in self.composicion:
            return True
        else:
            return False
        
    def calcular_densidad(self):
        return float(self.specific_gravity)*1000
    
    #formula gravedad especifica = densidad / densidad agua (1000)
    
    def mostrar_color(self): 
        fig, ax = plt.subplots()
        cuadrado = plt.Rectangle((0, 0), 1, 1, color=self.color)
        ax.add_patch(cuadrado)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        plt.axis('off') 
        plt.show()

    def imprimir_du_rom_org(self):
        print('El mineral ' + str(self.nombre) + ' tiene una dureza de ' + str(self.dureza) + ' de acuerdo a la escala de Mohs.')
        if self.rompimiento_por_fractura == True:
            print('El material ' + str(self.nombre) + ' se rompe por fractura.')
        else:
             print('El material ' + str(self.nombre) + ' se rompe por escisión.')
        print('El sistema de organización de los átomos en el material ' + str(self.nombre) + ' es ' + str(self.sistema_cristalino) + '.')