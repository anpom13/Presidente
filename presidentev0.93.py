import pygame
import sys
import math
#import main
import random

nhumans = 60
nopt= 2
pygame.font.init()
pauseg = 0
x = 0
y = 0
n = 70
starthumans = 6
year = 2023
month = 0
time = 0# 2 минуты -- игровой месяц
ids = [0]
infomod = ["info"]


monthevent = 0
typi = -1  # для табло с информацией (245,245,220)
numbi = -1
money = [25000]
xtest = 0
ytest = 0
m = 20
mu=1
cn = 0
foodc = 5
xx = 0
yy = 0
nds = 0.0
sp = None
medc = 10
tapped = 0
zagl = [] 
rm = [[0 for j in range(0,m)] for i in range (0,n)]
test = [0]
def pri(x):
  if test[0]==1:
    print(x)
#dictrus = 
wpdict = {"farm": "ферма", "clinic":"клиника", "port":"порт", "fur": "офис грузоперевозо", "immigration": "иммиграционное бюро", "shop": "магазин", "tavern" :"театр ", "ranch": "ранчо" ,"rome" :"ромовый завод", "cheese":"сырный завод","canns":"консервный завод" ,"cigar":"сигарный завод"}
exportprices = { "coffee":800,"cheese":500,"corn":400, "pineapple":600, "sugar":800, "tobacco":900, "meat":600, "milk":500, "fish":700, "aspirin": 1200, "rom":7000, "cigar":5000, "canns":1500 }
reszero = {"coffee":0, "cheese":0,"corn":0, "pineapple":0, "sugar":0, "tobacco":0, "meat":0, "milk":0, "fish":0, "aspirin": 0, "rom":0, "cigar":0, "canns":0 }
resone = {"coffee":1 ,"cheese":1,"corn":1, "pineapple":1, "sugar":1, "tobacco":1, "meat":1, "milk":1, "fish":1, "aspirin": 1, "rom":1, "cigar":1, "canns":1 }
eat = {"cheese", "corn","pineapple","meat","milk","fish","canns"}
names ={0: "Никита", 1:"Андрей", 2: "Пётр", 3: "Александр", 4: "Александра", 5:"Василий", 6:"Элина" , 7: "Диана", 8:"Алёна", 9: "Мария", 10: "Эльвира", 11: "Олеся", 12: "Тимофей", 13: "Яна", 14: "Артемий"}
surnames = {0: "Померанцес", 1: "Яковенко", 2: "Верлянко", 3: "Савченко", 4: "Калиниченко", 5: "Дюма", 6: "Шапиро", 7:"Никитенко", 8:"Живаго", 9:"Черных", 10: "Романенко", 11: "Паганини", 12: "Заика", 13: "Шарандак", 14:"Цыбулько"}

def render_road():
  
  for i in range(0,len(rm)):
    for j in range(0,len(rm[0])):
        if rm[i][j] < 10 and rm[i][j] > 0:
          xhum = (xx + 100 * i) * mu + (1 - mu) * (w / 2)
          yhum = (yy + 100 * j) * mu + (1 - mu) * (h / 2)
          pygame.draw.rect(sc, (200,0,0), (xhum, yhum, 100*mu, 100*mu))
        if rm[i][j] == 0:
          xhum = (xx + 100 * i) * mu + (1 - mu) * (w / 2)
          yhum = (yy + 100 * j) * mu + (1 - mu) * (h / 2)
          pygame.draw.rect(sc, (100,100,100), (xhum, yhum, 100*mu, 100*mu))
      

def al(a,l): #a -- кортеж из двух элементов, l -- двуменрный список
  i = len(l)
  j = len(l[0])
  if a[0]>=0 and a[0]<=i-1:
    if a[1]>=0 and a[1]<= j-1:
      
      return 1
    else: 
      return 0
  else:
    return 0


def alr(a,l):
  if al(a,l) == 1:
    x = l[a[0]][a[1]] 
    if x > 0 and x< 10:
      return 1
    else:
      return -1
  else:
    return -2
    
    #return "ne dopisano"
def nodes(ac, di,di2): 
  acc = set()
  for i in ac:
    
    if (i[0],i[1]) in di:
      acc = acc
    else:
      di[i] = 0
      #print("zero")
    b = (i[0]+1,i[1])
    if alr(b,rm) == 1:
      x = rm[b[0]][b[1]]
      if b in di:
        if di[b] > di[i]+x:
          di[b] = di[i]+x
          acc.add(b)
          #print("right")
          di2[b] = di2[i]+[0]
      else:
        di[b] = x + di[i]
        acc.add(b)
        #print("right0")
        x = di2[i]
        #x = list(x)
        di2[b] = di2[i]+[0]
        #di2[b] = x.append(0)
        #print(type(di2[i]))
    b = (i[0]-1,i[1])
    if alr(b,rm) == 1:
      x = rm[b[0]][b[1]]
      if b in di:
        if di[b] > di[i]+x:
          di[b] = di[i]+x
          acc.add(b)
          #print("left2")
          di2[b] = di2[i]+[2]
      else:
        di[b] = x + di[i]
        acc.add(b)
        #print("left2")
        di2[b] = di2[i]+[2]
    b = (i[0],i[1]+1)
    if alr(b,rm) == 1:
      x = rm[b[0]][b[1]]
      if b in di:
        if di[b] > di[i]+x:
          di[b] = di[i]+x
          acc.add(b)
          #print("up1")
          di2[b] = di2[i]+[1]
      else:
        di[b] = x + di[i]
        acc.add(b)
        #print("up1")
        di2[b] = di2[i]+[1]
    b = (i[0],i[1]-1)
    if alr(b,rm) == 1:
      x = rm[b[0]][b[1]]
      
      if b in di:
        if di[b] > di[i]+x:
          di[b] = di[i]+x
          acc.add(b)
          #print("down3")
          di2[b] = di2[i]+[3]
      else:
        di[b] = x + di[i]
        acc.add(b)
        #print("down3")
        di2[b] = di2[i]+[3]
  if len(acc) > 0:
      #print(di)
      #print(acc)
      di = nodes(acc,di,di2)[0]
      di2 = nodes(acc,di,di2)[1]
  else:
      di = di#nodes(acc,al,di)
  return (di,di2)
      
def nod2(a,z,rm):
  ac = {a}
  di = {}
  di2 = {}
  di3 = {}
  for i in range (0,n):
    for j in range (0,m):
      if alr((i,j),rm) == 1:
        di2[(i,j)] = []
  ss = nodes(ac,di,di2)[1]
  if z in ss:
    return ss[z]
  else:
    return []


# функция которая делает из начальной координаты и списка направлений список узлов

def nods(a, z, s):
  l = []
  c = 0
  d = 0
  b = a
  l.append(b)
  for i in range(0,len(s)):
    if i != 0:
      if s[i] != s[i-1]:
        x = i-d
        d = i
        y = s[i-1]
        if y == 0:
          b = (b[0] + x, b[1])
          l.append(b)
        if y == 1:
          b = (b[0], b[1]+x)
          l.append(b)
        if y == 2:
          b = (b[0] - x, b[1])
          l.append(b)
        if y == 3:
          b = (b[0], b[1]-x)
          l.append(b)
  
    
  l.append(z)
  return l
#s = [0,0,0,0,3,3,3,2]
z = (6,13)
a = (0,7)
#print(nods(a,z,s))
#print(nod2(a,z,rm))

def nod3(a,z,l):
  if alr(a,rm) == 1 and alr(z,rm) == 1:
    if a == z:
      return(a,a)
    else:
      s = nod2(a,z,l)
      if len(s) > 0:
        return nods(a,z,s)
      else:
        return 0
  else:
    return 0


def sigg(x):
  if x >0:
    return 1
  if x == 0:
    return 0
  if x < 0:
    return 1
def g(l):
  d = 0
  m = []
  for i in range(0,len(l)-1):
    dx = l[i+1][0]-l[i][0]
    dy = l[i+1][1]-l[i][1]
    d += math.sqrt(dx*dx+dy*dy)
    d += 1
    m.append((d,i))
    if i!=len(l)-2:
      d = d
  return (d,m)
  
def gg(l,x):
  d = g(l)[0]
  m = g(l)[1]
  gg_1 = 0
  gg_2 = 0
  for i in range (0,len(m)):
    if m[i][1]>=0:
      j = m[i][1]
      gg_1 = i
      a = l[j]
      b = l[j+1]
      if i == 0:
        if x < m[i][0]:
          #print("a=")
          #print(a)
          #print(b)
          #print(x)
          
          return hhh(a,b,x)
      elif x >= m[i-1][0] and x <= m[i][0]:
        t = x-m[i-1][0]
        return hhh(a,b,t)
  return(0,0) #чтобы в случае ошибок не выдавало nontype
      
    
def hhh(a,b,x):
  #print("s1")
  dx = b[0]-a[0]
  dy = b[1]-a[1]
  d = math.sqrt(dx*dx+dy*dy)
  if d == 0:
    return a
  if x >=0 and x < d-1:
    z = x
    dxx = dx*z/d+a[0]
    dyy = dy*z/d+a[1]
  else:
    dxxx = (d-1)/d*dx+a[0]
    dyyy = (d-1)/d*dy+a[1]
    z = (x - d + 1) / 2
    dxx = dxxx + z*dx/d
    dyy = dyyy + z*dy/d
  return (dxx,dyy)

def graphsv(a):
  di2 = {}
  a = {a}
  retu = set()
  for i in range (0,len(rm)):#n
    for j in range (0,len(rm[0])):#m
      if alr((i,j),rm) == 1:
        di2[(i,j)] = []
  ss = nodes(a,{},di2)[0]
  for i in range (0,len(rm)):#n
    for j in range (0,len(rm[0])):#m
      if (i,j) in ss:
        retu.add((i,j))
  return retu

class car(object):
    def __init__(self, xt = 800):
        self.x = 0.0
        self.y = 100.0
        self.max_speed = 20
        self.speed = 0.0
        self.max_acel = 0.2
        self.acel = 0.0
        self.bacel = 0.1
        self.xt = 8
        self.a = 0
        self.s = 1
        self.tren = self.max_acel/self.max_speed*700
        self.rx = 0
        self.ry = 0
    def gas(self, s=100.0):
        self.acel = float(self.max_acel * s)
        if self.speed + self.acel/FPS <= self.max_speed:
            self.speed += float(self.acel/FPS)*self.s
        else:
            self.speed = self.max_speed
        #print("gas"+str(self.x)+"------------")
    def brake(self, s = 100):
        self.acel = -self.bacel*s
        if self.speed + self.acel/FPS > 0:
            self.speed += self.acel/FPS
            #self.s = 0
        else:
            self.speed = 0
    def life(self,l):
        a = self.speed/FPS
        #print("a =" + str(a))
        if self.x + a < self.xt:
          self.x += self.speed/FPS
        else:
          self.x = self.xt
        self.speed -= self.speed*self.tren/FPS
        #print("x = " + str(self.x))
        if self.xt - self.x > self.brake_way()/30:
            self.gas()
            #print("acel")
            #print(self.acel)
            
        else:
            self.brake()
            #print("brake")
            self.a = 100
        self.renderg(l)
    def brake_way(self):
        #print("speed")
        #print(self.speed)
        #print(self.speed*self.speed/2/self.bacel)
        return self.speed*self.speed/2/self.bacel
        
    def render(self):
        pygame.draw.circle(sc, ORANGE, (self.x*100, 200+self.a), 50)
    def renderg(self,l):
      #s = gg(l,self.x)
      #print(type(s))
      #print(s)
      
      self.rx = gg(l,self.x)[0]
      self.ry = gg(l,self.x)[1]
      xhum = (xx + 100 * self.rx) * mu + (1 - mu) * (w / 2)
      yhum = (yy + 100 * self.ry) * mu + (1 - mu) * (h / 2)
      s = (xhum + 50*mu,yhum + 50*mu)
      pygame.draw.circle(sc, ORANGE, s, 30*mu)



def pooo(a,b,i):
  if a >= i.x and a <= i.x+i.xx and b >= i.y and b <= i.y+i.yy:
    return True
  else:
    return False

def mo(self):
  if self >= 0:
    return self
  else:
    return -self

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

