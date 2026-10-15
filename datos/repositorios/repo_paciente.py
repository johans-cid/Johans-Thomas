from datos.modelos.paciente import Paciente

def Listado_pacientes():
    pacientes = Paciente.select() 
    if pacientes:
        return pacientes

def guardar_paciente(paciente: Paciente):
    try:
        paciente_nuevo = paciente.save()
        return paciente_nuevo
    except 