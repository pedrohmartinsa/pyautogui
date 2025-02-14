import pyautogui as pag
import time

#pegar posições do mouse e da tela
time.sleep(5)
print(pag.position())
print(pag.locateOnScreen("BotaoNovo.png"))

# botaoNovo = pag.locateOnScreen("BotaoNovo.png")
#
# pag.click(botaoNovo)
