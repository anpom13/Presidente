import math
import pygame
#from buttons import *
from exchange import *

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

def sumdic(d):
  a = 0
  for i in d:
    a += d[i]
  return a

def medlist(l):
  a = 0
  for i in l:
    a += i
  if len(l) != 0:
    return a/len(l)
  else:
    return 13

def sumlist(l):
  a = 0
  for i in l:
    a += i
  if len(l) != 0:
    return a
  else:
    return a
def updlist(l, a, n=12):
  if len(l)<n:
    l.append(a)
  else:
    for i in range(len(l)-1):
      l[i] = l[i+1]
    l[n-1] = a
  return l
class rmarker(object):
  def __init__(self, x, y, range = 10, res = "tree"):
    self.x = x
    self.y = y
    self.range = range
class resourse(object):
  def __init__(self, x,y,type):
    self.x = x
    self.y = y
    self.type = type
    self.amount = 10000
class roaad(object): 
#этот класс "клеточной" дороги. Реализации нодами пока не планируется
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.type = None
    self.directs = {1:"up", 2:"right"}
    self.ud = "updown"
    self.lr = "leftright"
    self.xx = 1
    self.yy = 1
  def gennodes(self):
      n1 = (self.x, self.y)
      n2 = (self.x, self.y + self.yy)
      n3 = (self.x + self.xx, self.y)
      n4 = (self.x+self.xx, self.y+ self.yy)
      
      ws = {n1,n2,n3,n4}
      
      walknodes.add(n1)
      walknodes.add(n2)
      walknodes.add(n3)
      walknodes.add(n4)
      self.walknodes = set()
      self.walknodes.add(n1)
      self.walknodes.add(n2)
      self.walknodes.add(n3)
      self.walknodes.add(n4)
      wnodesv(n1, n2)
      wnodesv(n1, n3)
      
      wnodesv(n2, n4)
      wnodesv(n3, n4)
      
      wnodesv(n1, n4)
      wnodesv(n2, n3)
      #for i in ws:
        #for j in ws:
          #if i!=j:
            #wnodesv(i,j)
      
      #теперь генерируем "грани"
      g1 = set() #грань x-xx-y
      for i in range(self.x+1, self.x + self.xx):
        g1.add( (i,self.y) )
      g2 = set() #грань x-xx-yy
      for i in range(self.x+1, self.x + self.xx):
        g2.add( (i,self.yy + self.y) )
      g3 = set()
      for i in range(self.y+1, self.y + self.yy):
        g3.add( (self.x, i) )
      g4 = set()
      for i in range(self.y+1, self.y + self.yy):
        g4.add( (self.x + self.xx, i) )
  def setdir(self, roadset):
    x = self.x
    y = self.y
    l = (x-1,y)
    r = (x+1,y)
    u = (x, y-1)
    d = (x, y+1)

    if (x-1,y) in roadset and (x+1,y) in roadset:
      self.lr = "leftright"
    elif (x-1,y) in roadset:
      self.lr = "left"

    elif (x+1,y) in roadset:
      self.lr = "right"
    
    else:
      self.lr = None
    if u in roadset and d in roadset:
      self.ud = "updown"
    elif (x, y-1) in roadset:
      self.ud = "up"
    elif (x, y+1) in roadset:
      self.ud = "down"
    
    else:
      self.ud = None
  def draw(self, xx, yy, w, h, mu):
    xh = (xx + 100 * self.x) * mu + (1 - mu) * (w / 2)
    yh = (yy + 100 * self.y) * mu + (1 - mu) * (h / 2)
    pygame.draw.rect(sc, (70,70,70), (xh+20*mu, yh+20*mu, 100*mu-40*mu, 100*mu-40*mu))
    if self.ud == "up":
      pygame.draw.rect(sc, (70,70,70), (xh+20*mu, yh, 100*mu-40*mu, 100*mu-20*mu))
    if self.ud == "down":
      pygame.draw.rect(sc, (70,70,70), (xh+20*mu, yh+20*mu, 100*mu-40*mu, 100*mu-20*mu))
    if self.ud == "updown":
      pygame.draw.rect(sc, (70,70,70), (xh+20*mu, yh, 100*mu-40*mu, 100*mu))
    if self.lr == "left":
      pygame.draw.rect(sc, (70,70,70), (xh, yh+20*mu, 100*mu-20*mu, 100*mu-40*mu))
    if self.lr == "right":
      pygame.draw.rect(sc, (70,70,70), (xh+20*mu, yh+20*mu, 100*mu-20*mu, 100*mu-40*mu))
    if self.lr == "leftright":
      pygame.draw.rect(sc, (70,70,70), (xh, yh+20*mu, 100*mu, 100*mu-40*mu))
