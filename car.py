from building import *
import math
import pygame

gor = {"right", "left"}
ver = {"up", "down"}

def getfield(x,y, bui):
  dx = (x - bui.x)/bui.xx
  dy = (y - bui.y)/ bui.yy
  dislist = [dx, 1-dx, dy, 1-dy]
  for i in dislist:
    if i<-0.2:
      print("Предупреждение: векторное поле формирует неправильно")
  mi = min(dislist)
  if mi == dislist[0] or mi == dislist[1]:
    return "updown"
  if mi == dislist[2] or mi == dislist[3]:
    #return "leftright"
    return "leftright"
def dircross(c1,c2):
 if c1!=0 and c2!=0:
  if c1.direction in gor and c2.direction  in ver:
    return True
  if c1.direction in ver and c2.direction  in gor:
    return True
 return False

def pointdir(vertices, point):
    n = len(vertices)
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        x, y = point

        if x1 == x2 and y1 == y2:
            continue

        if x1 == x2:
            if min(y1, y2) <= y <= max(y1, y2) and x == x1:
                if y1 < y2:
                    return "up"
                else:
                    return "down"
        else:
            if min(x1, x2) <= x <= max(x1, x2) and y == y1:
                if x1 < x2:
                    return "right"
                else:
                    return "left"

    return 0


def adv(a,b):
  return (a[0]+b[0], a[1]+b[1])
def miv(a,b):
  return (a[0]-b[0], a[1]-b[1])
def muv(a,b):
  return(a[0]*b,a[1]*b)
def rov(a):
  return(math.sqrt(a[0]**2 + a[1]**2))
def norv(a): #нормированный вектор
  return muv(a, 1/(rov(a)))
def pperv(v): #нормированный правые перпендикуляр
  a = v[0]
  b = v[1]
  if a == 0 and b> 0:
    return (0.125,0)
  if a == 0 and b < 0:
    return (-0.125,0)
  if b == 0 and a > 0:
    return(0, -0.125)
  if b == 0 and a<0:
    return(0,0.125)
  return(0,0)
def gh(l):
  if len(l) == 0:
    return l
  if len(l) == 1:
    return l
  if len(l) == 2:
    x = l[0]
    y = l[1]
    v = miv(y,x)
    a = pperv(v)
    return (adv(x,a),adv(y,a))
  m = l.copy()
  for i in range (0, len(l)-1):
    a = miv(l[i+1], l[i])
    c = pperv(a)
    #print(c)
    #b = muv(norv(miv(l[i+1], l[i+2])), 0.25)
    #c = adv(a,b)
    m[i] = adv(m[i],c)
    m[i+1]= adv(m[i+1],c)
  return m
    

    
  


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
      noddd = nodes(acc,di,di2)
      #di = nodes(acc,di,di2)[0]
      #di2 = nodes(acc,di,di2)[1]
      di = noddd[0]
      di2 = noddd[1]
  else:
      di = di#nodes(acc,al,di)
  return (di,di2)
      
def nod21(a,z,rm,nodess):
  ac = {a}
  di = {}
  di2 = {}
  di3 = {}
  for i in range (0,n):
    for j in range (0,m):
      if alr((i,j),rm) == 1:
        di2[(i,j)] = []
  ss = nodess[1]
  if z in ss:
    return ss[z]
  else:
    return []

def nodesr(a,roadset):
  ac = {a}
  di = {}
  di2 = {}
  di3 = {}
  for i in roadset:
    
        di2[i] = []
  return nodes(ac,di,di2)

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

def nod31(a,z,l,nodess):
  if alr(a,rm) == 1 and alr(z,rm) == 1:
    if a == z:
      return(a,a)
    else:
      s = nod21(a,z,l,nodess)
      if len(s) > 0:
        return nods(a,z,s)
      else:
        return 0
  else:
    return 0

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
  mddd = g(l)
  d = mddd[0]      #g(l)[0]
  m = mddd[1]   #g(l)[1]
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
def graphsv2(a, nodess):
  #di2 = {}
  #a = {a}
  retu = set()
  #for i in roadset:#n
    
        #di2[i] = []
  ss = nodess[0]
  for i in ss:#n
    
        retu.add(i)
  return retu