class garage(object):
  def __init__(self, x, y, xt,yt):
    self.x = x
    self.y = y
    self.xt = xt
    self.yt = yt
    self.color = (200,200,200)
    self.text = "Гараж"
    self.rlists = {}
    self.rd = {}
    self.rm = {}
    self.genlists()
    print("lllllllllllllllllllllllllllllllllllllll")
    print(self.rlists)
    print(self.rm)
  def genlist(self, bt):
           a = (self.xt,self.yt)
           #a = (garages[self.gi].xt,garages[self.gi].yt)
           md = 1000000000
           mi = -1
           mj = -1
           svset = graphsv(a)
           for i in range(0,len(rm)):
             for j in range(0,len(rm[0])):
               if alr((i,j),rm) ==1 and (i,j) in svset:
                 dx = bt.x - i
                 dy = bt.y - j
                 ds = math.sqrt(dx * dx + dy * dy)
                 if ds <= md:
                   mi = i
                   mj = j
                   md = ds
           #a = (garages[self.gi].xt,garages[self.gi].yt)
           print(mi)
           if mi < 0:
             return 0
           else:
             b = (mi,mj)
             bt.testp5 = str(b)
             rlist = nod3(a,b,rm)
             self.rlists[bt] = rlist
             self.rd[bt]= g(rlist)[0]
             self.rm[bt] = b
             print(self.rm)
             #return (rlist, g(rlist))
    
  def genlists(self):
    for i in buildings:
      self.genlist(i)
      
    

  def pos_on(self):
      pos = pygame.mouse.get_pos()
      xh = int(pos[0])
      yh = int(pos[1])
      xtest = ((xh - (1 - mu) * (w / 2)) / mu - xx) / 100
      ytest = ((yh - (1 - mu) * (h / 2)) / mu - yy) / 100
      xtest = int(xtest)
      ytest = int(ytest)
      if xtest == self.x and ytest == self.y:
          return 1

  def infodis(self):
      #resourses = "Количество еды: " + str(self.amount)
      name = "Гараж"
      #workers = "Работает: " + str(self.nwork) + " из " + str(self.maxnwork)
      #sal = "Зарплата: " + str(self.salary)
      pygame.draw.rect(sc, (225, 225, 220), (0, h / 2, w + 250, h / 2 + 50))
      f1 = pygame.font.SysFont('arial', 40)
      text1 = f1.render(name, True, (0, 0, 0))
      #text2 = f1.render(resourses, True, (0, 0, 0))
      #text3 = f1.render(workers, True, (0, 0, 0))
      #text4 = f1.render(sal, True, (0, 0, 0))
      sc.blit(text1, (0, h / 2))
      #sc.blit(text2, (0, h / 2 + 40))
      #sc.blit(text3, (0, h / 2 + 80))
      #sc.blit(text4, (0, h / 2 + 120))
  def draw(self):
    xhum = (xx + 100 * self.x) * mu + (1 - mu) * (w / 2)
    yhum = (yy + 100 * self.y) * mu + (1 - mu) * (h / 2)
    pygame.draw.rect(sc, (0, 255, 0), (xhum, yhum, 100 * mu, 100 * mu))
    i = int(40*mu)
    if i > 12:
            f1 = pygame.font.SysFont('arial', int(i))
            text1 = f1.render(self.text, True,
                      (180, 0, 0))
            sc.blit(text1, (xhum,yhum+ 40*mu))
  def prii(self):
      zagl = []#print ("garage(" + str(self.x) + str(self.y) + ")")
class home(object):
    def __init__(self, a = 13, b = 3, n =20, q = 10, c = 0, o = 255, l= 0 ):
        self.x = a #0
        self.y = b #1
        self.max_number = n#
        self.number = 0
        self.h_list = []#
        self.rent = 0#
        self.quality = q #max -- 100
        self.color = (c,o,l)
        self.text = "Дом"
        #self.amount = 0
    def pos_on(self):
        pos = pygame.mouse.get_pos()
        xh = int(pos[0])
        yh = int(pos[1])
        xtest = ((xh-(1-mu)*(w/2))/mu-xx)/100
        ytest = ((yh-(1-mu)*(h/2))/mu-yy)/100
        xtest = int(xtest)
        ytest = int(ytest)
        if xtest == self.x  and ytest == self.y:
              return 1
    def infodis(self):
      resourses = "Качество жилья: " + str(int(self.quality))
      name = "Дом"
      workers = "Живёт: " + str(self.number) + " из " + str(self.max_number)
      sal = "Цена аренды: " + str(self.rent)
      pygame.draw.rect(sc, (225,225,220), (0, h/2, w+250, h/2+50))
      f1 = pygame.font.SysFont('arial', 40)
      for i in buttonsfarm:
        i.active = 1
      buttonsfarm[1].text = name
      #buttonsfarm[2].text = resourses
      #buttonsfarm[3].text = workers
      #buttonsfarm[4].text = sal
      text1 = f1.render(name, True,(0, 0, 0))
      text2 = f1.render(resourses, True,(0, 0, 0))
      text3 = f1.render(workers, True,(0, 0, 0))
      text4 = f1.render(sal, True,(0, 0, 0))
      sc.blit(text1, (0, h/2))
      sc.blit(text2, (0, h/2 + 40))
      sc.blit(text3, (0, h/2 + 80))
      sc.blit(text4, (0, h/2 + 120))
    def draw(self):
        xhum = (xx + 100 * self.x) * mu + (1 - mu) * (w / 2)
        yhum = (yy + 100 * self.y) * mu + (1 - mu) * (h / 2)
        pygame.draw.rect(sc, (0, 255, 0), (xhum, yhum, 100 * mu, 100 * mu))
        i = int(40*mu)
        if i > 12:
            f1 = pygame.font.SysFont('arial', int(i))
            text1 = f1.render(self.text, True,
                      (180, 0, 0))
            sc.blit(text1, (xhum,yhum+ 40*mu))



