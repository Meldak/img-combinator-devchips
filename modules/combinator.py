""" Clase del combinador de imagenes"""

from os import walk, path
# import sys
# from pathlib import Path
from pprint import pprint


class combinator:
    """ Clase del combinador de imagenes"""
    def __init__(self, img_dir, output_dir):
        """Inicializador de un combinador, requiere directorio de imagenes y directorio de salida"""
        self.origin_path = img_dir
        self.output_path = output_dir
        self.images = loadSourceImages(self.origin_path)
        
        pprint(self.images)


def loadSourceImages(pth):
    """ Obtiene los nombres y paths de las imagenes"""
    # img={}
    files={}

    for (dir_path, dir_names, file_names) in walk(pth):
        if  len(file_names) != 0:
            if path.isdir(dir_path):
                dir_name = path.basename(dir_path) if path.basename(dir_path) != '' else '/'
                img={}
                for fname in file_names:
                    if path.isfile(path.join(dir_path,fname)):
                        img[fname] ={'path' : path.join(dir_path,fname)}
                files[dir_name] = img
    return files

