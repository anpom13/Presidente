from human import *

class family(object):
  def __init__(self):
    self.type = None
    self.wife = None
    self.husbant = None
    self.children = []
    self.homenumber = -1
  def __add__(self, fam):
    res = family()
    if self.wife == None and self.husbant != None and fam.wife != None and fam.husbant == None:
      res.wife = fam.wife
      res.husbant = self.husbant
      res.children = self.children+fam.children
      res.type = "full"
      self.dehome(homes)
      fam.dehome(homes)
      res.wife.family = res
      res.husbant.family = res
      return res
    if self.wife != None and self.husbant == None and fam.wife == None and fam.husbant != None:
      res.wife = self.wife
      res.husbant = fam.husbant
      res.children = self.children+fam.children
      res.type = "full"
      self.dehome(homes)
      fam.dehome(homes)
      res.wife.family = res
      res.husbant.family = res
      return res
    return 0
  def dehome(self, homes):
    if self.homenumber >= 0:
      #homes[self.homenumber].number -= 1
      if self in homes[self.homenumber].families:
        homes[self.homenumber].families.remove(self)
        homes[self.homenumber].number = len(homes[self.homenumber].families)
        self.homenumber = -1
      else:
        print("Ошибка синхронизации жилищных паспортов. Полное восстановление базы не предусмотрено")
        
        homes[self.homenumber].number = len(homes[self.homenumber].families)
        self.homenumber = -1
        
        
        
    self.homenumber = -1
    
    if self.husbant != None:
          self.husbant.homenumber = -1
    if self.wife != None:
          self.wife.homenumber = -1
    for ch in self.children:
      ch.homenumber = -1
  def birth(self):
    chil = human()
    chil.age = 0
    chil.state = "child2"
    self.children.append(chil)
    childrens.append(chil)
    humans.append(chil)
  def findhome(self, buildings, homes):
      FPS = FPSl[0]
      #print("findhome")
      #print("fam", self.husbant, )
      if self.husbant != None:
        f = self.husbant.work_n
        hum = self.husbant
      else:
        f = self.wife.work_n
        hum = self.wife
      if f >= 0:
        xhum = buildings[f].x
        yhum = buildings[f].y
      else:
        xhum = hum.x
        yhum = hum.y
      
      priorl= []
      dist = xhum*xhum+yhum*yhum
      for i in homes:
        if len(i.families) < i.max_number:

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
        if self.husbant != None:
          self.husbant.homenumber = maxin
        if self.wife != None:
          self.wife.homenumber = maxin
        for ch in self.children:
          ch.homenumber = maxin
        #homes[maxin].number += 1
        homes[maxin].families.append(self)
        homes[self.homenumber].number = len(homes[self.homenumber].families)
        print(homes[maxin].families)
        print(len(homes[maxin].families))
        print("дом нашёл")
        
      else:
        maxi = maxi
        

def choseattackbui():
  for i in buildings:
    if i.type == "farm":
      return i
  return buildings[-2]
  

def beginconflict():
  bui = choseattackbui()
  print("началось восстание")
  activearmy.clear()
  activerebels.clear()
  for i in humans:
        if i.work_n != -1:
          if buildings[i.work_n].type == "army1":
            i.state = "armyconf1"
            print("солдат мобилизован")
            activearmy.add(i)
            i.attacbui = bui
            i.warstage = 0
  for i in rebels:
    i.state = "rebelconf1"
    i.attacbui = bui
    print("повстанец бунтует")
    activerebels.add(i)
    
    
def endconflict():
  activerebels.clear()
  activearmy.clear()
  for i in humans:
        if i.work_n != -1:
          if buildings[i.work_n].type == "army1":
            i.state = 2
            
  for i in rebels:
    i.state = "rebel"
  
mainfunc["beginconflict"]=beginconflict
mainfunc["endconflict"]=endconflict