class building(object):
    def __init__(self, a = 2, b = 2, type = "farm", id = 0):
        self.id = id
        self.type = type
        self.subtype = ""
        
        self.x = a#
        self.y = b#
        
        self.xt = a # для гаража и зданий которые привязаны к дороге
        self.yt = b
        
        
        self.t1 = 0
        self.t2 = 0
        self.mode = ""
        
        self.testp1 = ""
        self.testp2 = ""
        self.testp3=""
        self.testp4 = ""
        self.testp5 = ""
        self.testp6 = ""
        self.workallow = 0
        self.in_allow = 0
        self.out_allow = 0
        self.live_allow = 0
        self.visit_allow = 0
        self.fun_allow = 0
        self.eat_allow = 0
        self.workers= []
        self.h_list = []
        self.visiters = []
        self.pvisiters = []
        self.max_visiters = 0
        self.pvisiters = 0
        
        self.resourses = 0
        self.price = 15
        
        self.rtype = 0 #тип ресурса который производит здание
        self.inres = reszero.copy()
        self.outres = reszero.copy()
        self.poutres = reszero.copy()
        self.pinres = reszero.copy()
        self.pinres2 = reszero.copy()
        self.alinres = reszero.copy()#для каждого типа зданий своё, ресурсы которые здание хочет покупать
        self.aloutres = reszero.copy() #ресурсы которое здание хочет продавать
        self.amount = 0
        self.salary = 0#зп рабочих
        self.nwork = 0 #количество рабочих
        self.maxnwork = 0 #макс количество рабочих
        self.text = "здание"
        
        self.max_number =0 # из класса "home"
        self.number = 0
        self.h_list = []#
        self.rent = 0#
        self.quality = 0 #max -- 100
        
        
        self.settype(self.type)
        
        
    def f_fun_allow(self):
      if self.fun_allow == 1 and self.f_visit_allow()==1:
        return 1
      else:
        return 0
    def f_visit_allow(self):
      if self.visit_allow == 1 and len(self.visiters) < self.max_visiters:
        return 1
      else:
        return 0
    def f_eat_allow(self):
      if self.eat_allow == 1:
        leat = set()
        for r in self.outres:
          if r in eat: #и r в alotres
            leat.add(r)
        cnt = 0
        l = []
        for r in eat:
          l.append(min(self.outres[r], self.poutres[r]))
        #print(l)
        #print(self.outres)
        if max(l) > 10:
          return 1
        else:
          return 0
      else:
        return 0
    def settype(self, type):
      if type == "shop":
        
        self.workallow = 1
        self.nwork = 0
        self.maxnwork = 1
        self.in_allow = 1
        self.salary = 5
        self.eat_allow = 1
        
        for i in eat:
          self.alinres[i] = 1
        self.text = "Магазин"
      if type == "rome":
        self.workallow = 1
        self.maxnwork = 12
        self.salary = 10
        self.text = "Ром"
        self.alinres = reszero.copy()
        self.aloutres = resone.copy()
        self.alinres["sugar"] = 1
        self.in_allow = 1
        self.out_allow = 1
        #self.rtype = "meat"
        #self.subtype = "Для этого здания нет режимов работы"
      if type == "cheese":
        self.workallow = 1
        self.maxnwork = 12
        self.salary = 10
        self.text = "Сыр"
        self.alinres = reszero.copy()
        self.aloutres = resone.copy()
        self.alinres["milk"] = 1
        self.in_allow = 1
        self.out_allow = 1
      if type == "cigar":
        self.workallow = 1
        self.maxnwork = 12
        self.salary = 10
        self.text = "Сигареты"
        self.alinres = reszero.copy()
        self.aloutres = resone.copy()
        self.alinres["tobacco"] = 1
        self.in_allow = 1
        self.out_allow = 1
      if type == "canns":
        self.workallow = 1
        self.maxnwork = 12
        self.salary = 10
        self.text = "Консервы"
        self.subtype = "meat"
        self.alinres = reszero.copy()
        self.aloutres = resone.copy()
        self.alinres[self.subtype] = 1
        self.in_allow = 1
        self.out_allow = 1
      if type == "tavern":
        self.workallow = 1
        self.maxnwork = 3
        self.visit_allow = 1
        self.salary = 5
        self.fun_allow = 1
        self.max_visiters = 6
        self.text = "Театр"
      if type == "fur":
        
        self.workallow = 1
        self.nwork = 0
        self.maxnwork = 5
        self.salary = 5
        self.mode = "auto"
        
        self.text = "Фуры"
      if type == "port":
        self.workallow = 1
        self.nwork = 0
        self.maxnwork = 4
        self.alinres = resone.copy()
        self.text = "Порт"
        self.salary = 5
        
        self.in_allow = 1
        self.out_allow = 0
      if type == "rancho":
        self.workallow = 1
        self.workers= []
        self.price = 15
        self.eat_allow = 1
        #self.rtype = "meat"
        self.inres = reszero.copy()
        self.aloutres = resone.copy()
        self.amount = 50
        self.salary = 5
        self.nwork = 0
        self.maxnwork = 2
        self.text = "Ранчо"
        #self.rtype = "meat"
        self.subtype = "meat"
        
        self.in_allow = 0
        self.out_allow = 1
      if type == "farm":
        self.workallow = 1
        self.workers= []
        self.price = 15
        self.eat_allow = 1
        self.rtype = "corn"
        self.inres = reszero.copy()
        self.aloutres = resone.copy()
        self.amount = 50
        self.salary = 5
        self.nwork = 0
        self.maxnwork = 6
        self.text = "Ферма"
        self.rtype = "corn"
        self.subtype = "corn"
        
        self.in_allow = 0
        self.out_allow = 1
      if type == "home":
        self.max_number = 20#
        self.number = 0
        self.h_list = []#
        self.rent = 0#
        self.quality = 0 #max -- 100
        #self.color = (c,o,l)
        self.text = "Дом"
      if type == "clinic":
        self.workers = []
        self.workallow = 1
       
        
        self.amount = 50
        self.salary = 4
        self.nwork = 0
        self.maxnwork = 3
        self.text = "клиника"
      if type == "imigration":
        self.workers = []
        self.workallow = 1
       
        
        #self.amount = 50
        self.salary = 4
        self.nwork = 0
        self.maxnwork = 3
        self.text = "бюро имигр"
    def pos_on(self):
        pos = pygame.mouse.get_pos()
        xh = int(pos[0])
        yh = int(pos[1])
        xtest = ((xh-(1-mu)*(w/2))/mu-xx)/100
        ytest = ((yh-(1-mu)*(h/2))/mu-yy)/100
        xtest = int(xtest)
        ytest = int(ytest)
        if xtest == self.x  and ytest == self.y:
              return 1
    
        
        
      
      
      
    def infodis(self):
      #priorl2 = []
      mode1 = ""
      mode2 = ""
      mode3 = ""
      mode4 = ""
      mode5 = ""
      other1 = ""
      other2 = ""
      other3= ""
      other4= ""
      other5= ""
      other6 = ""
      if self.workallow == 1:
        other6  = "рабочие:"
      idinfo2 = ""
      for i in buttonsinfomen:
        i.active = 1
      if buttonsinfomen[0].press() == 1:
        infomod[0] = "info"
        priorl2 = butdisinfo
      if buttonsinfomen[1].press()==1:
        infomod[0] = "mode"
        priorl2 = butdismode
      if buttonsinfomen[2].press()==1:
        infomod[0] = "money"
        priorl2 = butdisprice
      if buttonsinfomen[3].press()==1:
        infomod[0] = "stat"
        priorl2 = butdisstat
      if buttonsinfomen[4].press()==1:
        infomod[0] = "other"
        priorl2 = butdisother
      resourses = "не доделано: " + str(int(self.outres["corn"]))
      name = "Здание"
      workers = "Работает: " + str(self.nwork) + " из " + str(self.maxnwork)
      sal = "Зарплата: " + str(int(self.salary))
      price = "Цена: " + str(int(self.price))
      if self.subtype != "":
        subtype = "режим работы: "+ str(self.subtype)
      else:
        subtype = "у данного здания нет режимов работы"
      eatallow = ""
      idinfo = ""
      if self.eat_allow == 0:
        eatallow = "здание не предоставляет пищу"
        price = ""
        butdisprice[2].active = 0
        butdisprice[3].active = 0
      else:
        eatallow = "здание предоставляет пищу"
      if self.type == "tavern":
        name = "Театр"
        resourses = "Посетители: " + str(len(self.visiters))
        idinfo = "Одно из немногих местных развлечений"
        price = "Цена: " + str(int(self.price))
      if self.type == "rome":
        resourses = "Количество рома на складе: " + str(int(self.outres["rom"]))
        name = "Ромовый завод"
        other1 = "ром:  " + str(int(self.outres["rom"]))
        other2 = "сахар:" + str(int(self.inres[ "sugar" ]))
        #other6 = str(int(self.pinres[ "sugar" ]))
        idinfo = "делает ром из сахара"
      if self.type == "cigar":
        resourses = "Количество сигар на складе: " + str(int(self.outres["cigar"]))
        name = "Сигаретная фабрика"
        other1 = "сигары:  " + str(int(self.outres["cigar"]))
        other2 = "табак:" + str(int(self.inres[ "tobacco" ]))
        #other6 = str(int(self.pinres[ "sugar" ]))
        idinfo = "делает сигары из табака"
      if self.type == "cheese":
        resourses = "Количество сыра на складе: " + str(int(self.outres["cheese"]))
        name = "Сырный завод"
        other1 = "сыр:   " + str(int(self.outres["cheese"]))
        other2 = "молоко:" + str(int(self.inres[ "milk" ]))
        #other6 = str(int(self.pinres[ "sugar" ]))
        idinfo = "делает сыр из молока"
      if self.type == "canns":
        resourses = "Количество товара на складе: " + str(int(self.outres["canns"]))
        name = "Консервный завод"
        other1 = "консервы: " + str(int(self.outres["canns"]))
        other2 = "ананасы:  " + str(int(self.inres[ "pineapple" ]))
        other3 = "кофе:  " + str(int(self.inres[ "coffee" ]))
        other4 = "мясо:  " + str(int(self.inres[ "meat" ]))
        mode1 = "мясо"
        mode2 = "ананасы"
        mode3 = "кофе"
        #other6 = str(int(self.pinres[ "sugar" ]))
        idinfo = "делает консервы из мяса, кофе или ананасов"
      if self.type == "rancho":
        resourses = "Количество еды: " + str(int(self.outres[self.subtype]))
        name = "Ферма"
        workers = "Работает: " + str(self.nwork) + " из " + str(self.maxnwork)
        sal = "Зарплата: " + str(int(self.salary))
        price = "Цена: " + str(int(self.price))
        mode1 = "мясо"
        mode2 = "молоко"
        #mode3 = "кофе"
        #mode4 = "табак"
        #mode5 = "сахар"
        other1 = "мяса:  " + str(int(self.outres["meat"]))
        other2 = "молока:" + str(int(self.outres[ "milk" ]))
        #other3=  "кофе " + str(self.outres[ "coffee" ])
        #other4=  "табака: " + str(self.outres[ "tobacco" ])
        #other5=  "сахара: " + str(self.outres[ "sugar" ])
        idinfo = "Производит молоко или мясо"
      if self.type == "farm":
        resourses = "Количество еды: " + str(int(self.outres[self.subtype]))
        name = "Ферма"
        workers = "Работает: " + str(self.nwork) + " из " + str(self.maxnwork)
        sal = "Зарплата: " + str(int(self.salary))
        price = "Цена: " + str(int(self.price))
        mode1 = "кукуруза"
        mode2 = "ананасы"
        mode3 = "кофе"
        mode4 = "табак"
        mode5 = "сахар"
        other1 = "кукурузы:" + str(int(self.outres["corn"]))
        other2 = "ананасов:" + str(int(self.outres[ "pineapple" ]))
        other3=  "кофе:     " + str(int(self.outres[ "coffee" ]))
        other4=  "табака:   " + str(int(self.outres[ "tobacco" ]))
        other5=  "сахара:   " + str(int(self.outres[ "sugar" ]))
        #other6 = str(self.poutres["tobacco"])
        idinfo = "На ферме может производиться кукуруза, кофе, ананасы, табак и сахар"
      if self.type == "clinic":
        resourses = "Количество медикаментов: " + str(int(self.amount))
        name = "Клиника"
        workers = "Работает: " + str(self.nwork) + " из " + str(self.maxnwork)
        sal = "Зарплата: " + str(int(self.salary))
        price ="Цена: "+ str(int(self.price))
        idinfo = "Недавно мы нашли на острове огромный склад аспирина. В этом здании врачи открывают колбы для островитян"
      if self.type == "home":
        resourses = "Качество жилья: " + str(int(self.quality))
        name = "Дом"
        workers = "Живёт: " + str(self.number) + " из " + str(self.max_number)
        sal = "Цена аренды: " + str(self.rent)
        #price = str(self.id)
        price = ""
        idinfo = "Здесь люди удовлетворяют нужду в отдыхе"
      if self.type == "fur":
        resourses = ""
        name = "Офис грузоперевозок"
        #mode1 = " Авто "
        #mode2 = "Ручной"
        price = ""
        idinfo = "Основное здание в экономике острова. Перевозит грузы из одних зданий в другие"
      if self.type == "shop":
        resourses = ""
        name = "Магазин"
        other1 = "кукурузы: " + str(int(self.outres["corn"]))
        other2 = "ананасов: " + str(int(self.outres[ "pineapple" ]))
        other3=  "кофе:     " + str(int(self.outres[ "coffee" ]))
        other4=  "табака:   " + str(int(self.outres[ "tobacco" ]))
        other5=  "сахара:   " + str(int(self.outres[ "sugar" ]))
        #price = ""
        idinfo = "Перепродаёт товары которые люди произвели на ферме, ранчо и заводах"
      if self.type == "port":
        resourses = ""
        name = "Порт"
        price = ""
        idinfo = "Экспортирует товары, произведённые на острове"
        cnt = 0
        for i in self.inres:
          cnt += self.inres[i]
        idinfo2 = "на складе: " + str(int(cnt))
          
      if self.type == "imigration":
        resourses = ""
        name = "Бюро иммиграции"
        price = ""
        idinfo = "Привлекает иммигрантов на остров"
      
      #pygame.draw.rect(sc, (225,225,220), (0, h/2, w+250, h/2+50))
      buttonsfarm[0].active = 1
      buttonsfarm[1].active = 1
      
      
      if infomod[0] == "mode":
        priorl2 = butdismode
      if infomod[0] == "other":
        priorl2 = butdisother
      if infomod[0] == "money":
        priorl2 = butdisprice
      if infomod[0] == "stat":
        priorl2 = butdisstat
      if infomod[0] == "info":
        priorl2 = butdisinfo
      for i in priorl2:
        i.active = 1
      s = self.type
      if self.eat_allow == 0:
       if s!="clinic" and s!="tavern":
        butdisprice[2].active = 0
        butdisprice[3].active = 0
      if self.workallow == 0:
        butdisprice[0].active = 0
        butdisprice[1].active = 0
        
        butdisprice[2].active = 0
        butdisprice[3].active = 0
      butdisstat[0 ].text =str( self.testp1 )
      butdisstat[1 ].text =str( self.testp2 )
      butdisstat[2 ].text =str( self.testp3 )
      butdisstat[3 ].text =str( self.testp4 )
      butdisstat[4 ].text =str( self.testp5 )
      #price = str(infomod[0])
      butdisinfo[0].text = idinfo
      butdisinfo[1].text = idinfo2
      butdismode[0].text = mode1
      butdismode[1].text = mode2
      butdismode[2].text = mode3
      butdismode[3].text = mode4
      butdismode[4].text = mode5
      butdisother[0].text = other1
      butdisother[1].text = other2
      butdisother[2].text = other3
      butdisother[3].text = other4
      butdisother[4].text = other5
      butdisother[5].text = other6
      buttonsfarm[1].text = name #везде
      butdisprice[5].text = resourses #в главную информацию
      butdisprice[6].text = workers# в price
      butdisprice[7].text = sal#в price
      butdisprice[4].text = price# тоже в price
      intersale = 1/fps*4
      interprice = 1/fps*4
      if self.salary > 10:
        intersale = (3+self.salary)/fps
      if self.price > 10:
        interprice = (3+self.price) /fps
      if butdisprice[0].press() == 1:
        self.salary += intersale
      if butdisprice[1].press() == 1:
        if self.salary-intersale > 0:
          self.salary -= intersale
        else:
          self.salary = 0
      if butdisprice[2].press() == 1:
        self.price += interprice
        
      if butdisprice[3].press() == 1:
        self.price -= interprice
      if self.type == "farm":
        if butdismode[0].press() == 1:
          self.subtype = "corn"
        if butdismode[1].press() == 1:
          self.subtype = "pineapple"
        if butdismode[2].press() == 1:
          self.subtype = "coffee"
        if butdismode[3].press() == 1:
          self.subtype = "tobacco"
        if butdismode[4].press() == 1:
          self.subtype = "sugar"
      if self.type == "fur":
        if butdismode[0].press() == 1:
          self.mode = "auto"
        if butdismode[1].press() == 1:
          self.mode = "manual"
      if self.type == "canns":
        if butdismode[0].press() == 1:
          self.subtype = "meat"
          self.alinres = reszero.copy()
          self.alinres[self.subtype] = 1
        if butdismode[1].press() == 1:
          self.subtype = "pineapple"
          self.alinres = reszero.copy()
          self.alinres[self.subtype] = 1
        if butdismode[2].press() == 1:
          self.subtype = "coffee"
          self.alinres = reszero.copy()
          self.alinres[self.subtype] = 1
        
        butdismode[5].text = str(self.f_eat_allow()) #self.subtype -- для тестов
        butdismode[5].text = self.subtype
      if self.type == "rancho":
        if butdismode[0].press() == 1:
          self.subtype = "meat"
        if butdismode[1].press() == 1:
          self.subtype = "milk"
      butdismode[6].text = eatallow #self.subtype -- для тестов
      butdismode[5].text = subtype
      #f1 = pygame.font.SysFont('arial', 40)
      #text1 = f1.render(name, True,(0, 0, 0))
      ##text2 = f1.render(resourses, True,(0, 0, 0))
      #text3 = f1.render(workers, True,(0, 0, 0))
      #text4 = f1.render(sal, True,(0, 0, 0))
      #sc.blit(text1, (0, h/2))
      #sc.blit(text2, (0, h/2 + 40))
      #sc.blit(text3, (0, h/2 + 80))
      #sc.blit(text4, (0, h/2 + 120))
      j = 0
      if infomod[0] == "other":
       for i in self.workers:
        buttonshuman[i].x = w/3*2
        buttonshuman[i].y = h/3*2 + 30 + 20*j
        buttonshuman[i].active = 1
        j += 1
        
        
    def draw(self):
        xhum = (xx + 100 * self.x) * mu + (1 - mu) * (w / 2)
        yhum = (yy + 100 * self.y) * mu + (1 - mu) * (h / 2)
        pygame.draw.rect(sc, (0,0,0), (xhum, yhum, 100*mu, 100*mu))
        i = int(40*mu)
        if i > 12:
            f1 = pygame.font.SysFont('arial', int(i))
            text1 = f1.render(self.text, True,
                      (180, 0, 0))
            sc.blit(text1, (xhum,yhum+ 40*mu))





