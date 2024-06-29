#import pygame
import sys
import math
#import main
import random
import numpy as np
#import noise
#from testsave import*


from savestate import *
testllm.append(locallaymap())

#humans[0].education = 1
laymod = ["none", 0]#elec, beauty, freedom,
#электричество — отображать до 
ytest2=None
xtest2 = None

roads = {}



timeint = 0

pmot = "да"

mu=1
cn = 0
foodc = 5
xx = 0
yy = 0
broadv = 0

#print(roadset)
#markers.append(rmarker(30,10))
#markers.append(rmarker(0,0,5))

class isl(object):
  def __init__(self):
    self.money = money
    self.rub = money[0]
    self.dol = money[1]
def gentreemarkers(n,m):
  for i in range(1):
    markers.append(rmarker(random.randint(0,n), random.randint(0,m), random.randint(0,10)))
def gentreemap(n,m):
 for mar in markers:
  aa = min(mar.x,n-1)
  bb = min(mar.y,m-1)
  for i in range (aa-mar.range-1, aa+mar.range+2):
    for j in range (bb -mar.range-1, bb + mar.range+2):
      ds = math.sqrt( (i-aa)**2 + (j-bb)**2) 
      if ds <= mar.range and al((i,j),rm) == 1:
        treemap[i][j] += int(mar.range - ds)
        
def gentree(n,m):
    gentreemap(n,m)
    for i in range(len(treemap)):
      for j in range(len(treemap[0])):
        if treemap[i][j]> 0:
          trees[(i,j)] = [tree(i, j+ 0.25)]
        if treemap[i][j]> 1:
          trees[(i,j)].append(tree(i+0.5, j+ 0.25))
        if treemap[i][j]> 2:
          trees[(i,j)].append(tree(i+0.25, j+ 0.25))
        if treemap[i][j]> 3:
          trees[(i,j)].append(tree(i+0.75, j+ 0.25))
        if treemap[i][j]> 4:
          trees[(i,j)].append(tree(i+0.125, j+ 0.25))
        if treemap[i][j]> 5:
          trees[(i,j)].append(tree(i+0.625, j+ 0.25))
        if treemap[i][j]> 6:
          trees[(i,j)].append(tree(i+0.375, j+ 0.25))
        if treemap[i][j]> 7:
          trees[(i,j)].append(tree(i+0.875, j+ 0.25))
gentreemarkers(n//3,m//3)
gentree(n,m)
def crossroad(roa,roads):
  a = roa[0]
  b = roa[1]
  clist = []
  if (a+1, b) in roads:
    clist.append("right")
  if (a-1, b) in roads:
    clist.append("left")
  if (a, b-1) in roads:
    clist.append("up")
  if (a, b+1) in roads:
    clist.append("down")
  if len(clist) == 4:
    return "quad"
  if len(clist) == 3:
    return "triple"

def calcmrot():
  meat = 0
  mhealth = 0
  mfun = 0
  mhome = 0
  mcnt = 0
  for i in buildings:
    if i.eat_allow == 1:
      if i.nwork > 0:
        #for j in eat:
          
        mcnt += 1#i.outres[j]
        meat += i.price#*i.outres[j]
  if mcnt > 0:
    meat = meat/mcnt*10/5
  else:
    meat = "None"
  mcnt = 0
  for i in clinics:
    if i.health_allow == 1:
      if i.nwork > 0:
        mcnt += i.amount
        mhealth += i.price*i.amount
  if mcnt > 0:
    mhealth = mhealth/mcnt*10/6
  else:
    mhealth = "None"
    
  mcnt = 0
  for i in buildings:
    if i.fun_allow == 1:
      if i.nwork > 0:
        mcnt += 1
        mfun += i.price
  if mcnt > 0:
    mfun = mfun/mcnt*10/5
  else:
    mfun = "None"
    
  mcnt = 0
  for i in buildings:
   if i.live_allow == 1:
      
        mcnt += i.quality/50
        mhome += i.rent
  if mcnt > 0:
    mhome = mhome/mcnt
  else:
    mhome = "None"
  allmrot["home"][0]= mhome
  allmrot["fun"][0] = mfun
  allmrot["eat"][0]= meat
  allmrot["health"][0]= mhealth
  allmrot["dollar"][0]= dcourse[0]


def lerp(a, b, x):
    return a + x * (b - a)

def fade(t):
    return 6 * t**5 - 15 * t**4 + 10 * t**3

def gradient(h, x, y):
    vectors = np.array([[0, 1], [0, -1], [1, 0], [-1, 0]])
    g = vectors[h % 4]
    return g[0] * x + g[1] * y

def perlin_noise(x, y, seed=0):
    np.random.seed(seed)
    X = np.array(x, dtype=int)
    Y = np.array(y, dtype=int)
    x = x - X
    y = y - Y

    h = np.random.randint(0, 256, size=(X.size + 1, Y.size + 1)) % 16
    a = np.array([gradient(h[i, j], x[i, j], y[i, j]) for i in range(X.size) for j in range(Y.size)]).reshape(X.shape)
    b = np.array([gradient(h[i, j + 1], x[i, j], y[i, j] - 1) for i in range(X.size) for j in range(Y.size)]).reshape(X.shape)
    c = np.array([gradient(h[i + 1, j], x[i, j] - 1, y[i, j]) for i in range(X.size) for j in range(Y.size)]).reshape(X.shape)
    d = np.array([gradient(h[i + 1, j + 1], x[i, j] - 1, y[i, j] - 1) for i in range(X.size) for j in range(Y.size)]).reshape(X.shape)

    u = fade(x)
    v = fade(y)

    return lerp(lerp(a, c, u), lerp(b, d, u), v)
#testmap = perlin_noise(100,100)

def genhmap(n,m, scale):
    height_map = np.zeros((n, m))
    x_coords = np.tile(np.arange(w) / scale, (h, 1))
    y_coords = np.tile(np.arange(h) / scale, (w, 1)).T
    height_map = perlin_noise(x_coords, y_coords, 2)
    
    return height_map

def gentreemap(height_map, tree_threshold=0.2):
    tree_map = np.zeros(height_map.shape)
    for y in range(height_map.shape[0]):
        for x in range(height_map.shape[1]):
            elevation = height_map[y, x]
            if elevation > tree_threshold:
                tree_map[y, x] = perlin_noise(x / scale, y / scale, seed + 1)  # Используйте другое значение seed для генерации деревьев
    return tree_map
def genres(contr, type):
  for i in range(contr):
    a = random.randint(0,len(rm))
    b = random.randint(0,len(rm[0]))
    resour = resourse(a,b,type)
    resourses.append(resour)
    
def layres():
  for i in resourses:
    if i.type == "iron" or i.type == "gold" or i.type == "coal":
      for j in range(i.x - 3, i.x+4):
            for wj in range(i.y - 3, i.y+4):
              if al((j,wj),rm):
                if i.type == "iron":
                  ironlay[j][wj] = 255
                if i.type == "gold":
                  goldlay[j][wj] = 255
                if i.type == "coal":
                  coallay[j][wj] = 255
                
    
      

pygame.font.init()

genres(1, "iron")
genres(1, "gold")
genres(1, "coal")
#bouxitlay = genhmap(n,m,1)
#goldlay = gentreemap(bouxitlay)
layres()

def pri(x):
  if test[0]==1:
    print(x)
#dictrus = 

roadset = set()
def gtor(a,xt,yt, xx, yy,w,h,mu):
  ii = a[0]
  jj = a[1]
  xh = (xx + 100 * ii) * mu + (1 - mu) * (w / 2)
  yh = (yy + 100 * jj) * mu + (1 - mu) * (h / 2)
  return (xh, yh, xt*mu, yt*mu)
#eleclay[0][0] = 255
class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, size, color, alpha=180):
        super().__init__()
        self.image = pygame.Surface((math.ceil(size), math.ceil(size)))
        self.image.fill(color)
        self.image.set_alpha(alpha)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

