from glob import glob
from os import path, walk, rename
from time import sleep
from terminal_text_color.text_color import TextColor
from terminal_text_color import AlertTextColor
tc = TextColor()
atc = AlertTextColor()
if __name__ == "__main__":
    folders = [x[0] for x in walk(".")] # listamos todos los folders en la carpeta
    folders.pop(0) # removemos el primer espacio de la lista
    folders = [i.replace(".\\", "") for i in folders] # quitamos la informacion del nombre que no interesa
    
    for folder in folders: # para cada folder
        i = 0 # inicamos una variable en 0
        try:
            for filename in glob(f"{folder}\*.mat"): # leemos cada archivo .mat
                # creamos un nuevo nombre de archivo
                new_filename = path.join(folder, f"{folder}_signal_{i}.mat")
                # renombramos el anterior con el nuevo
                rename(filename, new_filename)
                # imprimimos la confirmacion
                print(tc.default_green("Cambiando {filename} a {new_filename}"))
                i += 1 # sumamos +1 al contador
                sleep(0.5)
        except Exception as fail:
            print(tc.default_red(f"ERROR: {fail}"))
        atc.custom(f"el folder {folder} a terminado")# imprimimos que termino un folder

        sleep(5)
            