from avl import AVLTree
from image_widget import ImageWidget
import customtkinter as ctk
import os
import random
from menu import Menu

class App(ctk.CTk):
  def __init__(self):
    super().__init__()
    ctk.set_appearance_mode('light')
    ctk.set_default_color_theme('green')
    self.geometry('1000x400')
    self.title('Árbol AVL')
    self.minsize(800, 400)

    self.rowconfigure(0, weight=1)
    self.columnconfigure(0, weight=4, uniform='a')
    self.columnconfigure(1, weight=6, uniform='a')

    self.avl_tree = AVLTree()
    # Dibujar el árbol AVL inicial
    self.image_widget = ImageWidget(self)
    self.menu = Menu(self, self.avl_tree, self)

    self.mainloop()
  
  # Método para actualizar el recorrido del árbol
  def update_tree_traversal(self, avl_tree, root):
    nodes = avl_tree.level_order_traversal(root)
    self.menu.traversal_frame.node_list = nodes
    self.menu.traversal_frame.draw_traversal()


  # Método para dibujar el árbol AVL
  def draw_avl_tree(self,avl_tree, root):
    image_path = avl_tree.visualize_tree(root)
    if image_path:
      self.image_widget.show_image(image_path)

App()