class human(object):

    def __init__(self, a=0, b=0, id = 0):
        """Constructor"""
        
        self.id = id
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.p4 = 0
        
        
        self.wwt = 0
        
        
        self.thinfo1 = ""
        self.thinfo2 = ""
        self.thinfo3 = ""
        self.thinfo4 = ""
        self.thinfo5 = "я приехал на остров"
        
        self.life = 1
        self.wstage = 0# внутренние переменные для работы
        self.wj = 0
        self.wj2 = 0
        self.wa = 0
        self.wg = 0
        self.wres = ""
        self.wl = 0
        
        self.wresourses = reszero.copy()
        
        self.x  = a          #0
        self.y = b           #1
        self.xt = 8#2
        self.yt = 1#3
        self.speed = random.uniform(0.7, 1.1)
        self.state = 2    #двигается, делает, думает, работает#5
        self.type_target = -1#6
        self.number_target = 0#7
        
        self.aeat = 0
        self.amed = 0
        self.findworkp = 0
        
        
        self.teat = ""

        self.hap_eat = 10#8
        self.hap_health = 10
        self.hap_fun = 10
        self.rest = 0
        self.money = 90
        self.pprice = 0

        self.car = 0
        self.cars = 0
        self.k_hap_fun = random.randint(1,1000)
        self.k_eat = random.randint(1,1000)
        self.k_money = random.randint(1,1000)
        self.k_hap_health = random.randint(1,1000)
        self.k_rest = random.randint(1,1000)
        self.mi = -1
        self.mj = -1
        self.gi = -1
        self.work_type = -1
        self.age = random.randint(18,45)

        self.work_n = -1
        self.list = []
        
        self.cash = 0
        self.kcash = 0.01 #написать функцию, которая зависит от счастья. Когда появляются банки, может быть < 0
        self.homenumber = -1 #поиск дома -- составляем рейтинг по всем домам исходя из ренты и расположения, выбираем лучший
        self.salary = 0
        self.target = 0

        self.worktime = 0
        self.wt = 0
        self.name = names[random.randint(0,14)] + " " + surnames[random.randint(0,14)]
        #self.homenumber = -1
        
        self.allinfo = ""
    def initial(self):
        self.id = self.id
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.p4 = 0
        self.target = 0
        
        self.thinfo1 = ""
        self.thinfo2 = ""
        self.thinfo3 = ""
        self.thinfo4 = ""
        self.thinfo5 = "Я приехал на остров!"
        
        
        self.wstage = 0# внутренние переменные для работы
        self.wj = 0
        self.wj2 = 0
        self.wa = 0
        self.wg = 0
        self.wres = ""
        self.wl = 0
        
        self.wwa = 0
        self.wwi = 0
        self.wwj = 0
        self.wwres = 0
        self.wwb = 0
        
        
        self.wresourses = reszero.copy()
        
        self.x  = 0          #0
        self.y = 0           #1
        self.xt = 8#2
        self.yt = 1#3
        self.speed = 1#4
        self.state = 2    #двигается, делает, думает, работает#5
        self.type_target = -1#6
        self.number_target = 0#7
        
        self.aeat = 0
        self.amed = 0
        self.life = 1
        
        
        self.teat = ""

        self.hap_eat = 10#8
        self.hap_health = 10
        self.hap_fun = 10
        self.rest = 0
        self.money = 90
        self.pprice = 0
        

        self.car = 0
        self.cars = 0
        self.k_hap_fun = random.randint(3,9)
        self.k_eat = random.randint(3,9)
        self.k_money = random.randint(3,9)
        self.k_hap_health = random.randint(3,9)
        self.k_rest = random.randint(3,9)
        self.mi = -1
        self.mj = -1
        self.gi = -1
        self.work_type = -1

        self.work_n = -1
        self.list = []
        
        self.cash = 0
        self.kcash = 0.01 #написать функцию, которая зависит от счастья. Когда появляются банки, может быть < 0
        self.homenumber = -1 #поиск дома -- составляем рейтинг по всем домам исходя из ренты и расположения, выбираем лучший
        self.salary = 0

        self.worktime = 0
        self.wt = 0
        self.name = str(self.id)+names[random.randint(0,14)] + " " + surnames[random.randint(0,14)]
        #self.homenumber = -1
        
        self.allinfo = ""
    def tupd(self, stri):
      stri = str(stri)
      self.thinfo1 = self.thinfo2
      self.thinfo2 = self.thinfo3
      self.thinfo3 = self.thinfo4
      self.thinfo4 = self.thinfo5
      self.thinfo5 = stri
    def infodis(self):
      buttonsfarm[0].active = 1
      buttonsfarm[1].active = 1
      for i in buttonsinfomen:
        i.active = 1
      if buttonsinfomen[0].press() == 1:
        infomod[0] = "info"
        priorl2 = butdisinfo
      if buttonsinfomen[1].press()==1:
        infomod[0] = "mode"
        priorl2 = butdismode
      if buttonsinfomen[2].press()==1:
        infomod[0] = "money"
        priorl2 = butdisprice
      if buttonsinfomen[3].press()==1:
        infomod[0] = "stat"
        priorl2 = butdisstat
      if buttonsinfomen[4].press()==1:
        infomod[0] = "other"
        priorl2 = butdisother
      stdi= {0:"идет в ", 1:"занят, ", 2: "думает"}
      ttdi = {0: "ест в ", 1:"лечится в ", 2:"отдыхает в ", 3:"работает в ", 4:"веселится в "}
      
      res2 = ""
      w = ""
      if self.work_n < 0:
        w = "безработный"
      else:
        w = buildings[self.work_n].type
        if w in wpdict:
          w = wpdict[w]
      workpl = "место работы: " + w
      if self.state == 1:
        res = self.target.type
        if res in wpdict:
          res = wpdict[res]
        res2 = ttdi[self.type_target] + res
      if self.state == 0:
        res2 = self.target.type
        if res2 in wpdict:
          res2 = wpdict[res2]
      resourses = "статус: "+ stdi[self.state] + res2
      age = "возраст: " + str(self.age)
      
      name = self.name
      workers = "деньги:              " + str(int(self.money))
      sal = "зарплата на момент найма" + str(int(self.salary))
      #pygame.draw.rect(sc, (225,225,220), (0, h/2, w+250, h/2+50))
      if infomod[0] == "mode":
        priorl2 = butdismode
      if infomod[0] == "other":
        priorl2 = butdisother
        
        #pygame.draw.rect(sc, (0,0,0), (w/2, h/1.5 +20, self.hap_eat , 70))
      if infomod[0] == "money":
        priorl2 = butdisprice
      if infomod[0] == "stat":
        priorl2 = butdisstat
      if infomod[0] == "info":
        priorl2 = butdisinfo
      for i in priorl2:
        i.active = 1
      for i in butdisprice:
        i.text = ""
      for i in butdisinfo:
        i.text = ""
      for i in butdismode:
        i.text = ""
      for i in butdisother:
        i.text = ""
      for i in butdisstat:
        i.text = ""
      
      buttonsfarm[1].text = name
      butdisinfo[0].text = age
      butdisinfo[1].text = workpl
      butdisprice[4].text = resourses
      butdisprice[5].text = workers
      butdisprice[6].text = sal
      butdisstat[0].text = "сытость: " + str(int(self.hap_eat))
      butdisstat[1].text = "здоровье: " + str(int(self.hap_health))
      butdisstat[2].text = "веселье: " + str(int(self.hap_fun))
      butdisstat[3].text = "отдых: " + str(int(self.rest))
      butdisother[0].text= self.thinfo1
      butdisother[1].text = self.thinfo2
      butdisother[2].text = self.thinfo3
      butdisother[3].text = self.thinfo4
      butdisother[4].text = self.thinfo5
      
      
      f1 = pygame.font.SysFont('arial', 40)
      text1 = f1.render(name, True,(0, 0, 0))
      text2 = f1.render(resourses, True,(0, 0, 0))
      text3 = f1.render(workers, True,(0, 0, 0))
      text4 = f1.render(sal, True,(0, 0, 0))
      #sc.blit(text1, (0, h/2))
      #sc.blit(text2, (0, h/2 + 40))
      #sc.blit(text3, (0, h/2 + 80))
      #sc.blit(text4, (0, h/2 + 120))
    ##def goto2:
    def goto2(self, gxt,gyt):
      dx = gxt - self.x
      dy = gyt - self.y
      ds = math.sqrt(dx * dx + dy * dy)
      k = ds / self.speed
      if k != 0.0:
        dxx = (dx / k) / FPS
        dyy = (dy / k) / FPS
      else:
        dxx = 1000000000000
        dyy = 100000000000
      if mo(dx) > mo(dxx) + 0.1 or mo(dy) > mo(dyy) + 0.1:
        self.x += dxx
        self.y += dyy
      else:
        self.x = gxt
        self.y = gyt
        #self.car = gst
    def goto(self, gxt,gyt,gst):
      dx = gxt - self.x
      dy = gyt - self.y
      ds = math.sqrt(dx * dx + dy * dy)
      k = ds / self.speed
      if k != 0.0:
        dxx = (dx / k) / FPS
        dyy = (dy / k) / FPS
      else:
        dxx = 1000000000000
        dyy = 100000000000
      if mo(dx) > mo(dxx) + 0.1 or mo(dy) > mo(dyy) + 0.1:
        self.x += dxx
        self.y += dyy
      else:
        self.x = gxt
        self.y = gyt
        self.car = gst
        #self.car = 0
    def gowalk(self):
      if self.state == 0:  # идёт
        self.goto(self.xt,self.yt,0)
        if self.x == self.xt and self.y == self.yt:
          self.state = 1
    def gotocw2(self, gxt,gyt):
        self.wg = 1
        if self.car == 0: #
          self.gi = -1
          gd = 10000000
          for i in range (0,len(garages)):
                dx = self.x - garages[i].x
                dy = self.y - garages[i].y
                ds = math.sqrt(dx * dx + dy * dy)
                if ds <= gd:
                  self.gi = i
                  gd = ds
          if self.gi >=0:
           a = (garages[self.gi].xt,garages[self.gi].yt)
           md = 1000000000
           self.mi = -1
           self.mj = -1
           svset = graphsv(a)
           for i in range(0,len(rm)):
            for j in range(0,len(rm[0])):
              if alr((i,j),rm) ==1 and (i,j) in svset:
                dx = gxt - i
                dy = gyt - j
                ds = math.sqrt(dx * dx + dy * dy)
                if ds <= md:
                   self.mi = i
                   self.mj = j
                   md = ds
           if self.mi < 0:
                dc = -1
           else:
                dc = ds
          
                  #print("self.gi______________________________________gi")
                  #print(self.gi)
                  #print(garages)
            
           dx = self.x - gxt
           dy = self.y - gyt
           ds = math.sqrt(dx * dx + dy * dy)
          if self.gi>=0 and self.mi >=0 and self.car == 0 and md + gd + 3< ds:
           
              self.car = 1
          else:
              self.car = 7
              
        if self.car == 1:
            self.goto(garages[self.gi].x,garages[self.gi].y,3)
            #print("gi")
            #print(self.gi)
           
            #print("sc1")
            #print(self.car)
        if self.car == 3:
             #self.goto(self.mi,self.mj,5)
             a = (garages[self.gi].xt,garages[self.gi].yt)
             b = (self.mi,self.mj)
             self.list = nod3(a,b,rm)
             #print("list = ")
             #print(self.list)
             self.car = 4
             self.cars = car()
             #print(g(self.list))
             self.cars.xt = g(self.list)[0]
             #print("sc3")
             #print("mi")
             #print(self.mi)
             #print(self.car)
        if self.car == 4:
          #self.cars.life(self.list)
          ca = self.cars
          self.cars.life(self.list)
          #self.cars.x += 60/FPS
          #print(self.list)
          #print("ready")
          #print("sc4")
          if self.cars.x >= self.cars.xt:
            self.x = self.mi
            self.y = self.mj
            self.car = 5
            self.cars = 0
          #ca.renderg(self.list)
        if self.car == 5:
             #print("sc5")
             self.goto(gxt,gyt,6)
             if self.x > gxt-0.25 and self.x < gxt + 0.25:
               if self.y > gyt-0.25 and self.y < gyt + 0.25:
                 self.x = gxt
                 self.y = gyt
                 self.state = 1
                 self.car = 0
                 #print("sc66")
             #print("xt")
             #print(self.xt)
        if self.car == 6:
              
             #print("state1")
             self.state = 1
             self.car = 0
             #print("sc6")
             #self.gi = -1
             #self.mi = -1
        if self.car == 7:
          self.goto(gxt,gyt,8)
        if self.car == 8:
          self.wg = 0
    def gotocw3(self, gxt,gyt):
        self.wg = 1
        if self.car == 0:
          self.gi = -1
          gd = 10000000
          for i in range (0,len(garages)):
                dx = self.x - garages[i].x
                dy = self.y - garages[i].y
                ds = math.sqrt(dx * dx + dy * dy)
                if ds <= gd:
                  self.gi = i
                  gd = ds
          if self.gi >=0:
           a = (garages[self.gi].xt,garages[self.gi].yt)
           md = 1000000000
           self.mi = -1
           self.mj = -1
           for i in range(0,len(rm)):
            for j in range(0,len(rm[0])):
              if alr((i,j),rm) ==1 and nod3(a,(i,j),rm)!=0:
                dx = gxt - i
                dy = gyt - j
                ds = math.sqrt(dx * dx + dy * dy)
                if ds <= md:
                   self.mi = i
                   self.mj = j
                   md = ds
           if self.mi < 0:
                dc = -1
           else:
                dc = ds

           dx = self.x - gxt
           dy = self.y - gyt
           ds = math.sqrt(dx * dx + dy * dy)
          if self.gi>=0 and self.mi >=0 and self.car == 0 and md + gd + 3< ds:
           
              self.car = 1
          else:
              self.car = 7
              
        if self.car == 1:
            self.goto(garages[self.gi].x,garages[self.gi].y,3)
            
        if self.car == 3:
             
             b = (self.mi,self.mj)
             self.list = nod3(a,b,rm)
             
             self.car = 4
             self.cars = car()
             
             self.cars.xt = g(self.list)[0]
             
        if self.car == 4:
          #self.cars.life(self.list)
          ca = self.cars
          self.cars.life(self.list)
          if self.cars.x >= self.cars.xt:
            self.x = self.mi
            self.y = self.mj
            self.car = 5
            self.cars = 0
        if self.car == 5:
             self.goto(gxt,gyt,6)
             if self.x > gxt-0.25 and self.x < gxt + 0.25:
               if self.y > gyt-0.25 and self.y < gyt + 0.25:
                 self.x = gxt
                 self.y = gyt
                 self.state = 1
                 self.car = 0
        if self.car == 6:
             self.state = 1
             self.car = 0
        if self.car == 7:
          self.goto(gxt,gyt,8)
        if self.car == 8:
          self.wg = 0
    def gotocw(self, gxt,gyt):
        self.wg = 1
        if self.car == 0: # переделать модуль. сначала ищем ближайший гараж, затем ищем ближайшую дорогу среди тех (!)которые связаны с гаражом!!!
          #print("sc0")
          self.gi = -1
          gd = 10000000
          for i in range (0,len(garages)):
                dx = self.x - garages[i].x
                dy = self.y - garages[i].y
                ds = math.sqrt(dx * dx + dy * dy)
                if ds <= gd:
                  self.gi = i
                  gd = ds
          if self.gi >=0:
           self.mi = garages[self.gi].rm[self.target][0]
           self.mj = garages[self.gi].rm[self.target][1]
           dx = self.target.x - self.mi
           dy = self.target.y- self.mj
           md = math.sqrt(dx * dx + dy * dy)
           dx = self.x - self.target.x
           dy = self.y - self.target.y
           ds = math.sqrt(dx * dx + dy * dy)
          if self.gi>=0 and gd + md + garages[self.gi].rd[self.target]/8< ds:
           
              self.car = 1
          else:
              self.car = 7
              
        if self.car == 1:
            self.goto(garages[self.gi].x,garages[self.gi].y,3)
            #print("gi")
            #print(self.gi)
           
            #print("sc1")
            #print(self.car)
        if self.car == 3:
             #self.goto(self.mi,self.mj,5)
             a = (garages[self.gi].xt,garages[self.gi].yt)
             b = (self.mi,self.mj)
             self.list = garages[self.gi].rlists[self.target]
             #print("list = ")
             #print(self.list)
             self.car = 4
             self.cars = car()
             #print(g(self.list))
             self.cars.xt = garages[self.gi].rd[self.target]
             #print("sc3")
             #print("mi")
             #print(self.mi)
             #print(self.car)
        if self.car == 4:
          #self.cars.life(self.list)
          ca = self.cars
          self.cars.life(self.list)
          #self.cars.x += 60/FPS
          #print(self.list)
          #print("ready")
          #print("sc4")
          if self.cars.x >= self.cars.xt:
            self.x = self.mi
            self.y = self.mj
            self.car = 5
            self.cars = 0
          #ca.renderg(self.list)
        if self.car == 5:
             #print("sc5")
             self.goto(gxt,gyt,6)
             if self.x > gxt-0.25 and self.x < gxt + 0.25:
               if self.y > gyt-0.25 and self.y < gyt + 0.25:
                 self.x = gxt
                 self.y = gyt
                 self.state = 1
                 self.car = 0
                 #print("sc66")
             #print("xt")
             #print(self.xt)
        if self.car == 6:
              
             #print("state1")
             self.state = 1
             self.car = 0
             #print("sc6")
             #self.gi = -1
             #self.mi = -1
        if self.car == 7:
          self.goto(gxt,gyt,8)
        if self.car == 8:
          self.wg = 0
        
          
    def go(self):
      if self.state == 0:  # идёт
        self.gotocw(self.xt,self.yt)
        if self.car == 8:
          self.state = 1
          self.car = 0
          #print("walk")
    def findhome(self):
      #print("findhome")
      f = self.work_n
      if f >= 0:
        xhum = buildings[f].x
        yhum = buildings[f].y
      else:
        xhum = self.x
        yhum = self.y
      
      priorl= []
      dist = xhum*xhum+yhum*yhum
      for i in homes:
        if i.number < i.max_number:
          xh = xhum-i.x
          yh = yhum-i.y
          dis = xh*xh+yh*yh
          p = i.quality
          priorl.append((100-dis)*p*(100-i.rent))
          #i.number += 1
        else:
          priorl.append(-100000000)
      if len(priorl) == 0:
          priorl = [-100000000]
      maxi = max(priorl)
      maxin = priorl.index(maxi)
      if maxi != -100000000:
        self.homenumber = maxin
        homes[maxin].number += 1
      else:
        maxi = maxi
        #homes.append(home(random.randint(-10,10), random.randint(-10,10),2,1, random.randint(0,255)))
    #def findwork(self):
      #print("findwork")
    def findwork(self):
      if self.work_n >=0:
        buildings[self.work_n].nwork-= 1
        buildings[self.work_n].workers.remove(self.id)
      i = self.homenumber
      if i == -1:
        xhum = self.x
        yhum = self.y
      else:
        xhum = homes[i].x
        yhum = homes[i].y
      l = buildings
      priorl = []
      for wp in l:
        if wp.workallow == 1 and wp.maxnwork > wp.nwork:
          dx = (xhum - wp.x)**2
          dy = (yhum - wp.x)**2
          dist = math.sqrt(dx+dy)
          pd = (1000-dist)/100
          pw = 1-(wp.nwork/wp.maxnwork)
          priorl.append((pd+wp.salary+wp.salary)*pw)
        
        else:
          priorl.append(-100000000)
          #print(wp.work_allow)
      if len(priorl) == 0:
          priorl = [-100000000]
      maxi = max(priorl)
      maxin = priorl.index(maxi)
      if maxi != -100000000:
        #print(priorl)
        self.work_n = maxin
        self.salary = buildings[maxin].salary
        buildings[maxin].nwork += 1
        buildings[maxin].workers.append(self.id)
    def findwork2(self):
      if self.work_type == 0:
        farms[self.work_n].nwork-= 1
        farms[self.work_n].workers.remove(self.id)
      if self.work_type == 1:
        clinics[self.work_n].nwork-= 1
        clinics[self.work_n].workers.remove(self.id)
      i = self.homenumber
      if i == -1:
        xhum = self.x
        yhum = self.y
      else:
        xhum = homes[i].x
        yhum = homes[i].y
      l = farms + clinics
      priorl = []
      for wp in l:
        if wp.maxnwork > wp.nwork:
          dx = (xhum - wp.x)**2
          dy = (yhum - wp.x)**2
          dist = math.sqrt(dx+dy)
          pd = (1000-dist)**3
          priorl.append(pd*wp.salary*wp.salary)
          
        else:
          priorl.append(-100000000)
      if len(priorl) == 0:
          priorl = [-100000000]
      maxi = max(priorl)
      maxin = priorl.index(maxi)
      if maxin in range(0,len(farms)) and maxi != -100000000:
        self.work_type = 0
        self.work_n = maxin
        self.salary = farms[maxin].salary
        farms[maxin].nwork += 1
        farms[maxin].workers.append(self.id)
      if maxin in range(len(farms),len(clinics)+len(farms)) and maxi != -100000000:
        self.work_type = 1
        self.work_n = maxin-len(farms)
        self.salary = clinics[maxin-len(farms)].salary
        clinics[maxin-len(farms)].nwork += 1
        clinics[maxin-len(farms)].workers.append(self.id)
    def workshop(self):
     
      f = self.work_n
      if self.wstage == 0:
        wsd = {}
        wsa= 0
        for i in buildings[f].inres:
          wsd[buildings[f].inres[i]] = i
        wsa = max(wsd)
        if wsa > 0:
          self.wres = wsd[wsa]
          self.wstage = 1
        else:
          self.wstage = 98
      if self.wstage == 1:
          
          buildings[f].inres[self.wres]-= 5/FPS
          buildings[f].pinres[self.wres]-= 5/FPS
          buildings[f].outres[self.wres]+= 5/FPS
          buildings[f].poutres[self.wres]+= 5/FPS
          if buildings[f].inres[self.wres] <0 :
            #buildings[f].inres[self.wres] = 0
            self.wstage = 100
      if self.wstage >= 98 and self.wstage < 100:
          self.wstage += 1/10/FPS
          if self.wstage >= 99:
            self.wstage = 100
      if self.wstage == 100:
          self.money += buildings[f].salary
          money[0]-= buildings[f].salary
          self.wstage = 0
          self.state = 2
          self.tupd("Конец рабочего дня")
    def workrancho(self):
        f = self.work_n
        wores = buildings[f].subtype
        if buildings[f].salary > 0 and buildings[f].outres[wores] < 1000:
          buildings[f].amount += 1 * math.sqrt( buildings[f].salary)/ FPS/10
          buildings[f].outres[wores] += 1 * math.sqrt(buildings[f].salary)/ FPS/10
          buildings[f].poutres[wores] += 1 * math.sqrt(buildings[f].salary)/ FPS/10
          money[0] -= buildings[f].salary / FPS/10
          self.money += buildings[f].salary / FPS/10
        self.worktime += 1 / FPS / 10

        if self.worktime >= 1:
             self.state = 2
             self.worktime = 0
             self.tupd("Конец рабочего дня")
    def workfarm(self):
      
        f = self.work_n
        
        wores = buildings[f].subtype
        if buildings[f].salary > 0 and buildings[f].outres[wores] < 2000:
          buildings[f].amount += 1 * math.sqrt( buildings[f].salary)/ FPS/10
          buildings[f].outres[wores] += 1 * math.sqrt(buildings[f].salary)/ FPS/10
          buildings[f].poutres[wores] += 1 * math.sqrt(buildings[f].salary)/ FPS/10
          money[0] -= buildings[f].salary / FPS/10
          self.money += buildings[f].salary / FPS/10
        self.worktime += 1 / FPS / 10

        if self.worktime >= 3:
             self.state = 2
             self.worktime = 0
             self.tupd("Конец рабочего дня")
    def workclinic(self):
        f = self.work_n
        buildings[f].amount += 1 * math.sqrt(buildings[f].salary) / FPS
        money[0] -= buildings[f].salary / FPS
        self.money += buildings[f].salary / FPS
        buildings[f].amount += (3 / FPS)
        self.worktime += 1 / FPS / 2

        if self.worktime >= 10:
             self.state = 2
             self.worktime = 0
             self.tupd("Конец рабочего дня")
    def workimig(self):
     if self.wstage == 0:
      f = self.work_n
      self.wt += 1/FPS
      efec = math.sqrt(buildings[f].salary)
      if buildings[f].resourses < 2000:
        
        buildings[f].resourses += efec/FPS
        self.money += buildings[f].salary/FPS
        money[0] -= buildings[f].salary/FPS
      else:
        addhuman()
        buildings[f].resourses = 0
        self.tupd("Я привлёк человека на остров!")
      if self.wt > 10:
        self.wstage = 1
        self.wt = 0
     if self.wstage == 1:
       self.state = 2
       self.wstage = 0
       self.tupd("Конец рабочего дня")
       
    def workfur(self):
      f = self.work_n
      if self.wstage == 1313:
        self.wj.poutres[self.wres] -= self.wa
        self.wj2.pinres[self.wres] += self.wa
        self.wstage = 1
      if self.wstage == 0:
        #print("begin")
        inset = set()
        outset = set()
        for j in buildings:
          if j.out_allow == 1:
            #print(j.outres)
            for i in j.outres:
              if j.aloutres[i] !=0 and j.poutres[i]>150:
                outset.add(i)
        for j in buildings:
          if j.in_allow == 1 and j.nwork != 0:
            #print(j.inres)
            for i in j.inres:
              #if j.type == "shop"
                #print(j.nwork)
                #print(j.alinres[i])
                #print(j.pinres[i])
              if j.alinres[i]!=0 and j.pinres[i]<200*math.sqrt(j.salary)*j.nwork:
                inset.add(i)
                
        wset = inset & outset
        #print(wset)
        #print(outset)
        #print(wset)
        #print(inset)
        #print(outset)
        wj = 0
        wa = 0 #количество
        maxwprior = 0
        wprior = 0
        wk = 0
        wj2 = 0
        maxwa=0
        
        wp1= 0
        wp2 = 0
        wp3 = 0
        wp4 = 0
        #print(wset)
        
        
              
            
        for j in buildings:
          if j.out_allow == 1:
            for i in buildings:
              if i.in_allow == 1:
                for k in wset:
                  if j.aloutres[k]!=0 and i.alinres[k]!=0 and j.poutres[k]>150:
                    #print("ok")
                    wp1 = j.poutres[k]#ещё один словарь сделать?
                    self.testp = wp1
                    
                    wp4 = i.pinres[k]
                    i.testp4 = wp4
                    wp3 = min(5000, 75*math.sqrt(i.salary)*i.nwork)
                    i.testp3 = wp3
                    if wp4>wp3:
                      wp2=0
                    else:
                      wp2 = min(wp3 - wp4,wp1)
                      i.testp2 = wp2
                    wprior = wp2
                    if i.type == "port" and (j.type == "farm" or j.type == "rancho"):
                      wprior = wp2/4
                    if i.type == "shop":
                      wprior = wp2/5
                    
                    if wprior > maxwprior:
                      maxwprior = wprior
                      wa = wp2
                      wj = j
                      wj2 = i
                      wk = k
                      #self.wstage = 1313
                
                
        
        
        #self.testp1 = wp1
        #self.testp2 = wp2
        if wa > 0 and wj != 0:
          self.wstage = 1313
          self.wj2 = wj2
          self.wa = wa
          ##wj.poutres[wk] -= wa
          #wj2.pinres[wk] += wa
          #print(self.wj)
          self.wj = wj
          self.wres = wk
        else:
          self.wstage = 100
      
      if self.wstage == 1:
        wj = self.wj
        #print("st1")
        self.gotocw2(self.wj.x,self.wj.y)
        if self.car == 8:
          self.wstage = 10
          self.car = 0
          self.wg = 0
      if self.wstage == 10:
        wj = self.wj
        wa = self.wa
        
        if wj.outres[self.wres] >= 15/FPS and self.wg<=wa-15/ FPS :
          self.wresourses[self.wres] += 15/ FPS
          self.wg+= 15/ FPS
          wj.outres[self.wres] -= 15/FPS
          money[0] -= buildings[f].salary / FPS
          self.money += buildings[f].salary / FPS
        elif self.wg>wa-15/ FPS:
          #self.wresourses[self.wres] += wj.outres[self.wres]
          #wj.outres[self.wres] = 0
          wj.outres[self.wres] += self.wg-wa
          self.wresourses[self.wres] -= self.wg-wa
          self.wstage = 20
          self.wj = 0
          self.wg = 0
        elif wj.outres[self.wres] <= 15/FPS:
          self.wresourses[self.wres] += wj.outres[self.wres]
          wj.outres[self.wres] = 0
          
          self.wstage = 20
          self.wj = 0
          self.wg = 0
        else:
          self.wstage = 20
          self.wj = 0
          self.wg = 0
      
        
            
      if self.wstage == 20:
        wj = self.wj2
        #print("st20")
        self.gotocw2(wj.x,wj.y)
        if self.car == 8:
          self.wstage = 21
          self.car = 0
      if self.wstage == 21:
        wj = self.wj2
        if self.wresourses[self.wres] >= 15/FPS:
          wj.inres[self.wres] += 15/ FPS
          self.wresourses[self.wres] -= 15/FPS
          money[0] -= buildings[f].salary / FPS
          self.money += buildings[f].salary / FPS
        else:
          wj.inres[self.wres] += self.wresourses[self.wres]
          self.wresourses[self.wres]
          self.wstage = 100
          self.wj = 0
      if self.wstage == 100:
        
        self.state = 2
        self.wstage = 0
        self.tupd("Конец рабочего дня")
    def workrome(self):
      f = buildings[self.work_n]
      if self.wstage == 0:
        self.wt = 0
        self.wstage = 1
      if self.wstage == 1:
        if f.inres["sugar"] > 0:
          f.inres["sugar"] -= math.sqrt(f.salary)/FPS/8
          f.pinres["sugar"] -= math.sqrt(f.salary)/FPS/8
          f.outres["rom"]+= math.sqrt(f.salary)/FPS/8
          f.poutres["rom"]+= math.sqrt(f.salary)/FPS/8
        self.money += f.salary/FPS
        money[0]-=f.salary/FPS
        self.wt += 1/FPS
        if self.wt > 10:
          self.wt = 0
          self.wstage = 10
      if self.wstage == 10:
        self.state = 2
        self.wstage = 0
        self.tupd("Конец рабочего дня")
    
    def workcheese(self):
      f = buildings[self.work_n]
      if self.wstage == 0:
        self.wt = 0
        self.wstage = 1
      if self.wstage == 1:
        if f.inres["milk"] > 0:
          f.inres["milk"] -= math.sqrt(f.salary)/FPS/8
          f.pinres["milk"] -= math.sqrt(f.salary)/FPS/8
          f.outres["cheese"]+= math.sqrt(f.salary)/FPS/8
          f.poutres["cheese"]+= math.sqrt(f.salary)/FPS/8
        self.money += f.salary/FPS
        money[0]-=f.salary/FPS
        self.wt += 1/FPS
        if self.wt > 10:
          self.wt = 0
          self.wstage = 10
      if self.wstage == 10:
        self.state = 2
        self.wstage = 0
        self.tupd("Люблю сыр, но на сегодня хватит")
        
    def workcanns(self):
      f = buildings[self.work_n]
      if self.wstage == 0:
        self.wt = 0
        self.wstage = 1
      if self.wstage == 1:
        if f.inres[f.subtype] > 0:
          f.inres[f.subtype] -= math.sqrt(f.salary)/FPS/8
          f.pinres[f.subtype] -= math.sqrt(f.salary)/FPS/8
          f.outres["canns"]+= math.sqrt(f.salary)/FPS/8
          f.poutres["canns"]+= math.sqrt(f.salary)/FPS/8
        self.money += f.salary/FPS
        money[0]-=f.salary/FPS
        self.wt += 1/FPS
        if self.wt > 10:
          self.wt = 0
          self.wstage = 10
      if self.wstage == 10:
        self.state = 2
        self.wstage = 0
        self.tupd("Конец рабочего дня")
        
    def workcigar(self):
      f = buildings[self.work_n]
      if self.wstage == 0:
        self.wt = 0
        self.wstage = 1
      if self.wstage == 1:
        if f.inres["tobacco"] > 0:
          f.inres["tobacco"] -= math.sqrt(f.salary)/FPS/8
          f.pinres["tobacco"] -= math.sqrt(f.salary)/FPS/8
          f.outres["cigar"]+= math.sqrt(f.salary)/FPS/8
          f.poutres["cigar"]+= math.sqrt(f.salary)/FPS/8
        self.money += f.salary/FPS
        money[0]-=f.salary/FPS
        self.wt += 1/FPS
        if self.wt > 10:
          self.wt = 0
          self.wstage = 10
      if self.wstage == 10:
        self.state = 2
        self.wstage = 0
        self.tupd("Конец рабочего дня")
    
    def workthe(self):
      f = self.work_n
      if self.wstage == 0:
        self.wa = 0
        self.wstage = 1
      if self.wstage == 1:
        self.wa += 1/FPS
        self.money += buildings[f].salary/FPS
        money[0] -= buildings[f].salary/FPS
        if self.wa >= 10:
          self.wstage = 100
      if self.wstage == 100:
        self.wa = 0
        self.state = 2
        self.tupd("Хватит с меня работы актером")
    def workport(self):
      f = self.work_n
      if self.wstage == 0:
        #print("begin")
        wpr = buildings[f].inres
        
        wpg = {}
        for i in wpr:
          wpg[wpr[i]] = i
        cr = wpg[max(wpg)]
        self.wstage = 1
        self.wpr = wpr
        self.wcr = cr
      if self.wstage == 1:
        if self.wpr[self.wcr] > 0:
          f = self.work_n
          cr = self.wcr
          wpr = self.wpr
          buildings[f].pinres[cr] -= 50/FPS
          wpr[cr] -= 50/FPS
          money[0] += 50*exportprices[cr]/FPS/100
          #money[0] -= buildings[f].salary / FPS
          #self.money += buildings[f].salary / FPS
        else:
          self.wpr[self.wcr]= 0
          self.state = 2
          self.wstage = 0
          self.money += 120
          self.tupd("Всю работу сделал")
    
    def think(self):
        if self.findworkp ==1:
          self.findwork()
          self.findworkp = 0
        thinkmaxmoney = 100
        funp = (10 - self.hap_fun) * self.k_hap_fun / 10
        healp = (10 - self.hap_health) * self.k_hap_health / 10  # приоритет здоровья
        eatp = (10 - self.hap_eat) * self.k_eat / 10  # приоритет еды
        restp = (10 - self.rest) * self.k_rest / 10  # приоритет отдыха
        workp = (100 - self.money) * self.k_money/100  # приоритет работы, сделать так что зависит от средней зп и от зп чела или от прожиточного минимума
        self.wwt += 1/FPS
        if self.state == 2:  # как думает куда идти
            self.p1 = healp
            self.p2 = eatp
            self.p3 = restp
            self.p4 = workp
            #self.tupd("Думаю-думаю-думаю")

            cnte = 0
            cntc = 0
            cntf = 0
            for j in buildings:
                if j.f_eat_allow() == 1 and self.money > j.price*3:
                  cnte = 1
            for j in buildings:
              if j.f_fun_allow() == 1 and j.f_visit_allow() == 1:
                cntf = 1
                  #print("eatallowed")
            for j in clinics:
              cntc += j.amount

            priorl = []  # 0 -- еда 1 -- здоровье 2 -- развлчение 3 -- работа

            if cnte == 1 and self.money>0:  # 0
                priorl.append(eatp)
            else:
                priorl.append(-100000000000000000)
                #pri("noeat")
                self.p2 = -4

            if len(clinics) > 0 and self.money > 1 and cntc > 1:  # 1
                priorl.append(healp)
            else:
                priorl.append(-100000000000000000)
                self.p1 = -4

            if self.homenumber != -1:
                priorl.append(restp)
            else:
                priorl.append(-100000000000000000)
                self.findhome()
                self.p3 = -4
                #pri("nohome")

            if self.work_n != -1:  # 2
                priorl.append(workp)
            else:
                priorl.append(-100000000000000000)
                
                self.findwork()
                self.p4 = -4
            if cntf == 1 and self.money>0:  # 0
                priorl.append(funp)
            else:
                priorl.append(-100000000000000000)
                #pri("noeat")
                #self.p2 = -4
            maxi = max(priorl)
            maxin = priorl.index(maxi)
            #self.tupd("maxin = "+ str(maxin))
            #print("maxin = " + str(maxin))
            if maxi != -100000000000000000:
                self.type_target = maxin
                #print("maxin")
                #print(maxin)
            else:
                self.type_target = -1
            if self.wwt > 70 and self.work_n != -1:
              self.type_target = 3
              self.wwt = 0
              #self.tupd("Давно я не был на работе")
                #print(priorl)
            #if self.money <= 1 and self.work_type != -1:
                #self.type_target = -1
                #pri("moneyforce")
                #self.type_target = 3
            
            
            #self.tupd("maxin = " + str(maxin))
                
            #print(
