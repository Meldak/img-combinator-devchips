""" Clase del combinador de imagenes"""

from os import walk, path, mkdir
# import sys
# from pathlib import Path
from pprint import pprint
# import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

from PIL import Image
from itertools import product


class Combinator ():
    """ Clase del combinador de imagenes"""
    resolution = {"high":0,
                  "width":0 }
    dimention = ()
    items={}
    
    
    def __init__(self, img_dir, output_dir, base=0):
        """Inicializador de un combinador, requiere directorio de imagenes y directorio de salida"""
        self.origin_path = img_dir
        self.output_path = output_dir
        self.images = load_source_images(self.origin_path)
        self.canvas = self.set_canvas(base)
        self.alpha = 0.5
        self.beta = 0.5
        # pprint(self.images)
        
        self.stage_output()

    def test_read_image(self, folder=0):
        """ Funcion prueba para vizualizar una imagen """
        img = Image.open(self.images[list(self.images.keys())[folder]][0]['path'])
        plt.imshow(img)
        plt.show()
        # img = cv.imread(img_path, cv.IMREAD_UNCHANGED)
        # cv.imshow('Tests View', img)
        # cv.waitKey(0)
        # cv.destroyAllWindows()

    def combinate(self, sav=False, shw=False):
        """Funcion de combinacion"""
        
        # temp = combinations(self.items, 2)
        prod = product(list(self.items.values())[0],list(self.items.values())[1])
        
        
        for imgs in list(prod):
            # pprint(i)
            name = 'av'
            comb = self.canvas.copy()
            for img_path in imgs:
                name+=f'-{path.splitext((path.basename(img_path)))[0]}'
                comb = Image.alpha_composite(comb,Image.open(img_path))
                # Image.sa
            print(name)
            if sav:
                save_path = path.join(self.output_path, name+'.png')
                if not path.exists(save_path):
                    comb.save(save_path)
            if shw:
                show(comb)
            # break
    
    
    def set_statics(self, statics:[]):
        """Funcion de combinacion"""

        if len(statics)>0:
            for static in statics:
                img_path = self.images[static][0]['path']
                # print(static)
                img = Image.open(img_path) 
                self.canvas = Image.alpha_composite(self.canvas,img)

            if 'Background' not in statics:
                statics.append('Background')
                
        
        for group in self.images:
            if group not in statics:
                self.items[group]=[]
                for idx,item in list(self.images[group].items()):
                    self.items[group].append(item['path'])

        # self.items=[]
        # for group in self.images:
        #     if group not in statics:
        #         for idx,item in list(self.images[group].items()):
        #             self.items.append(item['path'])
                                        
        # pprint(self.items)
                
        
        
    def set_canvas(self, base=0):
        """Genera el Canvas del proyecto con base al primer objeto de la lista de images"""

        if type(base) == int:
            img = Image.open(self.images[list(self.images.keys())[0]][0]['path']) 

        elif type(base) == str:
            img = Image.open(self.images[base][0]['path'])

        self.set_resolution(img.size)
        return Image.new("RGBA",self.dimention)


    def set_resolution(self, shape):
        self.dimention = shape
        self.resolution['hight']= shape[0]
        self.resolution['width']= shape[1]

    def stage_output(self):
        if not path.exists(self.output_path):
            mkdir(path.join(self.output_path))
            




def get_mask(img):
    """ Genera una mascara de la imagen  dada"""
    shapes = np.zeros_like(img, np.uint8)
    # print(img.shape)
    h , w = img.shape[:2]
    
    shapes[0:h , 0:w ] = img
    
    return shapes.astype(bool)
            
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

def show(canvas):
    plt.imshow(canvas)
    plt.show()