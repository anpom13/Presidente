
from car import *



def export(bui, res, val):
     
          bui.inres[res] -= val
          bui.pinres[res] -= val
          if bui.pinres[res] < 0:
            bui.pinres[res] = 0
          #money[0] += 50*exportprices[cr]/FPS/100
          #if buildings[f].paymod == "wage":
          transact("outside", 0, getexportprise(res)*val/100, type = "other")

def produce(f, val = 0, pres = "corn", type = "main", res = None, ):
  if res != None:
    f.inres[res] -= val
    f.pinres[res] -= val
    if f.pinres[res] < 0:
       f.pinres[res] = 0
  f.outres[pres]+= val
  f.poutres[pres]+= val
  f.statres[pres][0]+= val
  f.updstat("prodused", val)
  
  
def humtransact(frohum, tohum, val, type = "main"):
  if courseon[0] == True:
    if tohum == "outside":
      frohum.money -= val*dcourse[0]
      mainbanks[0].change(val*dcourse[0])
  if courseon[0] == False:
    if tohum == "outside":
      frohum.money -= val
      
  if tohum == "island":
      frohum.money -= val
def transact(fro, to, val, type = "main", type2 = "main"):

  #print(money)
#  if type == "main":
      #a = humans[1000000000]
  if fro == "island1":
      money[0] -= val
  if fro == "island":
    fromon = money[0]
    money[0] -= val
    to.money += val
    expendi["main"][-1]+= val
    balancestat["main"][-1] -= val
    if type!="main":
      expendi[type][-1]+=val
      balancestat[type][-1] -= val
      if type2!="main" and type2!=type:
        expendi[type2][-1]+=val
        balancestat[type2][-1] -= val
    
  elif to == "island":
    tomon = money[0]
    fro.money -= val
    money[0] += val
    incomedi["main"][-1]+= val
    balancestat["main"][-1] += val
    if type!="main":
      balancestat[type][-1] += val
      incomedi[type][-1]+= val
      if type2!="main" and type2!=type:
        incomedi[type2][-1]+=val
        balancestat[type2][-1] += val
    
  elif fro == "outside":
    if courseon[0] == True:
      #money[1] += val
      minfins[0].extransact(val)
      #print(money)
      outincomedi["main"][-1]+= val
      balancestat["main"][-1] += val
      if type!="main":
        outincomedi[type][-1]+=val
        balancestat[type][-1] += val
        if type2 != "main" and type2 != type:
            outincomedi[type2][-1] += val
            balancestat[type2][-1] += val
    if courseon[0] == False:
      money[0] += val
      outincomedi["main"][-1]+= val
      balancestat["main"][-1] += val
      if type!="main":
        outincomedi[type][-1]+=val
        balancestat[type][-1] += val
        if type2 != "main" and type2 != type:
            outincomedi[type2][-1] += val
            balancestat[type2][-1] += val
  elif to == "outside":
    if courseon[0] == True:
      money[1] -= val
    
      outexpendi["main"][-1]+= val
      balancestat["main"][-1] -= val
      if type!="main":
        outexpendi[type][-1]+=val
        balancestat[type][-1] -= val
        if type2 != "main" and type2 != type:
            outexpendi[type2][-1] += val
            balancestat[type2][-1] -= val
    if courseon[0] == False:
      money[0] -= val
    
      outexpendi["main"][-1]+= val
      balancestat["main"][-1] -= val
      if type!="main":
        outexpendi[type][-1]+=val
        balancestat[type][-1] -= val
        if type2 != "main" and type2 != type:
            outexpendi[type2][-1] += val
            balancestat[type2][-1] -= val
    
  else:
    fro.money -= val
    to.money += val

def pay_upkeep(self):
      transact(0, "outside", self.upkeep, type = "upkeep")


def human_func_gostraight(self, gxt, gyt):
      FPS = FPSl[0]
      dx = gxt - self.x
      dy = gyt - self.y
      ds = math.sqrt(dx * dx + dy * dy)
      self.walk_ds = ds
      k = ds / self.speed
      
      
      if k != 0.0:
        dxx = (dx / k) / FPS
        dyy = (dy / k) / FPS
      else:
        dxx = 1000000000000
        dyy = 100000000000
      #if mo(dx) > mo(dxx) + 0.1 or mo(dy) > mo(dyy) + 0.1:
      fk = math.sqrt(dxx * dxx + dyy * dyy)
      if fk <= ds:
        lv1 = self.x + dxx + 0.5
        lv2 = self.y + dyy + 0.5
        self.x += dxx
        self.y += dyy
      else:
        self.x = gxt
        self.y = gyt
        return True

def human_func_gobylist(self, list):
    le = len(list)
    #print(list)
    if self.swalk < le:
      if self.gostraight(list[self.swalk][0], list[self.swalk][1]) == True:
        self.swalk += 1
    else:
        self.swalk = 0
        return True