#self.type_target)

            if self.type_target == 1:
                xs = 10000000000
                for j in range(0, len(clinics)):

                    xm = self.x - clinics[j].x
                    xm = xm * xm
                    ym = self.y - clinics[j].y
                    ym = ym * ym
                    if xs > xm + ym:
                        xj = j
                        xs = xm + ym
                self.xt = clinics[xj].x
                self.yt = clinics[xj].y
                self.state = 0
                self.number_target = xj
                self.target = clinics[xj]
                self.tupd("Иду за аспирином")
                
                
                #print(i[2])
                #print("test4")
            elif self.type_target == 0:
                xj = -1
                xs = 100
                for j in range(0, len(buildings)):
                    if buildings[j].f_eat_allow() == 1 and self.money > buildings[j].price*3:  #переделать условие, пока затычка
                        xm = self.x - buildings[j].x
                        xm = xm * xm
                        ym = self.y - buildings[j].y
                        ym = ym * ym
                        if xs > xm + ym:
                            xj = j
                            xs = xm + ym
                
                if xj > -1:
                  wa = 0
                  wr = ""
                  for i in buildings[xj].outres:
                    if i in eat:
                      if min(buildings[xj].outres[i], buildings[xj].poutres[i]) > wa:
                        wa = min(buildings[xj].outres[i], buildings[xj].poutres[i])
                        wr = i
                  if wa > 0:
                    heat = 10 - self.hap_eat
                    meat = self.money/buildings[xj].price
                    self.pprice = buildings[xj].price
                    self.aeat = min(wa, meat,heat)
                    self.teat = wr
                    self.xt = buildings[xj].x
                    self.yt = buildings[xj].y
                    self.state = 0
                    self.number_target = xj
                    self.target = buildings[xj]
                    buildings[xj].poutres[wr] -= self.aeat
                    self.wg = 0
                    self.tupd("Иду за едой")
                  else:
                    self.tupd("Сошел с ума от емысле о еде")
                  #когда будем делат по модели predictable, здесь будем считать и уменьшать pres здания
                  #его будем считать как минимум из продуктов которые человек может купить, которые ему нужны чтобы добрать сытость до 10 и доступных продуктов
               # print(i[2])
                #print("test5")
            ##################################### решили идти за деньгами

            elif self.type_target == 2:
                if self.homenumber != -1:
                    self.xt = homes[self.homenumber].x
                    self.yt = homes[self.homenumber].y
                    self.state = 0
                    self.tupd("Пойду посплю")
                    #print("chosen_rest")
                    self.target = homes[self.homenumber]
                    
                else:
                  self.findhome()
                  self.state = 2

            elif self.type_target == 3:
                if self.work_n >= 0: 
                    self.xt = buildings[self.work_n].x
                    self.yt = buildings[self.work_n].y
                    self.state = 0
                    self.tupd("Пора работать")
                    self.target = buildings[self.work_n]
                    self.wstage = 0
                    #print("chosen_work")
            elif self.type_target == 4:
                xj = -1
                xs = 10000000000000000
                for j in range(0, len(buildings)):
                    if buildings[j].f_fun_allow() == 1:  #переделать условие, пока затычка
                        xm = self.x - buildings[j].x
                        xm = xm * xm
                        ym = self.y - buildings[j].y
                        ym = ym * ym
                        if xs > xm + ym:
                            xj = j
                            xs = xm + ym
                if xj > -1:
                  
                    self.xt = buildings[xj].x
                    self.yt = buildings[xj].y
                    buildings[xj].visiters.append(self)
                    self.state = 0
                    self.number_target = xj
                    self.target = buildings[xj]
                    self.tupd("Пойду веселиться")
                else:
                  self.tupd("Сошел с ума от веселья")
            #else:
              #self.tupd("тип цели "+ str(self.type_target))
              #self.state = 0
              #self.tupd("Пойду погуляю")
              #self.type_target = -1
              #self.xt = random.uniform(0,n-1)
              #self.yt = random.uniform(0,m-1)
              

                


    def do(self):
        if self.state == 1:
            n = 1
            if self.type_target == 0:  # ест
                #print("eating")
                wa = self.aeat
                f = buildings[self.number_target]
                
                if f.outres[self.teat]>3/FPS and self.wg <= wa - 3/FPS and self.money>=3/FPS:
                  
                    self.hap_eat += 3 / FPS
                    self.wg += 3/FPS
                    self.money -= 3 * self.pprice/ FPS
                    money[0] += 3 * self.pprice/ FPS
                    buildings[self.number_target].outres[self.teat] -= 3 / FPS
                elif self.money <= 3 * self.pprice/ FPS:
                  self.money = 0
                  #print(self.aeat)
                  f.poutres[self.teat] += (wa - self.wg) + 0.001
                  f.outres[self.teat] += 0.001
                  self.state = 2
                  self.hap_eat = 10
                  self.wg = 0
                  self.aeat = 0
                elif self.wg > wa -3/FPS:
                    f.outres[self.teat] += self.wg-wa + 0.001
                    f.poutres[self.teat] +=  0.001
                    self.hap_eat -= self.wg-wa
                    self.state = 2
                    self.hap_eat = 10
                    self.wg = 0
                    self.aeat = 0
                    
                elif f.outres[self.teat] <= 3/FPS:
                    self.hap_eat += f.outres[self.teat]
                    f.outres[self.teat] = 0.001
                    f.poutres[self.teat] += (wa - self.wg) + 0.001
                    self.state = 2
                    self.hap_eat = 10
                    self.wg = 0
                    self.aeat = 0
                elif self.money <= 3 * self.pprice/ FPS:
                  self.money = 0.001
                  f.poutres[self.teat] += wa - self.wg + 0.001
                  f.outres[self.teat]+= 0.001
                  self.state = 2
                  self.hap_eat = 10
                  self.wg = 0
                  self.aeat = 0
                else:
                  f.poutres[self.teat] += wa - self.wg + 0.001
                  f.outres[self.teat]+= 0.001
                  self.state = 2
                  self.hap_eat = 10
                  self.wg = 0
                  self.aeat = 0
                ######################################
            if self.type_target == 1:  # лечится
              if (clinics[self.number_target].amount
>= 0.1):
                self.hap_health += (3 / FPS) * (1 - nds)
                clinics[self.number_target].amount -= (3 / FPS) * (1 - nds)
                self.money -= medc / FPS
                money[0] += medc / FPS
                #print(i[8][3])
                #print("money t2")
                if self.hap_health >= 10:
                    self.hap_health = 10
                    self.state = 2
                if self.money <= 0:
                    self.money = 0
                    self.state = 2
              else:
                self.state = 2
                self.hap_health = 10

            if self.type_target == 2:
                self.rest += 6 / FPS
                #print(self.rest)
                if self.rest >= 10:
                    self.state = 2
                    self.hap_rest = 10

            if self.type_target == 3:

                #if self.work_type == -1:
                    #print("DD")

                if buildings[self.work_n].type == "farm":  # если работаешь на плантации 1) зп работнику из бюджета 2) увеличение количества еды на ферме
                    self.workfarm()
                    #self.tupd("Фермерам тяжело")
                if buildings[self.work_n].type == "clinic":  # если работаешь в аптеке
                    #i[2] = health[11][0]
                    #i[3] = health[11][1]
                    self.workclinic()
                if buildings[self.work_n].type == "port":
                  self.workport()
                if buildings[self.work_n].type == "fur":
                  self.workfur()
                if buildings[self.work_n].type == "imigration":
                  self.workimig()
                if buildings[self.work_n].type == "shop":
                  self.workshop()
                if buildings[self.work_n].type == "tavern":
                  self.workthe()
                if buildings[self.work_n].type == "rancho":
                  self.workrancho()
                if buildings[self.work_n].type == "rome":
                  self.workrome()
                if buildings[self.work_n].type =="cheese":
                  self.workcheese()
                if buildings[self.work_n].type == "canns":
                  self.workcanns()
                if buildings[self.work_n].type == "cigar":
                  self.workcigar()
                
            if self.type_target == -1:
              self.state = 2
            if self.type_target == 4:
              if self.hap_fun<8 and self.money > 0:
                    self.hap_fun += 2 / FPS
                    self.money -= 2 *  buildings[self.number_target].price/ FPS
                    money[0] += 2 *  buildings[self.number_target].price/ FPS
              else:
                self.state = 2
                self.hap_fun = 10
                #li = buildings[self.number_target].visiters.index(self)
                buildings[self.number_target].visiters.remove(self)
                self.tupd("Хватит с меня веселья")


    def draw(self):
        xhum = (xx + 100 * self.x) * mu + (1 - mu) * (w / 2)
        yhum = (yy + 100 * self.y) * mu + (1 - mu) * (h / 2)
        if xhum >= -100 and xhum <= w+100 and yhum > -100 and yhum < h+100:
          pygame.draw.circle(sc, ORANGE, (xhum + 50 * mu, yhum + 50 * mu), 5 * mu)
          if len(humans) < 50:
           pygame.font.init()
           i = int(20*mu)
           if i > 12:
            f1 = pygame.font.SysFont('arial', int(20*mu))
            text1 = f1.render(self.name, True,
                      (255, 255, 255))
            sc.blit(text1, (xhum,yhum))


