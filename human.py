import math
import pygame


from humanfunc import *

#from mlists import *
import random


class human(object):

    def __init__(self, a=0, b=0, id = 0):
        """Constructor"""
        self.life = 1

        self.maintype = "human"
        
        self.warstage = 0
        self.id = id
        self.hp = 60
        self.p1 = 0
        self.p2 = 0
        self.p3 = 0
        self.p4 = 0
        self.wwalk = 0
        self.swalk = 0
        self.wwt = 0
        self.education = 0
        self.edupoint = 0
        self.realwork = "base"
        
        self.skills = {
          "clerk":0,
          "farming":0,
          "industrial":0
        }

        dictfrac = {
            1:"capitalists",
            2: "communists",
            3:"intellectuals",
            4:"militarists",
            5:"beauty",
            6:"nationalists",
            7:"loyalists"
        }
        numfrac = random.randint(1,3)

        self.kfrac = {}

        for i in range(numfrac):
            lfr = dictfrac[random.randint(1,7)]
            self.kfrac[lfr] = random.randint(1,3)

        print(self.kfrac)






        self.student = False
        self.gotocw_check_stage_car3 = False
        
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
        
        self.wotworkt = random.uniform(3, 10)
        
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
        
        self.dismod = 0
        
        self.teat = ""

        self.hap_eat = 10#8
        self.hap_health = 10
        self.hap_fun = 10
        self.rest = 10
        self.money = 90
        self.pprice = 0
        
        self.hap_eat2 = random.uniform(3, 10)
        self.hap_health2 = random.uniform(3, 10)
        self.hap_fun2 = random.uniform(3, 10)
        self.rest2 = random.uniform(3, 10)
        if gameparametrs["religion"] == True:
            self.hap_reg2 = random.uniform(3, 10)
        
        
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
        self.target = 1.5

        self.work_n = -1
        self.list = []
        self.keats = {}
        for i in eat:
          self.keats[i] = random.uniform(0.3, 2.0)
        #self.keats["corn"] = 0.1
        #self.keats["cheese"] = 5
        #self.keats["meat"] = 10
        self.cash = 0
        self.kcash = 0.01 #написать функцию, которая зависит от счастья. Когда появляются банки, может быть < 0
        self.homenumber = -1 #поиск дома -- составляем рейтинг по всем домам исходя из ренты и расположения, выбираем лучший
        self.salary = 0
        #self.target = 0 #building(type = "none")

        self.worktime = 0
        self.maxinre = 1000
        self.wt = 0
        self.name = names[random.randint(0,14)] + " " + surnames[random.randint(0,14)]
        #self.homenumber = -1
        self.phap = {
          "food":[50],#список из 12 попыток поесть
          "job":[50],
          "home":[50], #список из 12 последних замеров качества жилья
          "freedom":[50],
          "beauty":[50],
          "freedom":[50],#свобода около дома и работы
        "fun":[50],#доступность развлечений * качество
        "job":[50],#качество работы * коэф частоты смены работы#хрень. Сколько он может купить на зарплату, нормированно и сколько может потратить за границей 
        "health":[50],#качество медицины * доступность
        "respect":[50],
        "main":[50],
        "safety":[50]
          
        }

        self.happiness = { 
        "food":50, #доступность еды умножитьна нормированный к разнообразия
        "safety":50,
        "home":50,#=качество жилья
        "beauty":50,#красота около дома и работы
        "freedom":50,#свобода около дома и работы
        "fun":50,#доступность развлечений * качество
        "job":50,#качество работы * коэф частоты смены работы#хрень. Сколько он может купить на зарплату, нормированно и сколько может потратить за границей 
        "health":50,#качество медицины * доступность
        "respect":50,
        "main":50
        }

        self.khappiness = {
            "food": random.randint(0,10),  # доступность еды умножитьна нормированный к разнообразия
            "safety": random.randint(0,10),
            "home": random.randint(0,10),  # =качество жилья
            "beauty": random.randint(0,10),  # красота около дома и работы
            "freedom": random.randint(0,10),  # свобода около дома и работы
            "fun": random.randint(0,10),  # доступность развлечений * качество
            "job": random.randint(0,10),
            # качество работы * коэф частоты смены работы#хрень. Сколько он может купить на зарплату, нормированно и сколько может потратить за границей
            "health": random.randint(0,10),  # качество медицины * доступность
            "respect": random.randint(0,10)
        }

        if gameparametrs["religion"] == True:
            self.phap["religion"] = [50]
            self.happiness["religion"] = 50
            self.khappiness["religion"] = random.randint(0,10)

        self.lres = {
          "food":100,
          "health":500,
          "age":75
        }
        
        self.allinfo = ""
    
        #self.homenumber = -1
        
        self.allinfo = ""
        sdic = {0:"male", 1:"female"}
        self.sex = sdic[random.randint(0,1)]
        self.movedic = {}
    def sethap(self, buildings, lays):
      
      hhbeauty = 50
      hwbeauty = 50
      cnt = 0
      sumf = 0
      sumb = 0
      
      
      
      if self.homenumber == -1:
        self.phap["home"] = updlist(self.phap["home"],10,1)
      else:
        ho = homes[self.homenumber]
        self.phap["home"] = updlist(self.phap["home"], homes[self.homenumber].quality,1)
        for i in range(ho.x -2,ho.x+3):
          for j in range(ho.y-2,ho.y+3):
            if al((i,j),rm ) == 1:
              cnt += 1
              sumb += lays["beauty"][i][j]/255*100
              sumf += lays["freedom"][i][j]/255*100
      if cnt > 0:
        medb1 = sumb/cnt
        medf1 = sumf/cnt
      else:
        medb1, medf1 = 50,50
      cnt = 0
      sumf = 0
      sumb = 0
      if self.work_n == -1:
        self.phap["job"] = updlist(self.phap["job"],0,1)#доделать
        
      else:
        wo = buildings[self.work_n] 
        #self.phap["job"] = updlist(self.phap["job"],wo.salary,1)
        
        jobh = 0
        jhe = 0
        if allmrot["eat"][-1] != "None":
          if allmrot["eat"][-1] > 0:
            jhe = wo.salary/allmrot["eat"][-1]/2
          else:
            jhe = 1
        else:
          jhe = 0
          
        jhf = 0
        if allmrot["fun"][-1] != "None":
          if allmrot["fun"][-1] > 0:
            jhf = wo.salary/allmrot["fun"][-1]/2
          else:
            jhf = 1
        else:
          jhf = 0
        
        jhh = 0
        if allmrot["home"][-1] != "None":
          if allmrot["home"][-1] > 0:
            jhh = wo.salary/allmrot["home"][-1]
          else:
            jhh = 1
        else:
          jhh = 0
        
        jhho = 0
        if allmrot["health"][-1] != "None":
          if allmrot["health"][-1] > 0:
            jhho = wo.salary/allmrot["health"][-1]
          else:
            jhho = 1
        else:
          jhho = 0
        jhd = 0
        if allmrot["dollar"][-1] != "None":
          if allmrot["dollar"][-1] > 0:
            jhd = wo.salary/allmrot["dollar"][-1]
          else:
            jhd = 1
        else:
          jhd = 0
        #print(allmrot)
        #print(jhe)
        #print(jhho)
        #print(jhf)
        #print(jhh)
        #print(jhd)
        jhe = min(1.7, math.sqrt(jhe))
        
        jhho = min(1, math.sqrt(jhho))
        #print(jhho)
        jhf = min(2, math.sqrt(jhf))
        
        jhh = min(1.2, math.sqrt(jhh))
        
        jhd = min(3, math.sqrt(jhd))
        
        jobh = min(min(0.3*jhe + 0.2 * jhh + 0.15 * jhf +0.2*jhh + 0.1*jhd, 1.3)*100*wo.workqmodifer,100)
        
        #print(jobh)
        
        if jobh>100:
          jobh = 100
        #jobh = max(100, jobh)
        
        updlist(self.phap["job"],jobh,1)
        #print(self.phap["job"])
        for i in range(wo.x -2,wo.x+3):
          for j in range(wo.y-2,wo.y+3):
            if al((i,j),rm ) == 1:
              cnt += 1
              sumb += lays["beauty"][i][j]/255*100
              sumf += lays["freedom"][i][j]/255*100
      if cnt > 0:
        medb2 = sumb/cnt
        medf2 = sumf/cnt
      else:
        medb2, medf2 = 50,50
      self.phap["freedom"] = updlist(self.phap["freedom"],(medf1+medf2)/2,1)
      self.phap["beauty"] = updlist(self.phap["beauty"],(medb1+medb2)/2,1)
      self.happiness["freedom"] = medlist(self.phap["freedom"])
      self.happiness["beauty"] = math.sqrt(medlist(self.phap["beauty"])/25)*50
      self.happiness["job"] = medlist(self.phap["job"])
      self.happiness["home"] = medlist(self.phap["home"])
      self.happiness["fun"] = medlist(self.phap["fun"])
      self.happiness["health"] = medlist(self.phap["health"])
      self.happiness["food"] = medlist(self.phap["food"])


      lsum = 0
      ld = 0

      for i in self.kfrac:
          ld += self.kfrac[i]
          lsum += politrespect[i][-1] * self.kfrac[i]


      resp = int(lsum/ld)
      if gamevalues["last_tax_reduction"] + 36 > monthl[0]:
          resp = min(100, resp+20)
          #print("Снижение налогов дейчствует")
      #else:
          #print('Cнижение налогов НЕ действует')
      self.happiness["respect"] = resp


      llsum = 0
      llk = 0
      for i in self.khappiness:
          llk += self.khappiness[i]
          llsum += self.khappiness[i] * self.happiness[i]

      self.happiness["main"] = int(llsum / llk)
        
        
        
      
      
    def tupd(self, stri):
      stri = str(stri)
      self.thinfo1 = self.thinfo2
      self.thinfo2 = self.thinfo3
      self.thinfo3 = self.thinfo4
      self.thinfo4 = self.thinfo5
      self.thinfo5 = stri
    def infodis(self, buildings):
      self.dismod = 1
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
      if self.state in stdi:
        resourses = "статус: "+ stdi[self.state] + res2
      else:
        resourses = ""
      age = "возраст: " + str(self.age)
      
      name = self.name
      workers = "деньги:              " + str(int(self.money))
      sal = "зарплата на момент найма: " + str(int(self.salary))
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
      #for i in butdisprice:
        #i.text = ""
      for i in butdisinfo:
        i.text = ""
      for i in butdismode:
        i.text = ""
      for i in butdisother:
        i.text = ""
      for i in butdisstat:
        i.text = ""
      
      
      setbtext()
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
      butdisstat[4].text = "работа: " + str(int(self.wotworkt))
      butdisstat[5].text = "кработа: " + str(int(self.happiness["job"]))
      butdisstat[6].text = "коасота: " + str(int(self.happiness["beauty"]))
      butdisstat[7].text = "кдом: " + str(int(self.happiness["home"]))
      butdisstat[8].text = "кfreedom: " + str(int(self.happiness["freedom"]))
      butdisstat[9].text = "notset: " + str(int(self.happiness["job"]))
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
      FPS = FPSl[0]
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
    
    def gostraight(self, gxt, gyt):
      return human_func_gostraight(self, gxt, gyt)
      #идет прямо до определенной точки, а когда доходит, возвращает True
    def gobylist(self, list):
      return human_func_gobylist(self, list)
    def goto(self, gxt,gyt,gst, tuse = "main"):
     #gxt = list(lxt)
     #gyt = list(lyt)
     human_func_goto(self, gxt,gyt,gst, tuse = "main")
    def gowalk(self):
      FPS = FPSl[0]
      if self.state == 0:  # идёт
        self.goto(self.xt,self.yt,0)
        if self.x == self.xt and self.y == self.yt:
          self.state = 1
    def gotocw2(self, gxt,gyt, garages, xx, yy, mu):
        FPS = FPSl[0]
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
          self.cars.life(self.list, xx, yy, mu)
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
    
    def findgarage(self, set = set()):
      gd = 10000000
      gar = None
      garlist = []
      for i in range (0,len(garages)):
           if i not in set:
                dx = self.x - garages[i].x
                dy = self.y - garages[i].y
                ds = math.sqrt(dx * dx + dy * dy)
                garlist.append((ds, garages[i], garages[i].n_visitors))
      garlist.sort()
      print(garlist)
      return garlist
    def garmin(self):
      if self.gar != None:
        if self in self.gar.visitors:
          self.gar.n_visitors -= 1
          self.gar.visitors.discard(self)
    def garplus(self):
      if self.gar != None:
        self.gar.n_visitors += 1
        self.gar.visitors.add(self)
    def gotocw(self, gxt,gyt, garages, xx, yy, mu):
        FPS = FPSl[0]
        self.wg = 1
        if self.car == 0: # переделать модуль. сначала ищем ближайший гараж, затем ищем ближайшую дорогу среди тех (!)которые связаны с гаражом!!!
          #print("sc0")
          self.gi = -1
          gd = 10000000
          self.gar = None
          
          lcor = (int(self.x), int(self.y))
          if lcor not in garagedic:
            fg = self.findgarage()
            if fg != None:
              garagedic[lcor] = fg
          if lcor in garagedic:
            lcor = lcor
            garlist = garagedic[lcor]
            for j in garlist:
              i = j[1]
              if i.max_visitors > len(i.visitors):
                self.gar = i #garagedic[lcor][1]
                dx = self.x - self.gar.x
                dy = self.y - self.gar.y
                gd = math.sqrt(dx * dx + dy * dy)
                break
            
            #print("гараж нашелся сам")
            
            
            
          #else:
            #print("поиск гаража")
            #for i in range (0,len(garages)):
                #dx = self.x - garages[i].x
                #dy = self.y - garages[i].y
                #ds = math.sqrt(dx * dx + dy * dy)
                #if ds <= gd:
                  #self.gi = i
                  #self.gar = garages[i]
                  #garagedic[lcor] = self.gar
                  #gd = ds
          lmds1 = 10000
          lmds2 = 10000
          lmet1 = None
          lmet2 = None
          for met in metrolist:
            dx = met.x - self.x
            dy = met.y - self.y
            metrods = math.sqrt(dx*dx+dy*dy)
            if metrods < lmds1:
              lmds1 = metrods
              lmet1 = met
          for met in metrolist:
            dx = met.x - self.target.x
            dy = met.y - self.target.y
            metrods = math.sqrt(dx*dx+dy*dy)
            if metrods < lmds2 and lmds2 != lmds1:
              lmds2 = metrods
              lmet2 = met
          if self.gar != None:
            if self.target not in self.gar.rlists:
              ggi = self.gar
              ggg = self.gar.genlist(self.target,ggi.nodest, ggi.svset)
              print(ggg)
              #print("генерация пути")
            self.car = self.car
            #self.gar.n_visitors += 1
            
            self.mi = self.gar.rm[self.target][0]
            self.mj = self.gar.rm[self.target][1]
            dx = self.target.x - self.mi
            dy = self.target.y- self.mj
            md = math.sqrt(dx * dx + dy * dy)
          dx = self.x - self.target.x
          dy = self.y - self.target.y
          ds = math.sqrt(dx * dx + dy * dy)
          par1 = ds
          if self.gar != None:
            par2 = gd + md + self.gar.rd[self.target]/8
          else:
            par2 = 10000
          if lmet1!=None and lmet2!=None:
            par3 = lmds1+lmds2 +1
          else:
            par3 = 10000
          priorlist = [par1,par2,par3]
          lmin = min(priorlist)
          minprl = priorlist.index(lmin)
          #if self.gar != None and gd + md + self.gar.rd[self.target]/8< ds:
          if minprl == 1:
              self.gar.visitors.add(self)
              self.car = 1
          elif minprl == 0:
              self.car = 7
          elif minprl == 2:
              self.car = 1303
              self.undeground1 = lmet1
              self.undeground2 = lmet2
              self.ungrotime = 0
        if self.car == 1303:
          self.goto(self.undeground1.x,self.undeground1.y,1313)
        if self.car == 1313:
          FPS = FPSl[0]
          self.ungrotime += 1/FPS
          if self.ungrotime > 5:
            self.x = self.undeground2.x
            self.y = self.undeground2.y
            self.car = 7
        if self.car == 1:
          if self.gar != None:
            self.goto(self.gar.x,self.gar.y,3)
          else:
            self.car = 7
            
            #print("gi")
            #print(self.gi)
           
            #print("sc1")
            #print(self.car)
        if self.car == 3:
             #self.goto(self.mi,self.mj,5)
           self.gotocw_check_stage_car3 = True
           if self.gar.resolve == True:
             self.gar.visitors.discard(self)
             self.gar.resolve = False
             a = (self.gar.xt,self.gar.yt)
             b = (self.mi,self.mj)
             if self.target not in self.gar.rlists:
              ggi = self.gar
              ggi.genlist(self.target,ggi.nodest, ggi.svset)
             self.list = self.gar.rlists[self.target]
             self.gotocw_garage_object = self.gar
             #print("list = ")
             #print(self.list)
             self.car = 4
             self.cars = car()
             #print(g(self.list))
             self.cars.xt = self.gar.rd[self.target]
             #print("sc3")
             #print("mi")
             #print(self.mi)
             #print(self.car)
             self._resolve_gar_parametr = False
        if self.car == 4:
          
          #self.cars.life(self.list)
          ca = self.cars
          self.cars.life(self.list, xx, yy, mu)
          #self.cars.x += 60/FPS
          #print(self.list)
          #print("ready")
          #print("sc4")
          
          
          if self.gotocw_check_stage_car3 == True:
           if self.cars.x > 3 and self._resolve_gar_parametr == False:
            
            self.gotocw_garage_object.resolve = True
            self.gotocw_garage_object.n_visitors -= 1
            #self.gar.resolve = True
            self._resolve_gar_parametr = True
            self.garmin()
          if self.cars.x >= self.cars.xt:
            self.x = self.mi
            self.y = self.mj
            self.car = 0
            self.cars = 0
            if self.gotocw_check_stage_car3 == True:
             if self._resolve_gar_parametr == False:
              #self.gar.resolve = True
              self._resolve_gar_parametr = True
              self.gotocw_garage_object.resolve = True
              self.gotocw_garage_object.n_visitors -= 1
              self.garmin()
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
          self.x = gxt
          self.y = gyt
          self.state = 1
          self.car = 0
          self.gotocw_check_stage_car3 = False
        
          
    def go(self, garages, xx, yy, mu):
      #if self.target == 0 and len(buildings) > 0:
          #self.target = buildings[0]
      #print(self.type_target)
      if self.type_target == 3:
        self.target = buildings[self.work_n]
      FPS = FPSl[0]
      if self.state == 0:  # идёт
        self.gotocw(self.target.x,self.target.y, garages, xx, yy, mu)
        if self.car == 8:
          self.state = 1
          self.car = 0
          #print("walk")
    def fire(self):
      if self.work_n != -1:
        f = buildings[self.work_n]
        if self.id in f.workers:
          f.workers.remove(self.id)
          f.nwork -= 1
        self.work_n = -1
    def becomerebel(self):
        self.fire()
        self.state = "rebel"
        rebels.append(self)
    
    def findhome(self, buildings, homes):
      self.family.findhome(buildings, homes)
        #print(homes)
        #print("домов нет")
        #homes.append(home(random.randint(-10,10), random.randint(-10,10),2,1, random.randint(0,255)))
    #def findwork(self):
      #print("findwork")
    def findworknoedu(self, buildings, homes):
        FPS = FPSl[0]
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
            if wp.workallow == 1 and wp.maxnwork > wp.nwork and wp.workedu <= self.education:
                dx = (xhum - wp.x) ** 2
                dy = (yhum - wp.x) ** 2
                dist = math.sqrt(dx + dy)
                pd = (1000 - dist) / 100
                pw = 1 - (wp.nwork / wp.maxnwork)
                priorl.append((pd + wp.salary + wp.salary) * pw)

            else:
                priorl.append(-100000000)
                # print(wp.work_allow)
        if len(priorl) == 0:
            priorl = [-100000000]
        maxi = max(priorl)
        maxin = priorl.index(maxi)
        if maxi != -100000000:
            # print(priorl)
            self.work_n = maxin
            self.salary = buildings[maxin].salary
            buildings[maxin].nwork += 1
            buildings[maxin].workers.append(self.id)
            self.state = 2

    def fs(self, buildings, homes):
        FPS = FPSl[0]
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
            if wp.edu_allow == 1 and wp.maxnstud > wp.nstud and wp.type == "school":
                dx = (xhum - wp.x) ** 2
                dy = (yhum - wp.x) ** 2
                dist = math.sqrt(dx + dy)
                pd = (1000 - dist) / 100
                pw = 1 - (wp.nstud / wp.maxnstud)
                priorl.append(pd * pw)
            else:
                priorl.append(-100000000)

        if len(priorl) == 0:
            priorl = [-100000000]

        maxi = max(priorl)
        maxin = priorl.index(maxi)
        self.work_n = maxin
        # self.salary = buildings[maxin].salary
        buildings[maxin].nstud += 1
        buildings[maxin].students.append(self.id)
        self.state = 2
        self.realwork = "stud"
        self.student = True
        print("шавел школу")

    def findwork(self, buildings, homes):
        FPS = FPSl[0]




        if self.work_n >= 0 and self.realwork == "base":
            buildings[self.work_n].nwork -= 1

            if self.id in buildings[self.work_n].workers:
                buildings[self.work_n].workers.remove(self.id)
            else:
                print("Ошибка синхронизации списков рабочих, восстановление")
                self.work_n = -1
                for i in buildings:
                    i.workers.clear()
                for i in humans:

                    if i.work_n != -1:
                        #print("this is works")
                        buildings[i.work_n].workers.append(i.id)
                        buildings[i.work_n].nwork = len(buildings[i.work_n].workers)



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
            wp.nwork = len(wp.workers)
            if wp.workallow == 1 and wp.maxnwork > wp.nwork:
                dx = (xhum - wp.x) ** 2
                dy = (yhum - wp.x) ** 2
                dist = math.sqrt(dx + dy)
                pd = (1000 - dist) / 100
                pw = 1 - (wp.nwork / wp.maxnwork)
                priorl.append((pd + wp.salary + wp.salary) * pw)

            else:
                priorl.append(-100000000)
                # print(wp.work_allow)
        if len(priorl) == 0:
            priorl = [-100000000]

        maxi = max(priorl)
        maxin = priorl.index(maxi)
        priorl = []
        for wp in l:
            if wp.workallow == 1 and wp.maxnwork > wp.nwork and wp.workedu <= self.education:
                dx = (xhum - wp.x) ** 2
                dy = (yhum - wp.x) ** 2
                dist = math.sqrt(dx + dy)
                pd = (1000 - dist) / 100
                pw = 1 - (wp.nwork / wp.maxnwork)
                priorl.append((pd + wp.salary + wp.salary) * pw)

            else:
                priorl.append(-100000000)
                # print(wp.work_allow)
        if len(priorl) == 0:
            priorl = [-100000000]

        max1 = max(priorl)
        maxin2 = priorl.index(max1)

        if maxi != -100000000:
            if buildings[maxin].workedu <= self.education:
                # print(priorl)
                self.work_n = maxin
                self.salary = buildings[maxin].salary
                buildings[maxin].nwork += 1
                buildings[maxin].workers.append(self.id)
                buildings[maxin].nwork = len(buildings[maxin].workers)
                self.state = 2
                self.realwork = "base"
                self.tupd("1")
            else:
                scnt = 0
                for i in buildings:
                    if i.edu_allow == 1:
                        v = i.maxnstud - i.nstud
                        scnt += v
                if scnt == 0:
                    self.findworknoedu(buildings, homes)
                else:
                    self.fs(buildings, homes)
                    print("school")

    def findshchool(self, buildings, homes):
        FPS = FPSl[0]
        if self.work_n >= 0 and self.realwork == "base":
            buildings[self.work_n].nwork -= 1
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
            if wp.edu_allow == 1 and wp.maxnstud > wp.nstud and wp.type == "school":
                dx = (xhum - wp.x) ** 2
                dy = (yhum - wp.x) ** 2
                dist = math.sqrt(dx + dy)
                pd = (1000 - dist) / 100
                pw = 1 - (wp.stud / wp.maxnstud)
                priorl.append(pd * pw)
            else:
                priorl.append(-100000000)

        if len(priorl) == 0:
            priorl = [-100000000]

        maxi = max(priorl)
        maxin = priorl.index(maxi)
        self.work_n = maxin
        # self.salary = buildings[maxin].salary
        buildings[maxin].nstud += 1
        buildings[maxin].students.append(self.id)
        self.state = 0
        self.realwork = "stud"
        print("шавел школу")
        print(buildings[maxin].students)

    def findwork2(self, buildings):
      FPS = FPSl[0]
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
    def getskill(self, skill):
      if skill not in self.skills:
            self.skills[skill] = 0
      return self.skills[skill]
    def incskill(self, skill):
      if skill not in self.skills:
            self.skills[skill] = 0
      self.skills[skill] += 0.3
      if self.skills[skill] > 10:
               self.skills[skill] = 10
    def workpolice(self, buildings):
      FPS = FPSl[0]
      f = buildings[self.work_n]
      f.range = 0
      f.freedompow = 0
      for i in f.workers:
        f.freedompow += (2+(humans[i].getskill("police")/2))*15
        f.range += 6 + humans[i].getskill("police")/3
      f.range = int(f.range)
      #f.laymap.circlefill(f.freedompow, f.range)
      f.laymap.circlefill(f.freedompow,25,full = True)
      #f.laymap.fullfill(70, 2)
      f.laymap.updatelay("safe")
      self.incskill("liberty")
      self.state = 2
    def workgazeta(self, buildings):
      FPS = FPSl[0]
      f = buildings[self.work_n]
      f.range = 0
      f.freedompow = 0
      for i in f.workers:
        f.freedompow += (2+(humans[i].getskill("liberty")/2))*15
        f.range += 6 + humans[i].getskill("liberty")/3
      f.range = int(f.range)
      #f.laymap.circlefill(f.freedompow, f.range)
      f.laymap.circlefill(f.freedompow,25,full = True)
      #f.laymap.fullfill(70, 2)
      f.laymap.updatelay()
      self.incskill("liberty")
      self.state = 2
      
    def worklogg(self, buildings, xx, yy, mu):
      FPS = FPSl[0]
      f = buildings[self.work_n]
      if self.wstage == 0:
        f = buildings[self.work_n]
        self.wtree = 0
        #ищем дерево
        lv1 = max(0, f.x-10)
        lv2 = min(f.x+11, len(rm))
        lv3 = max(0, f.y-10)
        lv4 = min(f.y+11, len(rm[0]))
        lvmin = 100000
        lvtree = None
        for i in range(lv1, lv2):
          for j in range(lv3, lv4):
            if (i,j) in trees:
             for tr in trees[(i,j)]:
              if tr.startlog == 0:
                dx = tr.x - self.x
                dy = tr.y - self.y
                ds = dx*dx + dy*dy
                if ds < lvmin:
                  lvmin = ds
                  lvtree = tr
                  mi = i
                  mj = j
        if lvtree != None:
          self.wtree = lvtree
          lvtree.startlog = 1
          self.wstage = 1
          self.treex = mi
          self.treey = mj
        else:
          self.wtree = 0
          self.wstage = 100
      if self.wstage == 1:
        wj = self.wtree
        #print("st1")
        self.gotocw2(wj.x,wj.y, garages, xx, yy, mu)
        if self.car == 8:
          self.wstage = 10
          self.car = 0
          self.wg = 0
      if self.wstage == 10:
        self.wtree.hp -= 5/FPS
        if self.wtree.hp < 0:
          self.wstage = 20
          trees[(self.treex,self.treey)].remove(self.wtree)
      if self.wstage == 20:
        wj = f
        #print("st1")
        self.gotocw2(wj.x,wj.y, garages, xx, yy, mu)
        if self.car == 8:
          self.wstage = 100
          self.car = 0
          self.wg = 0
          #buildi.inres[self.wres]-= 5/FPS
          #buildings[f].pinres[self.wres]-= 5/FPS
          f.outres["loggs"]+= 150
          f.poutres["loggs"]+= 150
      if self.wstage == 100:
        self.wstage = 0
        self.state = 2
        self.wtree = 0
        
        
      
    def workshop(self, buildings):
      FPS = FPSl[0]
      f = self.work_n
      if self.wstage == 0:
        wsd = {}
        wsa= 0
        for i in buildings[f].inres:
          wsd[buildings[f].inres[i]] = i
        wsa = max(wsd)
        if wsa > 0 and wsd[wsa] in buildings[f].inres:
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
          #self.money += buildings[f].salary
          #money[0]-= buildings[f].salary
          if buildings[f].paymod == "wage":
            transact("island", self, buildings[f].salary)
          self.wstage = 0
          self.state = 2
          self.tupd("Конец рабочего дня")
          
    def schoolstudy(self,buildings):
      FPS = FPSl[0]
      f = self.work_n
      ff = buildings[f]
      if self.edupoint<=10:
        edup = (1/FPS*buildings[f].nwork/buildings[f].maxnwork)
        if ff.mode == "main":
            edup = edup*1.15
        if gamevalues["likbez"] == True:
            edup = edup * 1.3
        self.edupoint += edup
      else:
        print(buildings[self.work_n].nstud)
        buildings[self.work_n].nstud-= 1
        print(buildings[self.work_n].students)
        print(self.id)
        if self.id in buildings[self.work_n].students:
          buildings[self.work_n].students.remove(self.id)
        self.work_n = -1
        self.education = 1
        self.state = 2
        
        
    def workmine(self, buildings):
        FPS = FPSl[0]
        f = self.work_n
        
        wores = buildings[f].subtype
        if buildings[f].salary > 0 and buildings[f].outres[wores] < 2000 and buildings[f].mineres.amount>0:
          buildings[f].amount += 1 * math.sqrt( buildings[f].salary)/ FPS/10
          #buildings[f].outres[wores] += 1 * math.sqrt(buildings[f].salary)/ FPS/10
          #buildings[f].poutres[wores] += 1 * math.sqrt(buildings[f].salary)/ FPS/10
          buildings[f].mineres.amount -= 1 * math.sqrt( buildings[f].salary)/ FPS/10
          #money[0] -= buildings[f].salary / FPS/10
          #self.money += buildings[f].salary / FPS/10
          if "mining" not in self.skills:
            self.skills["mining"] = 0
          val = 7 * math.sqrt(math.sqrt(math.sqrt( buildings[f].salary))) + self.skills["mining"]*3
          produce(buildings[f], val/FPS, wores, type = "mining")
          if buildings[f].paymod == "wage":
            transact("island", self, buildings[f].salary / FPS/10)
        self.worktime += 1 / FPS / 10
        if buildings[f].mineres.amount<=0:
             self.state = 2
             self.worktime = 0
             self.tupd("Ресурсы закончились")

        if self.worktime >= 3:
             if "mining" not in self.skills:
                self.skills["mining"] = 0
             self.skills["mining"] += 0.3
             if self.skills["mining"] > 10:
               self.skills["mining"] = 10
             self.state = 2
             self.worktime = 0
             self.tupd("Конец рабочего дня")
    def workrancho(self, buildings):
        FPS = FPSl[0]
        f = self.work_n
        wores = buildings[f].subtype
        if buildings[f].salary > 0 and buildings[f].outres[wores] < 1000:
          buildings[f].amount += 1 * math.sqrt( buildings[f].salary)/ FPS/10
          #buildings[f].outres[wores] += 1 * math.sqrt(buildings[f].salary)/ FPS/10
          #buildings[f].poutres[wores] += 1 * math.sqrt(buildings[f].salary)/ FPS/10
          val = 3 + self.getskill("farming")
          produce(buildings[f], val/FPS, wores, type = "farming")
          #money[0] -= buildings[f].salary / FPS/10
          #self.money += buildings[f].salary / FPS/10
          if buildings[f].paymod == "wage":
            transact("island", self, buildings[f].salary / FPS/10)
        self.worktime += 1 / FPS

        if self.worktime >= 5:
             self.incskill("farming")
             self.state = 2
             self.worktime = 0
             self.tupd("Конец рабочего дня")
    def workfarm(self, buildings):
        FPS = FPSl[0]
        f = self.work_n
        
        wores = buildings[f].subtype
        if buildings[f].salary > 0 and buildings[f].outres[wores] < 2000:
          buildings[f].amount += 1 * math.sqrt( buildings[f].salary)/ FPS/5
          #buildings[f].outres[wores] += 1 * math.sqrt(buildings[f].salary)/ FPS/10
          #buildings[f].poutres[wores] += 1 * math.sqrt(buildings[f].salary)/ FPS/10
          val = math.sqrt( buildings[f].salary)/ FPS/5
          if allmrot["eat"][0] != "None":
            if allmrot["eat"][0] > 0:
              val = buildings[f].salary/ allmrot["eat"][0]
          val = 3*math.sqrt( math.sqrt(math.sqrt( buildings[f].salary))) + self.getskill("farming")
          produce(buildings[f], val/ FPS, wores, type = "farming")
          #money[0] -= buildings[f].salary / FPS/10
          #self.money += buildings[f].salary / FPS/10
          
          if buildings[f].paymod == "wage":
            transact("island", self, buildings[f].salary / FPS/5)
          
        self.worktime += 1 / FPS 

        if self.worktime >= 4:
             self.incskill("farming")
             self.state = 2
             self.worktime = 0
             self.tupd("Конец рабочего дня")
    def workclinic(self, buildings):
        #f = self.work_n
        FPS = FPSl[0]
        h = self.target
        h.amount += 1 * math.sqrt(h.salary) / FPS
        if h.paymod == "wage":
          money[0] -= h.salary / FPS
          self.money += h.salary / FPS
        h.amount += (3 / FPS)
        self.worktime += 1 / FPS / 2

        if self.worktime >= 10:
             self.state = 2
             self.worktime = 0
             self.tupd("Конец рабочего дня")
    def workimig(self, buildings):
      FPS = FPSl[0]
      self.state = 2
      self.wstage = 0
      self.incskill("imigration")
      self.tupd("Конец рабочего дня")
    def workimig2(self, buildings):
     FPS = FPSl[0]
     if self.wstage == 0:
      f = self.work_n
      self.wt += 1/FPS
      efec = math.sqrt(buildings[f].salary)
      if buildings[f].resourses < 30:
        
        buildings[f].resourses += efec/FPS
        #self.money += buildings[f].salary/FPS
        #money[0] -= buildings[f].salary/FPS
        if buildings[f].paymod == "wage":
          transact("island", self, buildings[f].salary / FPS)
      else:
        addhuman()
        buildings[f].resourses = 0
        self.tupd("Я привлёк человека на остров!")
      if self.wt > 20:
        self.wstage = 1
        self.wt = 0
     if self.wstage == 1:
       self.state = 2
       self.wstage = 0
       self.tupd("Конец рабочего дня")
    
    def workbuild(self, buildings, garages, xx, yy, mu):
      FPS = FPSl[0]
      f = self.work_n
      
      if self.wstage == 0:
        wprior = 100000000000
        ibu = None
        for i in buildings:
          if i.bready == 0:
            dx = self.x - i.x
            dy = self.y - i.y
            bprior = (dx*dx + dy*dy)*(math.sqrt(len(i.builders))+1)
            
            if wprior > bprior:
              wprior = bprior
              ibu = i
        if wprior < 100000000000:
          self.bb = ibu
          ibu.builders.append(self)
          self.wstage = 1
        else:
          self.wstage = 0
          self.state = 2
          self.incskill("building")
      #if self.wstage != 0:
       #if self.bb.bready == 1:
        #self.wstage = 0
        #self.state = 2
        #self.bb.builders.remove(self)
        #self.wt = 0
      if self.wstage == 1:
       #if self.wt < 10:
        
        wj = self.bb
        #print("st1")
        self.gotocw2(wj.x,wj.y, garages, xx, yy, mu)
        if self.car == 8:
          self.wstage = 10
          self.car = 0
          self.wg = 0
      if self.wstage == 10:
       if self.wt < 5:
        wj = self.bb
        if  wj.bproc>=wj.bpready:
          wj.bready = 1
          self.state = 2
          self.wstage = 0
          self.bb.builders.remove(self)
          wj.settype(wj.type)
        else:
          wj.bproc += (2 + self.getskill("building"))/FPS 
          self.wt += 1/FPS
       else:
          self.state = 2
          self.wstage = 0
          self.incskill("building")
          if self in self.bb.builders:
            self.bb.builders.remove(self)
          self.wt = 0
          #wj.settype(wj.type)
      
    def workfur(self, buildings, garages, xx, yy, mu):
      FPS = FPSl[0]
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
                    i.testp1 = "есть в другом( pout)" + str(wp1)
                    
                    wp4 = i.pinres[k]
                    i.testp4 = "есть в этом (pin): " + str(wp4)
                    wp3 = min(15000, 15*math.sqrt(i.salary)*i.nwork)
                    wp3 = i.maxinres
                    i.testp3 = "нужно: "+ str(wp3)
                    if wp4>wp3:
                      wp2=0
                    else:
                      wp2 = min(wp3-wp4,wp1) + (wp3 - wp4)/10000
                      
                      i.testp2 = "мин нужно, есть в pin" + str(wp2)
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
        if wa > 0 and wj.x > -1000000000000000:
          #self.wstage = 1313
          self.wj2 = wj2
          self.wa = wa
          ##wj.poutres[wk] -= wa
          #wj2.pinres[wk] += wa
          #print(self.wj)
          self.wj = wj
          self.wres = wk
          self.wj.poutres[self.wres] -= self.wa
          self.wj2.pinres[self.wres] += self.wa
          self.wstage = 1
        else:
          self.wstage = 100
      
      if self.wstage == 1:
        wj = self.wj
        #print("st1")
        self.gotocw2(self.wj.x,self.wj.y, garages, xx, yy, mu)
        if self.car == 8:
          self.wstage = 10
          self.car = 0
          self.wg = 0
      if self.wstage == 10:
        wj = self.wj
        wa = self.wa
        
        self.wresourses[self.wres] += wa
        self.wg += wa
        wj.outres[self.wres] -= wa
        self.wstage = 20
        if self.wj2.type == "port":
            self.wj.updstat("export", wa * getexportprise(self.wres)/100)
        #self.wj = 0
        self.wg = 0
        if 1 == 0:
         if wj.outres[self.wres] >= 150/FPS and self.wg<=wa-150/ FPS :
          self.wresourses[self.wres] += 150/ FPS
          self.wg+= 150/ FPS
          wj.outres[self.wres] -= 150/FPS
          #money[0] -= buildings[f].salary / FPS
          #self.money += buildings[f].salary / FPS
         elif self.wg>wa-150/ FPS:
          #self.wresourses[self.wres] += wj.outres[self.wres]
          #wj.outres[self.wres] = 0
          wj.outres[self.wres] += self.wg-wa
          self.wresourses[self.wres] -= self.wg-wa
          self.wstage = 20
          self.wj = 0
          self.wg = 0
         elif wj.outres[self.wres] <= 150/FPS:
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
        self.gotocw2(wj.x,wj.y, garages, xx, yy, mu)
        if self.car == 8:
          self.wstage = 21
          self.car = 0
      if self.wstage == 21:
        wj = self.wj2
        if self.wresourses[self.wres] >= 1500/FPS and 1 == 0:
          wj.inres[self.wres] += 1500/ FPS
          self.wresourses[self.wres] -= 1500/FPS
          #money[0] -= buildings[f].salary / FPS
          #self.money += buildings[f].salary / FPS
          if buildings[f].paymod == "wage":
            transact("island", self, buildings[f].salary / FPS)
          
        else:
          wj.inres[self.wres] += self.wresourses[self.wres]
          
          self.wresourses[self.wres] = 0
          self.wstage = 100
          self.wj = 0
      if self.wstage == 100:
        
        self.state = 2
        self.wstage = 0
        self.tupd("Конец рабочего дня")
    def workrome(self, buildings):
      FPS = FPSl[0]
      f = buildings[self.work_n]
      if self.wstage == 0:
        self.wt = 0
        self.wstage = 1
      if self.wstage == 1:
        if f.inres["sugar"] > 0:
          #f.inres["sugar"] -= math.sqrt(f.salary)/FPS/8
          #f.pinres["sugar"] -= math.sqrt(f.salary)/FPS/8
          #f.outres["rom"]+= math.sqrt(f.salary)/FPS/8
          #f.poutres["rom"]+= math.sqrt(f.salary)/FPS/8
          val = 6.6 + self.getskill("industy")*5/10
          produce(f, val/ FPS, "rom", "industry", "sugar")
          #self.money += f.salary/FPS
          #money[0]-=f.salary/FPS
          if f.paymod == "wage":
            transact("island", self, f.salary/FPS)
        self.wt += 1/FPS
        if self.wt > 10:
          self.wt = 0
          self.wstage = 10
      if self.wstage == 10:
        self.incskill("industry")
        self.state = 2
        self.wstage = 0
        self.tupd("Конец рабочего дня")
    
    def worklumber(self, buildings):
      FPS = FPSl[0]
      f = buildings[self.work_n]
      if self.wstage == 0:
        self.wt = 0
        self.wstage = 1
      if self.wstage == 1:
        if f.inres["loggs"] > 0:
          #f.inres["sugar"] -= math.sqrt(f.salary)/FPS/8
          #f.pinres["sugar"] -= math.sqrt(f.salary)/FPS/8
          #f.outres["rom"]+= math.sqrt(f.salary)/FPS/8
          #f.poutres["rom"]+= math.sqrt(f.salary)/FPS/8
          val = 6.6 + self.getskill("industy")*5/10
          produce(f, val/FPS, "lumber", "industry", "loggs")
          #self.money += f.salary/FPS
          #money[0]-=f.salary/FPS
          if f.paymod == "wage":
            transact("island", self, f.salary/FPS)
        self.wt += 1/FPS
        if self.wt > 10:
          self.wt = 0
          self.wstage = 10
      if self.wstage == 10:
        self.incskill("industry")
        self.state = 2
        self.wstage = 0
        self.tupd("Конец рабочего дня")
    def workfurniture(self, buildings):
      FPS = FPSl[0]
      f = buildings[self.work_n]
      if self.wstage == 0:
        self.wt = 0
        self.wstage = 1
      if self.wstage == 1:
        if f.inres["lumber"] > 0:
          #f.inres["sugar"] -= math.sqrt(f.salary)/FPS/8
          #f.pinres["sugar"] -= math.sqrt(f.salary)/FPS/8
          #f.outres["rom"]+= math.sqrt(f.salary)/FPS/8
          #f.poutres["rom"]+= math.sqrt(f.salary)/FPS/8
          val = 6.6 + self.getskill("industy")*5/10
          
          produce(f, val/FPS, "furniture", "industry", "lumber")
          #self.money += f.salary/FPS
          #money[0]-=f.salary/FPS
          if f.paymod == "wage":
            transact("island", self, f.salary/FPS)
        self.wt += 1/FPS
        if self.wt > 10:
          self.wt = 0
          self.wstage = 10
      if self.wstage == 10:
        self.state = 2
        self.wstage = 0
        self.incskill("industry")
        self.tupd("Конец рабочего дня")
    def workjewerly(self, buildings):
      FPS = FPSl[0]
      f = buildings[self.work_n]
      if self.wstage == 0:
        self.wt = 0
        self.wstage = 1
      if self.wstage == 1:
        if f.inres["gold"] > 0:
          #f.inres["sugar"] -= math.sqrt(f.salary)/FPS/8
          #f.pinres["sugar"] -= math.sqrt(f.salary)/FPS/8
          #f.outres["rom"]+= math.sqrt(f.salary)/FPS/8
          #f.poutres["rom"]+= math.sqrt(f.salary)/FPS/8
          produce(f, 1 * math.sqrt(f.salary)/ FPS/8, "jewerly", "industry", "gold")
          #self.money += f.salary/FPS
          #money[0]-=f.salary/FPS
          if f.paymod == "wage":
            transact("island", self, f.salary/FPS)
        self.wt += 1/FPS
        if self.wt > 10:
          self.wt = 0
          self.wstage = 10
      if self.wstage == 10:
        self.state = 2
        self.wstage = 0
        self.tupd("Конец рабочего дня")
    def workweapon(self, buildings):
      FPS = FPSl[0]
      f = buildings[self.work_n]
      if self.wstage == 0:
        self.wt = 0
        self.wstage = 1
      if self.wstage == 1:
        if f.inres["iron"] > 0:
          #f.inres["sugar"] -= math.sqrt(f.salary)/FPS/8
          #f.pinres["sugar"] -= math.sqrt(f.salary)/FPS/8
          #f.outres["rom"]+= math.sqrt(f.salary)/FPS/8
          #f.poutres["rom"]+= math.sqrt(f.salary)/FPS/8
          produce(f, 1 * math.sqrt(f.salary)/ FPS/8, "weapon", "industry", "iron")
          #self.money += f.salary/FPS
          #money[0]-=f.salary/FPS
          if f.paymod == "wage":
            transact("island", self, f.salary/FPS)
        self.wt += 1/FPS
        if self.wt > 10:
          self.wt = 0
          self.wstage = 10
      if self.wstage == 10:
        self.state = 2
        self.wstage = 0
        self.tupd("Конец рабочего дня")
    def workcheese(self, buildings):
      FPS = FPSl[0]
      f = buildings[self.work_n]
      if self.wstage == 0:
        self.wt = 0
        self.wstage = 1
      if self.wstage == 1:
        if f.inres["milk"] > 0:
          #f.inres["milk"] -= math.sqrt(f.salary)/FPS/8
          #f.pinres["milk"] -= math.sqrt(f.salary)/FPS/8
          #f.outres["cheese"]+= math.sqrt(f.salary)/FPS/8
          #f.poutres["cheese"]+= math.sqrt(f.salary)/FPS/8
          produce(f, 1 * math.sqrt(f.salary)/ FPS/8, "cheese",  "industry", "milk")
        #self.money += f.salary/FPS
        #money[0]-=f.salary/FPS
        if f.paymod == "wage":
          transact("island", self, f.salary/FPS)
        
        self.wt += 1/FPS
        if self.wt > 10:
          self.wt = 0
          self.wstage = 10
      if self.wstage == 10:
        self.state = 2
        self.wstage = 0
        self.tupd("Люблю сыр, но на сегодня хватит")
        
    def workcanns(self, buildings):
      FPS = FPSl[0]
      f = buildings[self.work_n]
      if self.wstage == 0:
        self.wt = 0
        self.wstage = 1
      if self.wstage == 1:
        if f.inres[f.subtype] > 0:
          #f.inres[f.subtype] -= math.sqrt(f.salary)/FPS/8
          #f.pinres[f.subtype] -= math.sqrt(f.salary)/FPS/8
          #f.outres["canns"]+= math.sqrt(f.salary)/FPS/8
          #f.poutres["canns"]+= math.sqrt(f.salary)/FPS/8
          produce(f, 1 * math.sqrt(f.salary)/ FPS/8, "canns",  "industry", f.subtype)
          #self.money += f.salary/FPS
          #money[0]-=f.salary/FPS
          if f.paymod == "wage":
            transact("island", self, f.salary/FPS)
        self.wt += 1/FPS
        if self.wt > 10:
          self.wt = 0
          self.wstage = 10
      if self.wstage == 10:
        self.state = 2
        self.wstage = 0
        self.tupd("Конец рабочего дня")
        
    def workcigar(self, buildings):
      FPS = FPSl[0]
      f = self.target#buildings[self.work_n]
      if self.wstage == 0:
        self.wt = 0
        self.wstage = 1
      if self.wstage == 1:
        if f.inres["tobacco"] > 0:
          #f.inres["tobacco"] -= math.sqrt(f.salary)/FPS/8
          #f.pinres["tobacco"] -= math.sqrt(f.salary)/FPS/8
          #f.outres["cigar"]+= math.sqrt(f.salary)/FPS/8
          #f.poutres["cigar"]+= math.sqrt(f.salary)/FPS/8
          produce(f, 1 * math.sqrt(f.salary)/ FPS/8, "cigar", "industry", "tobacco")
          #self.money += f.salary/FPS
          #money[0]-=f.salary/FPS
          if f.paymod == "wage":
            transact("island", self, f.salary/FPS)
          self.wt += 1/FPS
        if self.wt > 10:
          self.wt = 0
          self.wstage = 10
      if self.wstage == 10:
        self.state = 2
        self.wstage = 0
        self.tupd("Конец рабочего дня")
    
    def workthe(self, buildings):
      FPS = FPSl[0]
      f = self.work_n
      if self.wstage == 0:
        self.wa = 0
        self.wstage = 1
      if self.wstage == 1:
        self.wa += 1/FPS
        #self.money += buildings[f].salary/FPS
        #money[0] -= buildings[f].salary/FPS
        if buildings[f].paymod == "wage":
          transact("island", self, buildings[f].salary/FPS)
        
        if self.wa >= 10:
          self.wstage = 100
      if self.wstage == 100:
        self.wa = 0
        self.state = 2
        self.tupd("Хватит с меня работы актером")
    def workport(self, buildings):
      FPS = FPSl[0]
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
          
          #wpr[cr] -= 1/FPS
          #buildings[f].pinres[cr] -= 1/FPS
          #if buildings[f].pinres[cr] < 0:
            #buildings[f].pinres[cr] = 0
          #money[0] += 50*exportprices[cr]/FPS/100
          #if buildings[f].paymod == "wage":
          export(buildings[f], cr, 3/FPS)
          #transact("outside", 0, exportprices[cr]/FPS/100)
          
          #money[0] -= buildings[f].salary / FPS
          #self.money += buildings[f].salary / FPS
        else:
          self.wpr[self.wcr]= 0
          self.state = 2
          self.wstage = 0
          #self.money += 120
          self.tupd("Всю работу сделал")
    def think(self, buildings, garages, clinics, homes, thlist = []):
        if gameparametrs["no_think"] == True:

            return 0
        if gameparametrs["religion"] != True:
            human_func_think(self, buildings, garages, clinics, homes)
        else:
            human_func_think_relig(self, buildings, garages, clinics, homes)
                
              
            
    


    def do(self, buildings, clinics, garages, xx, yy, mu):
        human_func_do(self, buildings, clinics, garages, xx, yy, mu)

    def draw(self, xx,yy,mu,xi0,xi1, yj0, yj1):
        
        if self.x >= xi0 and self.y <= xi1 and self.y>= yj0 and self.y <= yj1:
        #if xhum >= -100 and xhum <= w+100 and yhum > -100 and yhum < h+100:
          xhum = (xx + 100 * self.x) * mu + (1 - mu) * (w / 2)
          yhum = (yy + 100 * self.y) * mu + (1 - mu) * (h / 2)
          
          if self.state == "armyconf1":
            pygame.draw.circle(sc, (0,50,255), (xhum + 50 * mu, yhum + 50 * mu), 15 * mu)
          elif self.state == "rebelconf1":
            
            pygame.draw.circle(sc, (255,50,0), (xhum + 50 * mu, yhum + 50 * mu), 15 * mu)
          elif self.dismod == 0:
            pygame.draw.circle(sc, ORANGE, (xhum + 50 * mu, yhum + 50 * mu), 5 * mu)
          else:
            pygame.draw.circle(sc, (0,0,255), (xhum + 50 * mu, yhum + 50 * mu), 15 * mu)
          if 0 < 0:
           pygame.font.init()
           i = int(20*mu)
           if i > 12:
            f1 = pygame.font.SysFont('arial', int(20*mu))
            text1 = f1.render(self.name, True,
                      (255, 255, 255))
            sc.blit(text1, (xhum,yhum))


def addhuman(nhum=1, xhum = 0, yhum = 0):
  for i in range (0,nhum):
    j = human(xhum,yhum,len(humans))
    humans.append(j)
    hbut = button(100, 26*i, 100,25)
    hbut.text = j.name
    buttonshuman.append(hbut)