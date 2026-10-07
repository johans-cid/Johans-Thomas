from datos.modelos.persona import Persona

def Listado_personas():
    personas = Persona.select() 
    if personas:
        return personas