def render_elay2():
  cell_sprites = pygame.sprite.Group()

    # Определение координат и размера клеток
    # (Аналогично исходной функции)
    # ...
  li = len(rm)# алгоритм который определяет с какими координатами объекты нужно рисовать
  lj = len(rm[0])
  xh = w
  yh = h
  xtest = ((xh-(1-mu)*(w/2))/mu-xx)/100
  ytest = ((yh-(1-mu)*(h/2))/mu-yy)/100
  xi1 = int(xtest)+1
  yj1 = int(ytest)+1
  xh = 0
  yh = 0
  xtest = ((xh-(1-mu)*(w/2))/mu-xx)/100
  ytest = ((yh-(1-mu)*(h/2))/mu-yy)/100
  xi0 = int(xtest)-1
  yj0 = int(ytest)-1
  if laymod[0] != "none":
        for i in range(max(0, xi0), min(len(eleclay), xi1 + 1)):
            for j in range(max(0, yj0), min(len(eleclay[0]), yj1 + 1)):
                if xi0 <= i <= xi1 and yj0 <= j <= yj1:
                    v = 0
                    if laymod[0] == "elec":
                        v = int(eleclay[i][j])
                    # (Остальные проверки laymod[0])

                    xhum = round((xx + 100 * i) * mu + (1 - mu) * (w / 2))
                    yhum = round((yy + 100 * j) * mu + (1 - mu) * (h / 2))

                    if v in range(0, 256):
                        color = (255 - v, v, 0)
                        if laymod[0] == "elec" and v == 0:
                            color = (0, 0, 0)
                        cell = Cell(xhum, yhum, 100 * mu, color)
                        cell_sprites.add(cell)
def render_elay3():
  #render_road2()
  li = len(rm)# алгоритм который определяет с какими координатами объекты нужно рисовать
  lj = len(rm[0])
  xh = w
  yh = h
  xtest = ((xh-(1-mu)*(w/2))/mu-xx)/100
  ytest = ((yh-(1-mu)*(h/2))/mu-yy)/100
  xi1 = int(xtest)+1
  yj1 = int(ytest)+1
  xh = 0
  yh = 0
  xtest = ((xh-(1-mu)*(w/2))/mu-xx)/100
  ytest = ((yh-(1-mu)*(h/2))/mu-yy)/100
  xi0 = int(xtest)-1
  yj0 = int(ytest)-1
  if laymod[0] != "none":
   for i in range(max(0,xi0),min(len(eleclay), xi1+1)):
    for j in range(max(0,yj0),min(len(eleclay[0]), yj1+1)):
      if i >= xi0 and i <= xi1 and j>= yj0 and j <= yj1:
          v = 0
          if laymod[0] == "elec":
            v = int(eleclay[i][j])
          if laymod[0] == "beauty":
            v = int(beautylay[i][j])
          if laymod[0] == "freedom":
            v = int(freedomlay[i][j])
          if laymod[0] == "oil":
            v = int(oillay[i][j])
          if laymod[0] == "gold":
            v = int(goldlay[i][j])
          if laymod[0] == "iron":
            v = int(ironlay[i][j])
          if laymod[0] == "bouxit":
            v = int(coallay[i][j])
          
          xhum = round((xx + 100 * i) * mu + (1 - mu) * (w / 2))
          yhum = round((yy + 100 * j) * mu + (1 - mu) * (h / 2))
          square = pygame.Surface((math.ceil(100*mu), math.ceil(100*mu)), pygame.SRCALPHA)
          if v in range(0,256):
            
            square.fill((255-v,v,0))
            if laymod[0] == "elec" and v == 0:
              square.fill((0,0,0))
          square.set_alpha(180)
          sc.blit(square, (xhum, yhum))
          #pygame.draw.rect(sc, (200,0,0), (xhum, yhum, 100*mu, 100*mu))
        
#import pygame
#import math

cell_cache = {}



def get_cell_image(size, color, alpha=180):
    key = (size, color, alpha)
    if key not in cell_cache:
        cell_image = pygame.Surface((math.ceil(size), math.ceil(size)), pygame.SRCALPHA)
        cell_image.fill(color)
        cell_image.set_alpha(alpha)
        cell_cache[key] = cell_image
    return cell_cache[key]

def render_elay():
    li = len(rm)
    lj = len(rm[0])
    xh = w
    yh = h
    xtest = ((xh - (1 - mu) * (w / 2)) / mu - xx) / 100
    ytest = ((yh - (1 - mu) * (h / 2)) / mu - yy) / 100
    xi1 = int(xtest) + 1
    yj1 = int(ytest) + 1
    xh = 0
    yh = 0
    xtest = ((xh - (1 - mu) * (w / 2)) / mu - xx) / 100
    ytest = ((yh - (1 - mu) * (h / 2)) / mu - yy) / 100
    xi0 = int(xtest) - 1
    yj0 = int(ytest) - 1
    
    if laymod[0] == "elec":
                    vv = eleclay
    if laymod[0] == "beauty":
                    vv = beautylay
    if laymod[0] == "freedom":
                    vv =freedomlay
    if laymod[0] == "oil":
                    vv = oillay
    if laymod[0] == "gold":
                    vv = goldlay
    if laymod[0] == "iron":
                    vv = ironlay
    if laymod[0] == "bouxit":
                    vv = coallay
    if laymod[0] == "safe":
      vv = safelay
    if laymod[0] != "none":
        for i in range(max(0, xi0), min(len(eleclay), xi1 + 1)):
            for j in range(max(0, yj0), min(len(eleclay[0]), yj1 + 1)):
                v = 0
                
                v = int(vv[i][j])

                xhum = round((xx + 100 * i) * mu + (1 - mu) * (w / 2))
                yhum = round((yy + 100 * j) * mu + (1 - mu) * (h / 2))

                if v in range(0, 256):
                    color = (255 - v, v, 0)
                    if laymod[0] == "elec" and v == 0:
                        color = (0, 0, 0)
                    cell_image = get_cell_image(100 * mu, color)
                    sc.blit(cell_image, (xhum, yhum))



def render_road():
  pygame.draw.rect(sc, (0,0,0), (w,h,100,100))
  a = (0,0)
  pygame.draw.rect(sc, (0,100,0), gtor(a,100*(len(rm)),100*(len(rm[0])), xx, yy,w,h,mu))
  
  li = len(rm)# алгоритм который определяет с какими координатами объекты нужно рисовать
  lj = len(rm[0])
  xh = w
  yh = h
  xtest = ((xh-(1-mu)*(w/2))/mu-xx)/100
  ytest = ((yh-(1-mu)*(h/2))/mu-yy)/100
  xi1 = int(xtest)+1
  yj1 = int(ytest)+1
  xh = 0
  yh = 0
  xtest = ((xh-(1-mu)*(w/2))/mu-xx)/100
  ytest = ((yh-(1-mu)*(h/2))/mu-yy)/100
  xi0 = int(xtest)-1
  yj0 = int(ytest)-1
  for ro in roadsetobj:
    ro.draw(xx,yy,w,h,mu)
  for ro in roadset:
    i = ro[0]
    j = ro[1]
    #if i >= xi0 and i <= xi1 and j>= yj0 and j <= yj1:
      #pygame.draw.rect(sc, (70,70,70), gtor(ro,100,100, xx, yy,w,h,mu))
  #for i in range(max(0,xi0),min(len(rm), xi1)):
    #for j in range(max(0,yj0),min(len(rm[0]),yj1)):
        #if rm[i][j] < 10 and rm[i][j] > 0:
          #xhum = (xx + 100 * i) * mu + (1 - mu) * (w / 2)
          #yhum = (yy + 100 * j) * mu + (1 - mu) * (h / 2)
          #pygame.draw.rect(sc, (200,0,0), (xhum, yhum, 100*mu, 100*mu))
        #if rm[i][j] == 0:
          #xhum = (xx + 100 * i) * mu + (1 - mu) * (w / 2)
          #yhum = (yy + 100 * j) * mu + (1 - mu) * (h / 2)
          #a = (i,j)
          #if xhum >= -100*mu and xhum <=w and yhum >= -100*mu and yhum <= h:
          #if i >= xi0 and i <= xi1 and j>= yj0 and j <= yj1:
            #pygame.draw.rect(sc, (100,100,100), gtor(a,100,100, xx, yy,w,h,mu))
      





