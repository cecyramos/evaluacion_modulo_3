# Evaluación del módulo
__Objetivo__

En esta actividad, desarrollarás una aplicación de línea de comandos que permitirá gestionar tareas de manera sencilla. Con este proyecto, aplicarás conocimientos fundamentales de Python, incluyendo el uso de estructuras de datos, funciones, control de flujo y módulos.

__Contexto__

Imagina que eres un desarrollador que necesita una herramienta ligera para organizar sus pendientes diarios desde la terminal. No quieres depender de aplicaciones externas ni de herramientas visuales avanzadas, sino algo simple y funcional que puedas ejecutar en cualquier sistema con Python instalado.

Para ello, construirás una aplicación que permita al usuario agregar tareas, verlas, marcarlas como completadas y eliminarlas. Además, las tareas deberán guardarse en un archivo para que no se pierdan cuando se cierre el programa.

__Requisitos del Proyecto__

1. __Menú interactivo__

* La aplicación debe mostrar un menú en la consola con opciones numéricas para que el usuario pueda elegir qué acción realizar.

2. __Operaciones básicas:__

* Agregar una nueva tarea.

* Listar todas las tareas con un indicador de estado (Pendiente o Completada).

* Marcar una tarea como completada.

* Eliminar una tarea.

* Salir del programa.

3. __Estructuras de datos__

* Utilizar diccionarios para representar cada tarea.

* Usar una lista para almacenar todas las tareas.

4. __Funciones__

* Dividir el código en funciones reutilizables para cada operación.

5. __Validaciones y manejo de errores__

* Evitar errores al ingresar opciones no válidas.

* Manejar archivos de manera segura para evitar pérdidas de datos.

__Ejemplo de Uso__

Cuando el usuario ejecute el programa, verá un menú como el siguiente:

--- Gestor de Tareas ---
1. Agregar tarea
2. Ver tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
Elige una opción: 

Al seleccionar una opción se ejecuta el código detrás de esa opción volvemos al menu hasta que el usuario seleccione Salir.
