from buttons import *

class semaphore(object):
  def __init__(self, x, y, type, subtype = None):
    
    self.x = x
    self.y = y
    self.time = 0
    self.maxtime = 2
    self.state = 0
    self.gostop = "go"
    self.cdic = {
      "left":set(),
      "right":set(),
      "up":set(),
      "down":set()
    }
    self.switchint = 100
    self.aldirect = {
      "up":1,
      "down":1,
      "right":1,
      "left":1
    }
    self.ldir = {
      "up":0,
      "down":0,
      "right":0,
      "left":0
    }
    self.direct = {}
    self.directl = []
    self.didir = {}
    self.subtype = subtype
    self.type = type
    self.settype(type)
  def settype(self, type):
    if type == "quad":
      self.aldirect = {
        "up":1,
        "down":1,
        "right":1,
        "left":1
      }
      self.direct = {
        "up":1,
        "down":1,
        "right":0,
        "left":0
      }
    if type == "triple":
      self.aldirect[self.subtype]= 0
      
    for i in self.aldirect:
        if self.aldirect[i] == 1:
          self.direct[i]= 1
          self.directl.append(i)
    self.state = self.directl[0]
    if type == "triple":
      for i in range(0,3):
        if i !=2:
          self.didir[self.directl[i]]= self.directl[i+1]
          print( "для, ", self.directl[i], "назначено ", self.didir[self.directl[i]])
        else:
          self.didir[self.directl[2]]= self.directl[0]
    if type == "quad":
      for i in range(0,4):
        if i !=3:
          self.didir[self.directl[i]]= self.directl[i+1]
          print( "для, ", self.directl[i], "назначено ", self.didir[self.directl[i]])
        else:
          self.didir[self.directl[3]]= self.directl[0]
          print( "для, ", self.directl[3], "назначено ", self.didir[self.directl[0]])
      self.didir = {'up': 'down', 'down': 'right', 'right': 'left', 'left': 'up'}
    self.direct[self.state]= 0
    print("semaphore", self.type)
    print(self.didir)
  def stop(self):
    for i in self.direct:
        self.direct[i]= 1
    self.gostop = "stop"
  def switchto(self, dir):
    for i in self.direct:
        self.direct[i]= 1
    self.direct[dir] = 0
    self.gostop = "go"
    self.state = dir
  def switch(self):
    if self.type == "triple" or self.type == "quad":
      self.state = self.didir[self.state]
      for i in self.direct:
        self.direct[i]=1
      self.direct[self.state]= 0
    if self.type == "quad" and 1 == 0:
      for i in self.direct:
        if self.direct[i]== 0:
          self.direct[i] = 1
        else:
          self.direct[i] = 0
  def life(self, FPS):
   
    self.time += 1/FPS
    #self.state = self.didir[self.state]
    lis = [len(self.cdic["right"]),len(self.cdic["left"]),len(self.cdic["down"]),len(self.cdic["up"])]
    if self.time >= 0.5 and self.gostop == "stop":
      self.state = self.didir[self.state]
      self.switchto(self.state)
      self.time = 0
    if self.time >= len(self.cdic[self.state])*3 and self.gostop == "go":
      if len(self.cdic[self.state]) == 0:
        self.state = self.didir[self.state]
        self.switchto(self.state)
        self.time = 0
      else:
        self.stop()
        self.time = 0
    if 1 == 1: #не рекомендую
     ma = max(lis)
     if len(self.cdic["right"]) == ma:
      self.switchto("right")
     if len(self.cdic["left"]) == ma:
      self.switchto("left")
     if len(self.cdic["up"]) == ma:
      self.switchto("up")
     if len(self.cdic["down"]) == ma:
      self.switchto("down")
    #if self.time >= self.maxtime:
      #self.switch()
      #self.time = 0
      
#a = tra(1,2,"triple", "up")