def human_func_goto(self, gxt,gyt,gst, tuse = "main"):
     #gxt = list(lxt)
     #gyt = list(lyt)
     if isinstance(gxt, list):
       if self.swalk <= len(gxt)-1:
         self.goto(gxt[self.swalk][0], gxt[self.swalk][1], self.swalk + 1, tuse = "walk")
       else:
         self.car = gst
     if isinstance(gxt, int) and self.wwalk == 20 and tuse == "main":
       #print(self.walkway)
       
       if self.gobylist(self.walkway) == True:
         self.car = gst
         self.x = gxt
         self.y = gyt
         self.wwalk = 0
       #print(self.walkway)
     if isinstance(gxt, int) and self.wwalk == 10:
      mds = 100
      mi = None
       
      lwcoord = (int(self.x), (self.y))
      checache = 0
      if lwcoord in walklistscache:
         if (gxt, gyt) in walklistscache[lwcoord]:
           checache = 1
           self.walkway = walklistscache[lwcoord][(gxt, gyt)]
           self.wwalk = 20
      else:
        walklistscache[lwcoord] = {}
         
      if checache == 0:
       for i in self.lbuild.walknodes:
         dx = mo(self.x - i[0] )
         dy = mo(self.y - i[1] )
         ds = dx + dy
         if ds < mds:
           mds = ds
           mi = i
           
       #self.fnode = mi
       #lwnodesr = wnodesr(mi, walknodes)[1]
       #if 1 > 0:
         #print("специально вызванная ошибка")
         #rm[0][0][0] = 10
       
       lwnodesr = wnodesr(mi, walknodes)[1]
       mds = 10000
       mi2 = None
       for i in lwnodesr:
         dx = mo(gxt - i[0] )
         dy = mo(gyt - i[1] )
         ds = dx + dy
         if ds < mds:
           mds = ds
           mi2 = i
       wlist = [mi] + lwnodesr[mi2]
       for i in range(len(wlist)):
         wlist[i] = (wlist[i][0]- 0.5, wlist[i][1]- 0.5)
       #self.walkway = wlist + [(gxt,gyt)]
       lbuild2 = vecmap[int(gxt)][int(gyt)] 
       
       if lbuild2 == 0:
         self.walkway = wlist + [(gxt,gyt)]
         walklistscache[lwcoord][(gxt, gyt)] = self.walkway
       
         
       else:
        lnf = next(iter(lbuild2.walknodes))
        lans = walksvsets[walksvdic[lnf]] # множество связных в вершин в котором живет lnf.    
        lwdic =  walksvdic[lnf]
        lnf0 = next(iter(self.lbuild.walknodes))
        lwdic0 = walksvdic[lnf0]
        if lwdic0 == lwdic:
          self.walkway = wlist + [(gxt,gyt)]
          walklistscache[lwcoord][(gxt, gyt)] = self.walkway
        else:
         mds = 1000000
         mi3 = None
         lan= wlist[-1]
         for i in lans:
           dx = mo( lan[0] - i[0])
           dy = mo( lan[1] - i[1])
           ds = dx + dy
           if ds < mds:
             mi3 = i
             mds = ds
         lwnodesr2 = wnodesr(mi3, walknodes)[1][(int(gxt),int(gyt))]
         for i in range(len(lwnodesr2)):
           lwnodesr2[i] = (lwnodesr2[i][0]- 0.5, lwnodesr2[i][1]- 0.5)
         mi3 = (mi3[0]-0.5, mi3[1]-0.5,)
         self.walkway = wlist + [mi3] + lwnodesr2 + [(gxt,gyt)]
         walklistscache[lwcoord][(gxt, gyt)] = self.walkway
       self.wwalk = 20
       ##print("это сгенерированный словарь связных вершин", lwnodesr)
       #print("это весь словарь", walkroads)
     if isinstance(gxt, int) and (self.wwalk == 0 or tuse == "walk"):
     
      #gxt = lxt[0]
      #gyt = lyt[0]
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
      #if mo(dx) > mo(dxx) + 0.1 or mo(dy) > mo(dyy) + 0.1:
      fk = math.sqrt(dxx * dxx + dyy * dyy)
      if fk <= ds:
        lv1 = self.x + dxx + 0.5
        lv2 = self.y + dyy + 0.5
        lbuild = vecmap[int(lv1)][int(lv2)]
        self.lbuild = lbuild
        #if len(self.movedic)>2:
          #self.movedic = {}
        if lbuild == 0:
          self.x += dxx
          self.y += dyy
          self.movedic = {}
        elif int(lv1) == int(gxt) and int(lv2) == int(gyt):
          self.x += dxx
          self.y += dyy
        else:
         #self.x += dxx
         #self.y += dyy
         self.wwalk = 10
         
      else:
        self.x = gxt
        self.y = gyt
        if tuse == "war":
          self.warstage = gst
        if tuse == "main":
          self.car = gst
        if tuse == "walk":
          self.swalk = gst
        if tuse == "return":
          return gst
        if tuse == "returntrue":
          return True
        #self.car = 0
        
