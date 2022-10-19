""" Main File """

import os
import sys
from modules.Combinator import Combinator

ROOT_DIR = os.path.dirname( os.path.abspath(__file__))
LAYERS_ROOT = "/mnt/d/Meldak/Proyectos/WIPS/Avatar/Layers/fullsize/"
OUTPUT_ROOT = "/mnt/d/Meldak/Proyectos/WIPS/Avatar/Combinations"

def main(argv):
    print(ROOT_DIR)    
    os.chdir(ROOT_DIR)

    current = Combinator(LAYERS_ROOT, OUTPUT_ROOT,'Background')
    # current.test_read_image(folder=4)
    current.set_statics(statics=['Background','Puerco','izq'])
    current.combinate(True,False)


if __name__ == '__main__':
    # print(sys.argv[1:])
    main(sys.argv[1:])
