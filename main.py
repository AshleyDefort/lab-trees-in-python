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

    # Construir árbol AVL inicial
    self.avl_tree = self.build_initial_avl_tree()

    # Dibujar el árbol AVL inicial
    self.image_widget = ImageWidget(self)
    self.draw_avl_tree(self.avl_tree, self.avl_tree.root)
    self.menu = Menu(self, self.avl_tree, self)

    self.mainloop()
  
  def update_tree_traversal(self, avl_tree, root):
    nodes = avl_tree.level_order_traversal(root)
    self.menu.traversal_frame.node_list = nodes
    self.menu.traversal_frame.draw_traversal()

  def build_initial_avl_tree(self):
    def load_random_images(path):
      dataset = {}
      all_files = []
      for category in os.listdir(path):
          category_path = os.path.join(path, category)
          if os.path.isdir(category_path):
              files = os.listdir(category_path)
              all_files.extend([os.path.join(category_path, file) for file in files])
      random_files = random.sample(all_files, min(7, len(all_files)))
      for file_path in random_files:
          category = os.path.basename(os.path.dirname(file_path))
          file_name = os.path.basename(file_path)
          size = os.path.getsize(file_path)
          if category not in dataset:
              dataset[category] = []
          dataset[category].append({'name': file_name, 'size': size})

      return dataset
    dataset_path = "data"
    dataset = load_random_images(dataset_path)
    avl_tree = AVLTree()
    for category, files in dataset.items():
        for file in files:
            avl_tree.root = avl_tree.insert(avl_tree.root, 
                                            file['name'],
                                            file['name'], 
                                            {'name': file['name'], 'type': category, 'size': file['size']})

    return avl_tree

  def draw_avl_tree(self,avl_tree, root):
    image_path = avl_tree.visualize_tree(root)
    if image_path:
      self.image_widget.show_image(image_path)

App()
