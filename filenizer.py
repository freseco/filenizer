import os
from pathlib import Path
import shutil

# La carpeta donde están los ficheros a ordenar
source_folder = "D:\\Downloads"

# La carpeta donde se crearán las subcarpetas por extensión
destination_folder = "D:\\Downloads"

# Recorrer todos los ficheros de la carpeta origen
for file in os.listdir(source_folder):
    path = Path(file)
    if(path.is_file()):  
        # Obtener el nombre y la extensión del fichero
        name, extension = os.path.splitext(file)
        # Si tiene extensión
        if extension:
            # Crear una subcarpeta con el nombre de la extensión si no existe
            subfolder = os.path.join(destination_folder, extension[1:])
            if not os.path.exists(subfolder):
                os.makedirs(subfolder)
                
            # Mover el fichero a la subcarpeta correspondiente
            source_file = os.path.join(source_folder, file)
            destination_file = os.path.join(subfolder, file)
            shutil.move(source_file, destination_file)