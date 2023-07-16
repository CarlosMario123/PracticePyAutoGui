import pyautogui as pg
import time
import random

mensajes = ["أنا أنظر إليك، دانييل"]
mensajes.append("سلام")
mensajes.append("брат")
mensajes.append("平和平和平和")
mensajes.append("パブロ、起きて")
mensajes.append("Pablo, expergiscere")
mensajes.append("брат")
time.sleep(5)
pg.write("la ia ha sido activada....")
pg.press("enter")
time.sleep(5)
for i in range(1500):
   
    elemento_aleatorio = random.choice(mensajes)
    pg.write(elemento_aleatorio)
    pg.press("enter")
   