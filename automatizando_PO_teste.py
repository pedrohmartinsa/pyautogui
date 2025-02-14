import pyautogui as pag
import time

cnpj = "001066970001"
site = "SO"
deposito = ""

pag.PAUSE = 1
time.sleep(4)

#clicar em "Novo"
posicaoBotaoNovo = pag.locateOnScreen("BotaoNovo.png")
pag.click(posicaoBotaoNovo)

#clicar em "Conta do fornecedor"
pag.moveTo(1357, 422, duration=2)
pag.click(clicks=2)

#colocar o cpf do fornecedor
pag.moveTo(388, 467)
pag.click(clicks=2)
pag.write(cnpj)

#clicar em "Aplicar"
pag.click(285, 716)

#clicar no fornecedor
pag.click(322, 502)

#rolar para baixo para ver o Site e Depósito
pag.moveTo(1583, 476)
pag.scroll(-300)

#clicar no Site e no Depósito, caso tenha
pag.moveTo(1688, 660)
pag.click()
pag.write(site)
pag.click(1360, 742)
#nem sempre tem depósito, então tem que verificar
if deposito == "":
    print("não tem deposito")
else:
    pag.moveTo(1690, 739)
    pag.click()
    pag.write(deposito)
    pag.click(1388, 498)

#clicar em OK e prosseguir
pag.click(1744, 939, duration=1)
