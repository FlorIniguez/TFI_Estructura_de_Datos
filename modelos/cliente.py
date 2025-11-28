class Cliente:
    def __init__(self, id_cliente,nombre,direccion):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion
        
    def __str__(self):
        return f"Cliente {self.id_cliente} - {self.nombre}"