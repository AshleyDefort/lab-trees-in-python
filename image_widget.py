import customtkinter as ctk
from tkinter import Canvas
from PIL import Image, ImageTk

class ImageWidget(Canvas):
  def __init__(self, parent):
    super().__init__(master=parent, bd=0, highlightthickness=0, relief='ridge')
    self.grid(row=0, column=1, sticky='nsew')

  def show_image(self, image_path):
    image = Image.open(image_path)
    self.image = ImageTk.PhotoImage(image) 
    self.create_image(0, 0, anchor='nw', image=self.image)
