
'''
python

'''

'''
plamificacion

-crear un usuario para almacenar sus datos
-la funcionalidad de este proyecto va guiada principalmente a la gestion de tareas, entre sus principales funcionalidades encontramos. 
-añadir: el usuario podra agragar una tarea a su lista.
-editar: el usuario tendrá la capacidad de editar cualquier tarea.
-marcar: el usuario puede marcar una tarea como "completada".
-listar: el programa le permitirá ver todas las tareas en lista, a su vez que podra ver si una tarea se encuentra completa o incompleta. 
-eliminar: el usuario podra eliminar la tarea que desee.
-guardar: el usuario podrá guardar la lista de tareas en un archivo.
-cargar: el usuario podra cargar suis tareas desde el archivo donde se encunentren almacenadas.

'''


import json
import os

# Ruta del archivo de usuarios y tareas
USERS_FILE = 'usuarios.json'

# Cargar los datos desde el archivo JSON
def cargar_usuarios():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as archivo:
            return json.load(archivo)
    return {}

# Guardar los datos en el archivo JSON
def guardar_usuarios(usuarios):
    with open(USERS_FILE, 'w') as archivo:
        json.dump(usuarios, archivo, indent=4)

# Registrar un nuevo usuario
def registrar_usuario():
    usuarios = cargar_usuarios()
    usuario = input('Nombre de usuario: ')
    
    if usuario in usuarios:
        print('El usuario ya existe. Intenta iniciar sesión.')
        return None
    
    contraseña = input('Contraseña: ')
    usuarios[usuario] = {'contraseña': contraseña, 'tareas': []}
    guardar_usuarios(usuarios)
    print(f'Usuario "{usuario}" registrado exitosamente.')
    return usuario

# Iniciar sesión con un usuario existente
def iniciar_sesion():
    usuarios = cargar_usuarios()
    usuario = input('Nombre de usuario: ')
    
    if usuario not in usuarios:
        print('Usuario no encontrado. Regístrate primero.')
        return None
    
    contraseña = input('Contraseña: ')
    if usuarios[usuario]['contraseña'] == contraseña:
        print(f'Bienvenido, {usuario}.')
        return usuario
    else:
        print('Contraseña incorrecta.')
        return None

# Agregar una nueva tarea
def agregar_tarea(usuario):
    usuarios = cargar_usuarios()
    titulo = input('Título de la tarea: ')
    tarea = {'titulo': titulo, 'completada': False}
    usuarios[usuario]['tareas'].append(tarea)
    guardar_usuarios(usuarios)
    print(f'Tarea "{titulo}" agregada para el usuario {usuario}.')

# Listar todas las tareas del usuario
def listar_tareas(usuario):
    usuarios = cargar_usuarios()
    tareas = usuarios[usuario]['tareas']
    
    # Ordenar las tareas por título en orden alfabético
    tareas_ordenadas = sorted(tareas, key=lambda t: t['titulo'])
    
    if tareas_ordenadas:
        for i, tarea in enumerate(tareas_ordenadas, 1):
            estado = '✔️' if tarea['completada'] else '❌'
            print(f'{i}. {tarea["titulo"]} - {estado}')
    else:
        print('No tienes tareas.')

# Marcar una tarea como completada
def completar_tarea(usuario, indice):
    usuarios = cargar_usuarios()
    tareas = usuarios[usuario]['tareas']
    
    if 0 <= indice < len(tareas):
        tareas[indice]['completada'] = True
        guardar_usuarios(usuarios)
        print(f'Tarea "{tareas[indice]["titulo"]}" marcada como completada.')
    else:
        print('Índice de tarea inválido.')

# Eliminar una tarea
def eliminar_tarea(usuario, indice):
    usuarios = cargar_usuarios()
    tareas = usuarios[usuario]['tareas']
    
    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        guardar_usuarios(usuarios)
        print(f'Tarea "{tarea_eliminada["titulo"]}" eliminada.')
    else:
        print('Índice de tarea inválido.')

# Menú principal
def mostrar_menu():
    print('\nGestor de Tareas')
    print('1. Agregar tarea')
    print('2. Listar tareas')
    print('3. Completar tarea')
    print('4. Eliminar tarea')
    print('5. Cerrar sesión')

def main():
    print('1. Iniciar sesión')
    print('2. Registrarse')
    opcion = input('Selecciona una opción: ')
    
    usuario = None
    if opcion == '1':
        usuario = iniciar_sesion()
    elif opcion == '2':
        usuario = registrar_usuario()

    if not usuario:
        return

    while True:
        mostrar_menu()
        opcion = input('Selecciona una opción: ')
        
        if opcion == '1':
            agregar_tarea(usuario)
        elif opcion == '2':
            listar_tareas(usuario)
        elif opcion == '3':
            listar_tareas(usuario)
            indice = int(input('Índice de la tarea a completar: ')) - 1
            completar_tarea(usuario, indice)
        elif opcion == '4':
            listar_tareas(usuario)
            indice = int(input('Índice de la tarea a eliminar: ')) - 1
            eliminar_tarea(usuario, indice)
        elif opcion == '5':
            print(f'Cerrando sesión de {usuario}.')
            break
        else:
            print('Opción inválida. Inténtalo de nuevo.')

# Ruta del archivo de tareas
TASKS_FILE = 'tareas.json'

# Cargar las tareas desde el archivo JSON
def cargar_tareas():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as archivo:
            return json.load(archivo)
    return []

# Guardar las tareas en el archivo JSON
def guardar_tareas(tareas):
    with open(TASKS_FILE, 'w') as archivo:
        json.dump(tareas, archivo, indent=4)

# Agregar una nueva tarea
def agregar_tarea_global(titulo):
    tareas = cargar_tareas()
    tarea = {
        'titulo': titulo,
        'completada': False
    }
    tareas.append(tarea)
    guardar_tareas(tareas)
    print(f'Tarea "{titulo}" agregada.')

# Listar todas las tareas
def listar_tareas_global():
    tareas = cargar_tareas()
    
    # Ordenar las tareas por título en orden alfabético
    tareas_ordenadas = sorted(tareas, key=lambda t: t['titulo'])
    
    if tareas_ordenadas:
        for i, tarea in enumerate(tareas_ordenadas, 1):
            estado = '✔️' if tarea['completada'] else '❌'
            print(f'{i}. {tarea["titulo"]} - {estado}')
    else:
        print('No hay tareas.')

# Marcar una tarea como completada
def completar_tarea_global(indice):
    tareas = cargar_tareas()
    if 0 <= indice < len(tareas):
        tareas[indice]['completada'] = True
        guardar_tareas(tareas)
        print(f'Tarea "{tareas[indice]["titulo"]}" marcada como completada.')
    else:
        print('Índice de tarea inválido.')

# Eliminar una tarea
def eliminar_tarea_global(indice):
    tareas = cargar_tareas()
    if 0 <= indice < len(tareas):
        tarea_eliminada = tareas.pop(indice)
        guardar_tareas(tareas)
        print(f'Tarea "{tarea_eliminada["titulo"]}" eliminada.')
    else:
        print('Índice de tarea inválido.')

if __name__ == '__main__':
    main()
