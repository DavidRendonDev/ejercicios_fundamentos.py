experiencia_L = input("¿tienes experiencia laboral ? (si/no): " )
titulo = input("¿tienes titulo profesional? (si/no): ")


tiene_experiencia = experiencia_L.upper() == 'si'
titulo_profesional = titulo.upper()== 'si'

puede_aplicar = tiene_experiencia and titulo_profesional

while True:
    print("puede aplicar para el trabajo")

else:
    print("NO PUEDES APLICAR VAYA SIGA DURMIENDO")