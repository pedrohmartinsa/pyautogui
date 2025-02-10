import pyautogui as pag
import time

pag.PAUSE = 0.5

time.sleep(3)

#localização da barra de pesquisa do meu Google (no tamanho da minha tela)
pag.click(863, 415)

#O texto que quero que pesquise
pag.write("Gatos dormindo")

#Para dar enter
pag.press("enter")

#A localização das imagens do meu Google (no tamanho da minha tela)
pag.click(349, 246)