class car(object):
    def __init__(self, xt = 800):
        self.x = 0.0
        self.y = 100.0
        self.max_speed = 35
        self.speed = 0.0
        self.max_acel = 0.06
        self.acel = 0.0
        self.bacel = 0.6
        self.xt = 8
        self.a = 0
        self.s = 1
        self.tren = self.max_acel/self.max_speed*700
        self.rx = 0
        self.ry = 0
        self.maxdist = 1
        self.mindistb= 0.2
        self.lrx = [0 for i in range (1)]
        self.lry = [0 for i in range (1)]
        self.active = 1
        cars.append(self)
        self.direction = "right"
        self.chank = (0,0)
        self.ch1 = None
        self.ch2 = None
        self.ch3 = None
        self.ch4 = None
    def getrc(self, l):
      return gg(l,self.x)
    def gas(self, s=100.0):
        FPS = FPSl[0]
        self.acel = float(self.max_acel * s)
        if self.speed + self.acel/FPS <= self.max_speed:
            self.speed += float(self.acel/FPS)*self.s
        else:
            self.speed = self.max_speed
        #print("gas"+str(self.x)+"------------")
    def brake(self, s = 100):
        FPS = FPSl[0]
        self.acel = -self.bacel*s
        if self.speed + self.acel/FPS > 0:
            self.speed += self.acel/FPS
            #self.s = 0
        else:
            self.speed = 0
    def disable(self):
      self.active = 0
    def life(self,l, xx, yy, mu):
        #print(l)
        self.direction = pointdir(l, (self.rx,self.ry))
        
        FPS = FPSl[0]
        a = self.speed/FPS
        #print("a =" + str(a))
        if self.x + a < self.xt:
          self.x += self.speed/FPS
        else:
          self.x = self.xt
        self.speed -= self.speed*self.tren/FPS
        #print("x = " + str(self.x))
        if self.xt - self.x > self.brake_way():
            #self.gas()
            #print("acel")
            #print(self.acel)
            gbv = 1
            gbv2 = 0
            ss = 100000
            roxi = gg(l,self.x + self.speed/ FPS)
            rrx = roxi[0]
            rry = roxi[1]
            dir2 = pointdir(l, (self.rx,self.ry))
            brakedi = self.brake_way()*2
            #print(self.direction)
            for i in semaphores:
              
              if self.direction == "up":
                if self.rx-i.x > -1 and self.rx-i.x < 1:
                   if i.y - self.ry < 2 and i.y - self.ry> -0.69:
                     i.cdic["up"].add(self)
              if self.direction == "down":
                 if self.rx-i.x > -1 and self.rx-i.x < 1:
                   if self.ry - i.y < 2 and self.ry - i.y> -0.69:
                     i.cdic["down"].add(self)
              
              if self.direction == "right":
                
                 if self.ry-i.y > -1 and self.ry-i.y < 1:
                   if i.x - self.rx < 2 and i.x - self.rx> -0.69:
                     i.cdic["right"].add(self)
              if self.direction == "left":
                
                 if self.ry-i.y > -1 and self.ry-i.y < 1:
                   if self.rx - i.x < 2 and self.rx - i.x>- 0.69:
                     i.cdic["left"].add(self)
                     
              if self.direction == "up":
                if i.direct["up"]==1:
                 if self.rx-i.x > -1 and self.rx-i.x < 1:
                   if i.y - self.ry < 0.7+brakedi and i.y - self.ry> 0.69:
                     gbv = 0
              if self.direction == "down":
                if i.direct["down"]==1:
                 if self.rx-i.x > -1 and self.rx-i.x < 1:
                   if self.ry - i.y < 0.7+brakedi and self.ry - i.y> 0.69:
                     gbv = 0
              if self.direction == "right":
                if i.direct["right"]==1:
                 if self.ry-i.y > -1 and self.ry-i.y < 1:
                   if i.x - self.rx < 0.7+brakedi and i.x - self.rx> 0.69:
                     gbv = 0
              if self.direction == "left":
                if i.direct["left"]==1:
                 if self.ry-i.y > -1 and self.ry-i.y < 1:
                   if self.rx - i.x < 0.7+brakedi and self.rx - i.x> 0.69:
                     gbv = 0
            chlist = carchanks[self.chank[0]][self.chank[1]]
            if self.ch1 != None:
              chlist = chlist + carchanks[self.ch1[0]][self.ch1[1]]
            if self.ch2 != None:
              chlist = chlist + carchanks[self.ch2[0]][self.ch2[1]]
            if self.ch3 != None:
              chlist = chlist + carchanks[self.ch3[0]][self.ch3[1]]
            if self.ch4 != None:
              chlist = chlist + carchanks[self.ch4[0]][self.ch4[1]]
            #for i in humans:
            for i in chlist:#carchanks[self.chank[0]][self.chank[1]]:
              
              if i.cars != 0 and len(i.list)>1 and i.cars != self:
                if self.direction == 0:
                  #self.gas()
                  gbv = gbv
                secp = self.brake_way(cmodul(self.speed - i.cars.speed))
                secp2 = self.brake_way()
                #if dircross(self, i.cars):
                if 1==0:
                  if cmodul(self.ry-i.cars.ry) > 1:
                    if self.direction == "right":
                       a1 = cmodul(i.cars.lry[0] - self.ry)
                       if  a1 >= 0.25 + self.brake_way() or cmodul( i.cars.ry -self.ry) >=0.25 + self.brake_way():
                        gbv = gbv
                        #print(000000000000000000000000000000000000)
                       else:
                        gbv = -1
                    if self.direction == "left":
                      
                       if cmodul(i.cars.lry[0] - self.ry) >= 0.25 +  self.brake_way() or cmodul( i.cars.ry -self.ry) >=0.25 + self.brake_way():
                        gbv = gbv
                        #print(000000000000000000000000000000000000)
                       else:
                        gbv = -1
                
                  
                if dir2 == "right" and i.cars.direction == "right":
                  if rry == i.cars.ry:
                    if i.cars.rx > self.rx:
                      a1 = i.cars.lrx[0] - rrx
                      a2 = i.cars.rx - rrx
                      if a1  >= 0.3 + secp2 or a2  >=0.4 + secp:
                        gbv = gbv
                        #if a1 < 0.7 + 2* secp or a2 < 1.2 + 2*secp:
                          #gbv = "halfbr"

                        #elif a1 < 0.7 + 7 *secp or a2 < 1.3 + 7*secp:
                          #gbv = "None"
                      else:
                        gbv = -1
                        
                if dir2 == "left" and i.cars.direction == "left":
                  if rry == i.cars.ry:
                    if i.cars.rx < self.rx:
                      a1 = i.cars.lrx[0] - rrx
                      a2 = i.cars.rx -rrx
                      if a1 <= -0.3 - secp2 or a2 <= -0.4- secp:
                        gbv = gbv
                        #if a1 > -0.7 - 2*secp or a2 > -1.2- 2*secp:
                          #gbv = "halfbr"
                        #elif a1 > -0.7 - 2*secp or a2 > -1.2- 2*secp:
                          #gbv = "None"

                      else:
                        gbv = -1

                if dir2 == "up" and i.cars.direction == "up":
                  if rrx == i.cars.rx:
                    if i.cars.ry > self.ry:
                      a1 = i.cars.lry[0] - rry
                      a2= i.cars.ry -rry
                      if  a1 >= 0.3 + secp2 or a2 >= 0.4 + secp:
                        gbv = gbv
                        #if a1 < 0.7 + 2*secp or a2 < 1.2 + 2*secp:
                          #gbv = "halfbr"
                          
                        #print(000000000000000000000000000000000000)
                      else:
                        gbv = -1
                if dir2 == "down" and i.cars.direction == "down":
                  if rrx == i.cars.rx:
                    if i.cars.ry < self.ry:
                      if i.cars.lry[0] - rry <= -0.3 - secp2 or i.cars.ry - rry <= -0.4 - secp:
                        gbv = gbv
                        #print(000000000000000000000000000000000000)
                      else:
                        gbv = -1
            if gbv == 1:
                  self.gas()
            elif gbv == 0:
                  self.brake()
            elif gbv == "halfbr":
              self.gas(15)
            elif gbv == -1:
              self.brake(130)
            
        else:
            self.brake()
            #print("brake")
            self.a = 100
        
        self.renderg(l, xx, yy, mu)
    def life2(self,l, xx, yy, mu):
        #print(l)
        self.direction = pointdir(l, (self.rx,self.ry))
        
        FPS = FPSl[0]
        a = self.speed/FPS
        #print("a =" + str(a))
        if self.x + a < self.xt:
          self.x += self.speed/FPS
        else:
          self.x = self.xt
        self.speed -= self.speed*self.tren/FPS
        #print("x = " + str(self.x))
        if self.xt - self.x > self.brake_way():
            #self.gas()
            #print("acel")
            #print(self.acel)
            gbv = 1
            gbv2 = 0
            ss = 100000
            mds = 100
            brakedi = self.brake_way()*2
            #print(self.direction)
            for i in semaphores:
              
              if self.direction == "up":
                if self.rx-i.x > -1 and self.rx-i.x < 1:
                   if i.y - self.ry < 2 and i.y - self.ry> -0.69:
                     i.cdic["up"].add(self)
              if self.direction == "down":
                 if self.rx-i.x > -1 and self.rx-i.x < 1:
                   if self.ry - i.y < 2 and self.ry - i.y> -0.69:
                     i.cdic["down"].add(self)
              
              if self.direction == "right":
                
                 if self.ry-i.y > -1 and self.ry-i.y < 1:
                   if i.x - self.rx < 2 and i.x - self.rx> -0.69:
                     i.cdic["right"].add(self)
              if self.direction == "left":
                
                 if self.ry-i.y > -1 and self.ry-i.y < 1:
                   if self.rx - i.x < 2 and self.rx - i.x>- 0.69:
                     i.cdic["left"].add(self)
                     
              if self.direction == "up":
                if i.direct["up"]==1:
                 if self.rx-i.x > -1 and self.rx-i.x < 1:
                   if i.y - self.ry < 0.7+brakedi and i.y - self.ry> 0.69:
                     gbv = 0
                     mds = 0.2 + brakedi
              if self.direction == "down":
                if i.direct["down"]==1:
                 if self.rx-i.x > -1 and self.rx-i.x < 1:
                   if self.ry - i.y < 0.7+brakedi and self.ry - i.y> 0.69:
                     gbv = 0
                     mds = 0.2 + brakedi
              if self.direction == "right":
                if i.direct["right"]==1:
                 if self.ry-i.y > -1 and self.ry-i.y < 1:
                   if i.x - self.rx < 0.7+brakedi and i.x - self.rx> 0.69:
                     gbv = 0
                     mds = 0.2 + brakedi
              if self.direction == "left":
                if i.direct["left"]==1:
                 if self.ry-i.y > -1 and self.ry-i.y < 1:
                   if self.rx - i.x < 0.7+brakedi and self.rx - i.x> 0.69:
                     gbv = 0
                     mds = 0.2 + brakedi
            chlist = carchanks[self.chank[0]][self.chank[1]]
            if self.ch1 != None:
              chlist = chlist + carchanks[self.ch1[0]][self.ch1[1]]
            if self.ch2 != None:
              chlist = chlist + carchanks[self.ch2[0]][self.ch2[1]]
            if self.ch3 != None:
              chlist = chlist + carchanks[self.ch3[0]][self.ch3[1]]
            if self.ch4 != None:
              chlist = chlist + carchanks[self.ch4[0]][self.ch4[1]]
            #for i in humans:
            #mds = 100
            sp = None
            roxi = gg(l,self.x + self.speed/ FPS)
            rrx = roxi[0]
            rry = roxi[1]
            dir2 = pointdir(l, (self.rx,self.ry))
            for i in chlist:#carchanks[self.chank[0]][self.chank[1]]:
              
              if i.cars != 0 and len(i.list)>1 and i.cars != self:
                if self.direction == 0:
                  #self.gas()
                  gbv = gbv
                secp = self.brake_way(cmodul(self.speed - i.cars.speed))
                secp2 = self.brake_way()
                #if dircross(self, i.cars):
                if 1==0:
                  if cmodul(self.ry-i.cars.ry) > 1:
                    if self.direction == "right":
                       a1 = cmodul(i.cars.lry[0] - self.ry)
                       if  a1 >= 0.25 + self.brake_way() or cmodul( i.cars.ry -self.ry) >=0.25 + self.brake_way():
                        gbv = gbv
                        #print(000000000000000000000000000000000000)
                       else:
                        gbv = -1
                    if self.direction == "left":
                      
                       if cmodul(i.cars.lry[0] - self.ry) >= 0.25 +  self.brake_way() or cmodul( i.cars.ry -self.ry) >=0.25 + self.brake_way():
                        gbv = gbv
                        #print(000000000000000000000000000000000000)
                       else:
                        gbv = -1
                
                
                if dir2 == "right" and i.cars.direction == "right":
                  if rry == i.cars.ry:
                    if i.cars.rx > self.rx:
                      a1 = i.cars.lrx[0] - rrx
                      a2 = i.cars.rx -rrx
                      ds = min(a1,a2)
                      if ds < mds:
                        mds = ds
                        sp = i.cars.speed
                      if a1  >= 0.3 + secp2 or a2  >=0.4 + secp:
                        gbv = gbv
                        #if a1 < 0.7 + 2* secp or a2 < 1.2 + 2*secp:
                          #gbv = "halfbr"
                          #print(000000000000000000000000000000000000)
                        #elif a1 < 0.7 + 7 *secp or a2 < 1.3 + 7*secp:
                          #gbv = "None"
                      else:
                        gbv = -1
                        
                if dir2 == "left" and i.cars.direction == "left":
                  if rry == i.cars.ry:
                    if i.cars.rx < self.rx:
                      a1 = i.cars.lrx[0] - rrx
                      a2 = i.cars.rx -rrx
                      ds = min(-a1,-a2)
                      if ds < mds:
                        mds = ds
                        sp = i.cars.speed
                      if a1 <= -0.3 - secp2 or a2 <= -0.4- secp:
                        gbv = gbv
                        #if a1 > -0.7 - 2*secp or a2 > -1.2- 2*secp:
                          #gbv = "halfbr"
                        #elif a1 > -0.7 - 2*secp or a2 > -1.2- 2*secp:
                          #gbv = "None"
                        #print(000000000000000000000000000000000000)
                      else:
                        gbv = -1
                        #print("popodiuhdjygdjygduygduygdjygdjydgjydgjydgjydg")
                if dir2 == "up" and i.cars.direction == "up":
                  if rrx == i.cars.rx:
                    if i.cars.ry > self.ry:
                      a1 = i.cars.lry[0] - rry
                      a2= i.cars.ry -rry
                      ds = min(a1,a2)
                      if ds < mds:
                        mds = ds
                        sp = i.cars.speed
                      if  a1 >= 0.3 + secp2 or a2 >= 0.4 + secp:
                        gbv = gbv
                        #if a1 < 0.7 + 2*secp or a2 < 1.2 + 2*secp:
                          #gbv = "halfbr"
                          
                        #print(000000000000000000000000000000000000)
                      else:
                        gbv = -1
                if dir2 == "down" and i.cars.direction == "down":
                  if rrx == i.cars.rx:
                    if i.cars.ry < self.ry:
                      ds = min( -i.cars.lry[0] + rry, -i.cars.ry +rry)
                      if ds < mds:
                        mds = ds
                        sp = i.cars.speed
                      if i.cars.lry[0] - rry <= -0.3 - secp2 or i.cars.ry -rry <= -0.4 - secp:
                        gbv = gbv
                        #print(000000000000000000000000000000000000)
                      else:
                        gbv = -1
            if gbv == 1:
                  self.gas(80)
            elif gbv == 0:
                  self.brake(90)
            elif gbv == "halfbr":
              self.gas(15)
            elif gbv == -1:
              self.brake(130)
            mds = 100
            roxi = gg(l,self.x + self.speed/ FPS)
            if sp != None:
              secp = self.brake_way(cmodul(self.speed - sp))
            else:
              secp = 0
            if mds > 1 + secp:
              mds = mds
            elif mds > 0.6 + secp:
              self.gas(60)
            elif mds > 0.5 + secp:
              self.brake(20)
            elif mds < 0.5 + secp:
              self.brake(100)
            elif mds < 0.4 + secp:
              self.brake(100)
            elif mds < 0.3 + secp:
              self.brake(250)
            elif mds < 0.25 + secp:
              self.speed = 0
        else:
            self.brake()
            #print("brake")
            self.a = 100
        
        self.renderg(l, xx, yy, mu)
    def brake_way(self, ss = 0):
        #print("speed")
        #print(self.speed)
        #print(self.speed*self.speed/2/self.bacel)
        return (self.speed-ss)*(self.speed-ss)/2/self.bacel/30
        
    def render(self,l, xx, yy, mu):
        xhum = (xx + 100 * self.rx) * mu + (1 - mu) * (w / 2)
        yhum = (yy + 100 * self.ry) * mu + (1 - mu) * (h / 2)
        s = (xhum + 50*mu,yhum + 50*mu)
        pygame.draw.circle(sc, ORANGE, s, 10*mu)
        #pygame.draw.circle(sc, ORANGE, (self.x*100, 200+self.a), 50)
    def renderg(self,l, xx, yy, mu):
      #s = gg(l,self.x)
      #print(type(s))
      #print(s)
      roxi = gg(l,self.x)
      #print(roxi)
      self.rx = roxi[0]#gg(l,self.x)[0]
      self.ry = roxi[1]#gg(l,self.x)[1]
      self.lrx = updlist(self.lrx, self.rx, 1)
      self.lry = updlist(self.lry, self.ry, 1)
      #xhum = (xx + 100 * self.rx) * mu + (1 - mu) * (w / 2)
      #yhum = (yy + 100 * self.ry) * mu + (1 - mu) * (h / 2)
      #s = (xhum + 50*mu,yhum + 50*mu)
      #pygame.draw.circle(sc, ORANGE, s, 10*mu)



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
    
