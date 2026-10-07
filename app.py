# from presentacion import cargar_menu

# cargar_menu()

from datos.repositorios.repo_persona import Listado_personas
from prettytable import prettytable


personas = Listado_personas()

for persona in personas:
    print(f"{persona.run} - {persona.nombre} - {persona.apellido} - {persona.fecha_nacimiento}")

