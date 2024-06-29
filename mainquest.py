from fractions import *
#from family import *







def addhuman3(nhum=1, xhum = 0, yhum = 0):
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
    

    humans.append(j)
    families.append(fam)
    hbut = button(100, 26*i, 100,25)
    hbut.text = j.name
    buttonshuman.append(hbut)

class mainquest(object):
  def __init__(self, quest = None):
    self.electionquest = None
    self.govquest = None
    self.questlist = [quest]
    self.quest = quest
    self.cnt = 0
    self.infolist = [quest]
    self.infomarker = None
    self.markerfind = False
  def infoshow(self):
    self.infolist = self.questlist.copy()
    if self.infomarker == None:
      self.markerfind = True
    for i in range(0,len(self.infolist)):
      si = self.infolist[i]
      if si.stage == None or si.ended == True or si.stage not in si.infoshows:
        self.infolist[i] = 0
        if self.infomarker == i:
          self.markerfind = True
      elif self.markerfind == True:
        self.markerfind = False
        self.infomarker = i
    if self.markerfind == False:
      self.infolist[self.infomarker].infoshow()
      
  def markerright(self):
    self.infolist = self.questlist.copy()
    for i in range(0,len(self.infolist)):
      si = self.infolist[i]
      if si.stage == None or si.ended == True or si.stage not in si.infoshows:
        self.infolist[i] = 0
    if self.infomarker != None and self.markerfind != True:
      l = len(self.infolist)
      cnt = 0
      mark = self.infomarker
      chec = 0
      contin = 1
      while cnt <= l:
        cnt += 1
        if contin == 1:
          if mark+1 < l:
            mark += 1
          else:
            mark = 0
          if self.infolist[mark] != 0:
            contin = 0
            chec = 1
      self.infomarker = mark
        
  def sublife(self):
    for i in self.questlist:
      if i.stage != None and i.ended == False:
        i.sublifef()
  def life(self):
    i = self.questlist[self.cnt]
    if i.begin == True:
          i.beginstage(0)
          #i.beginstages[0](i)
          i.begin = "begun"
    if i.stage != None and i.ended == False:
        i.life()
        
    if self.quest != None:
      self.quest.beginstage(0)
      self.quest = None
    if self.cnt < len(self.questlist)-1:
        self.cnt += 1
    else:
      self.cnt = 0
  def add(self, quest, usl = None):
    self.questlist.append(quest)
  def activatequest(self, name, stage = 0):
    for i in self.questlist:
      if i.name == name:
        i.beginstage(stage)
class quest(object):
  def __init__(self, name = None):
    self.name = name
    self.stage = None
    self.begin = False
    self.stages = []
    self.infoshows = {}#словарь который сопоставляет каждому stage словарь, который уходит в questwindow
    self.endstages = {}
    self.beginstages = {}
    self.checks = {}
    self.sublifes = {}
    self.parametrs = {}
    self.ended = False
    self.sublife = False
    self.time = 0

  def sublifef(self):
    if self.sublife == True:
      if self.stage in self.sublifes:
        #self.sublifes[self.stage](self)
        if self.sublifes[self.stage](self) == True:
          self.sublife = False
          questwindow["close"] = True
          questwindow["output"] = None
  def life(self):
    
    if self.check() == True:
      self.endstage()
  def check(self):
    #for i self.stages:
      #if self.stage == i:
    if self.checks[self.stage](self) == True:
      return True
      
  def infoshow(self):
    li = self.infoshows[self.stage]
    lw = questwindow
    lw["turn"] = True
    mainquests[0].infomarker = mainquests[0].questlist.index(self)

    for i in li:
      lw[i]= li[i]
  def endstage(self):
    self.endstages[self.stage](self)
  def beginstage(self, stage):
    questwindow["output"] = None
    self.stage = stage
    self.beginstages[self.stage](self)
