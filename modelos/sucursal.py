class Sucursal:
    def __init__(self,id_sucursal, nombre, provincia):
        self.id_sucursal = id_sucursal
        self.nombre = nombre
        self.provincia = provincia
        
    def __repr__(self):
        return f"Sucursal({self.id_sucursal}, {self.nombre})"