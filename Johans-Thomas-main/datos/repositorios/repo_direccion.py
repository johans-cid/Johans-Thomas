from datos.modelos.direccion import Direccion

def Listado_direcciones():
    direcciones = Direccion.select() 
    if direcciones:
        return direcciones