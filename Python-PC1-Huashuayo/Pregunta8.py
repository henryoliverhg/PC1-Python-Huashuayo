from datetime import datetime
ingresa_hora = input("Ingrese la hora actual en formato de 24hrs (ejemplo: 19:35): ")
hora = datetime.strptime(ingresa_hora, "%H:%M").time()

inicio_desayuno = datetime.strptime("7:00", "%H:%M").time()
fin_desayuno = datetime.strptime("8:00", "%H:%M").time()
inicio_almuerzo = datetime.strptime("12:00", "%H:%M").time()
fin_almuerzo = datetime.strptime("13:00", "%H:%M").time()
inicio_cena = datetime.strptime("18:00", "%H:%M").time()
fin_cena = datetime.strptime("19:00", "%H:%M").time()

if inicio_desayuno <= hora <= fin_desayuno:
    print("Es hora del desayno")
elif inicio_almuerzo <= hora <= fin_almuerzo:
    print("Es hora del almuerzo")
elif inicio_cena <= hora <= fin_cena:
    print("Es hora de la cena")
