import os
import random
import graphviz
import tempfile

#Clase para crear los nodos del árbol AVL
class Node:
  def __init__(self, name, data, aditional_data):
    self.name = name
    self.data = data
    self.aditional_data = aditional_data
    self.left = None
    self.right = None
    self.height = 1

#Clase para implementar el árbol AVL
class AVLTree:
  def __init__(self):
    self.root = None

  #Método para insertar un nodo en el árbol AVL
  def insert(self, root, name, data, aditional_data):
      print(name)
      if not root:
          #Si el árbol está vacío, se crea un nuevo nodo
          return Node(name, data, aditional_data)
      elif name < root.name:
          #Si el nombre del nodo a insertar es menor que el nombre del nodo actual, se inserta en el subárbol izquierdo
          root.left = self.insert(root.left, name, data, aditional_data)
      else:
          #Si el nombre del nodo a insertar es mayor que el nombre del nodo actual, se inserta en el subárbol derecho
          root.right = self.insert(root.right, name, data, aditional_data)
      #Se actualiza la altura del nodo actual
      root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
      #Se obtiene el factor de equilibrio del nodo actual
      balance = self.get_balance(root)
      #Se rebalancea el árbol si es necesario
      if balance > 1 and name < root.left.name:
          return self.right_rotate(root)
      if balance < -1 and name > root.right.name:
          return self.left_rotate(root)
      if balance > 1 and name > root.left.name:
          root.left = self.left_rotate(root.left)
          return self.right_rotate(root)
      if balance < -1 and name < root.right.name:
          root.right = self.right_rotate(root.right)
          return self.left_rotate(root)

      return root

  #Método para eliminar un nodo del árbol AVL
  def delete(self, root, name):
    if not root:
        # Si el árbol está vacío, no se realiza ninguna operación
        return root
    
    # Realizar la eliminación como en un ABB
    if name < root.name:
        root.left = self.delete(root.left, name)
    elif name > root.name:
        root.right = self.delete(root.right, name)
    else:
        # Caso de eliminación de un nodo con un solo hijo o sin hijos
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
          
        # Caso de eliminación de un nodo con dos hijos
        temp = self.min_value_node(root.right)
        root.name = temp.name
        root.data = temp.data
        root.aditional_data = temp.aditional_data
        root.right = self.delete(root.right, temp.name)
      
    # Actualizar la altura del nodo actual
    root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
    
    # Obtener el factor de equilibrio del nodo actual
    balance = self.get_balance(root)

    # Rebalancear el árbol si es necesario
    if balance > 1 and self.get_balance(root.left) >= 0:
        return self.right_rotate(root)
    if balance < -1 and self.get_balance(root.right) <= 0:
        return self.left_rotate(root)
    if balance > 1 and self.get_balance(root.left) < 0:
        root.left = self.left_rotate(root.left)
        return self.right_rotate(root)
    if balance < -1 and self.get_balance(root.right) > 0:
        root.right = self.right_rotate(root.right)
        return self.left_rotate(root)

    return root

  #Método para buscar un nodo en el árbol AVL
  def search(self, root, name):
      if not root:
          # Si el árbol está vacío, se retorna None
          return None
      if root.name == name:
          # Si el nombre del nodo actual es igual al nombre buscado, se retorna el nodo actual
          return root
      if root.name < name:
          # Si el nombre del nodo actual es menor que el nombre buscado, se busca en el subárbol derecho
          return self.search(root.right, name)
      # Si el nombre del nodo actual es mayor que el nombre buscado, se busca en el subárbol izquierdo
      return self.search(root.left, name)

  #Método para filtrar los nodos del árbol AVL según un tipo y un rango de tamaños
  def filter_nodes(self, root, node_list, node_type, minsize, maxsize):
      if not root:
          # Si el árbol está vacío, no se realiza ninguna operación
          return

      if root.aditional_data['type'] == node_type and minsize <= root.aditional_data['size'] < maxsize:
          # Si el nodo actual cumple con las condiciones, se agrega a la lista de nodos
          node_list.append(root.name)
      
      # Se filtran los nodos del subárbol izquierdo
      self.filter_nodes(root.left, node_list, node_type, minsize, maxsize)
      # Se filtran los nodos del subárbol derecho
      self.filter_nodes(root.right, node_list, node_type, minsize, maxsize)

  #Método para recorrer el árbol AVL en orden
  def level_order_traversal(self, root):
    if not root:
      # Si el árbol está vacío, se retorna una lista vacía
      return []

    # Se inicializa una lista para almacenar los nodos del recorrido
    result = []
    # Se obtiene la altura del árbol
    height = self.get_height(root)
    # Se recorre el árbol por niveles
    for i in range(1, height + 1):
        self._level_order_traversal(root, i, result)
    return result

  #Método auxiliar para recorrer el árbol AVL por niveles
  def _level_order_traversal(self, root, level, result):
      if not root:
          # Si el nodo actual es None, no se realiza ninguna operación
          return
      if level == 1:
          # Si el nivel actual es 1, se agrega el nombre del nodo actual a la lista de nodos
          result.append(root.name)
      elif level > 1:
          # Si el nivel actual es mayor que 1, se recorren los subárboles izquierdo y derecho
          self._level_order_traversal(root.left, level - 1, result)
          self._level_order_traversal(root.right, level - 1, result)
          
  #Método para obtener la altura de un nodo del árbol AVL
  def get_height(self, root):
      if not root:
          return 0
      return root.height

  #Método para obtener el factor de equilibrio de un nodo del árbol AVL
  def get_balance(self, root):
    if not root:
      # Si el nodo es None, se retorna 0
      return 0
    # Se retorna la diferencia entre la altura del subárbol izquierdo y la altura del subárbol derecho
    return self.get_height(root.left) - self.get_height(root.right)

  #Método para realizar una rotación a la derecha en el árbol AVL
  def right_rotate(self, z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
    y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    return y

  #Método para realizar una rotación a la izquierda en el árbol AVL
  def left_rotate(self, z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
    y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

    return y

  #Método para obtener el nodo con el valor mínimo en un subárbol (sucesor)
  def min_value_node(self, node):
      current = node
      while current.left is not None:
          current = current.left
      return current

  #Método para visualizar el árbol AVL
  def visualize_tree(self, root):
    if root is None:
      # Si el árbol está vacío, no se realiza ninguna operación
      return
    # Se crea un objeto de la clase Digraph de Graphviz
    dot = graphviz.Digraph()
    # Se llama al método auxiliar para visualizar el árbol
    self._visualize_tree(root, dot)
    # Se crea un archivo temporal para almacenar la imagen del árbol
    dot.render('avl_tree', format='png', view=False)
    # Se retorna la ruta del archivo temporal
    return 'avl_tree.png'

  #Método auxiliar para visualizar el árbol AVL
  def _visualize_tree(self, root, dot):
      if root is not None:
          # Se agrega el nodo actual al grafo
          dot.node(str(root.name), label=str(root.data))
          if root.left is not None:
              # Si el nodo actual tiene un hijo izquierdo, se agrega la arista correspondiente
              dot.edge(str(root.name), str(root.left.name))
              self._visualize_tree(root.left, dot)
          if root.right is not None:
              # Si el nodo actual tiene un hijo derecho, se agrega la arista correspondiente
              dot.edge(str(root.name), str(root.right.name))
              self._visualize_tree(root.right, dot)

  #Método para obtener el nivel de un nodo en el árbol AVL
  def get_node_level(self, root, name):
    if not root:
      # Si el árbol está vacío, se retorna -1
      return -1
    if root.name == name:
      # Si el nombre del nodo actual es igual al nombre buscado, se retorna 0
      return 0
    if root.name < name:
      # Si el nombre del nodo actual es menor que el nombre buscado, se busca en el subárbol derecho
      return 1 + self.get_node_level(root.right, name)
    # Si el nombre del nodo actual es mayor que el nombre buscado, se busca en el subárbol izquierdo
    return 1 + self.get_node_level(root.left, name)
      
  #Método para obtener el padre de un nodo en el árbol AVL
  def get_node_parent(self, root, name):
    if not root:
      # Si el árbol está vacío, se retorna None
      return None
    if root.left and root.left.name == name:
      # Si el hijo izquierdo del nodo actual tiene el nombre buscado, se retorna el nombre del nodo actual
      return root.name
    if root.right and root.right.name == name:
      # Si el hijo derecho del nodo actual tiene el nombre buscado, se retorna el nombre del nodo actual
      return root.name
    if root.name < name:
      # Si el nombre del nodo actual es menor que el nombre buscado, se busca en el subárbol derecho
      return self.get_node_parent(root.right, name)
    # Si el nombre del nodo actual es mayor que el nombre buscado, se busca en el subárbol izquierdo
    return self.get_node_parent(root.left, name)

  #Método para obtener el abuelo de un nodo en el árbol AVL
  def get_node_grandparent(self, root, name):
      # Se obtiene el nombre del padre del nodo actual
      parent_name = self.get_node_parent(root, name)
      if parent_name:
        # Si el nodo actual tiene padre, se obtiene el nombre del abuelo
        return self.get_node_parent(root, parent_name)
      return None 

  def get_node_uncle(self, root, name):
      # Se obtiene el nombre del abuelo del nodo actual
      grandparent_name = self.get_node_grandparent(root, name)
      # Se obtiene el nombre del padre del nodo actual
      parent_name = self.get_node_parent(root, name) 
      if grandparent_name:
        # Si el nodo actual tiene abuelo, se busca al nodo abuelo
        grandparent = self.search(root, grandparent_name)
        if grandparent:
          # Si el hijo izquierdo del abuelo tiene el nombre del padre, se retorna el nombre del hijo derecho
          if grandparent.left and grandparent.left.name == parent_name:
            return grandparent.right.name 
          # Si el hijo derecho del abuelo tiene el nombre del padre, se retorna el nombre del hijo izquierdo
          elif grandparent.right: 
            return grandparent.left.name 
      return None
