""" Clase del combinador de imagenes"""

from os import walk, path
# import sys
# from pathlib import Path
from pprint import pprint
import cv2 as cv


class Combinator:
    """ Clase del combinador de imagenes"""
    def __init__(self, img_dir, output_dir):
        """Inicializador de un combinador, requiere directorio de imagenes y directorio de salida"""
        self.origin_path = img_dir
        self.output_path = output_dir
        self.images = load_source_images(self.origin_path)
        pprint(self.images)

    def test_read_image(self):
        """ Funcion prueba para vizualizar una imagen """
        img_path = self.images['Puerco'][0]['path']
        # print(img_path)
        img = cv.imread(img_path, cv.IMREAD_UNCHANGED)

        cv.imshow('Tests View', img)
        cv.waitKey(0)
        cv.destroyAllWindows()


def load_source_images(pth):
    """ Obtiene los nombres y paths de las imagenes"""
    # img={}
    files={}

    for (dir_path, dir_names, file_names) in walk(pth):
        if  len(file_names) != 0:
            if path.isdir(dir_path):
                dir_name = path.basename(dir_path) if path.basename(dir_path) != '' else '/'
                img={}
                for idx, fname in enumerate(file_names):
                    if path.isfile(path.join(dir_path,fname)):
                        img[idx] ={'path' : path.join(dir_path,fname)}
                files[dir_name] = img
    return files