class tree(object):
    def __init__(self, x, y, h = 0.5):
        self.x = x
        self.y = y
        self.h = h
        self.active = 1
        self.hp = 100
        self.startlog = 0
        #draw.line(screen, BLACK, (100, 100), (700, 500), 5)
    def draw(self, xx, yy,mu):
        xhum = int((xx + 100 * self.x) * mu + (1 - mu) * (w / 2))
        yhum = int((yy + 100 * self.y) * mu + (1 - mu) * (h / 2))
        if self.active == 1:
          pygame.draw.line(sc, (0,0,0), (xhum, yhum), (xhum, yhum + self.h*100*mu ))
          #math.ceil((self.xx)*100*mu), math.ceil((self.yy)*100*mu)))

class locallaymap(object):
  def __init__(self, srange = 25, type = "freedom", x=5, y=5):
    self.range = srange
    self.rm = [[0 for j in range(srange*2 + 1)] for i in range(srange*2 + 1)]
    self.prm = None
    self.center = (srange, srange)
    self.cx = srange-x
    self.cy = srange-y
    self.type = type
    self.changed = False
  def updatelay(self, type = None):
    if type == None:
      type = self.type
    if self.prm == None:
      self.prm = self.rm.copy()
      for i in range(len(self.rm) ):
        for j in range(len(self.rm[i])  ):
          if al((i-self.cx,j-self.cy),rm ) == 1:
            if al((i,j), self.rm) == 1:
              lays[type][i-self.cx][j-self.cy] += self.rm[i][j]
    if self.prm != None:
      for i in range(len(self.rm)  ):
        for j in range(len(self.rm[i]) ):
          if al((i-self.cx,j-self.cy), rm) == 1:
            if al((i,j), self.prm) == 1:
              lays[type][i-self.cx][j-self.cy] -= self.prm[i][j]
      
      self.prm = self.rm.copy()
      
      for i in range( len(self.rm)  ):
        for j in range( len(self.rm[i])  ):
          if al((i-self.cx,j-self.cy), rm) == 1:
            if al((i,j), self.rm) == 1:
              lays[type][i-self.cx][j-self.cy] += self.rm[i][j]
            
  def fullfill(self, val):
    #self.prm = self.rm.copy()
    for i in range(len(self.rm)):
      for j in range(len(self.rm[0])):
        self.rm[i][j] = val
  def circlefill(self, val, srange, full = False):
    #self.prm = self.rm.copy()
    x = self.center[0]
    y = self.center[1]
    self.rm[x][y] = val
    for i in range(len(self.rm)):
      for j in range(len(self.rm[0])):
           dx = x-i
           dy = y-j
           ds = math.sqrt(dx*dx+dy*dy)
           if ds <= srange:
             if full == False:
               rval =min(val*(srange-ds)/srange,255)
             else:
               rval = min(255,val)
             #if al((i,j), self.rm) == 1:
             self.rm[i][j] = int(rval)
               #print("val = ", rval, ", i = ", i, ", j = ", j)
           else:
             #if al((i,j), self.rm) == 1:
               self.rm[i][j] = 0
               #print("ds = ", ds, ", i = ", i, ", j = ", j, ", x = ", x, ", y = ", y)
def tfmode(self):
    return True
class mode():
    def __init__(self, action = tfmode):
        self.text0 = "краткое описание"
        self.text = 'описание модификации'
        self.price = 500
        self.action = action
        self.uslov = tfmode