class garage(object):
  def __init__(self, x, y, xt,yt):
    self.x = x
    self.y = y
    self.xx = 1
    self.yy = 1
    self.xt = xt
    self.yt = yt
    self.color = (200,200,200)
    self.text = "Гараж"
    self.visitors = set()
    self.max_visitors = 30
    self.n_visitors = 0
    self.rlists = {}
    self.rd = {}
    self.rm = {}
    self.svset = set()
    self.gennode()
    self.gensvset()
    self.resolve = True
    #self.genlists()
    #print("lllllllllllllllllllllllllllllllllllllll")
    #print(self.rlists)
    #print(self.rm)
  def __lt__(self, other):
        #if isinstance(other, MyClass):
        return self.x < other.x
  def clearing(self):
    self.rlists.clear()
    self.svset.clear()
    self.rlists.clear()
    self.rd.clear()
    self.rm.clear()
    garagedic.clear()
    walklistscache.clear()
  def gennode(self):
    a = (self.xt,self.yt)
    self.nodest = nodesr(a,roadset)
  def gensvset(self):
    self.svset = graphsv2(a, self.nodest)
  def genlist(self, bt,nodess, svset):
           a = (self.xt,self.yt)
           md = 1000000000
           mi = -1
           mj = -1
           for ro in roadset:
               if ro in svset:
                 dx = bt.x - ro[0]
                 dy = bt.y - ro[1]
                 ds = math.sqrt(dx * dx + dy * dy)
                 if ds <= md:
                   mi = ro[0]
                   mj = ro[1]
                   md = ds
           if mi < 0:
             return 0
           else:
             b = (mi,mj)
             bt.testp5 = str(b)
             rlist = [(self.x,self.y)]+list(nod31(a,b,rm,nodess))
             self.rlists[bt] = gh(rlist)
             self.rd[bt]= g(rlist)[0]
             self.rm[bt] = b
    
  def genlists(self):
    a = (self.xt,self.yt)
    self.nodest = nodesr(a,roadset)
    self.svset = graphsv2(a, self.nodest)
    for i in buildings:
      self.genlist(i,self.nodest, self.svset)
      
    

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
    i = int(40*mu)*self.xx
    if i > 12:
            f1 = pygame.font.SysFont('arial', int(i))
            text1 = f1.render(self.text, True,
                      (180, 0, 0))
            sc.blit(text1, (xhum,yhum+ 40*mu*self.yy))
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

brr1 = 0
brr2 = 0



def brroad():
  r = 0
  
  for event in ev:
    if event.type == pygame.MOUSEBUTTONDOWN:
      a = (0,0)
      pygame.draw.line(sc, WHITE, [10, 30], [290, 15], 3)
      
  for event in ev:
    if event.type == pygame.MOUSEBUTTONUP:
      b = (500,500)
  


#def bport(x,y):
def build(x,y, type, xx = 1, yy = 1, sstype = None):
#  xx -= 1
#  yy -= 1
  if build_allow(type, sstype):
    r = 1
    for i in range(x,x+xx):
      for j in range(y,y+yy):
        if al((i,j),rm) == 1:
          if rm[i][j] <= 0:
            r = r
          else:
            r= 0
        else:
          r=0
    if r == 1 and type == "mine":
      
      mdis = 100000
      mi = None
      for i in resourses:
        dx = i.x -x
        dy = i.y - y
        ds = math.sqrt(dx*dx +dy*dy)
        if ds < mdis:
          mdis = ds
          mi = i
      if mi!= None:
          transact(0,"outside", get_build_price(type, sstype), type = "building")
          if mi.type == "oil":
            
            if oillay[x][y] == 255:
              lvar = building(x,y,type, ids[0])
              lvar.xx = xx
              lvar.yy = yy
              lvar.mineres = mi
              buildings.append(lvar)
              for i in range(x, x+xx):
                for j in range(y,y+yy):
                  rm[i][j] = 100
          if mi.type == "coal":
            if coallay[x][y] == 255:
              lvar = building(x,y,type, ids[0])
              lvar.xx = xx
              lvar.yy = yy
              lvar.mineres = mi
              buildings.append(lvar)
              for i in range(x, x+xx):
                for j in range(y,y+yy):
                  rm[i][j] = 100
          if mi.type == "gold":
            if goldlay[x][y] == 255:
              lvar = building(x,y,type, ids[0])
              lvar.xx = xx
              lvar.yy = yy
              lvar.mineres = mi
              buildings.append(lvar)
              for i in range(x, x+xx):
                for j in range(y,y+yy):
                  rm[i][j] = 100
          if mi.type == "iron":
            if ironlay[x][y] == 255:
              lvar = building(x,y,type, ids[0])
              lvar.xx = xx
              lvar.yy = yy
              lvar.mineres = mi
              buildings.append(lvar)
              for i in range(x, x+xx):
                for j in range(y,y+yy):
                  rm[i][j] = 100
    
      
    if r == 1 and type != "mine":
      transact(0,"outside", get_build_price(type, sstype), type = "building")
      
      lvar = building(x,y,type, ids[0])
      lvar.xx = xx
      lvar.yy = yy
      
      
      
      
      #ids[0] += 1
      #homes.append(lvar)
      if type == "home":
        lvar.subtype = sstype
      buildings.append(lvar)
      if type == "beauty":
        i = lvar
        for j in range(i.x - i.range, i.x+i.range+1):
            for wj in range(i.y - i.range, i.y+i.range+1):
              if al((j,wj),rm):
                dx = i.x - j
                dy = i.y - wj
                ds = math.sqrt(dx*dx+dy*dy)
                if ds < 10:
                  beautylay[j][wj] += (10-ds)*5
                  if beautylay[j][wj] > 255:
                    beautylay[j][wj] = 255
      if type == "freedom":
        libertybuilds.append(lvar)
      if type == "rome":
        factories.append(lvar)
      if type == "home":
        lvar.subtype = sstype
        homes.append(lvar)
      if type == "cheese":
        factories.append(lvar)
      if type == "cigar":
        factories.append(lvar)
      if type == "canns":
        factories.append(lvar)
      if type == "clinic":
       clinics.append(lvar)
      if type == "metro":
        metrolist.append(lvar)
      for i in range(x, x+xx):
        for j in range(y,y+yy):
          rm[i][j] = 100
          vecmap[i][j] = lvar
          #print(vecmap[i][j])
      for i in range(max(0,x-1), min(x+xx+1, len(rm))):
        for j in range(max(0,y), min(y+yy, len(rm[0]))):
          #rm[i][j] = 100
          if vecmap[i][j] != 0:
            vecmap[i][j].gennodes()
          #print(vecmap[i][j])
      lvar.gennodes()

def bbuild(x,y):
 if al((x,y),rm) == 1:
  if rm[x][y] <= 0:
    lvar = building(x,y,"build", ids[0])
    #ids[0] += 1
    #homes.append(lvar)
    buildings.append(lvar)
    #factories.append(lvar)
    rm[x][y] = 100
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
    print("build")
    print(homes)
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
  for i in range(max(contmod[3]*10,0), min(contmod[3]*10+10, len(buttons2))):
    j = buttons2[i]
    if j.press() and j.active ==1:
      contmod[2] = i