def human_func_do(self, buildings, clinics, garages, xx, yy, mu):
        FPS = FPSl[0]
        if self.state == "rebelconf1":
          if self.warstage == 0:
            
            mi = None
            mds = 7
            for i in activearmy:
              dx = self.x - i.x
              dy = self.y - i.y
              ds = math.sqrt(dx*dx + dy*dy)
              if mds > ds:
                mds = ds
                mi = i
            if mi != None:
              self.targetsoldier = mi
              self.warstage = 15
            dx = self.x - self.attacbui.x
            dy = self.y - self.attacbui.y
            ds = math.sqrt(dx*dx + dy*dy)
            if ds > 5:
              self.gostraight(self.attacbui.x, self.attacbui.y)
            else:
              self.attacbui.hp -= 1/FPS
            if self.attacbui.hp < 0:
              mainfunc["endconflict"]()
              self.attacbui.destroy()
              self.attacbui.hp = 10
              print("тестовый параметр в строке 303 файла humanfunc")
              
          if self.warstage == 15:
            dx = self.x - self.targetsoldier.x
            dy = self.y - self.targetsoldier.y
            ds = math.sqrt(dx*dx + dy*dy)
            if ds >3:
              self.gostraight(self.targetsoldier.x, self.targetsoldier.y)
            if ds > 5:
              self.targetsoldier.hp -= 1/FPS
            if self.targetsoldier.hp < 0:
              self.warstage = 0
          
            #self.x= 30
            #self.y = 30
        if self.state == "armyconf1":
          if self.warstage == 0:
            self.tupd("повстанцев: "+ str(len(activerebels)))
            self.wwalk = 0
            self.swalk = 0
            self.car = 0
            
              
            mds = 10000
            mi = None
            for i in activerebels:
              dx = self.x - i.x
              dy = self.y - i.y
              ds = math.sqrt(dx*dx + dy*dy)
              if mds > ds:
                mds = ds
                mi = i
            if mi != None:
              self.warrebel = mi
              self.warstage = 10
            else:
              mainfunc["endconflict"]()
          if self.warstage == 10:
            #if self.goto(self.warrebel.x, self.warrebel.y, tuse = "returntrue", gst = 0) == True:
            if self.gobylist([(self.warrebel.x, self.warrebel.y)]) == True:
            
              self.warstage = 20
              self.wwalk = 0
              self.swalk = 0
              self.car = 0
            dx = self.x - self.warrebel.x
            dy = self.y - self.warrebel.y
            ds = math.sqrt(dx*dx + dy*dy)
            if ds < 5:
              self.tupd("конец стадии 2: "+ str(len(activerebels)))
              self.warstage = 20
              self.wwalk = 0
              self.swalk = 0
              self.car = 0
          if self.warstage == 20:
            dx = self.x - self.warrebel.x
            dy = self.y - self.warrebel.y
            ds = math.sqrt(dx*dx + dy*dy)
            if ds > 3:
              self.gostraight(self.warrebel.x, self.warrebel.y)
            self.warrebel.hp -= 1/FPS
            if self.warrebel.hp < 0:
              if self.warrebel in activerebels:
                activerebels.discard(self.warrebel)
              self.warstage = 0
              
              
        if self.state == 1:
            n = 1
            #if self.type_target == 0 and self.teat not in buildings[self.number_target].outres:
              #self.state = 2
            if self.type_target == 0:# and self.teat in buildings[self.number_target].outres:  # ест
                #print("eating")
              wa = self.aeat
              f = buildings[self.number_target]
              if f.type != "eatmarket":
                self.tupd("Потребляю нашу еду")
                if f.outres[self.teat]>3/FPS and self.wg <= wa - 3/FPS and self.money>=3/FPS:
                  
                    self.hap_eat += 3 / FPS
                    self.wg += 3/FPS
                    #self.money -= 3 * self.pprice/ FPS
                    #money[0] += 3 * self.pprice/ FPS
                    transact(self,"island",self.pprice/ FPS, type = "food")
                    f.updstat("this", self.pprice/ FPS)
                    buildings[self.number_target].outres[self.teat] -= 3 / FPS
                elif self.money <= 3 * self.pprice/ FPS:
                  self.money = 0
                  #print(self.aeat)
                  f.poutres[self.teat] += (wa - self.wg) + 0.001
                  f.outres[self.teat] += 0.001
                  self.state = 2
                  #self.hap_eat = 10
                  self.wg = 0
                  self.aeat = 0
                elif self.wg > wa -3/FPS:
                    f.outres[self.teat] += self.wg-wa + 0.001
                    f.poutres[self.teat] +=  0.001
                    self.hap_eat -= self.wg-wa
                    self.state = 2
                    #self.hap_eat = 10
                    self.wg = 0
                    self.aeat = 0
                    
                elif f.outres[self.teat] <= 3/FPS:
                    self.hap_eat += f.outres[self.teat]
                    f.outres[self.teat] = 0.001
                    f.poutres[self.teat] += (wa - self.wg) + 0.001
                    self.state = 2
                    #self.hap_eat = 10
                    self.wg = 0
                    self.aeat = 0
                elif self.money <= 3 * self.pprice/ FPS:
                  self.money = 0.001
                  f.poutres[self.teat] += wa - self.wg + 0.001
                  f.outres[self.teat]+= 0.001
                  self.state = 2
                  #self.hap_eat = 10
                  self.wg = 0
                  self.aeat = 0
                else:
                  f.poutres[self.teat] += wa - self.wg + 0.001
                  f.outres[self.teat]+= 0.001
                  self.state = 2
                  #self.hap_eat = 10
                  self.wg = 0
                  self.aeat = 0
              else:
                self.state = 2
                self.tupd("ем имп. еду в размере " + str(self.aeat))
                humtransact(self, "outside", f.prices[self.teat]*self.aeat)
                
                
                #self.money -= f.prices[self.teat]*self.aeat * dcourse[0]
                #mainbanks[0].change(val = f.prices[self.teat]*dcourse[0])
                #дописать — рубли должны еще поступать на биржу, там меняться на доллары. Потехническим причинам это делается после оплаты. 
                self.hap_eat += self.aeat
                #нужно дописать функцию. Здесь рассмотреть случай когда человек покупает импортированную еду. себестоимость выше на 20 процентов изза доставки. продавец может сделать стоимость выше — в списке цен. сейчас это exportprices + 20 процентов -- лежит в f.prices
                ######################################
            if self.type_target == 1:  # лечится
              if (clinics[self.number_target].amount
>= 0.1):
                self.hap_health += (3 / FPS) * (1 - nds)
                clinics[self.number_target].amount -= (3 / FPS) * (1 - nds)
                #self.money -= medc / FPS
                #money[0] += medc / FPS
                
                transact(self,"island", clinics[self.number_target].price/ FPS, type = "medicine")
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

            if self.type_target == 3 :
              self.target = buildings[self.work_n]
              if self.realwork == "stud":
                if buildings[self.work_n].type == "school":
                  self.schoolstudy(buildings)
              if self.realwork == "base":

                #if self.work_type == -1:
                    #print("DD")

                if buildings[self.work_n].type == "farm":  # если работаешь на плантации 1) зп работнику из бюджета 2) увеличение количества еды на ферме
                    self.workfarm(buildings)
                    #self.tupd("Фермерам тяжело")
                if buildings[self.work_n].type == "clinic":  # если работаешь в аптеке
                    #i[2] = health[11][0]
                    #i[3] = health[11][1]
                    self.workclinic(buildings)
                if buildings[self.work_n].type == "port":
                  self.workport(buildings)
                if buildings[self.work_n].type == "fur":
                  self.workfur(buildings, garages, xx, yy, mu)
                if buildings[self.work_n].type == "imigration":
                  self.workimig(buildings)
                if buildings[self.work_n].type == "shop":
                  self.workshop(buildings)
                if buildings[self.work_n].type == "tavern":
                  self.workthe(buildings)
                if buildings[self.work_n].type == "rancho":
                  self.workrancho(buildings)
                if buildings[self.work_n].type == "rome":
                  self.workrome(buildings)
                if buildings[self.work_n].type =="cheese":
                  self.workcheese(buildings)
                if buildings[self.work_n].type == "canns":
                  self.workcanns(buildings)
                if buildings[self.work_n].type == "cigar":
                  self.workcigar(buildings)
                if buildings[self.work_n].type == "build":
                  self.workbuild(buildings, garages, xx, yy, mu)
                if buildings[self.work_n].type == "mine":
                  self.workmine(buildings)
                if buildings[self.work_n].type == "logging":
                  self.worklogg(buildings, xx, yy, mu)
                if buildings[self.work_n].type == "lumber":
                  self.worklumber(buildings)
                if buildings[self.work_n].type == "furniture":
                  self.workfurniture(buildings)
                if buildings[self.work_n].type == "jewerly":
                  self.workjewerly(buildings)
                if buildings[self.work_n].type == "weapon":
                  self.workweapon(buildings)
                if buildings[self.work_n].type == "freedom":
                  self.workgazeta(buildings)
                if buildings[self.work_n].type == "police":
                  self.workpolice(buildings)
                if buildings[self.work_n].type == "army1":
                  self.state = 2
                if buildings[self.work_n].type == "army2":
                  self.state = 2
                  
                  
                self.wotworkt = 10
              
            if self.type_target == -1:
              self.state = 2

            if self.type_target == 5:

                self.state = 2
                self.hap_reg2 = 10

                if self in buildings[self.number_target].visiters:
                  buildings[self.number_target].visiters.remove(self)
                self.tupd("Макаронный монмтр меня любит")
            if self.type_target == 4:
              if self.hap_fun<10 and self.money > 0:
                    self.hap_fun += 2 / FPS
                    #self.money -= 2 *  buildings[self.number_target].price/ FPS
                    #money[0] += 2 *  buildings[self.number_target].price/ FPS
                    transact(self,"island",buildings[self.number_target].price/ FPS, type = "fun")
              else:
                self.state = 2
                self.hap_fun = 10
                #li = buildings[self.number_target].visiters.index(self)
                if self in buildings[self.number_target].visiters:
                  buildings[self.number_target].visiters.remove(self)
                self.tupd("Хватит с меня веселья")
