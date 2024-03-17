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
    self.add('Filtrar Nodos')
    self.add('Buscar Nodos')

    #frames
    AddDeleteFrame(self.tab('Inserción/Eliminación'), avl_tree, app)
    FilterFrame(self.tab('Filtrar Nodos'))
    SearchFrame(self.tab('Buscar Nodos'))
  


class AddDeleteFrame(ctk.CTkFrame):
  def __init__(self, parent, avl_tree, app):
    super().__init__(parent, fg_color='transparent')
    self.pack(expand=True, fill='both')
    # Define una función que crea una función lambda cuando es invocada
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
  def __init__(self, parent):
    super().__init__(parent, fg_color='transparent')
    self.pack(expand=True, fill='both')

class SearchFrame(ctk.CTkFrame):
  def __init__(self, parent):
    super().__init__(parent, fg_color='transparent')
    self.pack(expand=True, fill='both')

