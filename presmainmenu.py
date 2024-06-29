import pygame
import sys
import math
#import main
import random
import numpy as np

w = 800
h = 800
sc = pygame.display.set_mode((w, h))
mmenu = ["menu", "main", "game", "set"]


class button(object):
  def __init__(self, x = 0, y = 0, xx = 100, yy = 100, type = 0, col = (255,255,255), text = "кнопка"):
    self.x = x
    self.y = y
    self.xx = xx
    self.yy = yy
    self.type = type #квадрат/круг
    self.color = col
    self.instate = 0
    self.instate2 = 0
    self.text = text
    self.active =1
  def draw(self):
    if self.type == 0 and self.active == 1:
      pygame.draw.rect(sc, self.color, (self.x, self.y, self.xx, self.yy))
      pygame.font.init()
      
      if len(self.text) > 0:
        i = min(round(self.xx*40/100*6/len(self.text)), int(self.yy*2))
        
      else:
        i = 1
      
      f1 = pygame.font.SysFont('arial', i)
  
      text1 = f1.render(self.text, True,
                      (180, 0, 0))
      sc.blit(text1, (self.x,self.y))
    if self.type == 1 and self.active == 1:
      pygame.draw.circle(sc, self.color, (self.x + self.xx/2, self.y+self.xx/2), self.xx/2)
      
  def get_pos(self):
    if self.type == 0:
      return((self.x,self.x + self.xx, self.y, self.yy+self.y))
  def press(self):
    pressed = pygame.mouse.get_pressed()
    if pressed[0]==1 and self.active == 1:
        pos = pygame.mouse.get_pos()
        if pos[0] >= self.x and pos[0] <= self.xx+self.x  and pos[1] >= self.y and pos[1] <= self.yy+self.y:
              return 1
        else:
          zagl = []
          #print(404)
    else:
      zagl = []
      #print(403)
  def click(self):
    ev = pygame.event.get()
    for event in ev:
      if event.type == pygame.MOUSEBUTTONDOWN and self.active == 1:
         pos = pygame.mouse.get_pos()
         if pos[0] >= self.x and pos[0] <=self.xx+self.x and pos[1]>=self.y and pos[1] <= self.yy+self.y:
              return 1
         else:
           return 0


mainb = {
  "new_game":button(w/45, h - h/30 - h/10 , w/4.5, h/10), 
"load_game": button(w/45 + w/4.5 +w/45, h - h/30 - h/10 , w/4.5, h/10),
"settings": button(w/45*3 + w/4.5*2, h - h/30 - h/10 , w/4.5, h/10),
"quit": button(w/45*4 + w/4.5*3, h - h/30 - h/10 , w/4.5, h/10)
}
mainb["quit"].text = "Выйти"#mainmenub["new_game"] = button()
mainb["new_game"].text = "Новая игра"
mainb["load_game"].text = "Загрузить"
mainb["settings"].text = "Настройки"
mnewg = [
  button(w/8, h/11/5, w/4, h/5.5),
  button(w/8, h/11/5*2 + w/5.5, w/4, h/5.5),
  button(w/8, h/11/5*3 + w/5.5*2, w/4, h/5.5),
  button(w/8, h/11/5*4 + w/5.5*3, w/4, h/5.5)
  ]
mnewg[0].text = "Кампания"
mnewg[1].text = "Песочница"
mnewg[2].text = "Миссии"
mnewg[3].text = "Главное меню"
sb1 = [button(w/8,h/5,w/4, h/10), button(w/8,h/5*3,w/4, h/10)]
sb1t = []
sb2 = [button(w/8, h/11/5+50, w/4, h/5.5),
  button(w/8, h/11/5*2 + h/5.5+80, w/4, h/5.5),
  button(w/8, h/11/5*3 + h/5.5*2+110, w/4, h/5.5),
  button(w/2 + w/4, h/9 - h/20, w/7, h/9),
  button(w/2, h/22, w/4/2, h/11),
  button(w/2, h/22*2 + h/11, w/4/2, h/11),
  button(w/2, h/22*3 + h/11*2, w/4/2, h/11),
  button(w/2, h/22*4 + h/11*3, w/4/2, h/11),
  button(w/2, h/22*5 + h/11*4, w/4/2, h/11),
  button(w/2, h/22*6 + h/11*5, w/4/2, h/11),
  button(w/2 + w/4, h- h/9 - h/20, w/7, h/9)]
