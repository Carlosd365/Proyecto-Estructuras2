class Proveedor:
    def __init__(self, id, nombre, servicio, calificacion):
        self.Id = id
        self.Nombre = nombre
        self.Servicio = servicio
        self.Calificacion = calificacion

    def Imprimir(self):
        print(f"{self.Id} --- Nombre: {self.Nombre} --- Servicio a Ofrecer: {self.Servicio} --- Calificación: {self.Calificacion}⭐")

    def ImprimirporName(self):
        print(f"{self.Nombre} --- Servicio: {self.Servicio} --- Calificación: {self.Calificacion}⭐")

    def ImprimirporCalificacion(self):
        print(f"{self.Calificacion}⭐ --- Nombre: {self.Nombre} --- Servicio: {self.Servicio}")

    def ImprimirporServicio(self):
        print(f"{self.Servicio} --- Nombre: {self.Nombre} --- Calificación: {self.Calificacion}⭐")