def human_func_think(self, buildings, garages, clinics, homes, thlist = []):
      FPS = FPSl[0]
      #self.gobylist([(1,1),(5,5),(1,3),(5,9)])
      #if self.target == 0 and len(buildings) > 0:
          #self.target = buildings[0] #какойьо костыль
      
      if self.type_target == 3:
        self.target = buildings[self.work_n]
      if self.findworkp ==1 and self.state == 2:
          self.findwork(buildings, homes)
          self.findworkp = 0
          self.wstage = 0
      if self.state == 2:
        funp = (10 - self.hap_fun2) 
        healp = (10 - self.hap_health2)   # приоритет здоровья
        eatp = (10 - self.hap_eat2)   # приоритет еды
        restp = (10 - self.rest2)   # приоритет отдыха
        workp = max(10- self.wotworkt, 0)
        priorl = [eatp, healp, restp, workp, funp]
        if max(priorl) > 0.1:
          maxi = max(priorl)
          maxin = priorl.index(maxi)
          if maxin == 0:
            self.hap_eat2 = 10
            cnte = 0
            cnte2 = 0
            
            for j in buildings:
              if j.f_eat_allow() == 1 and self.money > j.price*3:
                cnte = 1
              if j.type == "eatmarket" and j.nwork > 0:
                if self.money > j.prices["corn"]*3*dcourse[0]:
                  cnte2 = 1
            if cnte2 == 1 or cnte == 1:
              
              #acmoney = min(self.money, max(math.sqrt(self.money), self.salary))
              acmoney = self.money
              amounteat = None
              hape = 0
              lprior = 0
              lveat = None
              xj = None
              if self.hap_eat >= 10:
                lvp = 0
              else:
                lvp = (10-self.hap_eat)*5
              if cnte == 1:
                for j in range(0, len(buildings)):
                  if buildings[j].f_eat_allow() == 1:
                    xm = self.x - buildings[j].x
                    xm = xm * xm
                    ym = self.y - buildings[j].y
                    ym = ym * ym
                    ds = math.sqrt(xm+ym)
                    
                    for i in eat:
                      eprice = buildings[j].prices[i]
                      amounteat2 = min(25-self.hap_eat, acmoney/eprice, buildings[j].poutres[i])
                      hape2 = (self.keats[i] + lvp)*amounteat2
                      #lprior2 = hape2/ds
                      if ds > 5:
                        lprior2 = hape2/ds
                      else:
                        lprior2 = hape2/5
                      if lprior2 > lprior:
                        lprior = lprior2
                        amounteat = amounteat2
                        lveat = i
                        xj = j
              if cnte2 == 1:
                for j in range(0, len(buildings)):
                  if buildings[j].type == "eatmarket" and buildings[j].nwork > 0:
                    xm = self.x - buildings[j].x
                    xm = xm * xm
                    ym = self.y - buildings[j].y
                    ym = ym * ym
                    ds = math.sqrt(xm+ym)
                    
                    for i in eat:
                      eprice = buildings[j].prices[i]*dcourse[0]
                      amounteat2 = min(25-self.hap_eat, acmoney/eprice)
                      hape2 = (self.keats[i]+lvp)*amounteat2
                      if ds > 5:
                        lprior2 = hape2/ds
                      else:
                        lprior2 = hape2/5 - ds/10000000
                      if lprior2 > lprior:
                        lprior = lprior2
                        amounteat = amounteat2
                        lveat = i
                        xj = j
              
              self.pprice = buildings[xj].prices[lveat]
              self.aeat = amounteat
              self.teat = lveat
              self.xt = buildings[xj].x
              self.yt = buildings[xj].y
              self.state = 0
              self.type_target = 0
              self.number_target = xj
                
              self.target = buildings[xj]
              if buildings[xj].type != "eatmarket":
                buildings[xj].poutres[lveat] -= self.aeat
              self.wg = 0
              self.tupd("цена еды" + str( buildings[xj].prices[self.teat]*dcourse[0]) + "тип " + str(self.teat))
              self.tupd("акденьги" + str(acmoney))
              self.phap["food"] = updlist(self.phap["food"], 100)
            else:
              self.state = 2
              self.tupd("Нет еды на острове")
              self.phap["food"] = updlist(self.phap["food"], 0)
              #условие которое выполняется если еды нет
              
              
              
              
          if maxin == 0 and 1==0:
              self.hap_eat2 = 10
              cnte = 0
              for j in buildings:
                if j.f_eat_allow() == 1 and self.money > j.price*3:
                  cnte = 1
              if cnte == 1:
                self.type_target = 0
                self.phap["food"] = updlist(self.phap["food"], 100)
                acmoney = min(self.money, max(sqrt(self.money), self.salary)) #формула по которой расчитываются деньги
                amounteat = 0 #количество еды которое готов купить — зависит от цены еды и от acmoney -- от 0 до 25
                hape= 0#завтсит от количества еды и от коэфициента предпочтения данного вида еды — от 1 до 100
                xj = -1
                xs = 1000000
                for j in range(0, len(buildings)):
                  if buildings[j].f_eat_allow() == 1 and self.money > buildings[j].price:  #переделать условие, пока затычка
                        xm = self.x - buildings[j].x
                        xm = xm * xm
                        ym = self.y - buildings[j].y
                        ym = ym * ym
                        if xs > xm + ym + buildings[j].price:
                            xj = j
                            xs = xm + ym + buildings[j].price
                
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
                    print(self.id)
                    print("нет еды2, вот мой phap")
                    print(self.phap["food"])
              else:
                  maxin = maxin ##############################################
                  self.phap["food"] = updlist(self.phap["food"], 0)
                  #print(self.id)
                  #print("нет еды, вот мой phap")
                  #print(self.phap["food"])
                  #print()
              self.hap_eat2 = 10
          if maxin == 1:
              self.hap_health2 = 10
              cntc = 0
              for j in clinics:
                
                  cntc += j.amount
              if cntc > 0:
                
                self.type_target = 1
                #self.type_target == 1:
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
                self.phap["health"] = updlist(self.phap["health"], clinics[xj].quality)
              else:
                self.phap["health"] = updlist(self.phap["health"], 0)
                maxin = maxin #############################################
              self.hap_health2 = 10
          if maxin == 2:
              self.rest2 = 10
              if self.homenumber != -1:
                    self.type_target = 2
                
                    self.xt = homes[self.homenumber].x
                    self.yt = homes[self.homenumber].y
                    self.state = 0
                    self.tupd("Пойду посплю")
                    #print("chosen_rest")
                    self.target = homes[self.homenumber]
              else:
                self.findhome(buildings, homes)
              self.rest2 = 10
            
          if maxin == 3:
              self.wotworkt = 10
              if self.work_n != -1:
                    self.type_target = 3
                    self.wotworkt = 10
                    self.xt = buildings[self.work_n].x
                    self.yt = buildings[self.work_n].y
                    self.state = 0
                    self.tupd("Пора работать")
                    self.target = buildings[self.work_n]
                    self.wstage = 0
                    #print(self.id)
                    #print("пошел работать")
                    #print("target")
                    #print(self.target)
              else:
                self.findwork(buildings, homes)
                
                
              self.wotworkt = 10
            
          if maxin == 4:
              self.hap_fun2 = 10
              cntf = 0
              for j in buildings:
               if j.f_fun_allow() == 1 and j.f_visit_allow() == 1:
                cntf = 1
              if cntf == 1:
                self.type_target = 4
                self.type_target = 4
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
                    self.phap["fun"] = updlist(self.phap["fun"], buildings[xj].quality)
                else:
                  self.tupd("Сошел с ума от веселья")
              else:
                maxin = maxin##############################################
                self.phap["fun"] = updlist(self.phap["fun"], 0)


