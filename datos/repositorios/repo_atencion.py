from datos.modelos.atencion import Atencion

def Listado_atenciones():
    atencion = Atencion.select() 
    if atencion:
        return atencion