class building(object):
    def __init__(self, a = 2, b = 2, type = "farm", id = 0):

        self.mode = None
        self.maintype = "building"
        self.mods = []
        self.modc = None

        self.modstates = [False, False, False, False, False, False, False]

        self.modes = []
        self.activemode = None
        self.nmode = 0
        self.modedic = {}

        self.modc1 = False
        self.modc2 = False
        self.modc3 = False

        self.families = []
        self.laymap = locallaymap(x = a, y = b)
        
        self.hp = 1000
        
        self.quality = 0
        self.freedompow = 0
        
        self.notdestroyed = True
        self.id = id
        self.type = type
        self.subtype = ""
        self.workedu = 0
        self.edu_allow = 0
        self.students = []
        self.nstud = 0
        self.maxnstud = 0
        self.color = (20,20,20)
        
        self.workqmodifer = 1.3
        
        
        self.paymod = "monthly"
        
        
        self.elecpow = 0
        self.range = 0
        
        self.bready = 0
        
        self.bproc = 1
        self.bpready = 100
        
        self.statres = reslist.copy()
        
        
        self.mineres = None
        self.x = a#
        self.y = b#
        self.xx = 1
        self.yy = 1
        
        self.xt = a # для гаража и зданий которые привязаны к дороге
        self.yt = b
        
        
        self.t1 = 0
        self.t2 = 0

        
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
        self.price = 1
        
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
        self.maxinres = 1000
        self.max_number =0 # из класса "home"
        self.number = 0
        self.h_list = []#
        self.rent = 0#
        self.quality = 0 #max -- 100
        self.beautyallow = 0
        
        self.health_allow = 1
        self.text = self.type
        self.powerout = 0
        self.powerin_allow = 0
        self.powerin = 0
        self.power_switch = 0
        
        self.builders = []
        self.upkeep = 0
        self.active = 1
        self.minfin = False
        #self.settype(self.type)
        self.monthstat = {
          "export":[0 for i in range (12)],
          "this":[0 for i in range (12)],
          "salary":[0 for i in range (12)],
          "upkeep":[0 for i in range (12)],
          "balance":[0 for i in range (12)],
          "prodused":[0 for i in range (12)]
        }
        self.allstat = {
          "export":0,
          "this":0,
          "salary":0,
          "upkeep":0,
          "balance":0,
          "prodused":0
        }
        
        self.prices = {}
        for i in eat:
          self.prices[i]=1
        ####пока затычка
        
          
          
        if self.type == "beauty":
          self.beautyallow = 1
          self.range = 15
          self.bready = 1
          self.text = "Сад"
        if self.type == "build":
          self.workallow = 1
          self.salary = 5
          self.nwork = 0
          self.maxnwork = 8
          self.bready = 1
          self.text = "Инженеры"
          
          self.active = 1

    def updstat(self, type, val):
      self.monthstat[type][-1] += val
      self.allstat[type]+= val
      if type == "export" or type == "this":
        self.updstat("balance", val)
      if type == "salary" or type == "upkeep":
        self.updstat("balance", -val)
    def resetstat(self):
      for i in self.monthstat:
        self.monthstat[i] = updlist(self.monthstat[i],0)
    def destroy(self):

        self.quality = 0
        self.notdestroyed = False
        #self.id = id
        #self.type = type
        self.subtype = ""
        self.workedu = 0
        self.edu_allow = 0
        self.students = []
        self.nstud = 0
        self.maxnstud = 0
        
        self.workqmodifer = 1.3
        
        
        self.paymod = "monthly"
        
        
        self.elecpow = 0
        self.range = 0
        
        self.bready = 1
        
        self.bproc = 1
        self.bpready = 100
        
        self.statres = reslist.copy()
        
        
        self.mineres = None
        #self.x = a#
        #self.y = b#
        #self.xx = 1
        #self.yy = 1
        
        #self.xt = a # для гаража и зданий которые привязаны к дороге
        #self.yt = b
        
        
        self.t1 = 0
        self.t2 = 0

        
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
        self.price = 0
        
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
        self.beautyallow = 0
        
        self.health_allow = 0
        self.text = self.type
        self.powerout = 0
        self.powerin_allow = 0
        self.powerin = 0
        self.power_switch = 0
        
        self.builders = []
        
        self.active = 0
        self.minfin = False
        self.upkeep = 0
        
        self.prices = {}
        for i in eat:
          self.prices[i]=1
    def disable(self):
      self.active = 0
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

        if max(l) > 10:
          return 1
        else:
          return 0
      else:
        return 0
    def settype(self, type):
     if self.notdestroyed == True:
      if self.type == "army1":
        self.workallow = 1
        self.maxnwork = 10
        self.salary = 10
      if self.type == "army2":
        self.workallow = 1
        self.maxnwork = 3
        self.salary = 20

      if self.type == "police":
        self.workallow = 1
        self.maxnwork = 6
        self.salary = 10
      if self.type == "minfin":
        self.workallow = 1
      if self.type == "mainbank":
        self.workallow = 1
      if self.type == "eatmarket":
        self.workallow = 1
        self.maxnwork = 1
        self.salary = 10
        self.text = "имп. еда"
        self.prices = {}
        for i in eat:
          self.prices[i]= exportprices[i]*1.2/100
        #self.aloutres = resone.copy()
      if self.type == "metro":
        self.workallow = 1
        self.maxnwork = 4
        self.upkeep = 200
        self.salary = 10
      if self.type == "palace":
        self.text = "Дворец"
        self.upkeep = 16
        self.workallow = 1
        self.maxnwork = 4
        self.salary = 10

        def action1(self):

            print("дворец украшен")

        palacemod1 = mode()
        palacemod1.action = action1
        palacemod1.text0 = "вазочки"
        palacemod1.text = "укарашает дворец"
        palacemod1.price = 5000

        self.mods.append(palacemod1)

        def action1(self):
            print("Будки есть")

        palacemod1 = mode()
        palacemod1.action = action1
        palacemod1.text0 = "Будки"
        palacemod1.text = "стражам лучше работается"
        palacemod1.price = 7000
        self.mods.append(palacemod1)
        def action1(self):
            print("Статуи есть")

        palacemod1 = mode()
        palacemod1.action = action1
        palacemod1.text0 = "Статуи Президентэ"
        palacemod1.text = "Люди не протестуют у дворца"
        palacemod1.price = 10000
        self.mods.append(palacemod1)
        print(self.mods)
      if self.type == "weapon":
        self.upkeep =60
        self.workallow = 1
        self.maxnwork = 12
        self.salary = 10
        self.text = "оружие"
        self.alinres = reszero.copy()
        self.aloutres = resone.copy()
        self.alinres["iron"] = 1
        self.in_allow = 1
        self.out_allow = 1
      if self.type == "jewerly":
        self.upkeep = 43
        self.workallow = 1
        self.maxnwork = 12
        self.salary = 10
        self.text = "Ювелир"
        self.alinres = reszero.copy()
        self.aloutres = resone.copy()
        self.alinres["gold"] = 1
        self.in_allow = 1
        self.out_allow = 1
      if self.type == "lumber":
        self.upkeep =16
        self.workallow = 1
        self.maxnwork = 12
        self.salary = 10
        self.text = "Лесопилка"
        self.alinres = reszero.copy()
        self.aloutres = resone.copy()
        self.alinres["loggs"] = 1
        self.in_allow = 1
        self.out_allow = 1
      if self.type == "furniture":
        self.upkeep =42
        self.workallow = 1
        self.maxnwork = 12
        self.salary = 10
        self.text = "Мебель"
        self.alinres = reszero.copy()
        self.aloutres = resone.copy()
        self.alinres["lumber"] = 1
        self.in_allow = 1
        self.out_allow = 1
      if self.type == "logging":
          self.upkeep = 5
        
          self.workallow = 1
          self.salary = 5
          self.nwork = 0
          self.maxnwork = 8
          self.bready = 1
          self.text = "Лесоруб"
          self.alinres = reszero.copy()
          self.aloutres = resone.copy()
          #self.alinres[self.subtype] = 1
          self.in_allow = 0
          self.out_allow = 1
      if type == "freedom":
        
        
        self.freedom_allow = 1
        self.workallow = 1
        self.workedu = 0
        self.maxnwork = 6
        self.salary = 10

        def lv(aa):
            aa.mode = "communists"
        lm = mode(lv)
        lm.text0 = "Голос трудящихся"
        lm.text = "Газета коммунистов"
        self.modes.append(lm)

        def lv(aa):
            aa.mode = "capitalists"
        lm = mode(lv)
        lm.text0 = "Торговля и промышленность"
        lm.text = "Газета капиталистов"
        self.modes.append(lm)

        def lv(aa):
            aa.mode = "army"
        lm = mode(lv)
        lm.text0 = "Солдато де фортуна"
        lm.text = "Газета военных"
        self.modes.append(lm)

        def lv(aa):
            aa.mode = "religion"
        lm = mode(lv)
        lm.text0 = "слово божье"
        lm.text = "Газета верующих"
        self.modes.append(lm)

        def lv(aa):
            aa.mode = "nationalists"
        lm = mode(lv)
        lm.text0 = "гордость нации"
        lm.text = "Газета националистов"
        self.modes.append(lm)

        def lv(aa):
            aa.mode = "revenue"
        lm = mode(lv)
        lm.text0 = "скидки и купоны"
        lm.text = "Приносит доход"
        self.modes.append(lm)

        print(self.modes)




      if type == "school":
        
        
        self.workallow = 1
        self.workedu = 1
        self.maxnwork = 6
        self.salary = 10
        
        self.edu_allow = 1
        self.students = []
        self.nstud = 0
        self.maxnstud = 5

        def lv(aa):
            aa.mode = "main"
        lm = mode(lv)
        lm.text0 = "Основное образование"
        lm.text = "Выше скорость"
        self.modes.append(lm)
        def lv(aa):
            aa.mode = "militarists"
        lm = mode(lv)
        lm.text0 = "Военное образование"
        lm.text = "Больше милитаристов"
        self.modes.append(lm)
        def lv(aa):
            aa.mode = "religion"
        lm = mode(lv)
        lm.text0 = "Религиозное образование"
        lm.text = "Больше религионеров"
        self.modes.append(lm)
      if type == "mine":
        self.upkeep = 10
        self.powerin_allow = 1
        self.powerin = 1000
        self.workallow = 1
        self.maxnwork = 12
        self.salary = 5
        self.out_allow = 1
        self.aloutres = resone.copy()
        self.subtype = self.mineres.type
      if type == "elec":
        self.upkeep = 6
        self.workallow = 1
        self.maxnwork = 12
        self.salary = 20
        self.elecpow = 1
        self.range = 5
        self.workedu = 1
      if type == "substation":
        self.workallow = 0
        self.maxnwork = 0
        self.salary = 0
        self.elecpow = 1
        self.range = 25
        self.workedu = 1
      if type == "shop":
        self.upkeep = 1
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
        self.upkeep = 73
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
        self.upkeep = 40
        self.maxnwork = 12
        self.salary = 10
        self.text = "Сыр"
        self.alinres = reszero.copy()
        self.aloutres = resone.copy()
        self.alinres["milk"] = 1
        self.in_allow = 1
        self.out_allow = 1
      if type == "cigar":
        self.upkeep = 33
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
        self.upkeep = 50
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
      if type == "childhome":
        self.workallow = 1
        self.maxnwork = 3
        self.visit_allow = 1
        self.salary = 5
        self.fun_allow = 1
        self.max_visiters = 6
        self.text = "Дом детства"

      if type == "church":
          self.upkeep = 3
          self.workallow = 1
          self.maxnwork = 4
          self.visit_allow = 1
          self.salary = 5
          #self.fun_allow = 1
          self.max_visiters = 12
          self.text = "Церковь"

      if type == "sobor":
          self.upkeep = 3
          self.workallow = 1
          self.maxnwork = 4
          self.visit_allow = 1
          self.salary = 5
          #self.fun_allow = 1
          self.max_visiters = 16
          self.text = "Церковь"
      if type == "tavern":
        
        self.upkeep = 3
        self.workallow = 1
        self.maxnwork = 3
        self.visit_allow = 1
        self.salary = 5
        self.fun_allow = 1
        self.max_visiters = 6
        self.text = "Театр"
      if type == "pub":
          self.upkeep = 3
          self.workallow = 1
          self.maxnwork = 3
          self.visit_allow = 1
          self.salary = 5
          self.fun_allow = 1
          self.max_visiters = 6
          self.text = "Театр"
      if type == "cabare":
          self.upkeep = 3
          self.workallow = 1
          self.maxnwork = 3
          self.visit_allow = 1
          self.salary = 5
          self.fun_allow = 1
          self.max_visiters = 6
          self.text = "Театр"
      if type == "night_club":
          self.upkeep = 3
          self.workallow = 1
          self.maxnwork = 3
          self.visit_allow = 1
          self.salary = 5
          self.fun_allow = 1
          self.max_visiters = 6
          self.text = "Театр"
      if type == "fur":
        self.upkeep = 6
        self.workallow = 1
        self.nwork = 0
        self.maxnwork = 5
        self.salary = 5
        self.mode = "auto"
        
        self.text = "Фуры"
      if type == "port":
        self.upkeep = 6
        self.workallow = 1
        self.nwork = 0
        self.maxnwork = 4
        self.alinres = resone.copy()
        self.text = "Порт"
        self.salary = 5
        
        self.in_allow = 1
        self.out_allow = 0
      if type == "rancho":
        self.upkeep = 2
        self.workallow = 1
        self.workers= []
        self.price = 1
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
        self.prices = {}
        for i in eat:
          self.prices[i]=1
      if type == "farm":
        self.upkeep = 4
        self.workallow = 1
        self.workers= []
        self.price = 1
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
        self.prices = {}
        for i in eat:
          self.prices[i]=1
        
        self.in_allow = 0
        self.out_allow = 1
        def lv(aa):
            aa.subtype = "corn"
            aa.rtype = "corn"
        lm = mode(lv)
        lm.text0 = "Кукуруза"
        lm.text = "Кукуруза"
        self.modes.append(lm)

        def lv(aa):
            aa.subtype = "pineapple"
            aa.rtype = "pineapple"
        lm = mode(lv)
        lm.text0 = "pineapple"
        lm.text = "pineapple"
        self.modes.append(lm)

        def lv(aa):
            aa.subtype = "tobacco"
            aa.rtype = "tobacco"
        lm = mode(lv)
        lm.text0 = "tobac"
        lm.text = "tobac"
        self.modes.append(lm)

        def lv(aa):
            aa.subtype = "sugar"
            aa.rtype = "sugar"
        lm = mode(lv)
        lm.text0 = "sugar"
        lm.text = "sugar"
        self.modes.append(lm)

        def lv(aa):
            aa.subtype = "coffee"
            aa.rtype = "coffee"
        lm = mode(lv)
        lm.text0 = "coffee"
        lm.text = "coffee"
        self.modes.append(lm)
      if type == "home":
        self.h_list = []#
        self.live_allow = 1
        self.number = 0
        if self.subtype == "tenement":
          self.upkeep = 13
          self.max_number = 12#
          self.rent = 1#
          self.quality = 40
          self.text = "Хрущевка"
        if self.subtype == "shanty":
          self.max_number = 1#
          self.rent = 0#
          self.quality = 15
          self.text = "Хибара"
        if self.subtype == "barak":
          self.upkeep = 1
          self.max_number = 3#
          self.rent = 1#
          self.quality = 25
          self.text = "Барак"
        if self.subtype == "country":
          self.upkeep = 2
          self.max_number = 2#
          self.rent = 1#
          self.quality = 50
          self.text = "Фазенда"
        if self.subtype == "house":
          self.upkeep = 6
          self.max_number = 2#
          self.rent = 1#
          self.quality = 70
          self.text = "Заг. дом"
        if self.subtype == "mansion":
          self.upkeep = 12
          self.max_number = 2#
          self.rent = 1#
          self.quality = 70
          self.text = "Особняк"
        if self.subtype == "apartment":
          self.upkeep = 16
          self.max_number = 6
          self.rent = 1#
          self.quality = 60
          self.text = "Аппартам."
        if self.subtype == "condonium":
          self.upkeep = 15
          self.max_number = 4
          self.rent = 1#
          self.quality = 85
          self.text = "Коммуна"
        if gamevalues["free_home"] == True:
            self.rent = 0
      if type == "clinic":
        
        
        self.workers = []
        self.workallow = 1
        self.health_allow = 1
        
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
    def pos_on(self, xx, yy, mu):
        pos = pygame.mouse.get_pos()
        xh = int(pos[0])
        yh = int(pos[1])
        xtest = ((xh-(1-mu)*(w/2))/mu-xx)/100
        ytest = ((yh-(1-mu)*(h/2))/mu-yy)/100
        xtest = int(xtest)
        ytest = int(ytest)
        if xtest >= self.x and xtest <=self.x+self.xx-1  and ytest >= self.y and ytest <= self.y + self.yy-1:
              return 1
    
        
        
      
    
    def gennodes(self):
      n1 = (self.x, self.y)
      n2 = (self.x, self.y + self.yy)
      n3 = (self.x + self.xx, self.y)
      n4 = (self.x+self.xx, self.y+ self.yy)
      
      ws = {n1,n2,n3,n4}
      
      walknodes.add(n1)
      walknodes.add(n2)
      walknodes.add(n3)
      walknodes.add(n4)
      self.walknodes = set()
      self.walknodes.add(n1)
      self.walknodes.add(n2)
      self.walknodes.add(n3)
      self.walknodes.add(n4)
      wnodesv(n1, n2)
      wnodesv(n1, n3)
      wnodesv(n2, n4)
      wnodesv(n3, n4)
      #for i in ws:
        #for j in ws:
          #if i!=j:
            #wnodesv(i,j)
      
      #теперь генерируем "грани"
      g1 = set() #грань x-xx-y
      for i in range(self.x+1, self.x + self.xx):
        g1.add( (i,self.y) )
      g2 = set() #грань x-xx-yy
      for i in range(self.x+1, self.x + self.xx):
        g2.add( (i,self.yy + self.y) )
      g3 = set()
      for i in range(self.y+1, self.y + self.yy):
        g3.add( (self.x, i) )
      g4 = set()
      for i in range(self.y+1, self.y + self.yy):
        g4.add( (self.x + self.xx, i) )
      g1 = g1 & walknodes
      g2 = g2 & walknodes
      g3 = g3 & walknodes
      g4 = g4 & walknodes
      #g1 = set()
      #g2 = set()
      #g3 = set()
      #g4 = set()
      for i in g1:
        self.walknodes.add(i)
        wnodesv(i, (self.x, self.y))
        wnodesv(i, (self.x + self.xx, self.y))
      for i in g2:
        self.walknodes.add(i)
        wnodesv(i, (self.x, self.y + self.yy))
        wnodesv(i, (self.x + self.xx, self.y + self.yy))
      for i in g3:
        self.walknodes.add(i)
        wnodesv(i, (self.x, self.y))
        wnodesv(i, (self.x, self.y + self.yy))
      for i in g4:
        self.walknodes.add(i)
        wnodesv(i, (self.x + self.xx, self.y))
        wnodesv(i, (self.x + self.xx, self.y + self.yy))


    def infodis(self):
     
      #priorl2 = []
      setbtext()
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
      if self.eat_allow == 0 and self.type != "minfin":
        eatallow = "здание не предоставляет пищу"
        price = ""
        butdisprice[2].active = 0
        butdisprice[3].active = 0
      elif infomod[0] == "price":
        eatallow = "здание предоставляет пищу"
        butdisprice[2].active = 1
        butdisprice[3].active = 1
      if self.type == "palace":
        name = "дворец"
        idinfo = "Это Ваша резиденция"
      if self.type == "build":
        name = "Сторительная контора"
        idinfo = "Работающие здесь люди строят новые здания на острове"
      if self.type == "metro":
        name = "Метрополитен"
        idinfo = "Позволяет быстро перемещаться по острову"
      if self.type == "elec":
        name = "Электростанция"
        resourses = "Всего:" +str(int(electro[0])) + "Дост:" + str(int(electro[1]))
        price = str(electro[2])+ " " + str(electro[3])
      if self.type == "mine":
        name = "Шахта"
        resourses = "На складе:" + str(int(self.outres[self.subtype]))+ " осталось:" + str(self.mineres.amount)
        idinfo = "Шахта позволяет добывать полезные ископаемые"
        price = self.power_switch
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
      if self.type == "mainbank":
        name = "Центральный банк"
        #price = "процент в цб" + str(minfins[0].part2)
        idinfo = "Главный банк острова. Печатает деньги, поддерживает курс рубля"
        mode1 = "free"
        mode2 = "support"
        #resourses = "обмен" + str(minfins[0].part)
      if self.type == "minfin":
        name = "Министерство финансов"
        price = "процент в цб" + str(minfins[0].part2)
        idinfo = "Устанавливает бюджетное правило"
        mode1 = "ex->цб"
        resourses = "обмен" + str(minfins[0].part)
        
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
        workers = "Живёт: " + str(len(self.families)) + " из " + str(self.max_number)
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
        lrlist = []
        for i in self.inres:
          cnt += self.inres[i]
          lrlist.append( (self.inres[i], i + ": ") )
        lrlist.sort(reverse = True)
        idinfo2 = "на складе: " + str(int(cnt))
        
        other1 =  lrlist[0][1] + str(int(lrlist[0][0]))
        other2 = lrlist[1][1] + str(int(lrlist[1][0]))
        other3 = lrlist[2][1] + str(int(lrlist[2][0]))
        other4 = lrlist[3][1] + str(int(lrlist[3][0]))
        other5 = lrlist[4][1] + str(int(lrlist[4][0]))
        other6 = lrlist[5][1] + str(int(lrlist[5][0]))
        other7 = lrlist[6][1] + str(int(lrlist[6][0]))
        other8 = lrlist[7][1] + str(int(lrlist[7][0]))
        other9 = lrlist[8][1] + str(int(lrlist[8][0]))
        other10 = lrlist[9][1] + str(int(lrlist[9][0]))
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
       if s!="clinic" and s!="tavern" and s!= "minfin" and s!="mainbank":
        butdisprice[2].active = 0
        butdisprice[3].active = 0
      elif infomod[0] == "price":
        butdisprice[2].active = 1
        butdisprice[3].active = 1
      if self.workallow == 0 and self.type != "minfin" and self.type != "mainbank":
        butdisprice[0].active = 0
        butdisprice[1].active = 0
        
        butdisprice[2].active = 0
        butdisprice[3].active = 0
      elif infomod[0] == "price":
        butdisprice[2].active = 1
        butdisprice[3].active = 1
      if infomod[0] == "price" and (self.type == "minfin" or self.type == "mainbank"):
        butdisprice[2].active = 1
        butdisprice[3].active = 1
        butdisprice[0].active = 1
        butdisprice[1].active = 1
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
      butdisstat[1].text = "Экспорт"
      butdisstat[11].text = str(sumlist(self.monthstat["export"]))
      
      butdisstat[21].text = str(self.allstat["export"])
      butdisstat[2].text = "местное потребл."
      butdisstat[12].text = str(sumlist(self.monthstat["this"]))
      butdisstat[22].text = str(self.allstat["this"])
      butdisstat[3].text = "Зарплата"
      butdisstat[13].text = str(sumlist(self.monthstat["salary"]))
      butdisstat[23].text = str(self.allstat["salary"])
      butdisstat[4].text = "Содержание"
      butdisstat[14].text = str(sumlist(self.monthstat["upkeep"]))
      butdisstat[24].text = str(self.allstat["upkeep"])
      butdisstat[5].text = "Баланс"
      butdisstat[15].text = str(sumlist(self.monthstat["balance"]))
      butdisstat[25].text = str(self.allstat["balance"])
      butdisstat[6].text = "Производство"
      butdisstat[16].text = str(sumlist(self.monthstat["prodused"]))
      butdisstat[26].text = str(self.allstat["prodused"])
      butdisstat[7].text = "готовая продукция"
      butdisstat[17].text = str(sumdic(self.outres))
      butdisstat[8].text = "На складе ресурсов"
      butdisstat[18].text = str(sumdic(self.inres))
      
      butdisstat[10].text = "за 12 мес."
      butdisstat[20].text = "за все время"
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
          
          
      if butdisprice[8].press() == 1:
        for i in buildings:
          if i.type == self.type:
            i.salary = self.salary
      if butdisprice[9].press() == 1:
        for i in buildings:
          if i.type == self.type:
            i.price = self.price
            if self.type != "minfin":
              i.prices = self.prices.copy()
      if butdisprice[2].press() == 1:
        self.price += interprice
        if self.type == "farm" or self.type == "rancho":
          for i in eat:
            self.prices[i]=self.price
      if butdisprice[3].press() == 1:
        self.price -= interprice
        if self.type == "farm" or self.type == "rancho":
          for i in eat:
            self.prices[i]=self.price
      if self.type == "minfin":
        minfins[0].part = self.salary
        minfins[0].part2 = self.price
      if self.type == "mainbank":
        if butdismode[0].press() == 1:
          self.subtype = "free"
          mainbanks[0].mode1 = "free"
        if butdismode[1].press() == 1:
          self.subtype = "support"
          mainbanks[0].mode1 = "support"
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
      if infomod[0] == "price" and self.type == "minfin":
        for i in butdisprice:
          i.active = 1
      if infomod[0] == "other":
       if self.type != "home":
        for i in self.workers:
         buttonshuman[i].x = w/3*2
         buttonshuman[i].y = h/3*2 + 30 + 20*j
         buttonshuman[i].active = 1
         j += 1
         
        
        
    def draw(self, xx, yy,mu):
      if self.notdestroyed == True:
        xhum = int((xx + 100 * self.x) * mu + (1 - mu) * (w / 2))
        yhum = int((yy + 100 * self.y) * mu + (1 - mu) * (h / 2))
        if self.active == 1:
          a = pygame.draw.rect(sc, self.color, (xhum+10*mu, yhum+ 10*mu, math.ceil((self.xx)*100*mu- 20*mu), math.ceil((self.yy)*100*mu-20*mu)))
        i = int(40*mu*self.xx)
        i = 10
        if i > 12:
            f1 = pygame.font.SysFont('arial', int(i))
            text1 = f1.render(self.text, True,
                      (180, 0, 0))
            sc.blit(text1, (xhum,yhum+ 40*mu*self.yy))