def human_func_think_relig(self, buildings, garages, clinics, homes, thlist=[]):
    FPS = FPSl[0]
    # self.gobylist([(1,1),(5,5),(1,3),(5,9)])
    # if self.target == 0 and len(buildings) > 0:
    # self.target = buildings[0] #какойьо костыль

    if self.type_target == 3:
        self.target = buildings[self.work_n]
    if self.findworkp == 1 and self.state == 2:
        self.findwork(buildings, homes)
        self.findworkp = 0
        self.wstage = 0
    if self.state == 2:
        regp = (10 - self.hap_reg2)
        funp = (10 - self.hap_fun2)
        healp = (10 - self.hap_health2)  # приоритет здоровья
        eatp = (10 - self.hap_eat2)  # приоритет еды
        restp = (10 - self.rest2)  # приоритет отдыха
        workp = max(10 - self.wotworkt, 0)
        priorl = [eatp, healp, restp, workp, funp, regp]
        if max(priorl) > 0.1:
            maxi = max(priorl)
            maxin = priorl.index(maxi)
            if maxin == 0:
                self.hap_eat2 = 10
                cnte = 0
                cnte2 = 0

                for j in buildings:
                    if j.f_eat_allow() == 1 and self.money > j.price * 3:
                        cnte = 1
                    if j.type == "eatmarket" and j.nwork > 0:
                        if self.money > j.prices["corn"] * 3 * dcourse[0]:
                            cnte2 = 1
                if cnte2 == 1 or cnte == 1:

                    # acmoney = min(self.money, max(math.sqrt(self.money), self.salary))
                    acmoney = self.money
                    amounteat = None
                    hape = 0
                    lprior = 0
                    lveat = None
                    xj = None
                    if self.hap_eat >= 10:
                        lvp = 0
                    else:
                        lvp = (10 - self.hap_eat) * 5
                    if cnte == 1:
                        for j in range(0, len(buildings)):
                            if buildings[j].f_eat_allow() == 1:
                                xm = self.x - buildings[j].x
                                xm = xm * xm
                                ym = self.y - buildings[j].y
                                ym = ym * ym
                                ds = math.sqrt(xm + ym)

                                for i in eat:
                                    eprice = buildings[j].prices[i]
                                    amounteat2 = min(25 - self.hap_eat, acmoney / eprice, buildings[j].poutres[i])
                                    hape2 = (self.keats[i] + lvp) * amounteat2
                                    # lprior2 = hape2/ds
                                    if ds > 5:
                                        lprior2 = hape2 / ds
                                    else:
                                        lprior2 = hape2 / 5
                                    if lprior2 > lprior:
                                        lprior = lprior2
                                        amounteat = amounteat2
                                        lveat = i
                                        xj = j
                    if cnte2 == 1:
                        for j in range(0, len(buildings)):
                            if buildings[j].type == "eatmarket" and buildings[j].nwork > 0:
                                xm = self.x - buildings[j].x
                                xm = xm * xm
                                ym = self.y - buildings[j].y
                                ym = ym * ym
                                ds = math.sqrt(xm + ym)

                                for i in eat:
                                    eprice = buildings[j].prices[i] * dcourse[0]
                                    amounteat2 = min(25 - self.hap_eat, acmoney / eprice)
                                    hape2 = (self.keats[i] + lvp) * amounteat2
                                    if ds > 5:
                                        lprior2 = hape2 / ds
                                    else:
                                        lprior2 = hape2 / 5 - ds / 10000000
                                    if lprior2 > lprior:
                                        lprior = lprior2
                                        amounteat = amounteat2
                                        lveat = i
                                        xj = j

                    self.pprice = buildings[xj].prices[lveat]
                    self.aeat = amounteat
                    self.teat = lveat
                    self.xt = buildings[xj].x
                    self.yt = buildings[xj].y
                    self.state = 0
                    self.type_target = 0
                    self.number_target = xj

                    self.target = buildings[xj]
                    if buildings[xj].type != "eatmarket":
                        buildings[xj].poutres[lveat] -= self.aeat
                    self.wg = 0
                    self.tupd("цена еды" + str(buildings[xj].prices[self.teat] * dcourse[0]) + "тип " + str(self.teat))
                    self.tupd("акденьги" + str(acmoney))
                    self.phap["food"] = updlist(self.phap["food"], 100)
                else:
                    self.state = 2
                    self.tupd("Нет еды на острове")
                    self.phap["food"] = updlist(self.phap["food"], 0)
                    # условие которое выполняется если еды нет

            if maxin == 0 and 1 == 0:
                self.hap_eat2 = 10
                cnte = 0
                for j in buildings:
                    if j.f_eat_allow() == 1 and self.money > j.price * 3:
                        cnte = 1
                if cnte == 1:
                    self.type_target = 0
                    self.phap["food"] = updlist(self.phap["food"], 100)
                    acmoney = min(self.money,
                                  max(sqrt(self.money), self.salary))  # формула по которой расчитываются деньги
                    amounteat = 0  # количество еды которое готов купить — зависит от цены еды и от acmoney -- от 0 до 25
                    hape = 0  # завтсит от количества еды и от коэфициента предпочтения данного вида еды — от 1 до 100
                    xj = -1
                    xs = 1000000
                    for j in range(0, len(buildings)):
                        if buildings[j].f_eat_allow() == 1 and self.money > buildings[
                            j].price:  # переделать условие, пока затычка
                            xm = self.x - buildings[j].x
                            xm = xm * xm
                            ym = self.y - buildings[j].y
                            ym = ym * ym
                            if xs > xm + ym + buildings[j].price:
                                xj = j
                                xs = xm + ym + buildings[j].price

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
                            meat = self.money / buildings[xj].price
                            self.pprice = buildings[xj].price
                            self.aeat = min(wa, meat, heat)
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
                            print(self.id)
                            print("нет еды2, вот мой phap")
                            print(self.phap["food"])
                else:
                    maxin = maxin  ##############################################
                    self.phap["food"] = updlist(self.phap["food"], 0)
                    # print(self.id)
                    # print("нет еды, вот мой phap")
                    # print(self.phap["food"])
                    # print()
                self.hap_eat2 = 10
            if maxin == 1:
                self.hap_health2 = 10
                cntc = 0
                for j in clinics:
                    cntc += j.amount
                if cntc > 0:

                    self.type_target = 1
                    # self.type_target == 1:
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
                    self.phap["health"] = updlist(self.phap["health"], clinics[xj].quality)
                else:
                    self.phap["health"] = updlist(self.phap["health"], 0)
                    maxin = maxin  #############################################
                self.hap_health2 = 10
            if maxin == 2:
                self.rest2 = 10
                if self.homenumber != -1:
                    self.type_target = 2

                    self.xt = homes[self.homenumber].x
                    self.yt = homes[self.homenumber].y
                    self.state = 0
                    self.tupd("Пойду посплю")
                    # print("chosen_rest")
                    self.target = homes[self.homenumber]
                else:
                    self.findhome(buildings, homes)
                self.rest2 = 10

            if maxin == 3:
                self.wotworkt = 10
                if self.work_n != -1:
                    self.type_target = 3
                    self.wotworkt = 10
                    self.xt = buildings[self.work_n].x
                    self.yt = buildings[self.work_n].y
                    self.state = 0
                    self.tupd("Пора работать")
                    self.target = buildings[self.work_n]
                    self.wstage = 0
                    # print(self.id)
                    # print("пошел работать")
                    # print("target")
                    # print(self.target)
                else:
                    self.findwork(buildings, homes)

                self.wotworkt = 10

            if maxin == 5:
                self.hap_reg2 = 10
                cntf = 0
                for i in buildings:
                    if i.type == "church" or i.type == "sobor":
                        if len(i.visiters) < i.max_visiters:
                           cntf = 1
                if cntf == 1:
                    self.type_target = 4
                    self.type_target = 4
                    xj = -1
                    xs = 10000000000000000
                    for j in range(0, len(buildings)):
                        i = buildings[j]
                        if i.type == "church" or i.type == "sobor":
                            if len(i.visiters) < i.max_visiters:  # переделать условие, пока затычка
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
                        self.phap["religion"] = updlist(self.phap["religion"], buildings[xj].quality)
                    else:
                        self.tupd("Сошел с ума от веселья")
                else:
                    maxin = maxin  ##############################################
                    self.phap["religion"] = updlist(self.phap["religion"], 0)

            if maxin == 4:
                self.hap_fun2 = 10
                cntf = 0
                for j in buildings:
                    if j.f_fun_allow() == 1 and j.f_visit_allow() == 1:
                        cntf = 1
                if cntf == 1:
                    self.type_target = 4
                    self.type_target = 4
                    xj = -1
                    xs = 10000000000000000
                    for j in range(0, len(buildings)):
                        if buildings[j].f_fun_allow() == 1:  # переделать условие, пока затычка
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
                        self.phap["fun"] = updlist(self.phap["fun"], buildings[xj].quality)
                    else:
                        self.tupd("Сошел с ума от веселья")
                else:
                    maxin = maxin  ##############################################
                    self.phap["fun"] = updlist(self.phap["fun"], 0)


