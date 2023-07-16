import pyautogui as pg
import time


while True:
    time.sleep(5)
    x, y = pg.position()
    print(f"Coordenadas del mouse: X = {x}, Y = {y}")