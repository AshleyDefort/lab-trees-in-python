# Laboratorio de Estructura de Datos II - Árboles AVL🌳
Este repositorio contiene una implementación en Python de un árbol AVL que se auto-balancea cada vez que se realiza una acción que lo requiera, como la inserción o eliminación de nodos. El árbol se construye utilizando los nombres de archivos como métrica para realizar las comparaciones.

## Dataset
La información utilizada para construir el árbol proviene del dataset "Images Dataset", que contiene 1803 imágenes divididas en 7 categorías: Bike, Cars, Cats, Dogs, Flowers, Horses y Human.

## Funcionalidades del Árbol
El árbol generado permite realizar las siguientes operaciones:
1. **Inserción de un Nodo:** Permite agregar un nuevo nodo al árbol.
2. **Eliminación de un Nodo:** Permite eliminar un nodo existente del árbol.
3. **Búsqueda de un Nodo:** Permite buscar un nodo utilizando la métrica dada (nombre del archivo).
4. **Filtrado de Nodos:** Permite buscar todos los nodos que cumplan con ciertos criterios, como pertenecer a una categoría específica o tener un tamaño de archivo dentro de un rango específico.
5. **Recorrido por Niveles del Árbol:** Permite mostrar el recorrido por niveles del árbol de manera recursiva, mostrando únicamente los nombres de los archivos.

## Operaciones con Nodos
Una vez obtenidos los nodos mediante las operaciones de búsqueda y filtrado, se pueden realizar las siguientes operaciones:
- **Obtener el Nivel del Nodo:** Permite conocer la profundidad del nodo en el árbol.
- **Obtener el Factor de Balanceo del Nodo:** Permite conocer el equilibrio del nodo en el árbol.
- **Encontrar el Padre del Nodo:** Permite identificar el padre del nodo seleccionado.
- **Encontrar el Abuelo del Nodo:** Permite identificar el abuelo del nodo seleccionado.
- **Encontrar el Tío del Nodo:** Permite identificar el tío del nodo seleccionado.

## Visualización del Árbol
Después de cada operación de inserción o eliminación, el árbol se muestra gráficamente utilizando la biblioteca graphviz en Python. Cada nodo del árbol contiene la información correspondiente al dataset.

## Estructura del Proyecto
- `avl_tree.py`: Contiene la implementación del árbol AVL con los métodos correspondientes a las funcionalidades y operaciones con nodos descritas anteriormente.
- `dataset.py`: Contiene las funciones para cargar los datos del dataset, verificar si un archivo existe en el dataset y retornar la información de una imagen con su nombre.
- `menu.py`: Contiene la interfaz de usuario para interactuar con el árbol.
- `panels.py`: Contiene las clases para los paneles de la interfaz de usuario.
- `main.py`: Script principal para ejecutar la aplicación. Aquí se inicializa la interfaz de la app y se genera un árbol inicial que consta de 7 nodos.
- `image_widget.py`: Contiene la clase para crear el widget con la imagen del árbol.
- `/data`: Carpeta que contiene todas las imágenes del dataset.