#архивные, сейсас неиспользуемые функции
def reserve_func_think2(self, buildings, garages, clinics, homes, thlist = []):
        FPS = FPSl[0]
        if self.target == 0 and len(buildings) > 0:
          self.target = buildings[0]
        if self.state == 2:
         if self.findworkp ==1:
          self.findwork(buildings, homes)
          self.findworkp = 0
          self.wstage = 0
         thinkmaxmoney = 100
         funp = (10 - self.hap_fun) 
         healp = (10 - self.hap_health)   # приоритет здоровья
         eatp = (10 - self.hap_eat)   # приоритет еды
         restp = (10 - self.rest)   # приоритет отдыха
         if allmrot["eat"][-1]!= "None":
           workp = (max(100, allmrot["eat"][-1]*2) - self.money)/10  # приоритет работы, сделать так что зависит от средней зп и от зп чела или от прожиточного минимума
         else: 
           workp = 11
         workp = max(10- self.wotworkt, 0)
         self.wwt += 1/FPS/10
        if self.state == 2:  # как думает куда идти
            self.p1 = healp
            self.p2 = eatp
            self.p3 = restp
            self.p4 = workp
            self.p5 = funp
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
                #print(homes)
                self.findhome(buildings, homes)
                self.p3 = -4
                #pri("nohome")

            if self.work_n != -1:  # 2
                priorl.append(workp)
            else:
                priorl.append(-100000000000000000)
                
                self.findwork(buildings, homes)
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
                xs = 1000000
                for j in range(0, len(buildings)):
                    if buildings[j].f_eat_allow() == 1 and self.money > buildings[j].price:  #переделать условие, пока затычка
                        xm = self.x - buildings[j].x
                        xm = xm * xm
                        ym = self.y - buildings[j].y
                        ym = ym * ym
                        if xs > xm + ym + buildings[j].price:
                            xj = j
                            xs = xm + ym + buildings[j].price
                
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
                    self.tupd("Сошел с ума от мыслей о еде")
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
                    self.wotworkt = 10
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
def reserve_func_gotocw3(self, gxt,gyt):
        FPS = FPSl[0]
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

                