from glob import glob
from os import path, walk, remove
from time import sleep
from terminal_text_color.text_color import TextColor
from terminal_text_color import AlertTextColor
from scipy.io import loadmat
import numpy as np

tc = TextColor()
atc = AlertTextColor()
if __name__ == "__main__":
    folders = [x[0] for x in walk("data")] # listamos todos los folders en la carpeta
    folders.pop(0) # removemos el primer espacio de la lista
    folders = [i.replace(".\\", "") for i in folders] # quitamos la informacion del nombre que no interesa

    for folder in folders:
        name_folder = folder.split("\\")[1]
        i = 0 # inicamos una variable en 0
        print(tc.default_blue(f"ABRIENDO FOLDER {folder}"))
        try:
            for filename in glob(f"{folder}\*.mat"):
                print(tc.default_yellow(f"Leyendo {filename}"))
                data_dict = loadmat(filename) # leemos el archivo .mat
                data_array = data_dict['val'] # almacenamos solo la informacion
                data = np.array(data_array) # guardamos en un array de numpy

                print(tc.default_yellow(f"Conviertiendo {filename}..."))
                # Save the array to a CSV file
                np.savetxt(f"{folder}\{name_folder}_signal_{i}.csv", data, delimiter=",")
                remove(filename) # eliminamos el archivo .mat
                print(tc.default_green(f"¡El archivo {filename} se ha convertido a {folder}/{name_folder}_signal_{i}.csv!"))
                i += 1 # sumamos +1 al contador
                sleep(0.5)
        except Exception as fail:
            print(tc.default_red(f"ERROR: {fail}"))
        atc.success(f"Terminado la carpeta {folder}")