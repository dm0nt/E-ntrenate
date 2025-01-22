# Función para convertir horas a otras unidades de tiempo
def convertir_tiempo(horas):
    dias = horas / 24  # Convertimos horas a días
    return dias

# Función principal que calcula el tiempo total de inversión
def calcular_tiempo(frecuencia, duracion, intensidad):
    # Lista de intensidades con las horas correspondientes
    intensidades = {"baja": 0.5, "moderada": 1, "alta": 2}

    # Obtenemos las horas correspondientes a la intensidad seleccionada
    inversion_diaria = intensidades.get(intensidad, 0)

    # Si la frecuencia es diaria, el cálculo es simple: multiplicar por la cantidad de días
    if frecuencia == "diaria":
        tiempo_total_horas = inversion_diaria * duracion
        tiempo_total_dias = convertir_tiempo(tiempo_total_horas)
    
    # Si la frecuencia es semanal, multiplicamos las horas diarias por 7 (días por semana)
    elif frecuencia == "semanal":
        tiempo_total_horas = inversion_diaria * 7 * duracion
        tiempo_total_dias = convertir_tiempo(tiempo_total_horas)

    # Mostrar el tiempo total con la intensidad aplicada
    print(f"Con una inversión de {inversion_diaria} horas por {frecuencia}, durante {duracion} {'día(s)' if frecuencia == 'diaria' else 'semana(s)'}:")
    print(f"Total de horas invertidas: {tiempo_total_horas:.2f} horas.")
    print(f"Total de días invertidos: {tiempo_total_dias:.2f} días.")

    # Cálculo de la intensidad aplicada
    if intensidad == "baja":
        print("Intensidad baja: Se recomienda un enfoque relajado y progresivo.")
    elif intensidad == "moderada":
        print("Intensidad moderada: Puedes desafiarte un poco más y mejorar rápidamente.")
    elif intensidad == "alta":
        print("Intensidad alta: Practicarás mucho y de forma intensiva para progresar rápidamente.")

# Solicitar datos al usuario
def main():
    print("¡Bienvenido al programa para calcular el tiempo invertido en tu hobby!")
    
    # Solicitar frecuencia (diaria o semanal)
    frecuencia = input("¿Qué frecuencia prefieres? (diaria o semanal): ").lower()
    
    # Solicitar duración (días o semanas)
    duracion = int(input(f"¿Cuántos {frecuencia}s planeas practicar? "))
    
    # Solicitar intensidad (baja, moderada, alta)
    intensidad = input("¿Cuál es la intensidad de tu práctica? (baja, moderada, alta): ").lower()
    
    # Llamar a la función de cálculo
    calcular_tiempo(frecuencia, duracion, intensidad)

# Ejecutar el programa
if __name__ == "__main__":
    main()
