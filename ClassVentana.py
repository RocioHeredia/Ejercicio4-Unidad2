
class Ventana:
    __x2_inf_Der = 500
    __y2_inf_Der = 500

    def __init__(self, titu='', x1=0, x2=500, y1=0, y2=500):
        self.__titulo = titu
        self.__x1_sup_Izq = max(0, x1)
        self.__y1_sup_Izq = max(0, y1)
        self.__x2_inf_Der = min(500, x2)
        self.__y2_inf_Der = min(500, y2)

    def getTitulo(self):
        return self.__titulo

    def alto(self):
        return self.__y2_inf_Der - self.__y1_sup_Izq

    def ancho(self):
        return self.__x2_inf_Der - self.__x1_sup_Izq

    def mostrar(self):
        print("Ventana '{}' Coordenadas: ({}, {}) - ({}, {})".format(self.__titulo, self.__x1_sup_Izq, self.__y1_sup_Izq, self.__x2_inf_Der, self.__y2_inf_Der))

    def moverDerecha(self, distancia=0):
        self.__x1_sup_Izq = min(500 - (self.__x2_inf_Der - self.__x1_sup_Izq), self.__x1_sup_Izq + distancia)
        self.__x2_inf_Der = min(500, self.__x2_inf_Der + distancia)

    def moverIzquierda(self, distancia=0):
        self.__x1_sup_Izq = max(0, self.__x1_sup_Izq - distancia)
        self.__x2_inf_Der = max(self.__x1_sup_Izq + (self.__x2_inf_Der - self.__x1_sup_Izq), self.__x2_inf_Der - distancia)

    def bajar(self, distancia=0):
        self.__y1_sup_Izq = min(500 - (self.__y2_inf_Der - self.__y1_sup_Izq), self.__y1_sup_Izq + distancia)
        self.__y2_inf_Der = min(500, self.__y2_inf_Der + distancia)

    def subir(self, distancia=0):
        self.__y1_sup_Izq = max(0, self.__x1_sup_Izq - distancia)
        self.__y2_inf_Der = max(self.__y1_sup_Izq + (self.__y2_inf_Der - self.__y1_sup_Izq), self.__y2_inf_Der - distancia)