que2 = quest()
#пример квеста из нескольких стадий. 
#стадия 1 — нужно построить ферму. награда — 100000 долларов
#стадия 2 — нужно скопить на счету 100000 рублей. Награда — 200 иммигрантов
def c0(self):
  cnt = 0

  for i in buildings:
    if i.type == "farm" and i.bready == 1:
      cnt += 1
  if cnt >= self.parametrs["farm"]+1:

    return True
    
  else:

    return False
    
def c1(par):
  if money[0]>= 100000:
    return True
  else:
    return False
    
def c2(par):
  if dcourse[0]>= 100000:
    return True
  else:
    return False
def c3(par):
  if allhap["food"][-1] >= 20:
    return True
  else:
    return False
def c5(self):
  cnt = 0
  for i in buildings:
    if i.type == "lumber" and i.bready == 1:
      cnt += 1
  if cnt >= self.parametrs["lumber"]+1:
    return True
  else:
    return False
def c6(self):
  if len(garages)>= self.parametrs["garage"]+1:
    return True
    
def c7(self):
  if growthdi["avsalary"][-1] > 100000:
    cnt = 0
    for i in buildings:
     if i.type == "eatmarket" and i.bready == 1:
      cnt += 1
    if cnt > 0:
      return True
def c8(self):
  cnt = 0
  for i in buildings:

    if i.type == "tavern" and i.bready == 1:
      cnt += 1
  
  if cnt >= self.parametrs["tavern"]+1:

    return True
  else:
    return False
def c9(self):
  if outincomedi["main"][-1] >= self.parametrs["income"] + 10000:
    return True
def c10(self):
  cnt = 0
  for i in buildings:
    if i.type == "cheese" and i.bready == 1:
      cnt += 1
  if cnt >= self.parametrs["cheese"]+10:
    return True
  else:
    return False
    
qcheck = {
  0:c0,
  1:c1,
  2:c2,
  3:c3,
  5:c5,
  6:c6,
  7:c7,
  8:c8,
  9:c9,
  10:c10
}

def b0(self):
  cnt = 0
  for i in buildings:
    if i.type == "farm":
      cnt += 1
  self.parametrs["farm"] = cnt
  self.infoshow()
def b1(self):
  self.infoshow()
def b2(self):
  self.infoshow()
def b5(self):
  self.infoshow()
  cnt = 0
  for i in buildings:
    if i.type == "lumber":
      cnt += 1
  self.parametrs["lumber"] = cnt
def b6(self):
  self.infoshow()
  self.parametrs["garage"] = len(garages)
def b8(self):

  cnt = 0
  for i in buildings:
    if i.type == "tavern":
      cnt += 1
  self.parametrs["tavern"] = cnt

  self.infoshow()
def b9(self):
  self.parametrs["income"] = outincomedi["main"][-1]
  self.infoshow()
def b10(self):
  cnt = 0
  for i in buildings:
    if i.type == "cheese":
      cnt += 1
  self.parametrs["cheese"] = cnt
  self.infoshow()
qbeg = {
  0:b0,
  1:b1,
  2:b2,
  3:b2,
  4:b2,
  5:b5,
  6:b6,
  7:b2,
  8:b8,
  9:b9,
  10:b10
  
}

def q0(self):
  money[1] += 100000
  self.beginstage(3)
def q1(self):
  addhuman3(250)
  self.beginstage(2)
def q2(self):
  #addhuman3(250)
  self.beginstage(3)
def q3(self):
  #money[1] += 100000
  self.beginstage(5)
def q4(self):
  #money[1] += 100000
  self.beginstage(5)
def q5(self):
  #money[1] += 100000
  self.beginstage(6)
def q6(self):
  #money[1] += 100000
  self.beginstage(7)
def q7(self):
  #money[1] += 100000
  self.beginstage(8)
def q8(self):
  #money[1] += 100000
  self.beginstage(9)
def q9(self):
  #money[1] += 100000
  self.beginstage(10)
def q10(self):
  #money[1] += 100000
  self.beginstage(1)
qend = {
  0:q0,
  1:q1,
  2:q2,
  3:q3,
  4:q4,
  5:q5,
  6:q6,
  7:q7,
  8:q8,
  9:q9,
  10:q10
}

