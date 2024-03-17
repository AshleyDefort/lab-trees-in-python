import os
import random
import graphviz
import tempfile

class Node:
  def __init__(self, name, data, aditional_data):
    self.name = name
    self.data = data
    self.aditional_data = aditional_data
    self.left = None
    self.right = None
    self.height = 1

class AVLTree:
  def __init__(self):
    self.root = None

  def insert(self, root, name, data, aditional_data):
      if not root:
          return Node(name, data, aditional_data)
      elif name < root.name:
          root.left = self.insert(root.left, name, data, aditional_data)
      else:
          root.right = self.insert(root.right, name, data, aditional_data)

      root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

      balance = self.get_balance(root)

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

  def delete(self, root, name):
      if not root:
          return root

      if name < root.name:
          root.left = self.delete(root.left, name)
      elif name > root.name:
          root.right = self.delete(root.right, name)
      else:
          if root.left is None:
              temp = root.right
              root = None
              return temp
          elif root.right is None:
              temp = root.left
              root = None
              return temp

          temp = self.min_value_node(root.right)
          root.name = temp.name
          root.right = self.delete(root.right, temp.name)

      if root is None:
          return root

      root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

      balance = self.get_balance(root)

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

  def search(self, root, name):
      if not root:
          return None
      if root.name == name:
          return root
      if root.name < name:
          return self.search(root.right, name)
      return self.search(root.left, name)

  def search_by_type_and_size_range(self, root, node_list, node_type, size_range):
      if not root:
          return

      if root.data['type'] == node_type and size_range[0] <= root.data['size'] < size_range[1]:
          node_list.append(root)

      self.search_by_type_and_size_range(root.left, node_list, node_type, size_range)
      self.search_by_type_and_size_range(root.right, node_list, node_type, size_range)

  def level_order_traversal(self, root):
      if not root:
          return

      queue = []
      queue.append(root)

      while queue:
          temp_node = queue.pop(0)
          print(temp_node.name)
          if temp_node.left:
              queue.append(temp_node.left)
          if temp_node.right:
              queue.append(temp_node.right)

  def get_height(self, root):
      if not root:
          return 0
      return root.height

  def get_balance(self, root):
      if not root:
          return 0
      return self.get_height(root.left) - self.get_height(root.right)

  def right_rotate(self, z):
      y = z.left
      T3 = y.right

      y.right = z
      z.left = T3

      z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
      y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

      return y

  def left_rotate(self, z):
      y = z.right
      T2 = y.left

      y.left = z
      z.right = T2

      z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
      y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

      return y

  def min_value_node(self, node):
      current = node
      while current.left is not None:
          current = current.left
      return current

  def visualize_tree(self, root):
    if root is None:
      return

    dot = graphviz.Digraph()
    self._visualize_tree(root, dot)
    dot.render('avl_tree', format='png', view=False)
    return 'avl_tree.png'

  def _visualize_tree(self, root, dot):
      if root is not None:
          dot.node(str(root.name), label=str(root.data))
          if root.left is not None:
              dot.edge(str(root.name), str(root.left.name))
              self._visualize_tree(root.left, dot)
          if root.right is not None:
              dot.edge(str(root.name), str(root.right.name))
              self._visualize_tree(root.right, dot)
