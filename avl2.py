import csv

# Definición de la clase Nodo AVL
class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

# Definición de la clase Árbol AVL
class AVLTree:
    def __init__(self):
        self.root = None

    # Operación de inserción en el árbol
    def insert(self, data):
        if not self.root:
            self.root = AVLNode(data)
        else:
            self.root = self._insert(self.root, data)

    # Función auxiliar para la inserción recursiva
    def _insert(self, node, data):
        if not node:
            return AVLNode(data)
        elif data['name'] < node.data['name']:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        # Actualización de la altura del nodo
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Balanceo del árbol después de la inserción
        balance = self._get_balance(node)

        # Casos de rotación para mantener el balance
        if balance > 1 and data['name'] < node.left.data['name']:
            return self._rotate_right(node)
        if balance < -1 and data['name'] > node.right.data['name']:
            return self._rotate_left(node)
        if balance > 1 and data['name'] > node.left.data['name']:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and data['name'] < node.right.data['name']:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # Rotación hacia la izquierda
    def _rotate_left(self, z):
        y = z.right
        T3 = y.left

        y.left = z
        z.right = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    # Rotación hacia la derecha
    def _rotate_right(self, z):
        y = z.left
        T2 = y.right

        y.right = z
        z.left = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    # Obtener la altura de un nodo
    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    # Obtener el factor de balance de un nodo
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # Recorrido por niveles del árbol
    def _level_order_traversal(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            result.append(node.data['name'])

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result

    def level_order_traversal(self):
        return self._level_order_traversal(self.root)

    # Búsqueda de un nodo por nombre
    def search(self, name):
        return self._search(self.root, name)

    def _search(self, node, name):
        if not node:
            return None
        elif node.data['name'] == name:
            return node
        elif name < node.data['name']:
            return self._search(node.left, name)
        else:
            return self._search(node.right, name)

    # Eliminación de un nodo por nombre
    def remove(self, name):
        self.root = self._remove(self.root, name)

    def _remove(self, node, name):
        if not node:
            return None
        elif name < node.data['name']:
            node.left = self._remove(node.left, name)
        elif name > node.data['name']:
            node.right = self._remove(node.right, name)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._remove(node.right, temp.data['name'])

        if not node:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Obtener el nivel de un nodo por nombre
    def get_node_level(self, name):
        return self._get_node_level(self.root, name, 1)

    def _get_node_level(self, node, name, level):
        if not node:
            return 0
        if node.data['name'] == name:
            return level
        down_level = self._get_node_level(node.left, name, level + 1)
        if down_level != 0:
            return down_level
        down_level = self._get_node_level(node.right, name, level + 1)
        return down_level

    # Obtener el factor de balance de un nodo por nombre
    def get_balance_factor(self, name):
        node = self.search(name)
        if node:
            return self._get_balance(node)
        return None

    # Encontrar el padre de un nodo por nombre
    def find_parent(self, name):
        return self._find_parent(self.root, name)

    def _find_parent(self, node, name):
        if not node:
            return None
        if (node.left and node.left.data['name'] == name) or (node.right and node.right.data['name'] == name):
            return node
        left_parent = self._find_parent(node.left, name)
        if left_parent:
            return left_parent
        return self._find_parent(node.right, name)

    # Encontrar el abuelo de un nodo por nombre
    def find_grandparent(self, name):
        parent = self.find_parent(name)
        if parent:
            return self.find_parent(parent.data['name'])
        return None

    # Encontrar el tío de un nodo por nombre
    def find_uncle(self, name):
        grandparent = self.find_grandparent(name)
        if grandparent:
            if grandparent.left and grandparent.left.data['name'] == name:
                return grandparent.right
            elif grandparent.right and grandparent.right.data['name'] == name:
                return grandparent.left
        return None

    # Búsqueda de nodos que cumplan un criterio específico
    def search_by_criteria(self, category, min_size, max_size):
        results = []
        self._search_by_criteria(self.root, category, min_size, max_size, results)
        return results

    def _search_by_criteria(self, node, category, min_size, max_size, results):
        if not node:
            return
        if node.data['type'] == category and min_size <= node.data['size'] < max_size:
            results.append(node.data)
        self._search_by_criteria(node.left, category, min_size, max_size, results)
        self._search_by_criteria(node.right, category, min_size, max_size, results)

