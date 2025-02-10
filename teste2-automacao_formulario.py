import pyautogui as pag
import time

time.sleep(2)
#dar uma pausa entre um comando e outro
pag.PAUSE = 0.5

#abrir google
pag.press("win")
pag.write("Google")
pag.click(724, 501)

#escolher minha conta
pag.click(776, 598)

#pesquisar "hashtag"hashtag

pag.click(863, 415)
pag.write("hashtag")
pag.press("enter")

#clicar na opção certa
pag.click(583, 341)

#mover até "Cursos"
pag.moveTo(613, 186)

#clicar em Pyhton
pag.click(889, 283)

#preencher o formulário
pag.click(525, 582)
pag.write("Pedro Henrique Martins Alves dos Santos")

pag.click(489, 641)
pag.write("pedroshenriquepsantos@gmail.com")

pag.click(478, 689)
pag.write("11 942243773")

pag.click(548, 757)
