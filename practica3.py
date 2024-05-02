from datetime import datetime

def obtener_datos_estudiantes(archivo):
    with open(archivo, 'r') as file:
        lineas = file.readlines()
    estudiantes = []
    estudiante = {}
    for linea in lineas:
        if linea.strip() == "":
            if estudiante:  
                estudiantes.append(estudiante)
                estudiante = {}
        else:
            partes = linea.strip().split(": ")
            if len(partes) == 2:  
                clave, valor = partes
                estudiante[clave] = valor
            else:
                print(f"Error: línea no válida: {linea}")
    if estudiante:  
        estudiantes.append(estudiante)
    return estudiantes

def generar_oficio(oficio_template, estudiante):
    with open(oficio_template, 'r') as file:
        template = file.read()
    now = datetime.now().strftime('%Y-%m-%d')
    oficio = template.replace('[Nombre]', estudiante.get('Nombre', ''))
    oficio = oficio.replace('[Apellido Paterno]', estudiante.get('Apellido Paterno', ''))
    oficio = oficio.replace('[Apellido Materno]', estudiante.get('Apellido Materno', ''))
    oficio = oficio.replace('[Fecha de Nacimiento]', estudiante.get('Fecha de Nacimiento', ''))
    oficio = oficio.replace('[Edad]', estudiante.get('Edad', ''))
    oficio = oficio.replace('[Número de Control]', estudiante.get('Número de Control', ''))
    oficio = oficio.replace('[Carrera]', estudiante.get('Carrera', ''))
    oficio = oficio.replace('[Semestre]', estudiante.get('Semestre', ''))
    oficio = oficio.replace('[Nombre del Instituto]', 'Ceti Colomos')
    oficio = oficio.replace('[Fecha de Emisión]', now)
    return oficio

def crear_oficios(estudiantes_archivo, oficio_template, output_folder):
    estudiantes = obtener_datos_estudiantes(estudiantes_archivo)
    for i, estudiante in enumerate(estudiantes, start=1):
        oficio = generar_oficio(oficio_template, estudiante)
        with open(f'{output_folder}/Oficio_{i}.txt', 'w') as file:
            file.write(oficio)

if __name__ == "__main__":
    estudiantes_archivo = 'personas.txt'
    oficio_template = 'oficio_template.txt'
    output_folder = 'oficios'
    crear_oficios(estudiantes_archivo, oficio_template, output_folder)
