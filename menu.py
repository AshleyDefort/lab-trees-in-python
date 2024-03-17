from panels import *
import customtkinter as ctk
from tkinter import messagebox
from dataset import load_all_images, is_file_in_dataset, get_file_data_by_name

class Menu(ctk.CTkTabview):
  def __init__(self, parent, avl_tree, app):
    super().__init__(parent)
    self.grid(row=0, column=0, sticky='nsew')

    #tabs
    self.add('Inserción/Eliminación')
    self.add('Buscar Nodo')
    self.add('Filtrar Nodos')
    self.add('Recorridos')

    #frames
    AddDeleteFrame(self.tab('Inserción/Eliminación'), avl_tree, app)
    SearchFrame(self.tab('Buscar Nodo'), avl_tree)
    FilterFrame(self.tab('Filtrar Nodos'), avl_tree)
    TraversalFrame(self.tab('Recorridos'), avl_tree)
  


class AddDeleteFrame(ctk.CTkFrame):
  def __init__(self, parent, avl_tree, app):
    super().__init__(parent, fg_color='transparent')
    self.pack(expand=True, fill='both')

    def make_insert_command(entry):
        return lambda: self.insert_node(avl_tree, app, entry)
    
    def make_delete_command(entry):
        return lambda: self.delete_node(avl_tree, app, entry)
    
    SliderPanel(self, 'Ingrese el nombre del nodo a insertar: ', 'Insertar Nodo', make_insert_command)
    SliderPanel(self, 'Ingrese el nombre del nodo a eliminar: ', 'Eliminar Nodo', make_delete_command)

  def insert_node(self, avl_tree, app, entry):
    dataset = load_all_images('data')
    node_name = entry.get()
    if avl_tree.search(avl_tree.root, node_name) is not None:
      messagebox.showerror('Error', f'El nodo con nombre {node_name} ya existe en el árbol')
      entry.delete(0, 'end')
    elif is_file_in_dataset(dataset, node_name):
      node_data, category = get_file_data_by_name(dataset, node_name)
      avl_tree.insert(avl_tree.root, node_name, node_name, node_data)
      entry.delete(0, 'end')
      app.draw_avl_tree()
    else:
      messagebox.showerror('Error', f'El nodo con nombre {node_name} no existe en el dataset')
      entry.delete(0, 'end')

  def delete_node(self, avl_tree, app, entry):
    node_name = entry.get()
    if avl_tree.search(avl_tree.root, node_name) is None:
      messagebox.showerror('Error', f'El nodo con nombre {node_name} no existe en el árbol')
      entry.delete(0, 'end')
      return
    avl_tree.delete(avl_tree.root, node_name)

class FilterFrame(ctk.CTkFrame):
  def __init__(self, parent, avl_tree):
    super().__init__(parent, fg_color='transparent')
    self.pack(expand=True, fill='both')

    def filter_command(option, min_size, max_size):
      return lambda: self.filter_nodes(avl_tree, option, min_size, max_size)
    
    FilterPanel(self, filter_command)
  
  def filter_nodes(self, avl_tree, option, min_size, max_size):
    category = option.get()
    min_size = min_size.get()
    max_size = max_size.get()
    if min_size == '' or max_size == '':
      messagebox.showerror('Error', 'Debe ingresar un valor para los tamaños mínimo y máximo')
      return
    if not min_size.isdigit() or not max_size.isdigit():
      messagebox.showerror('Error', 'Los valores de tamaño mínimo y máximo deben ser números enteros')
      return
    min_size = int(min_size)
    max_size = int(max_size)
    node_list = []
    if min_size > max_size:
      messagebox.showerror('Error', 'El tamaño mínimo no puede ser mayor que el tamaño máximo')
      return
    avl_tree.filter_nodes(avl_tree.root, node_list, category, min_size, max_size)
    if len(node_list) == 0:
      messagebox.showinfo('Información', 'No se encontraron nodos que cumplan con los criterios de búsqueda')
    else:
      FilteredNodes(self, node_list, avl_tree)

    return 

class SearchFrame(ctk.CTkFrame):
  def __init__(self, parent, avl_tree):
    super().__init__(parent, fg_color='transparent')
    self.pack(expand=True, fill='both')

    def search_command(entry):
      return lambda: self.search_node(entry, avl_tree)
    
    SearchPanel(self, 'Ingrese el nombre del nodo a buscar: ', search_command)

  def search_node(self, entry, avl_tree):
    node_name = entry.get()
    if avl_tree.search(avl_tree.root, node_name) is not None:
      nivel = avl_tree.get_node_level(avl_tree.root, node_name)
      balance = avl_tree.get_balance(avl_tree.search(avl_tree.root, node_name))
      node_parent = avl_tree.get_node_parent(avl_tree.root, node_name)
      grandparent = avl_tree.get_node_grandparent(avl_tree.root, node_name)
      uncle = avl_tree.get_node_uncle(avl_tree.root, node_name)
      InfoPanel(self, nivel, balance, node_parent, grandparent, uncle)
      ClearButtonPanel(self)
    else:
      messagebox.showerror('Error', f'El nodo con nombre {node_name} no existe en el árbol')
      entry.delete(0, 'end')
    return
  
class TraversalFrame(ctk.CTkFrame):
  def __init__(self, parent, avl_tree):
    super().__init__(parent, fg_color='transparent')
    self.pack(expand=True, fill='both')
    level_order_traversal_list = []
    node_list = avl_tree.level_order_traversal(avl_tree.root, level_order_traversal_list)
    TraversalPanel(self, node_list=level_order_traversal_list)


