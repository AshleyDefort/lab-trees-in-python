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

