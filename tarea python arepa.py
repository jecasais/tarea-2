# Función para convertir las cantidades de ingredientes a volumen (en cucharaditas)
def convertir_a_volumen(agua, harina, sal, aceite):
    cda_to_cdta = 3
    tza_to_cda = 16
    
    volumen_agua = agua * tza_to_cda * cda_to_cdta
    volumen_harina = harina * tza_to_cda * cda_to_cdta
    volumen_sal = sal
    volumen_aceite = aceite * cda_to_cdta
    
    return volumen_agua + volumen_harina + volumen_sal + volumen_aceite

# Función para calcular el volumen final después de la evaporación
def volumen_final(volumen_inicial):
    evaporacion = 0.10
    return volumen_inicial * (1 - evaporacion)

# Solicitud de cantidades de ingredientes al usuario
print("Ingrese la cantidad de ingredientes para una arepa:")
agua = float(input("Agua (en tazas): "))
harina = float(input("Harina PAN (en tazas): "))
sal = float(input("Sal (en cucharaditas): "))
aceite = float(input("Aceite (en cucharadas): "))

# Calculando el volumen inicial y final
volumen_inicial = convertir_a_volumen(agua, harina, sal, aceite)
volumen_arepa = volumen_final(volumen_inicial)

# Mostrando el resultado
print(f"El volumen de la arepa terminada es aproximadamente {volumen_arepa:.2f} cucharaditas.")
