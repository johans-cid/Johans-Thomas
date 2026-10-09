from datos.modelos.paciente import Paciente

def Listado_pacientes():
    pacientes = Paciente.select() 
    if pacientes:
        return pacientes