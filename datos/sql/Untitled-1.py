"""
Sistema de Reservas - Lavado de Autos
---------------------------------------
Programa de consola que permite:
  - Registrar clientes y reservar hora para lavado de auto
  - Elegir tipo de servicio y tipo de vehículo (afecta el precio)
  - Ver horarios disponibles por día
  - Listar todas las reservas
  - Cancelar una reserva
  - Guardar los datos en un archivo JSON (persisten entre ejecuciones)

Cómo ejecutarlo en VS Code:
  1. Abre este archivo en VS Code.
  2. Asegúrate de tener Python instalado.
  3. Ejecuta con "Run Python File" (F5) o desde la terminal:
         python sistema_reservas_lavado.py
"""

import json
import os
from datetime import datetime

ARCHIVO_DATOS = "reservas_lavado.json"

# ---------------------------------------------------------
# Configuración del negocio (puedes ajustar estos valores)
# ---------------------------------------------------------

SERVICIOS = {
    "1": {"nombre": "Lavado básico", "precio": 5000},
    "2": {"nombre": "Lavado premium (encerado)", "precio": 9000},
    "3": {"nombre": "Lavado completo (interior + motor)", "precio": 15000},
}

TIPOS_VEHICULO = {
    "1": {"nombre": "Auto pequeño", "recargo": 0},
    "2": {"nombre": "Camioneta / SUV", "recargo": 2000},
    "3": {"nombre": "Furgón / Camioneta grande", "recargo": 4000},
}

HORARIOS_DISPONIBLES = [
    "09:00", "10:00", "11:00", "12:00",
    "14:00", "15:00", "16:00", "17:00", "18:00"
]


# ---------------------------------------------------------
# Persistencia de datos
# ---------------------------------------------------------