i0 = {
  "turn":True,
  "name":"Андрей Померанцев",
  "description": "Привет! (Я автор этой игры). Я назначил тебя править островом. В общем, мы с его величеством решили, что ты прекрасно справишься с управлением колонией, Губернатор. Сейчас остров пережил непростые времена, ураган снёс почти всё. Твоя цель — восстановить остров. Мы будет тебе в этом помогать, чем можем, первое время",
  "target":"Цель: построить Ферму",
  "reward":"Награда: 100000 долларов",
  "option1":False,
  "option2":False,
  "option3":False,
  "accept":False,
  "close":True,
  "output":None
}

i1 = {
  "turn":True,
  "name":"Андрей Померанцев",
  "description": "Супер, остров начинает восстанавливаться. Я положил тебе немного денег на счет, чтобы тебе было проще выполнять свои обязанности. Но у Вас на острове там своя валюта вроде ходит.. Просто вот так вот перевести денег из одной валюту в другую не выйдет, сумма гигантская, просто курс обвалится на такой неликвидный товар. В общем сделай мне на острове 100000 рублей, ок?",
  "target":"Цель: накопить 100000 рублей",
  "reward":"Награда: 200 иммигрантов",
  "option1":False,
  "option2":False,
  "option3":False,
  "accept":False,
  "close":True,
  "output": None
}

i2 = {
  "turn":True,
  "name":"Андрей Померанцев",
  "description": "Хаха, круто, остров начинает жить. Но знаешь, эти вот, хм, люди.. слишком много едят. Причем еды импортной. сделай так, чтобы у них на это не хватило денег. Пусть курс местной валюты будет... 10000! Да, думаю норм. Выполни и потом поговорим. Ахаха",
  "target":"Цель: курс фунта должен достичь 10000",
  "reward":"следующее задание",
  "option1":False,
  "option2":False,
  "option3":False,
  "accept":False,
  "close":True,
  "output": None
}

i3 = {
  "turn":True,
  "name":"Андрей Померанцев",
  "description": "Теперь, когда у тебя есть ферма, нужно им, едой заниматься. Нужно достичь уровня удовлетворенности едой 20. Вот",
  "target":"Цель: уровень удовлетворенности едой должен быть больше 20",
  "reward":"Награда: следующее задание",
  "option1":False,
  "option2":False,
  "option3":False,
  "accept":False,
  "close":True,
  "output": None
}

i5 = {
  "turn":True,
  "name":"Андрей Померанцев",
  "description": "Его величество накануне осенило, как решить все проблемы твоего острова постройкой одного здания. Тебе нужно построить.. Лесопилку!",
  "target":"Цель: построить лесопилку",
  "reward":"Награда: следующее задание",
  "option1":False,
  "option2":False,
  "option3":False,
  "accept":False,
  "close":True,
  "output": None
}

i7 = {
  "turn":True,
  "name":"Андрей Померанцев",
  "description": "Слушай, я тут посмотрел.. бедно у тебя люди живут. Но не волнуйся, ты же можешь печатать деньги сколько угодно.. Так почему бы этим не воспользоваться? Давай просто импортируем на остров еду. Смори как — житель будет заказывать еду на остров, идти в банк, обменивать местную валюту на фунт, а затем приходить за едой и оплачивать её! Мои друзья возьмут только 20 процентов за доставку, а так.. Ну и да повысь им зарплату. Ну, в среднем до 100000. Чтобы уж наверняка",
  "reward":"Награда: следующее задание",
  "target":"Цель: средний уровень зарплаты выше 100000, построить маркет еды",
  "option1":False,
  "option2":False,
  "option3":False,
  "accept":False,
  "close":True,
  "output": None
}