#def bport(x,y):
def bcheese(x,y):
 if al((x,y),rm) == 1:
  if rm[x][y] <= 0:
    lvar = building(x,y,"cheese", ids[0])
    #ids[0] += 1
    #homes.append(lvar)
    buildings.append(lvar)
    factories.append(lvar)
    rm[x][y] = 100
def bcigar(x,y):
 if al((x,y),rm) == 1:
  if rm[x][y] <= 0:
    lvar = building(x,y,"cigar", ids[0])
    #ids[0] += 1
    #homes.append(lvar)
    buildings.append(lvar)
    factories.append(lvar)
    rm[x][y] = 100
def brancho(x,y):
 if al((x,y),rm) == 1:
  if rm[x][y] <= 0:
    lvar = building(x,y,"rancho", ids[0])
    #ids[0] += 1
    #homes.append(lvar)
    buildings.append(lvar)
    
    rm[x][y] = 100
def btaverne(x,y):
 if al((x,y),rm) == 1:
  if rm[x][y] <= 0:
    lvar = building(x,y,"tavern", ids[0])
    #ids[0] += 1
    #homes.append(lvar)
    buildings.append(lvar)
    rm[x][y] = 100
def bcanns(x,y):
 if al((x,y),rm) == 1:
  if rm[x][y] <= 0:
    lvar = building(x,y,"canns", ids[0])
    #ids[0] += 1
    #homes.append(lvar)
    buildings.append(lvar)
    factories.append(lvar)
    rm[x][y] = 100