def droad(x,y, xx = 1, yy = 1):
  for i in range(min(x,x+xx), max(x,x+xx)+1):
   for j in range(min(y,y+yy), max(y,y+yy)+1):
     if (i,j) in roadset:
        
        rm[i][j] = 0
        roadset.discard((i,j))
        proad[0] = x
        proad[1] = y
     lbuild = vecmap[i][j]
     print(lbuild)
     if lbuild != 0:
       if lbuild.type != "palace":
        for a in range(lbuild.x, lbuild.x + lbuild.xx):
          for b in range(lbuild.y, lbuild.y + lbuild.yy):
            rm[a][b]=0
            vecmap[a][b] = 0
        lbuild.destroy()
def broad(x,y, xx = 1, yy = 1):
 if build_allow("road"):
  r = 1
  for i in range(min(x,x+xx)+1, max(x,x+xx)+1):
      for j in range(min(y,y+yy)+1, max(y,y+yy)+1):
        if al((i,j),rm) == 1:
          if rm[i][j] <= 0:
            r = r
          else:
            r= 0
        else:
          r=0
  r = 1
  if r  == 1:
   for i in range(min(x,x+xx), max(x,x+xx)+1):
    for j in range(min(y,y+yy), max(y,y+yy)+1):
     if al((i,j),rm) == 1:
       if rm[i][j] <= 0:
        rm[i][j] = 1
        roadset.add((i,j))
        ro = roaad(i,j)
        ro.gennodes()
        ro.setdir(roadset)
        roaddic[(i,j)] = ro
        roadsetobj.append(ro)
        transact(0,"outside", get_build_price("road"), type = "building")
        for dd in [(0,0), (-1,0), (1,0), (0,-1), (0,-1)]:
          ddd = (i + dd[0],j+dd[1])
          if ddd  in roaddic:
            roaddic[ddd].setdir(roadset)
        trees.pop((i,j),None)
        proad[0] = x
        proad[1] = y
def bgarage(x,y):
 if build_allow("garage"):
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
     transact(0,"outside", get_build_price("garage"))
   if i == 1:
     garages.append(garage(x,y,x-1,y))
     rm[x][y]=100     
     transact(0,"outside", get_build_price("garage"))
   if i == 2:
     garages.append(garage(x,y,x,y+1))
     rm[x][y]=100
     transact(0,"outside", get_build_price("garage"))
   if i == 3:
     garages.append(garage(x,y,x,y-1))
     rm[x][y]=100
     transact(0,"outside", get_build_price("garage"))
