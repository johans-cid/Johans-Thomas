from datos.modelos.paciente import Paciente

def Listado_pacientes():
    try:
        pacientes = Paciente.select() 
        if pacientes:
                return pacientes
    except Exception as error:
        print(f"Ha ocurrido un error: {error}")
    pacientes = Paciente.select() 
    
def  obtener_paciente(rut_paciente)
     try:
        paciente


def guardar_paciente(paciente:Paciente):
    try:
        paciente_nuevo = paciente.save()
        if paciente_nuevo == 1:
             print(f"Se ha guardado correctamente: {paciente.Paciente}")
    except Exception as error:
        print(f"Ha ocurrido un error: {error}")

