import numpy as np
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: mycos <x>")
        sys.exit(1)

    x = float(sys.argv[1])
    result = np.cos(x)
    print(result)

if __name__ == "__main__":
    main()


    '''
    w terminalu:
    py -m venv NPDenv  - do zainstalowania wirtualnego środowiska
    NPDenv\Scripts\activate - aktywacja środowiska
    pip install . 
    rmdir /S /Q build dist mycos.egg-info __pycache__ - można usunąć pliki tymczasowe
    mycos 0 aby uruchomic
    pip show mycos - pokazuje metadata
    deactivate - deaktywacja środowiska
    '''