i6 = {
  "turn":True,
  "name":"Лорд Оуксворд",
  "description": "Здравствуйте, Губернатор. Я Лорд Оуксворд, официальный представитель Его Величества в этом регионе. До меня дошли слухи, что некий Андрей Померанцев, обращаясь от имени представителя Короны к Вам и другим Губернаторам выдает странные поручения. Ваш остров был выбран его Величеством как.. тайный агент. Продолжайте пока выполнять его поручения, чтобы он ни о чем не догадался, и постепенно мы выясним, что он задумал. А пока, постройте Гараж",
  "reward":"Награда: следующее задание",
  "target":"Цель: построить Гараж",
  "option1":False,
  "option2":False,
  "option3":False,
  "accept":False,
  "close":True,
  "output": None
}

i8 = {
  "turn":True,
  "name":"Лорд Оуксворд",
  "description": "Губернатор, у меня для Вас новое задание. Нашим агентам стало известно, что Андрей Померанцев планирует посетить Ваш остров. Вам нужно организовать ему прием, например, показав местный театр. Постройте театр по нашему специальному чертежу. В этом здании будет что-то вроде ловушки. Мы пошлём на остров наших агентов чтобы захватить Померанцева и допросить",
  "reward":"Награда: следующее задание",
  "target":"Цель: построить Театр",
  "option1":False,
  "option2":False,
  "option3":False,
  "accept":False,
  "close":True,
  "output": None
}

i9 = {
  "turn":True,
  "name":"Лорд Оуксворд",
  "description": "Губернатор, благодаря Вам мы узнали всю информцию об этом персонаже. Он втирался в доверие к Губернаторам разных островов, чтобы вовлечь их в какую-то.. мой банкир назвал это финансовой пирамидой. Я вижу, среди его писем, что он поручил Вам повысить зарплаты и распечатать денег. Как видите, это ни к чему не привело, кроме того что ваши деньги стали стоить.. меньше. Я знаю способ, как снова сделать так, чтобы ваши деньги хоть сколько-то стоили. Вам нужно увеличить экспорт. Ну и снизить зарплаты, если Вы еще этого не сделали. Король как раз скоро будет отмечать день рождения и ему нужен сахар.",
  "reward":"Награда: следующее задание",
  "target":"Цель: экспортировать товаров на 10000 долларов",
  "option1":False,
  "option2":False,
  "option3":False,
  "accept":False,
  "close":True,
  "output": None
}

i10 = {
  "turn":True,
  "name":"Лорд Оуксворд",
  "description": "Губернатор, хоть вы и нарвались на этого проходимца, но я заметил, что остров не только восстановился после Бури, но и начал, по местным меркам, процветать. Его Величество оценило результативность Вашей работы и решило, что дальнейшее пребывание Вас на этой должности, скажем так, не имеет смысла. Мы решили, что лучшим применением Ваших способностей будет управление островом в паре миль отсюда. Но Ваша работа здесь еще не завершена. Вам нужно построить Сыроварню. Точнее, 10 Сыроварен. Его величество очень любит сыр.",
  "reward":"Награда: победа в задании",
  "target":"Цель: построить здание — Сыроварня — в количестве 10",
  "option1":False,
  "option2":False,
  "option3":False,
  "accept":False,
  "close":True,
  "output": None
}

qinfo = {
  0:i0,
  1:i1,
  2:i2,
  3:i3,
  5:i5,
  6:i6,
  7:i7,
  8:i8,
  9:i9,
  10:i10
}

que2.infoshows = qinfo
que2.endstages = qend
que2.beginstages = qbeg
que2.checks = qcheck

#mainquests = [mainquest(que)]

