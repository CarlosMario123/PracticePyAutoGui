import pyautogui as pg
import time
from itertools import permutations
import string
import random



letras = list(string.ascii_lowercase)  #Obtener todas las letras minúsculas del alfabeto
# Generar todas las permutaciones posibles de las letras
#permutaciones = list(permutations(letras))

# Convertir las permutaciones en palabras
#palabras = [''.join(p) for p in permutaciones]

palabras = ["hola","mundo","hello"]

#primera vez
time.sleep(10)
pg.moveTo(470, 247)
pg.click()
pg.write("221220")
time.sleep(2)
pg.moveTo(531,298)
pg.click()
pg.write("c4to15mar")
pg.press("enter")

#cuando el login marca error
contador = 0
while contador < 5:
    # Realizar acciones dentro del ciclo
    time.sleep(3)
    pg.moveTo(531, 298)
    pg.click()
    pg.write("221220")
    pg.moveTo(458, 342)
    pg.click()
    time.sleep(2)
    palabra_aleatoria = random.choice(palabras)
    pg.write(palabra_aleatoria)
    pg.press("enter")
    
    contador += 1


