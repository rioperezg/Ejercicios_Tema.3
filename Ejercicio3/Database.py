"""
Dada una lista de las naves (y vehículos) de Star Wars –consideraremos a todos como naves– de las que conocemos su nombre, largo, 
tripulación y cantidad de pasajeros, desarrollar los algoritmos necesarios para resolver las actividades detalladas a continuación:

 realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente;

mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
indicar cuál es la nave que requiere mayor cantidad de tripulación;
mostrar todas las naves que comienzan con AT;
listar todas las naves que pueden llevar seis o más pasajeros;
 mostrar toda la información de la nave más pequeña y la más grande
"""
import csv, Config
class Nave:
    def __init__(self, Nombre, Largo, Tripulacion, Pasajeros):
        self.Nombre = Nombre
        self.Largo = Largo
        self.Tripulacion = Tripulacion
        self.Pasajeros = Pasajeros
    def __str__(self):
        return f"({self.Nombre} {self.Largo} {self.Tripulacion} {self.Pasajeros})"

class Naves:
    lista = []
    with open(Config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for Nombre, Largo, Tripulacion, Pasajeros in reader:
            nave =Nave(Nombre, Largo, Tripulacion, Pasajeros)
            lista.append(nave) 
    @staticmethod
    def buscar(Nombre):
        for nave in Naves.lista:
            if nave.Nombre == Nombre:
                return nave  
    @staticmethod
    def crear(Nombre, Largo, Tripulacion, Pasajeros):
        nave = Nave(Nombre, Largo, Tripulacion, Pasajeros)
        Naves.lista.append(nave)
        Naves.guardar()
        return nave
    @staticmethod
    def modificar(Nombre, Largo, Tripulacion, Pasajeros):
        for indice, nave in enumerate(Naves.lista):
            if nave.Nombre == Nombre:
                Naves.lista[indice].Nombre = Nombre
                Naves.lista[indice].Largo = Largo
                Naves.lista[indice].Tripulacion = Tripulacion
                Naves.lista[indice].Pasajeros = Pasajeros
                Naves.guardar()
                return Naves.lista[indice]
    @staticmethod
    def borrar(Nombre):
        for indice, nave in enumerate(Naves.lista):
            if nave.Nombre == Nombre:
                nave = Naves.lista.pop(indice)
                Naves.guardar()
                return nave
    @staticmethod
    def guardar():
        with open(Config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for nave in Naves.lista:
                writer.writerow((nave.Nombre, nave.Largo, nave.Tripulacion, nave.Pasajeros))   
    @staticmethod
    def Mostrar(Nombre, Largo, Tripulacion, Pasajeros):
        for nave in Naves.lista:
            if nave.Nombre == Nombre:
                return f"({Nombre} {Largo} {Tripulacion} {Pasajeros})"
    @staticmethod
    def Tripulantes():
        Nave_mas_trip = []
        for nave in Naves.lista:
            # Para hacer esta funcion se me ocurre crear una nueva lista e ir borrando el elemento si el numero de pasajeros es menor
            # al siguiente
            Nave_mas_trip.append(nave)
            if nave.Pasajeros < (nave + 1).Pasajeros:
                Nave_mas_trip.pop(nave)
            else:
                Nave_mas_trip.pop(nave + 1)
        return Nave_mas_trip
    def Naves_conAT(Nombre):
        for nave in Naves.lista:
            nave.Nombre = str(Nombre)
            for Nombre in Nombre:
                if Nombre[0] == "A" and Nombre[1] == "T":
                    return nave
                else:
                    pass 