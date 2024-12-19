import ctypes
import os

# Definir las constantes de atributos de archivo para Windows
FILE_ATTRIBUTE_HIDDEN = 0x02
FILE_ATTRIBUTE_SYSTEM = 0x04

def set_file_attributes(file_path, hidden=False, system=False):
    attributes = 0
    if hidden:
        attributes |= FILE_ATTRIBUTE_HIDDEN
    if system:
        attributes |= FILE_ATTRIBUTE_SYSTEM
    
    # Convertir el path a formato UTF-16 para Windows API
    file_path_wide = ctypes.create_unicode_buffer(file_path)
    
    # Usar SetFileAttributesW para cambiar los atributos
    success = ctypes.windll.kernel32.SetFileAttributesW(file_path_wide, attributes)
    
    if not success:
        raise OSError(f"No se pudieron cambiar los atributos del archivo: {file_path}")
    else:
        print(f"Atributos del archivo cambiados: {file_path}")

# Ruta del archivo a modificar
file_path = r"C:\Users\csarb\Downloads\GameSH"

# Hacer el archivo oculto y de sistema
set_file_attributes(file_path, hidden=False, system=False)