def brome(x,y):
 if al((x,y),rm) == 1:
  if rm[x][y] <= 0:
    lvar = building(x,y,"rome", ids[0])
    #ids[0] += 1
    #homes.append(lvar)
    buildings.append(lvar)
    factories.append(lvar)
    rm[x][y] = 100
def bhome(x,y):
 if al((x,y),rm) == 1:
  if rm[x][y] <= 0:
    lvar = building(x,y,"home", ids[0])
    ids[0] += 1
    homes.append(lvar)
    buildings.append(lvar)
    rm[x][y] = 100
def bclinic(x,y):
 if al((x,y),rm) == 1:
  if rm[x][y] <= 0:
    lvar = building(x,y, "clinic", ids[0])
    ids[0] += 1
    clinics.append(lvar)
    buildings.append(lvar)
    rm[x][y] = 100
def bfarm(x,y):
 if al((x,y),rm) == 1:
  if rm[x][y] <= 0:
    lvar = building(x,y,"farm", ids[0])
    ids[0] += 1
    farms.append(lvar)
    buildings.append(lvar)
    rm[x][y] = 100
def bport(x,y):
 if al((x,y),rm) == 1:
  if rm[x][y] <= 0:
    lvar = building(x,y,"port",ids[0])
    ids[0] += 1
    #ports.append(lvar)
    buildings.append(lvar)
    rm[x][y] = 100
def bfur(x,y):
 if al((x,y),rm) == 1:
  if rm[x][y] <= 0:
    lvar = building(x,y, "fur", ids[0])
    #furs.append(lvar)
    buildings.append(lvar)
    rm[x][y] = 100
def bshop(x,y):
 if al((x,y),rm) == 1:
  if rm[x][y] <= 0:
    lvar = building(x,y, "shop", ids[0])
    #furs.append(lvar)
    buildings.append(lvar)
    rm[x][y] = 100
def bimig(x,y):
 if al((x,y),rm) == 1:
  if rm[x][y] <= 0:
    lvar = building(x,y, "imigration", ids[0])
    #furs.append(lvar)
    buildings.append(lvar)
    rm[x][y] = 100
def get_build():
  for i in range(0,len(buttons2)):
    j = buttons2[i]
    if j.press():
      contmod[2] = i
def broad(x,y):
 if al((x,y),rm) == 1:
  x = int(x)
  y = int(y)
  if rm[x][y] <= 0:
    rm[x][y] = 1
def bgarage(x,y):
  i = -1
  if al((x,y),rm) == 1 and rm[x][y] <= 0:
   if al((x+1,y),rm) == 1:
    if rm[x+1][y] in range(1,9):
      i = 0
   if al((x-1,y),rm) == 1:
    if rm[x-1][y] in range(1,9):
      i = 1
   if al((x,y+1),rm) == 1:
    if rm[x][y+1] in range(1,9):
      
      i = 2
   if al((x,y-1),rm) == 1:
    if rm[x][y-1] in range(1,9):
      i = 3
   if i == 0:
     garages.append(garage(x,y,x+1,y))
     rm[x][y]=100
   if i == 1:
     garages.append(garage(x,y,x-1,y))
     rm[x][y]=100     
   if i == 2:
     garages.append(garage(x,y,x,y+1))
     rm[x][y]=100
   if i == 3:
     garages.append(garage(x,y,x,y-1))
     rm[x][y]=100

def infodis(ty,inn):
    #humans[0].infodis()
    if ty == 0:
        buildings[inn].infodis()
    if ty == 1:
        clinics[inn].infodis()
    if ty == 2:
      homes[inn].infodis()
    if ty == 10:
      humans[inn].infodis()
    


def addhuman(nhum=1, xhum = 0, yhum = 0):
  for i in range (0,nhum):
    j = human(xhum,yhum,len(humans))
    humans.append(j)
    hbut = button(100, 26*i, 100,25)
    hbut.text = j.name
    buttonshuman.append(hbut)
fpscnt = 1
if fpscnt <=30:
  fpscnt = 1

#def optithink(a):#каждый кадр обсчитываем 1/30 от всех людей
def razb(n,k,d): #n -- len(humans), k= 30, d =fpscnt
  if k>n:
    n=k
  l = []
  m = n/k
  for i in range(0,k):
    l.append(int(i*m))
  l.append(n)
  
  for i in range(l[d-1],l[d]):
    humans[i].think()
    #print(i)
    

  

contmod=[0,0,0]
FPS = 20
fps = 60
WIN_WIDTH = 1300
w = 1050
WIN_HEIGHT = 700
h = 800
WHITE = (255, 255, 255)
GG=(255,0,0)
ORANGE = (255, 150, 100)
WM = ORANGE
 
clock = pygame.time.Clock()
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
r = 30