############################
#electionquest и govquest
#govquest дает возможность продлить полномочия президентэ путем выполнения заданий короны
#election -- проводятся выборы
#еще должен быть квест революцтонеров, при завершении которого отключается qovquest и закускается electionquest
#оба квеста цикличны и не могут быть активны одновременно
#electionquest -- описание стадий.
#стадия 0 -- начало срока. Фиксирует текущую дату на старте.
#. условие проверки окончания стадии 1 — (срок президентства - 1) * 12 месяцев со стартового времени. При завершении стадии запускается стадия 99, если опция отмены выборов включена и стадия 100, если такой опции нет
#. стадия 99 — перед предвыборной компанией. Должно запрашиваться разрешение президента на проведение выборов. Если выборы проведены, то запускается стадия 150, если нет, то стадия 1
# стадия 100 — уведомляет президента о грядущих выборах. И сразу запускает стадию 150
# стадия 150 -- уведомлений нет. Фиксирует время, запускает условие проверки (11 месяцев), при завершении запускает стадию 190 или стадию 189
#стадия 189 — уведомление о выборах.
# стадия 190 — Президенте выбирает, фальсифицировать выборы или нет. Выбор отображается в параметрах квеста
# стадии 189 и 190 фиксируют время, отсчитывают 1 месяц и запускают стадию 200
# стадия 200 — в самом начале определяет, выиграл президентэ выборы или нет, если нет, то сразу переводит квест в стадию 999, если да, то уведомляет о победе и, пропускает проверку и при завершении переходит в стадию 0
#стадия 999 уведомляет о проигрыше и по идее игра должна закончиться

def b0(self):
  self.parametrs["begin"] = timelist[0]

  self.infoshow()
def c0(self):

  if timelist[0]>= self.parametrs["begin"] + 48:
    return True
def e0(self):
  self.beginstage(99)

i0 = {
  "turn":True,
  "name":"Советник",
  "description": "Президенте, начался ваш новый срок! Используйте его с умом, и может быть, вас выберут еще раз",
  "reward":False,
  "target":False,
  "option1":False,
  "option2":False,
  "option3":False,
  "accept":False,
  "close":True,
  "output": None
}

def b99(self):
  #self.parametrs["begin"] = timelist[0]
  self.sublife = True
  self.infoshow()
  
def c99(self):
  #if timelist[0]>= self.parametrs["begin"] + 4*12:
    return True
def e99(self):
  if self.parametrs["election"] == True:
    self.beginstage(150)
  if self.parametrs["election"] == False:
    self.beginstage(0)
def sf99(self):
  print(questwindow["output"])
  if questwindow["output"] == 1:
    self.parametrs["election"] = True
    return True
  if questwindow["output"] == 2:
    self.parametrs["election"] = False
    return True
i99= {
  "turn":True,
  "name":"Советник",
  "description": "Президенте, нужно выбрать, проводить выборы или нет!",
  "reward":False,
  "target":False,
  "option1":"Провести выборы",
  "option2":"Не проводить",
  "option3":False,
  "accept":False,
  "close":False
}

def b150(self):
  self.parametrs["begin"] = timelist[0]
  #self.infoshow()
def c150(self):
  if timelist[0]>= self.parametrs["begin"] + 11:
    return True
def e150(self):
  self.beginstage(190)
  
  
def sf190(self):
  if questwindow["output"] == 1:
    self.parametrs["falsif"] = True
    return True
  if questwindow["output"] == 2:
    self.parametrs["falsif"] = False
    return True
def b190(self):
  self.parametrs["begin"] = timelist[0]
  #self.infoshow()
  self.sublife = True
  self.infoshows[190]["description"] = "Президенте, нужно выбрать, нам нужны фальсификации или нет! Сейчас за вас готовы проголосовать " + str(numberfor(30)) + "а против вас выступает " + str(numberagainst(30)) + "граждан"
  self.infoshow()
def c190(self):
  if timelist[0]>= self.parametrs["begin"] + 1:
    return True
def e190(self):
  self.beginstage(200)

def numberfor(n):
  lcnt = 0
  for i in humans:
    if i.happiness["main"] >= n:
      lcnt += 1
  return lcnt
def numberagainst(n):
  lcnt = 0
  for i in humans:
    if i.happiness["main"] < n:
      lcnt += 1
  return lcnt

i190= {
  "turn":True,
  "name":"Советник",
  "description": "Президенте, нужно выбрать, нам нужны фальсификации или нет!",
  "reward":False,
  "target":False,
  "option1":"Фальсифицировать",
  "option2":"Не фальсифицировать",
  "option3":False,
  "accept":False,
  "close":False
}

