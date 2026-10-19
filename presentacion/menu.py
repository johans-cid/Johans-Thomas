from auxiliares import nombre_app, version_app, menu_principal

def cargar_menu():
    print()
    print(f"{nombre_app} - v{version_app}")
    print(f"{"=" * len(nombre_app)}===={"=" * len(version_app)}\n")

    for clave, valor in menu_principal.items():
        print(f"[{clave}] - {valor}")