def cargar_reservas():
    """Carga las reservas desde el archivo JSON, si existe."""
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def guardar_reservas(reservas):
    """Guarda la lista de reservas en el archivo JSON."""
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(reservas, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------
# Utilidades de entrada de datos
# ---------------------------------------------------------

def pedir_fecha():
    """Pide una fecha válida en formato DD-MM-AAAA."""
    while True:
        texto = input("Fecha de la reserva (DD-MM-AAAA): ").strip()
        try:
            fecha = datetime.strptime(texto, "%d-%m-%Y")
            if fecha.date() < datetime.now().date():
                print("  ⚠ No puedes reservar en una fecha pasada.")
                continue
            return texto
        except ValueError:
            print("  ⚠ Formato inválido. Usa DD-MM-AAAA (ej: 25-09-2026).")


def elegir_opcion(diccionario, titulo):
    """Muestra un menú de opciones (servicios o tipos de vehículo) y retorna la clave elegida."""
    print(f"\n{titulo}")
    for clave, valor in diccionario.items():
        extra = valor.get("precio", valor.get("recargo"))
        etiqueta = "precio" if "precio" in valor else "recargo"
        print(f"  {clave}) {valor['nombre']} (${extra:,.0f} de {etiqueta})")
    while True:
        opcion = input("Elige una opción: ").strip()
        if opcion in diccionario:
            return opcion
        print("  ⚠ Opción inválida, intenta nuevamente.")


def elegir_horario(reservas, fecha):
    """Muestra los horarios disponibles para una fecha y retorna el elegido."""
    ocupados = {r["hora"] for r in reservas if r["fecha"] == fecha and r["estado"] == "activa"}
    disponibles = [h for h in HORARIOS_DISPONIBLES if h not in ocupados]

    if not disponibles:
        return None

    print(f"\nHorarios disponibles para {fecha}:")
    for i, hora in enumerate(disponibles, start=1):
        print(f"  {i}) {hora}")

    while True:
        try:
            opcion = int(input("Elige el número del horario: ").strip())
            if 1 <= opcion <= len(disponibles):
                return disponibles[opcion - 1]
        except ValueError:
            pass
        print("  ⚠ Opción inválida, intenta nuevamente.")


# ---------------------------------------------------------
# Funciones principales del sistema
# ---------------------------------------------------------

def crear_reserva(reservas):
    """Flujo completo para crear una nueva reserva."""
    print("\n--- NUEVA RESERVA ---")
    nombre_cliente = input("Nombre del cliente: ").strip()
    telefono = input("Teléfono de contacto: ").strip()
    patente = input("Patente del vehículo: ").strip().upper()

    fecha = pedir_fecha()

    hora = elegir_horario(reservas, fecha)
    if hora is None:
        print("  ⚠ No quedan horarios disponibles para esa fecha. Elige otra fecha.")
        return

    clave_servicio = elegir_opcion(SERVICIOS, "Servicios disponibles:")
    clave_vehiculo = elegir_opcion(TIPOS_VEHICULO, "Tipo de vehículo:")

    servicio = SERVICIOS[clave_servicio]
    vehiculo = TIPOS_VEHICULO[clave_vehiculo]
    precio_total = servicio["precio"] + vehiculo["recargo"]

    nueva_reserva = {
        "id": len(reservas) + 1,
        "cliente": nombre_cliente,
        "telefono": telefono,
        "patente": patente,
        "fecha": fecha,
        "hora": hora,
        "servicio": servicio["nombre"],
        "vehiculo": vehiculo["nombre"],
        "precio_total": precio_total,
        "estado": "activa",
    }

    reservas.append(nueva_reserva)
    guardar_reservas(reservas)

    print("\n✔ Reserva creada con éxito:")
    imprimir_reserva(nueva_reserva)


def listar_reservas(reservas, solo_activas=True):
    """Muestra todas las reservas (activas por defecto)."""
    filtradas = [r for r in reservas if not solo_activas or r["estado"] == "activa"]

    if not filtradas:
        print("\nNo hay reservas para mostrar.")
        return

    print(f"\n{'ID':<4}{'Fecha':<12}{'Hora':<7}{'Cliente':<20}{'Patente':<10}"
          f"{'Servicio':<30}{'Total':>10}  Estado")
    print("-" * 100)
    for r in filtradas:
        print(f"{r['id']:<4}{r['fecha']:<12}{r['hora']:<7}{r['cliente']:<20}"
              f"{r['patente']:<10}{r['servicio']:<30}${r['precio_total']:>8,.0f}  {r['estado']}")


def cancelar_reserva(reservas):
    """Permite cancelar una reserva activa por su ID."""
    listar_reservas(reservas)
    if not any(r["estado"] == "activa" for r in reservas):
        return

    try:
        id_reserva = int(input("\nID de la reserva a cancelar: ").strip())
    except ValueError:
        print("  ⚠ ID inválido.")
        return

    for r in reservas:
        if r["id"] == id_reserva and r["estado"] == "activa":
            r["estado"] = "cancelada"
            guardar_reservas(reservas)
            print(f"✔ Reserva #{id_reserva} cancelada. El horario queda liberado.")
            return

    print("  ⚠ No se encontró una reserva activa con ese ID.")


def imprimir_reserva(r):
    """Imprime el detalle de una reserva individual."""
    print("-" * 40)
    print(f"  Cliente:   {r['cliente']} ({r['telefono']})")
    print(f"  Vehículo:  {r['vehiculo']} - Patente {r['patente']}")
    print(f"  Fecha:     {r['fecha']} a las {r['hora']}")
    print(f"  Servicio:  {r['servicio']}")
    print(f"  Total:     ${r['precio_total']:,.0f}")
    print("-" * 40)


# ---------------------------------------------------------
# Menú principal
# ---------------------------------------------------------

def mostrar_menu():
    print("\n" + "=" * 45)
    print("     SISTEMA DE RESERVAS - LAVADO DE AUTOS")
    print("=" * 45)
    print("1) Nueva reserva")
    print("2) Ver reservas activas")
    print("3) Ver todas las reservas (incluye canceladas)")
    print("4) Cancelar una reserva")
    print("5) Salir")


def main():
    reservas = cargar_reservas()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            crear_reserva(reservas)
        elif opcion == "2":
            listar_reservas(reservas, solo_activas=True)
        elif opcion == "3":
            listar_reservas(reservas, solo_activas=False)
        elif opcion == "4":
            cancelar_reserva(reservas)
        elif opcion == "5":
            print("¡Hasta pronto!")
            break
        else:
            print("  ⚠ Opción inválida, intenta nuevamente.")


if __name__ == "__main__":
    main()