gme = [button(w/8, 100, w/3*2, h-200),
button(w/4 + w/16, 250, w/2 - w/8, 50),
button(w/4 + w/16, 360, w/2 - w/8, 50),
button(w/4 + w/16, 470, w/2 - w/8, 50)]


smb = [button(w/4 + w/16, 150, w/2 - w/8, 50),
button(w/4 + w/16, 250, w/2 - w/8, 50),
button(w/4 + w/16, 350, w/2 - w/8, 50),
button(w/2-60+ 200, 170, 50, 50),
button(w/2+10+200, 170, 50, 50),
button(w/2-60+200, 270, 50, 50),
button(w/2+10+200, 270, 50, 50)]
smb[2].text = "Назад"
smb[3].text = " - "
smb[4].text = " + "
smb[5].text = " - "
smb[6].text = " + "
for i in smb:
  i.active = 0
gme[0].text = ""
gme[1].text = "Продолжить"
gme[2].text = "Настройки"
gme[3].text = "Главное меню"
sb1[0].text = "Создать остров"
sb1[1].text = "Назад"

while 1==1:
  if mmenu[0] == "menu":
    sc.fill((0,0,100))
    if mmenu[1] == "main":
      for i in mainb:
        mainb[i].draw()
        mainb[i].active = 1
      if mainb["quit"].press()==1:
      #game_run = 0
        mainb["quit"].text = ""
        #mmenu[0] = "game"
      if mainb["new_game"].click()==1:
        mmenu[1] = "new_game"
        #mmenu[0] = "game"
      if mainb["load_game"].press()==1:
        mmenu[1] = "load_game"
        mmenu[0] = "game"
    if mmenu[1] == "new_game":
        tl = mnewg
        for i in mnewg:
            i.draw()
        
        if mnewg[3].click() == 1:
            mmenu[1] = "main"
        if mnewg[1].press()==1:
            mmenu[1] = "sb1"
    if mmenu[1] == "sb1":
        for i in sb1+sb1t:
          i.draw()
        if sb1[1].click()==1:
          mmenu[1] = "new_game"
        if sb1[0].press() == 1:
          mmenu[1] = "sb2"
    if mmenu[1] == "sb2":
      if sb2[3].press() == 1:
        mmenu[1] = "sb1"
      sb2[0].text = "население:      " + str(int(nhumans))
      sb2[1].text = "ширина острова: " + str(int(n))
      sb2[2].text = "длина острова:  "+str(int(m))
      sb2[3].text = "назад"
      sb2[10].text = "создать"
      for i in {4,6,8}:
        sb2[i].text = " + "
        
          
      for i in {5,7,9}:
        sb2[i].text = " - "
      if sb2[4].press() == 1:
        nhumans += 1/FPS*nhumans
        
      if sb2[5].press() == 1:
        if nhumans > nopt+1/FPS*nhumans+1:
          nhumans -= 1/FPS*nhumans
        else:
          nhumans = nopt + 1
      if sb2[6].press() == 1:
        n += 1/FPS*n
      if sb2[7].press() == 1:
        n -= 1/FPS*n
      if sb2[8].press() == 1:
        m += 1/FPS*m
      if sb2[9].press() == 1:
        m -= 1/FPS*m
      if sb2[10].click() == 1:
        #mmenu[1] = "sb1"
        n = int(n)
        m = int(m)
        nhumans = int(nhumans)
        humans = []
        buildings = []
        clinics = []
        factories = []
        addhuman(nhumans)
        rm = [[0 for j in range(0,m)] for i in range (0,n)]
        rm = np.array(rm, dtype=int)
        mmenu[0] = "game"
      for i in sb2:
        i.draw()
        
        
    pygame.display.update()