build(n//2 - 5,m//2-3, "palace", xx = 10, yy = 6, sstype = None)
build(n//2 + 5 ,m//2-3-3, "fur", xx = 3, yy = 2, sstype = None)
build(n//2 - 3 ,m//2-3-3, "build", xx = 3, yy = 2, sstype = None)
build(0,0, "port", xx = 3, yy = 4, sstype = None)
#for j in range(n//2 - 5 - 5, n//2 - 5 + 6):
broad(n//2 - 5 - 5, m//2-3-1, 20,0)
for i in buildings:
  i.bready = 1
  i.settype(i.type)
#broad(n//2 - 5 +15, m//2-3-1)

walksvsets.clear()
lwset = set()
walksvdic.clear()
walknodes.clear()
walkroads.clear()
for i in buildings:
    i.gennodes()

print("begin")
print(walkroads)
print("processing")
add_additional_edges()
print(walkroads)
for i in roadsetobj:
    i.gennodes()
# print("end")
while len(lwset) < len(walknodes):
    la = walknodes - lwset
    le = next(iter(la))
    lwset.add(le)
    lv1 = wnodesr(le, walknodes)[0]
    lv2 = set(lv1.keys())
    # print(lv1)
    lwset = lwset | lv2
    for i in lv2:
        walksvdic[i] = len(walksvsets)

    walksvsets.append(lv2)
# print(walksvdic)
# print(walksvsets)
walklistscache.clear()
for i in roadsetobj:
    i.setdir(roadset)
    print(roadset)
    print((0, 0) in roadset)
for i in garages:
    i.clearing()
    i.gennode()
    i.gensvset()
# semaphores = []
for i in roadset:
    if crossroad(i, roadset) == "quad" or crossroad(i, roadset) == "triple":
        if i not in semset:
            sem = semaphore(i[0], i[1], "quad")
            semaphores.append(sem)
            semset.add(i)



# print("cont2")
def infodis(ty,inn):
    #humans[0].infodis()
    if ty == 0:
        buildings[inn].infodis()
    if ty == 1:
        clinics[inn].infodis()
    if ty == 2:
      homes[inn].infodis()
    if ty == 10:
      humans[inn].infodis(buildings)
    



fpscnt = 1
if fpscnt <=30:
  fpscnt = 1

#def optithink(a):#каждый кадр обсчитываем 1/30 от всех людей
def razb(n,k,d): #n -- len(humans), k= 30, d =fpscnt
 if k!=1:
  if k>n:
    n=k
  l = []
  m = n/k
  for i in range(0,k):
    l.append(int(i*m))
  l.append(n)
  
  for i in range(l[d-1],l[d]):
    humans[i].think(buildings, garages, clinics, homes)
    #print("razb" + str(homes))
    #print(i)
 else:
  for i in humans:
    i.think(buildings, garages, clinics, homes)
    

  


clock = pygame.time.Clock()

r = 30


#humans = [human(random.randint(0,n-1),
#random.randint(0,m-1),i) for i in range(0,starthumans)]
#addhuman(300)



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



mmenu = ["menu","main", "game", "menu"]

numhum = 0

    #print(1)
build_number = len(buildings)
numhum = 0

def addhuman2(nhum=1, xhum = 0, yhum = 0):
  for i in range (0,nhum):
    j = human(xhum,yhum,len(humans))
    j.state = 2
    fam = family()
    j.family = fam
    if j.sex == "male":
       j.family.husbant= j
       j.family.type = "husbant"
    if j.sex == "female":
      j.family.wife = j
      j.family.type = "wife"
    
    #print(j.sex)
    humans.append(j)
    families.append(fam)
    hbut = button(100, 26*i, 100,25)
    hbut.text = j.name
    buttonshuman.append(hbut)
addhuman2(nhumans)
humans[-1].education = 1

#n, 
for i in humans:
        if i.life == 1:
          numhum += 1

buttons[9].text = "  "+str(numhum)+"  "
for i in smb:
  i.active = 0
def gmd(l):
  alll = gme + smb + gmal
  for i in alll:
    if i not in l:
      i.active =0
  for i in l:
    i.active = 1
#print(roadset)
while game_run == 1:
  #sc.fill((0,0,100))
 FPS = FPSl[0]
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
        #humans = [human(id = ids[0]) for i in range(nhumans)]
        buildings = []
        clinics = []
        factories = []
        addhuman2(nhumans)
        rm = [[0 for j in range(0,m)] for i in range (0,n)]
        rm = np.array(rm, dtype=int)
        mmenu[0] = "game"
      for i in sb2:
        i.draw()
        
        
    pygame.display.update()
    #clock.tick(fps)
    
 if mmenu[0] == "game":
    if mmenu[2] == "game":
      for i in buttonsall:
        i.active = 1
      
      gmd([])
    if mmenu[2] == "almaniac":
      gmal[9].text0 = str(int(year))
      for i in buttonsall:
        i.active = 0
      gmd(gmal)
      
      if gmal[1].press() == 1:
        almod["main"] = "overview"
      if gmal[2].press() == 1:
        almod["main"] = "people"
      if gmal[3].press() == 1:
        almod["main"] = "economy"
      if gmal[4].press() == 1:
        almod["main"] = "politics"
      if gmal[5].press() == 1:
        almod["main"] = "lists"
      if gmal[6].press() == 1:
        almod["main"] = "other"
      gmal[7].text = almod["main"]
      gmal[8].text = almod["second"]
      setalmain(almod["main"])
      setalsec(almod["second"])
      if gmal[-1].press() == 1:
        mmenu[2] = "menu"
        gmd(gme)
        setalmain()
        setalsec()
      for i in albutmain[almod["main"]]:
        if i.press() == 1:
          almod["second"] = i.altype
        text0 = str(int(alsecdi[i.altype]["main"][-1]))
        i.text0 = ""
        for j in range(25-len(text0+i.text)):
          i.text0+=".."
        i.text0 += text0
      for i in albutsec[almod["second"]]:
        
        print(i.text, i.altype, alsecdi[i.altype])
        if alsecdi[i.altype][i.altype2][-1] == "None":
          text0 = "None"
        else:
          text0 = str(int(alsecdi[i.altype][i.altype2][-1]))
        i.text0 = ""
        for j in range(40-len(text0+i.text)):
          i.text0+=".."
        i.text0 += text0
          
          
    if mmenu[2] == "set":
      
      for i in buttonsall:
        i.active = 0
      gmd(smb)
      #for i in smb:
        #i.active = 1
      smb[0].text = "Оптимизация ии: " + str(int(nopt))
      smb[1].text = ""#"Предпросчет движений: " + str(pmot)
      if smb[2].press() == 1:
        mmenu[2] = "menu"
        for i in gme:
          i.active = 1
        for i in smb:
          i.active = 0
      if smb[4].press() == 1:
        if nopt < nhumans-2:
          nopt += 1
      if smb[3].press() == 1:
        if nopt > 3:
          nopt -= 1
      if smb[5].press() == 1:
        pmot = "да"
      if smb[5].press() == 1:
        pmot = "нет"
        
      
      gme[0].active = 1
    if mmenu[2] == "menu":
      pauseg = 1
      for i in gme:
        i.active= 1
      for i in buttonsall:
        i.active = 0
     
      if gme[1].press() == 1:
       mmenu[2] = "game"
       for i in buttonsall:
        i.active = 1
       for i in gme:
        i.active= 0
      if gme[2].press() == 1:
        mmenu[2] = "set"
      if gme[3].press() == 1:
        mmenu[2] = "almaniac"
      if gme[4].press() == 1:
        mmenu[0] = "menu"
        mmenu[1] = "main"
    if buttons[10].press()==1:
      pauseg = 0
      mmenu[2] = "menu"
      
      
    if questwindow["turn"] == True:
      #for i in questbuttons:
        #i.active = 1
      pauseg = 1
      mainquests[0].sublife()
      lb = questbuttons
      lw = questwindow
      lb[0].active = 1
      if lw["name"]!=False:
        lb[1].text = lw["name"]
        lb[1].active = 1
      else:
        lb[1].active = 0
      if lw["description"]!=False:
        lb[2].text = lw["description"]
        lb[2].active = 1
      else:
        lb[2].active = 0
      if lw["target"]!=False:
        lb[3].text = lw["target"]
        lb[3].active = 1
      else:
        lb[3].active = 0
      if lw["reward"]!=False:
        lb[4].text = lw["reward"]
        lb[4].active = 1
      else:
        lb[4].active = 0
      if lw["option1"]!=False:
        lb[5].text = lw["option1"]
        lb[5].active = 1
      else:
        lb[5].active = 0
      if lw["option2"]!=False:
        lb[6].text = lw["option2"]
        lb[6].active = 1
      else:
        lb[6].active = 0
      if lw["option3"]!=False:
        lb[7].text = lw["option3"]
        lb[7].active = 1
      else:
        lb[7].active = 0
      if lw["close"]!=False:
        #lb[9].text = lw["close"]
        lb[9].active = 1
        questbuttons[10].active = 1
      else:
        lb[9].active = 0
    else:
      for i in questbuttons:
        i.active = 0
    if questbuttons[9].click() == 1:
      questwindow["turn"] = False
      pauseg = 0
    if buttons[13].click() == 1:
      mainquests[0].infoshow()
    if questbuttons[10].click() == 1:
      mainquests[0].markerright()
      mainquests[0].infoshow()
    xh = w
    yh = h
    xtestp = ((xh-(1-mu)*(w/2))/mu-xx)/100
    ytestp = ((yh-(1-mu)*(h/2))/mu-yy)/100
    xi1 = int(xtestp)+1
    yj1 = int(ytestp)+1
    xh = 0
    yh = 0
    xtestp = ((xh-(1-mu)*(w/2))/mu-xx)/100
    ytestp = ((yh-(1-mu)*(h/2))/mu-yy)/100
    xi0 = int(xtestp)-1
    yj0 = int(ytestp)-1
  
    #print(garages)
    #for i in garages:
      #i.prii()
    get_build()
    #farms[0].infodis()
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            zagl = zagl
    i = 0
    #for i in range(0,len(buttons2)):
    if contmod[0] == 2:
        for j in buttons2:
          j.active = 0
        for j in range(max(contmod[3]*10,0), min(contmod[3]*10+10, len(buttons2))):
          buttons2[j].active = 1
        #buttons2[i].active = 1
        if i < len(buttons21):
          buttons21[i].active = 1
        buttons[3].active = 1
        buttons21[0].active = 1
        buttons21[1].active = 1
        buttons21[2].active = 1
    else:
        for j in buttons2:
          j.active = 0
        if i < len(buttons21):
          buttons21[i].active=0
        buttons2[i].active = 0
        buttons[3].active = 0
        buttons21[0].active = 0
        buttons21[1].active = 0
        buttons21[2].active = 0
    pos = pygame.mouse.get_pos()
    cmp = 0
    pr = pygame.MOUSEBUTTONDOWN
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    sc.fill((0,0,100))
    xtest = int(xtest)
    ytest = int(ytest)
    xhum = (xx + 100 * (xtest)) * mu + (1 - mu) * (w / 2)
    yhum = (yy + 100 * (ytest)) * mu + (1 - mu) * (h / 2)
    pygame.draw.rect(sc, (0,0,255), (xhum, yhum, 100*mu, 100*mu),8)
    if pauseg != 1:
      mainquests[0].life()
      
    

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
    
    for i in semaphores:
      for j in i.cdic:
        i.cdic[j] = set()
      #i.life(FPS)
    for i in humans:
       if pauseg != 1:
        if i.life == 1:
        #i.tupd("state = " + str(i.state))
        #print(i.state)
          #if i.state == 2:
          #i.tupd("Думаю-думаю")
          
            #i.think()
          if i.state == 0:
            i.go(garages, xx, yy, mu)
          #if i.state == 1:
          i.do(buildings, clinics, garages, xx, yy, mu)
          if i.hap_eat >= 0+1/FPS/4:
            i.hap_eat -= 1/FPS/4/5
          if i.hap_health > 0+1/FPS/4:
            i.hap_health -= 1/FPS/4/6
          if i.rest > 0+1/FPS/4:
            i.rest -= 1/FPS/4/4
          if i.hap_fun > 0+1/FPS/4:
            i.hap_fun -= 1/FPS/4/5
          
          if i.hap_eat2 >= 0+1/FPS/4:
            i.hap_eat2 -= 1/FPS/4/5
          if i.hap_health2 > 0+1/FPS/4:
            i.hap_health2 -= 1/FPS/4/6
          if i.rest2 > 0+1/FPS/4:
            i.rest2 -= 1/FPS/4/4
          if i.hap_fun2 > 0+1/FPS/4:
            i.hap_fun2 -= 1/FPS/4/5
          
          if i.wotworkt > 0+1/FPS/4:
            i.wotworkt -= 1/FPS/10/5
    for i in semaphores:
      i.life(FPS)
    tvar = -1
    ivar = -1
    render_road()
#    for i in clinics:
        #i.draw()
    #for i in farms:
        #i.draw()
        
        
    for i in buildings:
        i.draw(xx,yy,mu)
    
    #humans.append(
#human(random.randint(0,9),
#random.randint(0,9)))

    for i in garages:
      i.draw()
      
      
      
    render_elay()# тестовый рендер слоя электричества
    
    
    for j in actchanks:
            carchanks[j[0]][j[1]] = []
    actchanks = set()
    for i in humans:
        #print(i.target)
        if i.state != 1 or i.wg == 1:
          i.draw(xx,yy,mu,xi0,xi1, yj0, yj1)
          i.dismod = 0
        if i.cars != 0 and len(i.list)>1:
          i.cars.renderg(i.list, xx, yy, mu)
          i.cars.render(i.list, xx, yy, mu)
          chanx = int(i.cars.rx//2)
          chany = int(i.cars.ry//2)
          if al((chanx, chany), carchanks):
            actchanks.add((chanx,chany))
            carchanks[chanx][chany].append(i)
            i.cars.chank = (chanx,chany)
          if al((chanx+1, chany), carchanks):
            i.cars.ch1 = (chanx+1,chany)
          else:
            i.cars.ch1 = None
          if al((chanx-1, chany), carchanks):
            i.cars.ch2 = (chanx-1,chany)
          else:
            i.cars.ch2 = None
          if al((chanx, chany+1), carchanks):
            i.cars.ch3 = (chanx,chany+1)
          else:
            i.cars.ch3 = None
          if al((chanx, chany-1), carchanks):
            i.cars.ch4 = (chanx,chany-1)
          else:
            i.cars.ch4 = None
    for i in buttonsfarm + buttonshuman:
      i.active = 0
    infodis(typi,numbi)
    
    #infodis(10,0)#####################################################
    li = len(rm)# алгоритм который определяет с какими координатами объекты нужно рисовать
    lj = len(rm[0])
    xh = w
    yh = h
    xtest0 = ((xh-(1-mu)*(w/2))/mu-xx)/100
    ytest0 = ((yh-(1-mu)*(h/2))/mu-yy)/100
    xi1 = int(xtest0)+1
    yj1 = int(ytest0)+1
    xh = 0
    yh = 0
    xtest0 = ((xh-(1-mu)*(w/2))/mu-xx)/100
    ytest0 = ((yh-(1-mu)*(h/2))/mu-yy)/100
    xi0 = int(xtest0)-1
    yj0 = int(ytest0)-1


    #блок отрисовки


    #if i >= xi0 and i <= xi1 and j>= yj0 and j <= yj1:
    for j in trees:
      if j[0]>= xi0 and j[0]<= xi1 and j[1]>= yj0 and j[1] <= yj1:
        for i in trees[j]:
          i.draw(xx,yy,mu)
    
    for i in buttonslay:
      i.draw()
    for i in buttonsall + buttons21:
      i.draw()
    for i in questbuttons:
      i.draw()
    #sc.blit(text1, (250, 10))
    #sc.blit(datet, (350, 10))
    buttons[7].text = " " + date + " "
    buttons[8].text = " "+ str(int(money[0])) + "  "
    buttons[12].text = " "+ str(int(money[1])) + '$'+ str(round(dcourse[0], 2))
    #print(money)
    pygame.draw.rect(sc, (0,0,255), (xhum, yhum, 100*mu*(xxtest), 100*mu*(yytest)),8)
    if tvar == 1:
      pygame.draw.rect(sc, (0,0,255), (0, h/2, w, h/2))
    
    for i in gme+smb+gmal+gmaleco+gmaloverview+gmalpeople+gmalpolitics+gmallists+gmalsincome+gmalsexpense+gmalhap+gmalfrac+gmalbutall:
        i.draw()
    
    
    
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
    mdownevent[0] = 0
    for event in ev:
     if event.type == pygame.MOUSEBUTTONDOWN:
         #mousedownevent[0] = 1
         mdownevent[0] = 1
         lb = questbuttons
         lw = questwindow
         if lb[5].press()==1:
      #print("назат клавиша выбора опции квеста")
           questwindow["output"] = 1
      #print(questwindow)
         elif lb[6].press()==1:
           questwindow["output"] = 2
         elif lb[7].press()==1:
           questwindow["output"]= 3

         buttons21[0].text = "rotate"
         pos = pygame.mouse.get_pos()
         i = buttons[0]
         
         #print("x=")
         #print(x)
         #print("xx = ")
         #print(xx)         
         chrot = buttons21[0]
         cnex = buttons21[1]
         cprev = buttons21[2]
         if chrot.active == 1:
          if pos[0] in range (chrot.x, chrot.x + chrot.xx):
           if pos[1] > chrot.y and pos[1]< chrot.y + chrot.yy:
            if brot == 1:
             brot = 0
            else:
             brot = 1
         chrot = cnex
         if chrot.active == 1:
          if pos[0] in range (chrot.x, chrot.x + chrot.xx):
           if pos[1] > chrot.y and pos[1]< chrot.y + chrot.yy:
            if contmod[3]<=(len(buttons2)-1)//10:
             contmod[3]+= 1
         chrot = cprev
         if chrot.active == 1:
          if pos[0] in range (chrot.x, chrot.x + chrot.xx):
           if pos[1] > chrot.y and pos[1]< chrot.y + chrot.yy:
            if contmod[3]>0:
             contmod[3]-= 1
         chrot = buttons21[0]
         if pos[0] in range(i.x,i.xx+i.x)  and pos[1] in range (i.y,i.yy+i.y):
              if contmod[0]==2:
                   contmod[0] = 0
                   WM = (0,0,0)
                   pauseg = 0
                   
                   walksvsets.clear()
                   lwset = set()
                   walksvdic.clear()
                   walknodes.clear()
                   walkroads.clear()
                   for i in buildings:
                     i.gennodes()
                   
                   print("begin")
                   print(walkroads)
                   print("processing")
                   add_additional_edges()
                   print(walkroads)
                   for i in roadsetobj:
                     i.gennodes()
                   #print("end")
                   while len(lwset) < len(walknodes):
                     la = walknodes - lwset
                     le = next(iter(la))
                     lwset.add(le)
                     lv1 = wnodesr(le, walknodes)[0]
                     lv2 = set(lv1.keys())
                     #print(lv1)
                     lwset = lwset | lv2
                     for i in lv2:
                       walksvdic[i] = len(walksvsets)
                     
                     walksvsets.append(lv2)
                   #print(walksvdic)
                   #print(walksvsets)
                   walklistscache.clear()
                   for i in roadsetobj:
                     i.setdir(roadset)
                     print(roadset)
                     print((0,0) in roadset)
                   for i in garages:
                     i.clearing()
                     i.gennode()
                     i.gensvset()
                   #semaphores = []
                   for i in roadset:
                     if crossroad(i,roadset) == "quad" or crossroad(i,roadset) == "triple":
                       if i not in semset:
                         sem = semaphore(i[0],i[1], "quad")
                         semaphores.append(sem)
                         semset.add(i)
                   print(semaphores)
                   #print("cont0")
              else:
                  contmod[0] =2
                  WM = ORANGE
                  pauseg = 1
                  #print("cont2")
    
      
    if contmod[2]==0:
              pxxtest = 1
              pyytest = 1
    if contmod[2] == 1:
              pxxtest = 1
              pyytest = 1
    if contmod[2] == 2:
              pxxtest = 1
              pyytest = 2
    if contmod[2] == 3:
      pyytest = 1
      pxxtest = 1
      
    if contmod[2] == 4:
              pxxtest = 1
              pyytest = 1
    if contmod[2] == 5:
              pxxtest = 2
              pyytest = 2
    if contmod[2] == 6:
              pxxtest = 2
              pyytest = 3
    if contmod[2] == 7:
              pxxtest = 2
              pyytest = 1
    if contmod[2] == 8:
              pxxtest = 2
              pyytest = 3
    if contmod[2] == 9:
              pxxtest = 1
              pyytest = 2
    if contmod[2] == 10:
              pxxtest = 1
              pyytest = 2
    if contmod[2] == 11:
              pxxtest = 3
              pyytest = 2
    if contmod[2] == 12:
              pxxtest = 2
              pyytest = 4
    if contmod[2] == 13:
              pxxtest = 1
              pyytest = 2
    
    if contmod[2] == 14:
              pxxtest = 2
              pyytest = 3
    if buttons21[0].press() == 1:
             brot = brot
    if buttons21[1].press() == 1:
             brot = brot
    if brot == 0:
      xxtest = int(pxxtest)
      yytest = int(pyytest)
    if brot == 1:
      xxtest = int(pyytest)
      yytest = int(pxxtest)
    
    if contmod[0] == 2 and tapped == 0 and pressed[0] == 1:
     
            xh = int(pos[0])-50*(xxtest-1)*mu
            yh = int(pos[1])- 50*(yytest-1)*mu
            
            xtest = ((xh-(1-mu)*(w/2))/mu-xx)/100
            ytest = ((yh-(1-mu)*(h/2))/mu-yy)/100
            xtest = int(xtest)
            ytest = int(ytest)
    elif contmod[0] == 2:
      tapped = tapped
    else:
            xtest = 500
            ytest = 500
            #xxtest = 0
            #yytest = 0
    
    if pressed[0] == 1:
       numbip = -1
       for i in range(0, len(buildings)):
            if buildings[i].pos_on(xx, yy, mu) == 1 and tapped == 0 and buildings[i].notdestroyed == True:
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
            #print("contmod")
            #print(contmod[2])
            if broadv == 1:
              brroad()
            if contmod[2]==0:
              if xtest2 == None or (xtest2!=xtest and ytest2!=ytest):
                xtest2 = xtest
                ytest2 = ytest
              else:
                broad(xtest2,ytest2,xtest-xtest2, ytest -ytest2)
                xtest2 = xtest
                ytest2 = ytest
            if contmod[2]==1:
              #bfarm(xtest,ytest)
              #build(xtest,ytest, "farm", xxtest,yytest)
              bgarage(xtest,ytest)
            if contmod[2]==2:
              
              
              build(xtest,ytest, "port", xxtest,yytest)
            if contmod[2]==3:
              
              build(xtest,ytest, "fur", xxtest,yytest)
            
            if contmod[2]==4:
              build(xtest,ytest, "elec", xxtest,yytest)
            if contmod[2]==5:
              
              build(xtest,ytest, "substation", xxtest,yytest)
            if contmod[2]==6:
              
              build(xtest,ytest, "build", xxtest,yytest)
            if contmod[2]==7:
              build(xtest,ytest, "atom", xxtest,yytest)
              
            if contmod[2]==8:
              #bimig(xtest,ytest)
              
              xxtest = 1
              yytest = 1
              droad(xtest,ytest, 0,0)
            
            if contmod[2]==9:
              build(xtest,ytest, "metro", xxtest,yytest)
            
              
              
              
              
              
            if contmod[2]==10:
              build(xtest,ytest, "farm", xxtest,yytest)
            if contmod[2]==11:
              build(xtest,ytest, "rancho", xxtest,yytest)
            if contmod[2]==12:
              build(xtest,ytest, "shop", xxtest,yytest)
            if contmod[2]==13:
              build(xtest,ytest, "mine", xxtest,yytest)
            if contmod[2]==14:
              build(xtest,ytest, "logging", xxtest,yytest)
              
            
            if contmod[2]==20:
              build(xtest,ytest, "lumber", xxtest,yytest)
            if contmod[2]==21:
              build(xtest,ytest, "cigar", xxtest,yytest)
            if contmod[2]==22:
              build(xtest,ytest, "rome", xxtest,yytest)
            if contmod[2]==23:
              build(xtest,ytest, "jewerly", xxtest,yytest)
            if contmod[2]==24:
              build(xtest,ytest, "furniture", xxtest,yytest)
            if contmod[2]==25:
              build(xtest,ytest, "canns", xxtest,yytest)
            if contmod[2]==26:
              build(xtest,ytest, "weapon", xxtest,yytest)
            if contmod[2]==27:
              build(xtest,ytest, "cheese", xxtest,yytest)
            
              
            
            if contmod[2]==30:
              build(xtest,ytest, "home", xxtest,yytest, sstype = "shanty")
            if contmod[2]==31:
              build(xtest,ytest, "home", xxtest,yytest, sstype = "barak")
            if contmod[2]==32:
              build(xtest,ytest, "home", xxtest,yytest, sstype = "country")
            if contmod[2]==33:
              build(xtest,ytest, "home", xxtest,yytest, sstype = "house")
            if contmod[2]==34:
              build(xtest,ytest, "home", xxtest,yytest, sstype = "mansion")
            if contmod[2]==35:
              build(xtest,ytest, "home", xxtest,yytest, sstype = "tenement")
            if contmod[2]==36:
              build(xtest,ytest, "home", xxtest,yytest, sstype = "apartment")
            if contmod[2]==37:
              build(xtest,ytest, "home", xxtest,yytest, sstype = "condonium")
              
              
              
            if contmod[2]== 40:
              build(xtest,ytest, "school", xxtest,yytest)
            if contmod[2]== 41:
              build(xtest,ytest, "univ", xxtest,yytest)
            if contmod[2]== 42:
              build(xtest,ytest,"clinic", xxtest,yytest)
            if contmod[2]== 43:
              build(xtest,ytest,"clinic2", xxtest,yytest)
            if contmod[2]== 44:
              build(xtest,ytest,"hospital", xxtest,yytest)
            if contmod[2]== 45:
              build(xtest,ytest, "freedom", xxtest,yytest)
            if contmod[2]== 46:
              build(xtest,ytest, "radio", xxtest,yytest)
            if contmod[2]== 47:
              build(xtest,ytest, "tv", xxtest,yytest)
              
              
            if contmod[2] == 50:
              build(xtest,ytest, "imigration", xxtest,yytest)
            if contmod[2] == 51:
              build(xtest,ytest, "mainbank", xxtest,yytest)
            if contmod[2] == 52:
              build(xtest,ytest, "minfin", xxtest,yytest)
            if contmod[2] == 53:
              build(xtest,ytest, "police", xxtest,yytest)
            if contmod[2] == 54:
              build(xtest,ytest, "army1", xxtest,yytest)
            if contmod[2] == 60:
              build(xtest,ytest, "tavern", xxtest,yytest)
            if contmod[2] == 61:
              build(xtest,ytest, "eatmarket", xxtest,yytest)
            if contmod[2] == 70:
              build(xtest,ytest, "beauty", xxtest,yytest)
            
    if buttons[5].press():
      FPSl[0] = fps
      pauseg = 0
    if buttons[4].press():
      FPSl[0] = fps/30
      pauseg = 0
    if buttons[6].press():
      FPSl[0] = 100000000000
      pauseg = 1
    if buttons[11].press():
      laymod[1] = 1
      for i in buttonslay:
        i.active = 1
    if buttonslay[0].press():
      for i in buttonslay:
        i.active = 0
      laymod[1] = 0
      laymod[0] = "none"
    if buttonslay[1].press():
      laymod[0] = "elec"
    if buttonslay[2].press():
      laymod[0] = "beauty"
    if buttonslay[3].press():
      laymod[0] = "freedom"
      
      
    if buttonslay[4].press():
      laymod[0] = "oil"
    if buttonslay[5].press():
      laymod[0] = "iron"
    if buttonslay[6].press():
      laymod[0] = "bouxit"
    if buttonslay[7].press():
      laymod[0] = "gold"
    if buttonslay[8].press():
      laymod[0] = "safe"
      
    if pressed[0]==1:
        pos = pygame.mouse.get_pos()
        if sp is None:
            sp = pos
            xxx=xx
            yyy=yy
            a = 0
        i = buttons[1]
        j = buttons[2]
        if a!=0 and contmod[0]== 0:
          xx = xxx + (pos[0] - sp[0])*(1/mu)
          yy = yyy+ (pos[1] - sp[1])*(1/mu)
          if pos[0] in range(i.x,i.xx+i.x) and pos[1] in range(i.y, i.y+i.yy):
            mu=mu+0.015*mu
          if pos[0] in range(j.x,j.xx+j.x) and pos[1] in range(j.y, j.y+j.yy):
            mu=mu-0.015*mu
        a = 1
    else:
        sp = None
    tapped= 0
    monthp = month
    yearp = year
    if pauseg != 1:
      time+=1/FPS/40
      timeint += 1
    month = 1+time%12
    year = 2023+time//12
    timelist[0]= time
    
    
    if timeint%150 == 0:
      electro[0] = 0
      electro[1] = 0
      eleclay = arzero.copy()
      #beautylay = arzero.copy()
      
      for i in range(0, len(eleclay)):
        for j in range(0,len(eleclay[0])):
          eleclay[i][j] = 0
      #for i in range(0, len(eleclay)):
        #for j in range(0,len(eleclay[0])):
          #freedomlay[i][j] = 50
          
      if 1==0:# это нужно будет засунуть в yearevent
       for i in buildings:
        if i.beautyallow != 1:
          for j in range(i.x - 30, i.x+31):
            for wj in range(i.y - 30, i.y+31):
              if al((j,wj),rm):
                dx = i.x - j
                dy = i.y - wj
                ds = math.sqrt(dx*dx+dy*dy)
                if ds < 20:
                  freedomlay[j][wj] -= (20-ds) * i.nwork/50
                  if freedomlay[j][wj] <0:
                    freedomlay[j][wj] = 0
      
          
                    
      for i in elecbuildings:
        if i.elecpow == 1:
         if i.maxnwork >0:
          i.powerout = i.nwork/(i.maxnwork)*500
          electro[0] += i.powerout
          electro[1] += i.powerout
          
      epcnt = 0
      emcnt = 0
      
      for i in elecbuildings:
        if i.elecpow == 1:
          
          for j in range(i.x - i.range, i.x+i.range+1):
            for wj in range(i.y - i.range, i.y+i.range+1):
              if al((j,wj),rm):
                if epcnt > 0:
                  eleclay[j][wj] = 1+ int(254*epcnt/(epcnt+emcnt))
                elif epcnt+emcnt == 0:
                  eleclay[j][wj] = 255
                else:
                  eleclay[j][wj] = 1
                if electro[0] == 0:
                  eleclay[j][wj] = 1
      for i in buildings:
        if i.powerin_allow == 1:
          #print(eleclay)
          #print(i.x)
          #print(i.y)
          #print(electro[1] - i.powerin >0)
          #print(eleclay[i.x][i.y] != 0)
          if electro[1] - i.powerin >0 and eleclay[i.x][i.y] != 0:
            i.power_switch = 1
            electro[1] -= i.powerin
            epcnt += 1
          else:
            i.power_switch = 0
            emcnt += 1
      electro[2] = epcnt
      electro[3] = emcnt
    
    if int(monthp) != int(month):
      monthevent = 1
    else:
      monthevent = 0
    #menu = menu+1
    if int(yearp) != int(year):
      yearevent = 1
    else:
      yearevent = 0
    if yearevent == 1:
      #addhuman2(7)
      #lrebelcount = 0
      #for i in humans:
        #if lrebelcount < 5:
          
          #if i.state != "rebel":
            #lrebelcount += 1
            #i.becomerebel()
      #beginconflict()
      if 1==0:
       for i in range(len(freedomlay)):
        for j in range(len(freedomlay[0])):
          freedomlay[i][j] = 50
      for i in humans:
        i.age += 1
      if 1 == 0:
       for i in libertybuilds:
        for j in range(i.x - i.range, i.x+i.range+1):
            for wj in range(i.y - i.range, i.y+i.range+1):
              if al((j,wj),rm):
                
                freedomlay[j][wj] += i.freedompow
        
    if monthevent == 1:
      for i in families:
        if i.type == "full":
          vari = random.randint(0,100)
          #if vari < 2:
            #i.birth()
      for i in families:
        if i.type == "husbant":
         for j in families:
          if j.type == "wife":
            vari = random.randint(0,100)
            if vari < 2:
              nfam = i + j
              if i in families:
                families.remove(i)
              if j in families:
                families.remove(j)
              families.append(nfam)
      
      mainbanks[0].life()
      if courseon[0] == True:
        exchanges[0].update()
      calcmrot()
      allmrot["dollar"][0] = dcourse[0]
      growthdi["main"][-1]= len(humans)
      for i in buildings:
        pay_upkeep(i)
        #i.allstat["upkeep"] += i.upkeep
        #i.monthstat["upkeep"][-1] += i.upkeep
        i.updstat("upkeep", i.upkeep)
        
      for i in humans:
        if i.work_n != -1:
          if i.realwork == "base":
            if buildings[i.work_n].paymod == "monthly":
              #i.money += buildings[i.work_n].salary
              ltype = buildings[i.work_n].type
              transact("island", i, buildings[i.work_n].salary, type = getindustry(ltype))
              buildings[i.work_n].updstat("salary", buildings[i.work_n].salary)
              #buildings[i.work_n].allstat["salary"] += buildings[i.work_n].salary
        
      for i in buildings:
        i.resetstat()
      #print(allhapmon)
      for i in allhapmon:
        updlist(allhapmon[i],0)
      #print(allhapmon)
      buttonsall = buttons + buttons2 +  buttonsfarm + buttons21 + buttonshuman
      print("month")
      if courseon[0] == True:
        if money[0] < -10000:
          mainbanks[0].printmoney(-money[0])
      allsalary = 0
      nsalary = 0
      avsalary = 0
      numhum = 0
      buttons[9].text = "  "+str(numhum)+"  "
      #buttons[12].text = "$" + str(int(money[1]))
      for i in humans:
        if i.work_n != -1:
          allsalary += i.salary
          nsalary += 1
        i.sethap(buildings, lays)
        if i.life == 1:
          numhum += 1
        buttons[9].text = "  "+str(numhum)+"  "
        #i.initial()
        if i.student == False:
          i.findworkp = 1
        #i.findhome(buildings, homes)
        #for j in factories:
          #j.pinres = j.inres 
        
        for j in allhapmon:
          allhapmon[j][-1]+= i.happiness[j]
      #print(numhum)
      #print(allhapmon)
      #from testsave import*
      #clearal()
      #addhuman2(1)
      #sst(buildings)
      #testllm[0].circlefill(200, 4, full = True)
      #testllm[0].updatelay()
      if nsalary >0:
      
        growthdi["avsalary"][-1] = allsalary/nsalary
        allmrot["avsalary"][-1] = allsalary/nsalary
      for j in allhapmon:
          allhapmon[j][-1] = allhapmon[j][-1]/numhum
          allhap[j][-1] = medlist(allhapmon[j])
        
        
    clock.tick(fps)