def drw(a,b):
  dx = mo(a[0]-b[0])
  dy = mo(a[1]-b[1])
  return dx + dy
  
def fwalknodes(ac, di,di2): 
  acc = set()
  for i in ac:
    
    if i not in di:
      di[i] = 0
      di2[i] = []
    for b in walkroads[i]:
      x = drw(i,b)
      if b in di:
        if di[b] > di[i]+x:
          di[b] = di[i]+x
          acc.add(b)
          di2[b] = di2[i]+[b]
      else:
        di[b] = x + di[i]
        acc.add(b)
        x = di2[i]
        di2[b] = di2[i]+[b]
    
  if len(acc) > 0:
      #print(di)
      #print(acc)
      lvar = fwalknodes(acc,di,di2)
      #di = nodes(acc,di,di2)[0]
      #di2 = nodes(acc,di,di2)[1]
      di = lvar[0]
      di2 = lvar[1]
  else:
      di = di#nodes(acc,al,di)
  return (di,di2)

def fwalknodes_iter(ac, di, di2): 
    while len(ac) > 0:
        acc = set()
        for i in ac:
            if i not in di:
                di[i] = 0
                di2[i] = []
            for b in walkroads[i]:
                x = drw(i, b)
                if b in di:
                    if di[b] > di[i] + x:
                        di[b] = di[i] + x
                        acc.add(b)
                        di2[b] = di2[i] + [b]
                else:
                    di[b] = x + di[i]
                    acc.add(b)
                    di2[b] = di2[i] + [b]

        ac = acc

    return (di, di2)


def wnodesr(a,roadset):
  ac = {a}
  di = {}
  di2 = {}
  di3 = {}
  #for i in roadset:
    
        #di2[i] = []
  return fwalknodes_iter(ac,di,di2)
  
#walknodes = {(0,0), (1,1), (0,1), (1,0), (5,5)}
#wnodesv((0,0), (1,1))
#wnodesv((0,1), (1,1))
#wnodesv((0,1), (1,0))
#wnodesv((0,1), (5,5))

#print(nodesr((0,0), walkroads))

