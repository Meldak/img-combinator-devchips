
import os
from modules.combinator import combinator

ROOT_DIR = os.path.dirname( os.path.abspath(__file__))
LAYERS_ROOT = "/mnt/d/Meldak/Proyectos/WIPS/Avatar/Layers/fullsize/"
def main():
    
    
    
    print(os.path.curdir)
    # print(os.path.dirname( os.path.abspath(__file__)))
    os.chdir(ROOT_DIR)
    print(os.path.curdir)

    combinator(LAYERS_ROOT, ROOT_DIR)



if __name__ == '__main__':
  
    main()