def presidentwin(fals = False, porog = 50, other = None):
  ls = set()



  lvar2 = random.randint(50, 90)
  for i in humans:
    lvar = random.randint(0,100)
    if lvar < lvar2:
      ls.add(i)
  cntfor = 0
  cntagainst = 0

  for i in ls:
    if i.happiness["main"] >= porog:
      cntfor += 1

  for i in ls:
    if i.happiness["main"] < porog:
      cntagainst += 1

  dopvotes = 0
  if fals == True:
    dvp = random.randint(4, 20)

    dopvotes = max(2, dvp/100*dvp)

  if (cntfor + dopvotes) >= cntagainst:
    return (True, cntfor, cntagainst, dopvotes)
  else:
    return (False, cntfor, cntagainst, dopvotes)






def b200(self):
  #self.parametrs["begin"] = timelist[0]
  #self.infoshow()
  #self.sublife = True
  #здесь должна быть функция которая определит, проиграл выборы президентэ или нет

  winstat = presidentwin(self.parametrs["falsif"], 30)

  self.parametrs["win"] = winstat[0]

  if self.parametrs["win"] == True:
    if self.parametrs["falsif"] == True:
      self.infoshows[200]["description"] = "Пусть и не очень честно, но вы победили в выборах. За вас высказалось " + str(winstat[1]) + " граждан, а против вас " + str(winstat[2]) + ", еще " + str(winstat[3]) + " мы переубедили проголосовать за Вас."
    if self.parametrs["falsif"] == False:
      self.infoshows[200]["description"] = "Вы победили в выборах.  За вас высказалось " + str(winstat[1]) + " граждан, а против вас " + str(winstat[2])

  if self.parametrs["win"] == False:


    self.infoshows[200]["description"] = "Вы проиграли в выборах. За вас высказалось " + str(winstat[1]) + " граждан, а против вас " + str(winstat[2])
  self.infoshow()
def c200(self):
  return True
def e200(self):
  if self.parametrs["win"] == True:
    self.beginstage(0)
  if self.parametrs["win"] == False:
    self.beginstage(999)

i200= {
  "turn":True,
  "name":"Советник",
  "description": "этого текста не должно быть в игре",
  "reward":False,
  "target":False,
  "option1":False,
  "option2":False,
  "option3":False,
  "accept":False,
  "close":True
}

def b999(self):
  self.infoshow()

def c999(self):
  return True

def e999(self):
  self.stage = None
  self.ended = True


  
i999= {
  "turn":True,
  "name":"Советник",
  "description": "Увы и ах, но мы проиграли. Люди не оценили Ваших идей — может быть, им еще не пришло время. В любом случае нам нужно уезжать отсюда как можно быстрее. У меня как раз была приготовлена на этот случай спасательная лодка. Может быть, на следующем острове Вам повезёт больше..",
  "reward":False,
  "target":False,
  "option1":False,
  "option2":False,
  "option3":False,
  "accept":False,
  "close":True
}
eqi = {
  0:i0,
  99:i99,
  190:i190,
  200:i200,
  999:i999
}
eqb = {
  0:b0,
  99:b99,
  150:b150,
  190:b190,
  200:b200,
  999:b999
}

eqe = {
  0:e0,
  99:e99,
  150:e150,
  190:e190,
  200:e200,
  999:e999
}

eqc = {
  0:c0,
  99:c99,
  150:c150,
  190:c190,
  200:c200,
  999:c999
}
eqsf = {
  99:sf99,
  190:sf190
}
que = quest() #собираем квест
que.infoshows = eqi #то что игра будет показывать на экране (описание квеста)
que.endstages = eqe #то что происходит по завершении квеста
que.beginstages = eqb #то что происходит в начале квеста
que.checks = eqc #проверки для перехода на следующкю стадию
que.sublifes = eqsf
que.begin  = True
mainq = mainquest(que2)
mainq.add(que) #добавляем квест в менеджер квестов
mainq.electionquest = que
mainquests = [mainq] #вспавляем менеджер в список, который будет обрабатываться главным файлом