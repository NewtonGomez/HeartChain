from scipy.io import loadmat
from glob import glob
from os import walk, remove
from terminal_text_color.text_color import TextColor
from terminal_text_color import AlertTextColor
import pandas as pd

tc = TextColor()
atc = AlertTextColor()
errores = []
if __name__ == "__main__":
    folders = [x[0] for x in walk("./data")] # listamos todos los folders en la carpeta
    folders.pop(0) # removemos el primer espacio de la lista
    paths = [i.replace(".\\", "") for i in folders] # quitamos la informacion del nombre que no interesa
    for folder in paths: # para cada folder
        name_folder = folder.split("./data\\")[1]
        i = 0 # inicamos una variable en 0
        try:
            for filename in glob(f"{folder}\*.mat"): # leemos cada archivo .mat
                print(tc.default_yellow(f"abriendo {filename}"))
                data_dict = loadmat(filename)
                data_array = data_dict['val']
                data_array = data_array.transpose(1, 0)
                df = pd.DataFrame(data_array,columns=['signal'+str(n) for n in range(1)])
                df.to_csv(f"{folder}\{name_folder}_signal_{i}.csv")
                remove(filename) # borramos el archivo
                print(tc.default_green(f"El archivo {folder}\{name_folder}_signal_{i}.csv se ha creado"))
                i += 1
        except Exception as fail:
            atc.error(f"ERROR: {fail}")
            errores.append(fail)
        
        atc.success(f"{folder} terminado")
    
    atc.error(f"ERRORES")
    for error in errores:
        print(tc.default_red(error))