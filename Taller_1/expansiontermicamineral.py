from mineral import Mineral
import numpy as np
import matplotlib.pyplot as plt
import io


class ExpansionTermicaMineral(Mineral):
    def __init__(self, nombre, dureza, lustre, rompimiento_por_fractura, color, composicion, sistema_cristalino, specific_gravity, archivo):
        super().__init__(nombre, dureza, lustre, rompimiento_por_fractura, color, composicion, sistema_cristalino, specific_gravity)
        self.temperaturas = []
        self.volumenes = []
        self.cargar_datos_desde_csv(archivo)
    
    def cargar_datos_desde_csv(self, archivo):
        with open(archivo, 'r', encoding='utf-8') as datos:
            linea = datos.readline()
            linea = datos.readline()
            while len(linea) > 0:
                info = linea.strip().split(',')
                self.temperaturas.append(float(info[0]))
                self.volumenes.append(float(info[1]))
                linea = datos.readline()
    
    def coeficiente_de_expansion(self):

        T = self.temperaturas
        V = self.volumenes
        h = T[1]-T[0]

        derivadas = []
        for i in range(0,len(T)):
            if i == 0:
                derivada = (V[i+1])/(2*h)
                derivadas.append(derivada)
            elif i == len(T)-1:
                derivada = (-V[i-1])/(2*h)
                derivadas.append(derivada)
            else:
                derivada = (V[i+1]-V[i-1])/(2*h)
                derivadas.append(derivada)
        
        alfas = []
        for j in range(len(V)):
            alfa = (1/V[j])*(derivadas[j])
            alfas.append(alfa)
        
        alfa_prom = np.mean(alfas)
        error_global = np.std(derivadas)

        plt.figure(figsize=(10, 5))  
        plt.suptitle('Graficos para ' + self.nombre)

        plt.subplot(1, 2, 1) 
        plt.plot(T,V)
        plt.xlabel('Temperatura(°C)')
        plt.ylabel('Volumen(cc)')
        plt.title('Volumen vs Temperatura')

        plt.subplot(1, 2, 2) 
        plt.plot(T,alfas)
        plt.xlabel('Temperatura(°C)')
        plt.ylabel('Coeficiente de expansión térmica(1/°C)')
        plt.title('Alpha vs Temperatura')

        plt.tight_layout()
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        return(alfa_prom, error_global, buffer)
