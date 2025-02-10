import pyautogui as pag
import time

#da uma pausa entre um comando e outro do pyautogui
#pag.PAUSE = 0.5


#funções do mouse

#pag.click(x, y) -> para clicar em uma determinada posição
#pag.click(x, y, button = "right" ou  "middle") -> para escolher o botão do mouse que será clicado
#pag.click(x, y, clicks = 2) -> quantos clicks quero que o mouse dê

#pag.moveTo(x, y) -> apenas move até o local, não clica
#pag.moveTo(x, y, duration = 1) -> vai demorar 1 segundo para chegar até o destino

#pag.scroll() -> para scrollar na tela, num negativo para baixo e num positivo para cima