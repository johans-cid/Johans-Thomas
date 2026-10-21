from datos.modelos.persona import Persona


def listado_personas():
    try:
        personas = Persona.select().where(Persona.habilitado == True)
        if personas:
            return personas
    except Exception as error:
        print(f'Error: {error}')


def obtener_persona(run: str) -> Persona | None:
    try:
        persona = Persona.get(Persona.run == run)
        if persona:
            return persona
    except Exception as error:
        print(f'Error: {error}')


def guardar_persona(persona: Persona):
    try:
        respuesta = persona.save()
        if respuesta == 1:
            print(f'Se ha guardado con éxito: {persona.run}')
    except Exception as error:
        print(f'Error: {error}')


def eliminar_persona(run: str) -> int:
    try:
        return Persona.delete().where(Persona.run == run).execute()
    except Exception as error:
        print(f'Error: {error}')
        return 0