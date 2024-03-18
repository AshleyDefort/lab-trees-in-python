import os

# Función para cargar todas las imágenes de un directorio
def load_all_images(path):
  dataset = {}
  for category in os.listdir(path):
    category_path = os.path.join(path, category)
    if os.path.isdir(category_path):
      files = os.listdir(category_path)
      for file in files:
        file_path = os.path.join(category_path, file)
        category_name = os.path.basename(category_path)
        size = os.path.getsize(file_path)
        if category_name not in dataset:
          dataset[category_name] = []
        dataset[category_name].append({'name': file, 'size': size, 'type': category_name})
  return dataset

# Función para verificar si un archivo está en el dataset
def is_file_in_dataset(dataset, file_name):
  for category, files in dataset.items():
    for file_info in files:
      if file_info['name'] == file_name:
        return True
  return False

# Función para obtener los datos de un archivo por su nombre
def get_file_data_by_name(dataset, filename):
  # Iterar sobre todas las categorías en el dataset
  for category, files_in_category in dataset.items():
    # Buscar el archivo por su nombre en la lista de archivos de la categoría
    for file_data in files_in_category:
      if file_data['name'] == filename:
        # Se encontró el archivo, retornar sus datos y la categoría
        return file_data, category
  # Si no se encuentra el archivo en ninguna categoría, retornar None
  return None, None
