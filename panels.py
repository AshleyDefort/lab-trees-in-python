import customtkinter as ctk

class Panel(ctk.CTkFrame):
  def __init__(self, parent):
    super().__init__(parent, fg_color='#EEEEEE')
    self.pack(fill='x', pady=4, ipady=8)

class SliderPanel(Panel):
  def __init__(self, parent, text, text_button, button_command):
    super().__init__(parent)

    #layout
    self.rowconfigure((0,1), weight=1)
    self.columnconfigure((0,1), weight=1)

    ctk.CTkLabel(self, text=text, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=0, padx=4, sticky='w')
    entry = ctk.CTkEntry(self, font=ctk.CTkFont(family="Roboto", size=14))
    entry.grid(row=1, column=0, columnspan=2, sticky='ew', padx=4, pady=4)
    ctk.CTkButton(self, text=text_button, font=ctk.CTkFont(family="Roboto", size=14), corner_radius=5, command=button_command(entry)).grid(row=2, column=1, sticky='e', padx=4, pady=4)

class SearchPanel(Panel):
  def __init__(self, parent, text, button_command):
    super().__init__(parent)

    #layout
    self.rowconfigure((0,1), weight=1)
    self.columnconfigure((0,1), weight=1)

    ctk.CTkLabel(self, text=text, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=0, padx=4, sticky='w')
    entry = ctk.CTkEntry(self, font=ctk.CTkFont(family="Roboto", size=14))
    entry.grid(row=1, column=0, columnspan=2, sticky='ew', padx=4, pady=4)
    ctk.CTkButton(self, text='Buscar', font=ctk.CTkFont(family="Roboto", size=14), corner_radius=5, command=button_command(entry)).grid(row=2, column=1, sticky='e', padx=4, pady=4)

class FilterPanel(Panel):
  def __init__(self, parent, button_command):
    super().__init__(parent)

    #layout
    self.rowconfigure((0,1,2,3), weight=1)
    self.columnconfigure((0,1), weight=1)

    ctk.CTkLabel(self, text="Escoja la categoría del nodo deseada:", font=ctk.CTkFont(family="Roboto", size=14)).grid(row=0, column=0, padx=4, sticky='w')
    category = ctk.CTkOptionMenu(self,values= ['bike', 'cars', 'cats', 'dogs', 'flowers', 'horses', 'human'], font=ctk.CTkFont(family="Roboto", size=14))
    category.grid(row=0, column=1,padx=4, pady=4, sticky='w')
    ctk.CTkLabel(self, text='Tamaño mínimo:', font=ctk.CTkFont(family="Roboto", size=14)).grid(row=1, column=0, padx=4, sticky='w')
    minsize = ctk.CTkEntry(self, font=ctk.CTkFont(family="Roboto", size=14))
    minsize.grid(row=1, column=1, padx=4, pady=4, sticky='w')
    ctk.CTkLabel(self, text='Tamaño máximo:', font=ctk.CTkFont(family="Roboto", size=14)).grid(row=2, column=0, padx=4, sticky='w')
    maxsize = ctk.CTkEntry(self, font=ctk.CTkFont(family="Roboto", size=14))
    maxsize.grid(row=2, column=1, padx=4, pady=4, sticky='w')
    ctk.CTkButton(self, text='Filtrar', font=ctk.CTkFont(family="Roboto", size=14), corner_radius=5, command=button_command(category, minsize, maxsize)).grid(row=3, column=1, sticky='e', padx=4, pady=4)