humans = [human(random.randint(0,n-1),
random.randint(0,m-1),i) for i in range(0,starthumans)]
humans = []
buildings = []
factories = []
furs = []
ports = []
homes = []
clinics = []
farms = []
buttons = [button(), button(w-50,100), button(w-50, 220), button(0,h/2), button(w-10,0,50,50,0,(100,100,100)), button(w-70,0,50,50,0,(100,100,150)), button(w-130,0,50,50,0,(100,200,150)), button(210, 0, 150,50), button(210+150+10, 0, 150,50), button(530, 0, 150, 50)] #4 5 6 -- скорость игры 7 -- строить дом 8 —
# 0 build mode switcher 12 масштаб 3 строить
buttons2 = [button(0,h-110), button(110,h-110), button(220,h-110),  button(330,h-110), button(440,h-110), button(550,h-110), button(660,h-110), button(770,h-110),button(880,h-110),  button(0,h-220),button(110,h-220), button(550,h-220),  button(220,h-220), button(330,h-220), button(440,h-220)]
#b2 -- кнопки смены здания для строительства
buttonsfarm = [button(0,h/3*2, w+100,h+100), button(10, h//3*2 + 10, w/3-10, 20) ]
buttonsinfomen = [button(w - 80, h/3*2+5, 70,45), button(w - 80, h/3*2+51, 70,45), button(w-80, h/3*2+97, 70,45), button(w-80, h/3*2+143, 70,45), button(w-80, h/3*2+188, 70,45)]
butdisinfo = [button(50,h/3*2 +60, w*4/5, 15), button(50,h/3*2 +80, w*4/5, 15)]
butdismode = [button(w/2 +w/20, h/3*2 + h/20, w/10, h/10), button(w/2 +w/20 + w/9, h/3*2 + h/20, w/10, h/10), button(w/2 +w/20+w/4.5, h/3*2 + h/20, w/10, h/10), button(w/2+w/20, h/3*2 + h/20 + h/9, w/10, h/10),button(w/2 +w/20 + w/9, h/3*2 + h/20 + h/9, w/10, h/10), button(w/10, h/3*2 + h/20, w/2.5,h/25), button(w/10, h/3*2 + h/10, w/2.5,h/25), ]
butdisprice = [button(w/3, h/3*2 + 60, 50,50), button(w/3, h/3*2 + 90, 50,50) , button(w/3 + 60, h//3*2 + 60, 50,50), button(w/3 + 60, h/3*2 + 90, 50,50),button(20, h/3*2 + 210, w/3 - 20, 15), button(20, h/3*2 + 60, w/3-20, 15), button(20, h/3*2 + 110, w/3-20, 15),button(20, h/3*2 + 160, w/3 - 20, 15) ]
butdisstat = [button(50,h/3*2 + 50, 200,20), button(50,h/3*2 + 80, 200,20),button(50,h/3*2 + 110, 200,20),button(50,h/3*2 + 140, 200,20), button(50,h/3*2 + 170, 200,20)  ]
butdisother=[button(50,h/1.5+50,w/2 - 25,15),button(50,h/1.5+90,w/2 - 75,15),button(50,h/1.5+130,w/2 - 75,15),button(50,h/1.5+170,w/2 - 75,15),button(50,h/1.5+220,200,15),button(w/2,h/1.5+50,w/2,15) ]
buttonsfarm = buttonsfarm + buttonsinfomen+ butdismode+ butdisprice + butdisstat+ butdisother+butdisinfo
buttonsfarm[0].text = ""
buttonshuman = []
buttonsall = buttons + buttons2 + buttonsfarm + buttonshuman

garages = []
caars = set()
for i in homes:
  rm[i.x][i.y] = 100
for i in farms:
  rm[i.x][i.y] = 100
for i in clinics:
  rm[i.x][i.y] = 100
menu = 1
ww = w/3
hh = h/3
but = button(w/2 - ww/2, h/2-hh/2,ww,hh)
but.text = ""
buttons[0].text = "Строительство"
buttons[1].text = " + "
buttons[2].text = " - "
buttons[3].text = "Строить"
buttons[4].text = " >> "
buttons[5].text = " > "
buttons[6].text = "II"
buttons2[0].text = "Дом "
buttons2[1].text = "Ферма "
buttons2[2].text = "Клиника"
buttons2[3].text = "Дорога"
buttons2[4].text = "Гараж"
buttons2[5].text = "Грузы"
buttons2[6].text = "Порт"
buttons2[7].text = "Магаз"
buttons2[8].text = "Имиграция"
buttons2[9].text = "Ранчо"
buttons2[10].text = "Театр"
buttons2[11].text = " Ром  "
buttons2[12].text = "Консервы"
buttons2[13].text = " Сыр  "
buttons2[14].text = "Сигареты"

buttons[0].xx = 200
buttons[0].yy = 50
butdisprice[0].text = " + "
butdisprice[1].text = " - "
butdisprice[2].text = " + "
butdisprice[3].text = " - "
buttonsinfomen[0].text = "инфо"
buttonsinfomen[1].text = "режим"
buttonsinfomen[2].text = "деньги"
buttonsinfomen[3].text = "стат"
buttonsinfomen[4].text = "прочее"

numhum = 0
while menu == 1:
  sc.fill((0,0,100))
  
  but.draw()
  pygame.font.init()

  
  tcont = "Играть"
  tcont2 = "Президентэ"
  f1 = pygame.font.SysFont('arial', 40)
  f2 = pygame.font.SysFont('arial', 80)
  
  text1 = f1.render(tcont, True,
                      (180, 0, 0))
  text2 = f2.render(tcont2, True,
                      (180, 100, 140))

  sc.blit(text1, (but.x + 30,but.y+ 50))
  sc.blit(text2, (w/2 - 100,100))
#  buttons[7].text = tcont
#  buttons[8].text = tcont2
    #sc.blit(text2, (10, 100))
  pygame.display.update()
  if but.click()==1:
    menu = 0
    #print(0)
  else:
    menu = menu
    #print(1)
build_number = len(buildings)
numhum = 0
addhuman(nhumans)

for i in humans:
        if i.life == 1:
          numhum += 1
buttons[9].text = "  "+str(numhum)+"  "

while 1:
    
    #print(garages)
    #for i in garages:
      #i.prii()
    get_build()
    #farms[0].infodis()
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            zagl = zagl
    for i in range(0,len(buttons2)):
      if contmod[0] == 2:
        buttons2[i].active = 1
        buttons[3].active = 1
      else:
        buttons2[i].active = 0
        buttons[3].active = 0
  
    pos = pygame.mouse.get_pos()
    cmp = 0
    pr = pygame.MOUSEBUTTONDOWN
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    sc.fill((0,0,100))
    xtest = int(xtest)
    ytest = int(ytest)
    xhum = (xx + 100 * xtest) * mu + (1 - mu) * (w / 2)
    yhum = (yy + 100 * ytest) * mu + (1 - mu) * (h / 2)
    pygame.draw.rect(sc, (0,0,255), (xhum, yhum, 100*mu, 100*mu),8)

    

    #pygame.draw.circle(sc, GG,
                       #(w-80, 100), 50)
    #pygame.draw.rect(sc, WM, (1, 1, 100, 100))
    #print(pygame.font.match_font('verdana'))
    #C:\Windows\Fonts\verdana.ttf
    #pygame.font.SysFont('arial', 36)
    pygame.font.init()

    tcont = str(int(money[0])) +"$"
    f1 = pygame.font.SysFont('arial', 36)
    f2 = pygame.font.Font(None, 36)
    text1 = f1.render(tcont, True,
                      (180, 0, 0))
    date = str(int(month))+'/'+str(int(year))
    datet = f1.render(date, True,
                      (180, 0, 0))
    f2 = pygame.font.SysFont('serif', 48)
    #datetext = f2.render("World Мир", False,
                     # (0, 180, 0))

    #sc.blit(text1, (10, 50))
    #sc.blit(text2, (10, 100))

        #  x =
        #  y = yy + 100 * j
         # xcor =  xx + 100 * i*mu+(1-mu)*(w/2)
         # ycor = yy + 100 * j*mu+(1-mu)*(h/2)
         #i = (xcor - (1-mu)*(w/2) - xx)/100/mu
    # j = (ycor - yy - (1-mu)*(h/2))/100/mu
    if contmod[0] ==2:
      pauseg = 1
    if pauseg != 1:
      fpscnt+=1
      razb(len(humans),nopt, fpscnt)
    
      if fpscnt >=nopt:
        fpscnt = 0
    
    
    for i in humans:
       if pauseg != 1:
        if i.life == 1:
        #i.tupd("state = " + str(i.state))
        #print(i.state)
          #if i.state == 2:
          #i.tupd("Думаю-думаю")
          
            #i.think()
          if i.state == 0:
            i.go()
          if i.state == 1:
            i.do()
          if i.hap_eat > -10:
            i.hap_eat -= 0.7/FPS
          if i.hap_health > -10:
            i.hap_health -= 0.5/FPS
          if i.rest > -10:
            i.rest -= 0.7/FPS
          if i.hap_fun > -10:
            i.hap_fun -= 0.3/FPS

    tvar = -1
    ivar = -1
    render_road()
#    for i in clinics:
        #i.draw()
    #for i in farms:
        #i.draw()
        
        
    for i in buildings:
        i.draw()
    
    #humans.append(
#human(random.randint(0,9),
#random.randint(0,9)))

    for i in garages:
      i.draw()
    for i in humans:
        if i.state != 1 or i.wg == 1:
          i.draw()
        if i.cars != 0 and len(i.list)>1:
          i.cars.renderg(i.list)
    for i in buttonsfarm + buttonshuman:
      i.active = 0
    infodis(typi,numbi)
    for i in buttonsall:
        i.draw()
    #sc.blit(text1, (250, 10))
    #sc.blit(datet, (350, 10))
    buttons[7].text = " " + date + " "
    buttons[8].text = " "+ str(int(money[0])) + '$'+" "
    pygame.draw.rect(sc, (0,0,255), (xhum, yhum, 100*mu, 100*mu),8)
    if tvar == 1:
      pygame.draw.rect(sc, (0,0,255), (0, h/2, w, h/2))
    
    
    
    
    
    pygame.display.update()
    numhum = 0
    for i in humans:
        if i.life == 1:
          numhum += 1
        buttons[9].text = "  "+str(numhum)+"  "
    for i in buttonsall:
      if pooo(pos[0],pos[1],i) == True and i.active == 1:
        tapped = 1
    
    aaa = 0

    pressed = pygame.mouse.get_pressed()
    ev = pygame.event.get()
    for event in ev:
     if event.type == pygame.MOUSEBUTTONUP:


         pos = pygame.mouse.get_pos()
         i = buttons[0]
         
         #print("x=")
         #print(x)
         #print("xx = ")
         #print(xx)         
         if pos[0] in range(i.x,i.xx+i.x)  and pos[1] in range (i.y,i.yy+i.y):
              if contmod[0]==2:
                   contmod[0] = 0
                   WM = (0,0,0)
                   pauseg = 0
                   for i in garages:
                     i.genlists()
                   #print("cont0")
              else:
                  contmod[0] =2
                  WM = ORANGE
                  pauseg = 1
                  #print("cont2")
    
    
    if contmod[0] == 2 and tapped == 0 and pressed[0] == 1:
            xh = int(pos[0])
            yh = int(pos[1])
            xtest = ((xh-(1-mu)*(w/2))/mu-xx)/100
            ytest = ((yh-(1-mu)*(h/2))/mu-yy)/100
            xtest = int(xtest)
            ytest = int(ytest)
    elif contmod[0] == 2:
      tapped = tapped
    else:
            xtest = 500
            ytest = 500
    
    if pressed[0] == 1:
       numbip = -1
       for i in range(0, len(buildings)):
            if buildings[i].pos_on() == 1 and tapped == 0:
                typi = 0
                numbip = i
                numbi = i
                #money[0] = 1
       
       for i in range(0, len(buttonshuman)):
            if buttonshuman[i].press() == 1:
                typi = 10
                numbip = i
                numbi = i
       if tapped == 0 and numbip == -1:
                typi = -1

       if contmod[0] ==2:
          xh = int(pos[0])
          yh = int(pos[1])
          
          i = buttons[3]
          if pooo(xh, yh, i)==True:
            contmod[1] = 2
          else:
            contmod[1]=-1
          #i = buttons[7]
         
          if contmod[1] == 2:
            #homes.append(home(xtest, ytest, random.randint(0,255)))
            if contmod[2]==0:
              bhome(xtest,ytest)
            if contmod[2]==1:
              bfarm(xtest,ytest)
            if contmod[2]==2:
              bclinic(xtest,ytest)
            if contmod[2]==3:
              broad(xtest,ytest)
            if contmod[2]==4:
              bgarage(xtest,ytest)
            if contmod[2]==5:
              bfur(xtest,ytest)
            if contmod[2]==6:
              bport(xtest,ytest)
            if contmod[2]==7:
              bshop(xtest,ytest)
            if contmod[2]==8:
              bimig(xtest,ytest)
            if contmod[2]==9:
              brancho(xtest,ytest)
            if contmod[2]==10:
              btaverne(xtest,ytest)
            if contmod[2]==11:
              brome(xtest,ytest)
            if contmod[2]==12:
              bcanns(xtest,ytest)
            if contmod[2]==13:
              bcheese(xtest,ytest)
            if contmod[2]==14:
              bcigar(xtest,ytest)
           
          
    if buttons[5].press():
      FPS = fps
      pauseg = 0
    if buttons[4].press():
      FPS = fps/12
      pauseg = 0
    if buttons[6].press():
      FPS = 100000000000
      pauseg = 1
    
    if pressed[0]==1:
        pos = pygame.mouse.get_pos()
        if sp is None:
            sp = pos
            xxx=xx
            yyy=yy
            a = 0
        i = buttons[1]
        j = buttons[2]
        if a!=0 and contmod[0]==0:
          xx = xxx + (pos[0] - sp[0])*(1/mu)
          yy = yyy+ (pos[1] - sp[1])*(1/mu)
          if pos[0] in range(i.x,i.xx+i.x) and pos[1] in range(i.y, i.y+i.yy):
            mu=mu+0.015*mu
          if pos[0] in range(j.x,j.xx+j.x) and pos[1] in range(j.y, j.y+j.yy):
            mu=mu-0.015*mu
        a = 1
    else:
        sp = None
    clock.tick(fps)
    tapped= 0
    #typi = -1  # для табло с информацией (245,245,220)
    #numbi = -1
    monthp = month
    time+=1/120/FPS
    month = 1+time%12
    year = 2023+time//12
    if int(monthp) != int(month):
      monthevent = 1
    else:
      monthevent = 0
    if monthevent == 1:
      
      
      
      
      buttonsall = buttons + buttons2 +  buttonsfarm  + buttonshuman
      print("month")
      allsalary = 0
      nsalary = 0
      avsalary = 0
      numhum = 0
      buttons[9].text = "  "+str(numhum)+"  "
      for i in humans:
        if i.life == 1:
          numhum += 1
        buttons[9].text = "  "+str(numhum)+"  "
        #i.initial()
        i.findworkp = 1
        for i in factories:
          i.pinres = i.inres 
        #i.state = 2
        #if i.work_n != -1:
          #2allsalary+= 1
          #2nsalary += 1
      #if nsalary >10000000:#потом доделать
        #avsalary = allsalary/nsalary
        #for i in humans:
          #if i.salary < avsalary:
            #i.findwork()
        

