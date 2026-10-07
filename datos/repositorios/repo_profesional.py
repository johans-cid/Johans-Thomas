from datos.modelos.profesional import Profesional

def Listado_profesionales():
    profesionales = Profesional.select() 
    if profesionales:
        return profesionales