class InfoPanel(Panel):
  def __init__(self, parent, nivel, balance, node_parent, grandparent, uncle):
    super().__init__(parent)

    #layout
    self.rowconfigure((0,1,2,3,4), weight=1)
    self.columnconfigure((0,1), weight=1)

    ctk.CTkLabel(self, text="Nivel del nodo:", font=ctk.CTkFont(family="Roboto", size=14, weight="bold")).grid(row=0, column=0, padx=4, sticky='w')
    ctk.CTkLabel(self, text=nivel, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=0, column=1, padx=4, sticky='w')
    ctk.CTkLabel(self, text="Factor de balanceo:", font=ctk.CTkFont(family="Roboto", size=14, weight="bold")).grid(row=1, column=0, padx=4, sticky='w')
    ctk.CTkLabel(self, text=balance, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=1, column=1, padx=4, sticky='w')
    ctk.CTkLabel(self, text="Padre del nodo:", font=ctk.CTkFont(family="Roboto", size=14, weight="bold")).grid(row=2, column=0, padx=4, sticky='w')
    ctk.CTkLabel(self, text=node_parent, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=2, column=1, padx=4, sticky='w')
    ctk.CTkLabel(self, text="Abuelo del nodo:", font=ctk.CTkFont(family="Roboto", size=14, weight="bold")).grid(row=3, column=0, padx=4, sticky='w')
    ctk.CTkLabel(self, text=grandparent, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=3, column=1, padx=4, sticky='w')
    ctk.CTkLabel(self, text="Tío del nodo:", font=ctk.CTkFont(family="Roboto", size=14, weight="bold")).grid(row=4, column=0, padx=4, sticky='w')
    ctk.CTkLabel(self, text=uncle, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=4, column=1, padx=4, sticky='w')


class FilteredNodes(Panel):
    def __init__(self, parent, node_list, avl_tree):
      super().__init__(parent)

      # Layout
      self.rowconfigure((0, 1), weight=1)
      self.columnconfigure((0, 1), weight=1)
      self.info_panel = None
      ctk.CTkLabel(self, text="Escoja uno de los nodos:", font=ctk.CTkFont(family="Roboto", size=14)).grid(row=0, column=0, padx=4, sticky='w')
      node = ctk.CTkOptionMenu(self, values=node_list, font=ctk.CTkFont(family="Roboto", size=14))
      node.grid(row=0, column=1, padx=4, pady=4, sticky='w')
      ctk.CTkButton(self, text='Ver información', font=ctk.CTkFont(family="Roboto", size=14), corner_radius=5, command=lambda: self.view_info(node, avl_tree)).grid(row=1, column=1, padx=4, pady=4, sticky='ew')

    def view_info(self, node, avl_tree):
      if self.info_panel:
        self.info_panel.destroy()
      parent = avl_tree.get_node_parent(avl_tree.root, node.get())
      grandparent = avl_tree.get_node_grandparent(avl_tree.root, node.get())
      uncle = avl_tree.get_node_uncle(avl_tree.root, node.get())
      nivel = avl_tree.get_node_level(avl_tree.root, node.get())
      balance = avl_tree.get_balance(avl_tree.search(avl_tree.root, node.get()))
      self.info_panel = InfoPanel(self.master, nivel, balance, parent, grandparent, uncle)

class TraversalPanel(Panel):
  def __init__(self, parent, node_list):
    super().__init__(parent)

    #layout
    self.rowconfigure(0, weight=1)
    self.columnconfigure((0,1,2,3), weight=1)

    ctk.CTkLabel(self, text="Recorrido por Niveles:", font=ctk.CTkFont(family="Roboto", size=14, weight="bold")).grid(row=0, column=0, padx=4, sticky='w')
    node_sublists = [node_list[i:i+3] for i in range(0, len(node_list), 3)]
    for row_idx, sublist in enumerate(node_sublists, start=1):
      col_idx = 0
      for idx, node in enumerate(sublist):
        ctk.CTkLabel(self, text=node, font=ctk.CTkFont(family="Roboto", size=14)).grid(row=row_idx, column=col_idx, padx=4, sticky='w')
        if idx < len(sublist) - 1: 
          col_idx += 1
          ctk.CTkLabel(self, text="->", font=ctk.CTkFont(family="Roboto", size=14)).grid(row=row_idx, column=col_idx, padx=4, sticky='w')
          col_idx += 1