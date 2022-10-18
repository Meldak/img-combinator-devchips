""" Main File """

import os
import sys
from modules.Combinator import Combinator

ROOT_DIR = os.path.dirname( os.path.abspath(__file__))
LAYERS_ROOT = "/mnt/d/Meldak/Proyectos/WIPS/Avatar/Layers/fullsize/"

def main(argv):
    print(ROOT_DIR)    
    os.chdir(ROOT_DIR)

    current = Combinator(LAYERS_ROOT, ROOT_DIR)
    current.test_read_image()


if __name__ == '__main__':
    # print(sys.argv[1:])
    main(sys.argv[1:])
