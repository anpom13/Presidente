import pygame
from lists import *
import textwrap

def testfun():
  print(1313)


class button(object):
  def __init__(self, x = 0, y = 0, xx = 100, yy = 100, type = 0, col = (255,255,255), text = "кнопка", altype = "income",altype1 = "income", altype2 = "main",text0 = "", textscale = None, wrap = None):
    self.x = x
    self.y = y
    self.xx = xx 
    self.yy = yy
    self.type = type #квадрат/круг
    self.color = col
    self.instate = 0
    self.instate2 = 0
    self.text = text
    self.text0 = text0
    self.active =1
    self.altype = altype
    self.altype1 = altype1
    self.altype2 = altype2
    self.pressf = testfun
    
    self.mtif = 1000
    self.textscale = textscale
    self.wrap = wrap
  def draw(self):
    if self.type == 0 and self.active == 1:
      pygame.draw.rect(sc, self.color, (self.x, self.y, self.xx, self.yy))
      #pygame.font.init()
      self.text = str(self.text)
      if len(self.text) > 0:
        i = min(round(self.xx*40/100*6/len(self.text)), int(self.yy), self.mtif)
        #i = int(self.yy)
      else:
        i = 1
      if self.textscale != None:
        i = self.textscale
      f1 = pygame.font.SysFont('arial', i)
      if self.wrap!=None:
        wrap = self.wrap
      else:
        wrap = int(self.xx/i*5)
      wrapped_text = textwrap.wrap(self.text+self.text0, wrap )
      for j, line in enumerate(wrapped_text):
        rendered_text = f1.render(line, True, (180, 0, 0))
        sc.blit(rendered_text, ( self.x,self.y + j * i))
      #text1 = f1.render(self.text+self.text0, True,
                      #(180, 0, 0))
      #sc.blit(text1, (self.x,self.y))
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

    else:
      zagl = []

  def life():
    if self.pressf != None:
      if self.press()==1:
        self.pressf()
  def click(self):
    if self.press()==1:
      if mdownevent[0] == 1:
        return 1
    ev = pygame.event.get()
    
    for event in ev:
      if event.type == pygame.MOUSEBUTTONDOWN and self.active == 1:
         pos = pygame.mouse.get_pos()
         if pos[0] >= self.x and pos[0] <=self.xx+self.x and pos[1]>=self.y and pos[1] <= self.yy+self.y:
              return 1
         else:
           return 0
def setbtext():
  butdisprice[0].text = " + "
  butdisprice[1].text = " - "
  butdisprice[2].text = " + "
  butdisprice[3].text = " - "
  
buttons = [
  button(5, 5, text = "Строительство"), 
  button(w-110,110, text = "+"), 
button(w-110, 220, text = "-"), 
button(0,h/2, text = "Строит"), 

button(w-60,10,50,50,0,(100,100,100)), 
button(w-120,10,50,50,0,(100,100,150)), 
button(w-180,10,50,50,0,(100,200,150)), 


button(110, 10, 100,30), 
button(220, 10, 100,30), 
button(330, 10, 100, 30), 
button(550,10, 100, 40, text = "Меню"),  
button(660,10, 100, 40, text = "Слои"),
button(440,10, 100, 30, text = "Деньги 2"),#12
button(10,200, 50, 50, text = "Квест") #13

#12
] #4 5 6 -- скорость игры 7 -- строить дом 8 —
# 0 build mode switcher 12 масштаб 3 строить


#buttons[0].text = "Строительство"

buttons[4].text = " >> "
buttons[5].text = " > "
buttons[6].text = "II"

bxx = 80
buttons2 = [
  button(text = "дорога"),# в будущем, наверное, стоит переделать так чтобы она была не квадратиками, а линиями
  button(text = "гараж"),# нужно добавить waitlist для жителей, которые хотят выехать из гаража
  button(text = "порт"),
  button(text = "грузы"),#здание не совсем корректно работает, есть проблемы с pinres 2) нужно убрать зависимость величины склада от зарплаты рабочих
  button(text = "электро"),
  button(text = "подстанция"),
  button(text = "строит"),
  button(text = "атом"),
  button(text = "droad"),
  button(text = ""),#мб добавить метро, автобусные станции
  
  button(text = "ферма\nобычная"),#переделать так чтобы производительность зависела от соответствующего слоя (подумать как), переделать потребление еды (сейчас люди идут каждый раз покупать еду, нужно чтобы они делали запасы дома и ели уже там), в infodis добавить возможность не предоставлять её жителям
  button(text = "ранчо"),
  button(text = "рынок"),
  button(text = "шахта"),
  button(text = "лес"),
  button(text = ""), button(text = ""), button(text = ""), button(text = ""),button(text = ""),
  #тут нужно будет добавить настроек к зданиям (через infodis) и сделать так чтобы в некоторых из них можно было нанимать только рабочих с образованием
  button(text = "доски"),
  button(text =  "сигар"),
  button(text =  "ром"),
  button(text =  "ювелир"),
  button(text =  "фурнитура"),
  button(text =  "консервы"),
  button(text =  "оружие"),
  button(text ="сыр"  ),
  button(text =""  ),
  button(text =  ""),
  #для корректрой работы зданий нужно: 1) доработать модуль family 2) доработать функцию findhome класса human (перенести её в класс family) 3) внедрить алгоритм постройки палатки/лачуги с качеством жилья 10 (если жилье не найдено)
  button(text = "хибар"),
  button(text ="барак"  ),
  button(text ="фазенда"  ),
  button(text =  "дом"),
  button(text ="усадьба"  ),
  button(text ="хрущев"  ),
  button(text ="аппарт"  ),
  button(text ="комун"  ),
  button(text =""  ),
  button(text =""  ),
  
  button(text = "школа"),
  button(text =  "вуз-"),
  button(text =  "аптека"),
  button(text ="клиника-"  ),
  button(text ="больница-"  ),
  button(text ="газета-"  ),
  button(text ="радио-"  ),
  button(text ="тв"  ),
  button(text =""  ),
  button(text =""  ),
  
  button(text = "имиграция-+"),#для того чтобы работало норм, нужен модуль growth
  button(text =  "банк-"),#на первом этапе настройки в infodis
  button(text ="минфин-"  ),#на первом этапе настройки в infodis
  button(text ="полиция-"  ),
  button(text =  "казармы-"),
  button(text =""  ),
  button(text =""  ),
  button(text =""  ),
  button(text =  ""),
  button(text =""  ),
  
  button(text = "театр"),
  button(text ="маркет"  ),#нужно добавить p maxvisiters и f workeatmarket 
  button(text =""  ),
  button(text =  ""),
  button(text =""  ),
  button(text =""  ),
  button(text =""  ),
  button(text =""  ),
  button(text =""  ),
  button(text =""  ),
  
  button(text = "сад"),
  button(text =""  ),
  button(text =""  ),
  button(text =  ""),
  button(text =""  ),
  button(text =""  ),
  button(text =""  ),
  button(text =""  ),
  button(text =""  ),
  button(text =""  ),
  
#button(0,h-80, 70,70, text = "дом"), 
#button(80,h-80, bxx, bxx, text = "ферма"), 
#button(160,h-80, bxx, bxx, text = "клиника"),  
#button(240,h-80, bxx, bxx, text = "дорога"), 
#button(320,h-80, bxx, bxx, text = "гараж"), 
#button(400,h-80, bxx, bxx, text = "грузы"), 
#button(480,h-80,bxx, bxx, text = "порт" ), 
#button(560,h-80,bxx, bxx, text =  "магаз"),
#button(640,h-80, bxx, bxx, text = "имиграция" ),  
#button(0,h-160, bxx, bxx, text = "ранчо"),
#button(80,h-160, bxx, bxx, text = "театр"), 
#button(160,h-160, bxx, bxx, text = "ром"),  
#button(240,h-160,bxx, bxx, text = "консервы" ), 
#button(320,h-160,bxx, bxx, text = "сыр" ), 
#button(400,h-160,bxx, bxx, text = "сигареты" ),
#button(480,h-160, bxx, bxx, text = "Строит"), 
#button(560,h-160, bxx, bxx, text = "Элект") ,
#button(640,h-160,bxx, bxx, text = "Шахта" ),
#button(720,h-160, bxx, bxx, text = "Сад"),
#button(720, h-80, bxx,bxx,text = "Школа"),
#button(800, h-80, bxx,bxx,text = "вуз"),
#button(800, h-160, bxx,bxx,text = "Газета"),
#button(880, h-160, bxx,bxx,text = "Droad"),
#button(10, h-240, bxx,bxx,text = "лес"),#23
#button(90, h-240, bxx,bxx,text = "Доски"),
#button(170, h-240, bxx,bxx,text = "Мебель"),
#button(250, h-240, bxx,bxx,text = "Ювелир"),
#button(330, h-240, bxx,bxx,text = "Оружие"),
#button(410, h-240, bxx,bxx,text = "подстанц"),
#button(490, h-240, bxx,bxx,text = "атом"),
#button(570, h-240, bxx,bxx,text = "клиник2"),
#button(650, h-240, bxx,bxx,text = "больниц"),
#button(730, h-240, bxx,bxx,text = "радио"),
#button(810, h-240, bxx,bxx,text = "тв"),
#button(890, h-240, bxx,bxx,text = "цб"),
#button(890, h-160, bxx,bxx,text = "маркет")
]
b2var = 0
for i in range(0, len(buttons2)):
  if b2var<10:
    buttons2[i].x = 10+ (bxx+10)*b2var
    buttons2[i].y = h-10-bxx
    buttons2[i].xx = bxx
    buttons2[i].yy = bxx
    b2var += 1
  else:
    buttons2[i].x = 10
    buttons2[i].y = h-10-bxx
    buttons2[i].xx = bxx
    buttons2[i].yy = bxx
    b2var = 1

buttons21 = [button(w-110, h/2, text = "switch"), button(w-110, h/2 + 110, text = "дальше"), button(w-110, h/2 + 220, text = "назад")]
buttons2 = buttons2
#b2 -- кнопки смены здания для строительства
buttonsfarm = [button(0,h/3*2, w+100,h+100), button(10, h//3*2 + 10, w/3-10, 20) ]
buttonsinfomen = [button(w - 80, h/3*2+5, 70,45), button(w - 80, h/3*2+51, 70,45), button(w-80, h/3*2+97, 70,45), button(w-80, h/3*2+143, 70,45), button(w-80, h/3*2+188, 70,45)]
butdisinfo = [button(50,h/3*2 +60, w*4/5, 15), button(50,h/3*2 +80, w*4/5, 15)]
butdismode = [button(w/2 +w/20, h/3*2 + h/20, w/10, h/10),
              button(w/2 +w/20 + w/9, h/3*2 + h/20, w/10, h/10),
              button(w/2 +w/20+w/4.5, h/3*2 + h/20, w/10, h/10),
              button(w/2+w/20, h/3*2 + h/20 + h/9, w/10, h/10),
              button(w/2 +w/20 + w/9, h/3*2 + h/20 + h/9, w/10, h/10),
              button(w/10, h/3*2 + h/20, w/2.5,h/25),
              button(w/10, h/3*2 + h/10, w/2.5,h/25),




              ]
butdisprice = [
  button(w/3, h/3*2 + 60, 50,50), 
  button(w/3, h/3*2 + 90, 50,50) , 
  button(w/3 + 60, h//3*2 + 60, 50,50), 
  button(w/3 + 60, h/3*2 + 90, 50,50),
  button(20, h/3*2 + 210, w/3 - 20, 15), 
  button(20, h/3*2 + 60, w/3-20, 15), 
  button(20, h/3*2 + 110, w/3-20, 15),
  button(20, h/3*2 + 160, w/3 - 20, 15),  
  button(w/3 + 110, h/3*2 + 60, 150,50, text = "зп для всех"), 
  button(w/3 + 110, h/3*2 + 100, 150,50, text = "цена для всех")]
  
butdisstat = [
  button(50,h/3*2 + 50, 150,15), 
  button(50,h/3*2 + 70, 150,15),
  button(50,h/3*2 + 90, 150,15),
  button(50,h/3*2 + 110, 150,15), 
  button(50,h/3*2 + 130, 150,15),       
  button(50,h/3*2 + 150, 150,15), 
  button(50,h/3*2 + 170, 150,15),
  button(50,h/3*2 + 190, 150,15),
  button(50,h/3*2 + 210, 150,15),
  button(50,h/3*2 + 230, 150,15),
  #button(50,h/3*2 + 250, 150,15),
  
  button(205,h/3*2 + 50, 150,15), 
  button(205,h/3*2 + 70, 150,15),
  button(205,h/3*2 + 90, 150,15),
  button(205,h/3*2 + 110, 150,15), 
  button(205,h/3*2 + 130, 150,15),       
  button(205,h/3*2 + 150, 150,15), 
  button(205,h/3*2 + 170, 150,15),
  button(205,h/3*2 + 190, 150,15),
  button(205,h/3*2 + 210, 150,15),
  button(205,h/3*2 + 230, 150,15),
  #button(205,h/3*2 + 250, 150,15),
  
  button(360,h/3*2 + 50, 150,15), 
  button(360,h/3*2 + 70, 150,15),
  button(360,h/3*2 + 90, 150,15),
  button(360,h/3*2 + 110, 150,15), 
  button(360,h/3*2 + 130, 150,15),       
  button(360,h/3*2 + 150, 150,15), 
  button(360,h/3*2 + 170, 150,15),
  button(360,h/3*2 + 190, 150,15),
  button(360,h/3*2 + 210, 150,15),
  button(360,h/3*2 + 230, 150,15),
  #button(360,h/3*2 + 250, 150,15),
    
]
butdisother=[button(50,h/1.5+50,w/2 - 25,15),button(50,h/1.5+90,w/2 - 75,15),button(50,h/1.5+130,w/2 - 75,15),button(50,h/1.5+170,w/2 - 75,15),button(50,h/1.5+220,200,15),button(w/2,h/1.5+50,w/2,15) ]

# про инфодис и прочее. класса button мало. нужно разработать класс checkbox (проверять click будем в main), классы: "ползунок" (горионтальный), шкала готовности, класс где отображается просто текст (не одной строкой), ползунок (вертикальный) для перемотки текста
buttonsfarm = buttonsfarm + buttonsinfomen+ butdismode+ butdisprice + butdisstat+ butdisother+butdisinfo
buttonsfarm[0].text = ""
buttonshuman = []
#for i in buttonsinfomen+ butdismode+ butdisprice + butdisstat+ butdisother+butdisinfo:
  #i.color = (0,0,0)
buttonslay = [button(800,60, 100, 50),  button(690,60, 100, 50),button(580,60, 100, 50), button(470,60, 100, 50), button(360,60, 100, 50), button(250,60, 100, 50),button(140,60, 100, 50), button(30,60, 100, 50), button(30,120, 100, 50) ]


buttonsall = buttons + buttons2 + buttonsfarm + buttonshuman

buttonslay[0].text = "close"
buttonslay[1].text = "элек"
buttonslay[2].text ="красота"
buttonslay[3].text ="свобода"
buttonslay[4].text ="нефть"
buttonslay[5].text ="iron"
buttonslay[6].text ="уголь"
buttonslay[7].text ="золото"


#buttons2[0].text = "Дом "
#buttons2[1].text = "Ферма "
#buttons2[2].text = "Клиника"
#buttons2[3].text = "Дорога"
#buttons2[4].text = "Гараж"
#buttons2[5].text = "Грузы"
#buttons2[6].text = "Порт"
#buttons2[7].text = "Магаз"
#buttons2[8].text = "Имиграция"
#buttons2[9].text = "Ранчо"
#buttons2[10].text = "Театр"
#buttons2[11].text = " Ром  "
#buttons2[12].text = "Консервы"
#buttons2[13].text = " Сыр  "
#buttons2[14].text = "Сигареты"

buttons[0].xx = 100
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



gamerun = 1
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
gme = [button(w/8, 100, w/8*7, h-100),
button(w/4 + w/16, 250, w/2 - w/8, 50),
button(w/4 + w/16, 360, w/2 - w/8, 50),
button(w/4 + w/16, 470, w/2 - w/8, 50), 
button(w/4 + w/16, 580, w/2 - w/8, 50)]


##кнопки альманаха, переключение
gmal = [
  button(0, 0, w, h, text = "", col = (0,0,0)),
  button(w/45, 10, w/30*4,60, text = "обзор"),
  button(w/45*2+w/30*4, 10, w/30*4,60, text = "люди"),
  button(w/45*3+w/30*4*2, 10, w/30*4,60, text = "деньги"),
  button(w/45*4+w/30*4*3, 10, w/30*4,60, text = "политик"),
  button(w/45*5+w/30*4*4, 10, w/30*4,60, text = "списки"),
  button(w/45*6+w/30*4*5, 10, w/30*4,60, text = "прочее"),
  button(w/2/5, 80, w/2/5*3, 40, text = "обзор"),
  button(w/2/5 +w/2, 80, w/2/5*3, 40, text = "счастье"),
  button(w/2/10, 130 , w/2/10*9, 30, text = "год................"),
  button(w-90, h-70, 80,60, text = "x", col = (0,180,0))
  
]

"""gmaleco = [
  button(w/2/10, 170 , w/2/10*9, 25, text = "внутренний доход"),
  button(w/2/10, 200 , w/2/10*9, 25, text = "внешний доход", altype = "outincome"),
  button(w/2/10, 230 , w/2/10*9, 25, text = "внутренние траты", altype = "expenses"),
  button(w/2/10, 260 , w/2/10*9, 25, text = "внешние траты", altype = "outexpenses"),
  button(w/2/10, 290 , w/2/10*9, 25, text = "баланс", altype = "balance"),
  button(w/2/10, 320 , w/2/10*9, 25, text = "экспорт"),
  button(w/2/10, 350 , w/2/10*9, 25, text = "импорт"),
  button(w/2/10, 380 , w/2/10*9, 25, text = "доход"),
  button(w/2/10, 410 , w/2/10*9, 25, text = "средняя зарплата", altype = "mrot"),
  button(w/2/10, 440 , w/2/10*9, 25, text = "безработные"),
  button(w/2/10, 470 , w/2/10*9, 25, text = "вакансии"),
  button(w/2/10, 500 , w/2/10*9, 25, text = "общий доход", altype = "expenses"),
]"""

gmaleco = [
  button(w/2/10, 170 , w/2/10*9, 25, text = "Доход"),
  button(w/2/10, 200 , w/2/10*9, 25, text = "Расходы игрока", altype = "outincome"),
  button(w/2/10, 230 , w/2/10*9, 25, text = "Расходы острова", altype = "expenses"),
  button(w/2/10, 290 , w/2/10*9, 25, text = "баланс", altype = "balance"),
  button(w/2/10, 320 , w/2/10*9, 25, text = "Основной экспорт"),
  button(w/2/10, 350 , w/2/10*9, 25, text = "Экспортные цены"),
  button(w/2/10, 380 , w/2/10*9, 25, text = "Разрыв в доходах"),
  button(w/2/10, 410 , w/2/10*9, 25, text = "Средняя зарплата", altype = "mrot"),
  button(w/2/10, 440 , w/2/10*9, 25, text = "Средняя карибская зарплата"),
  button(w/2/10, 470 , w/2/10*9, 25, text = "Безработны"),
  button(w/2/10, 500 , w/2/10*9, 25, text = "Вакансии", altype = "expenses")]

gmalpeople = [
  button(w/2/10, 170 , w/2/10*9, 25, text = "Средний уровень счастья", altype = "happiness"),
  button(w/2/10, 200 , w/2/10*9, 25, text = "общее уважение", altype = "fractions"),
  button(w/2/10, 230 , w/2/10*9, 25, text = "средняя зарплата"),
  button(w/2/10, 260 , w/2/10*9, 25, text = "средний возраст"),
  button(w/2/10, 290 , w/2/10*9, 25, text = "качество пищи"),
  button(w/2/10, 320 , w/2/10*9, 25, text = "разрыв в доходах"),
  button(w/2/10, 350 , w/2/10*9, 25, text = "количество граждан", altype= "growth"),
  button(w/2/10, 380 , w/2/10*9, 25, text = "количество хижин")
]

gmaloverview = [
  button(w / 2 / 10, 170, w / 2 / 10 * 9, 25, text="Средний уровень счастья", altype="happiness"),
  button(w / 2 / 10, 200, w / 2 / 10 * 9, 25, text="Количество граждан", altype="growth"),
  button(w / 2 / 10, 230, w / 2 / 10 * 9, 25, text="Туристы"),
  button(w / 2 / 10, 260, w / 2 / 10 * 9, 25, text="Туристический рейтинг"),
  button(w / 2 / 10, 290, w / 2 / 10 * 9, 25, text="Баланс"),
  button(w / 2 / 10, 320, w / 2 / 10 * 9, 25, text="Расходы игрока"),
  button(w / 2 / 10, 350, w / 2 / 10 * 9, 25, text="Шверцарский счет")
]

gmalpolitics = [
  button(w/2/10, 170 , w/2/10*9, 25, text = "Уровень угрозы"),

  button(w / 2 / 10, 230, w / 2 / 10 * 9, 25, text="Коммунисты", altype="communists"),
  button(w/2/10, 200 , w/2/10*9, 25, text = "Общее уважение", altype = "fractions"),
button(w / 2 / 10, 260, w / 2 / 10 * 9, 25, text="Религиозная", altype="religion"),
  button(w / 2 / 10, 260, w / 2 / 10 * 9, 25, text="Милитаристы", altype="militarists"),

  button(w / 2 / 10, 290, w / 2 / 10 * 9, 25, text="Зелёные", altype="beauty"),
  button(w / 2 / 10, 320, w / 2 / 10 * 9, 25, text="Интеллектуалы", altype="intellectuals"),
  button(w / 2 / 10, 350, w / 2 / 10 * 9, 25, text="Капиталисты", altype="capitalists"),
  button(w / 2 / 10, 380, w / 2 / 10 * 9, 25, text="Националисты", altype="nationalists"),
  button(w / 2 / 10, 410, w / 2 / 10 * 9, 25, text="Лоялисты", altype="loyalists"),
  button(w/2/10, 440 , w/2/10*9, 25, text = "Демократические ожидания"),
  button(w/2/10, 470 , w/2/10*9, 25, text = "Отношения с США"),
  button(w/2/10, 500 , w/2/10*9, 25, text = "Отношения с Россией"),
  button(w/2/10, 530 , w/2/10*9, 25, text = "Влиятельная фракция"),
  button(w/2/10, 560 , w/2/10*9, 25, text = "Выборы")
]

gmallists = [
  button(w/2/10, 170 , w/2/10*8, 25, text = "Люди -- зарплата"),
  button(w/2/10, 200 , w/2/10*8, 25, text = "Люди -- Счастье"),
  button(w/2/10, 230 , w/2/10*8, 25, text = "Люди -- Уважение"),
  button(w/2/10, 260 , w/2/10*8, 25, text = "Люди -- Возраст"),
  button(w/2/10, 290 , w/2/10*8, 25, text = "Люди -- образование"),
  button(w/2/10, 320 , w/2/10*8, 25, text = "Люди -- Origin"),
  button(w/2/10, 350 , w/2/10*8, 25, text = "Люди -- Работа"),
  button(w/2/10, 380 , w/2/10*8, 25, text = "Фракции -- Капиталисты"),
  button(w/2/10, 410 , w/2/10*8, 25, text = "Фракции -- Коммунисты"),
  button(w/2/10, 440 , w/2/10*8, 25, text = "Фракции —— Интеллегенция"),
  button(w/2/10, 470 , w/2/10*8, 25, text = "Фракции -- Миллитаристы"),
  button(w/2/10, 500 , w/2/10*8, 25, text = "Фракции -- Зелёные"),
  button(w/2/10, 530 , w/2/10*8, 25, text = "Фракции -- Националисты"),
  button(w/2/10, 560 , w/2/10*8, 25, text = "Фракции -- Лоялисты")
]

gmalsincome = [
  button(w/2/10+w/2, 170 , w/2/10*8, 25, text = "Фермерство", altype2 = "farming"),
  button(w/2/10+w/2, 200 , w/2/10*8, 25, text = "Ископаемые", altype2 = "mining"),
  button(w/2/10+w/2, 230 , w/2/10*8, 25, text = "Дерево", altype2 = "logging"),
  button(w/2/10+w/2, 260 , w/2/10*8, 25, text = "Индустрия", altype2 = "industry"),
  button(w/2/10+w/2, 290 , w/2/10*8, 25, text = "Еда", altype2 = "food"),
  button(w/2/10+w/2, 320 , w/2/10*8, 25, text = "Медицина", altype2 = "medicine"),
  button(w/2/10+w/2, 350 , w/2/10*8, 25, text = "Развлечения", altype2 = "fun"),
  button(w/2/10+w/2, 380 , w/2/10*8, 25, text = "Бизнес рента", altype2 = "rent"),
  button(w/2/10+w/2, 410 , w/2/10*8, 25, text = "Аренда квартир", altype2 = "homerent"),
  button(w/2/10+w/2, 440 , w/2/10*8, 25, text = "Прочее", altype2 = "other"),
  
]

gmalsexpense = [
  button(w/2/10+w/2, 170 , w/2/10*8, 25, text = "Фермерство", altype = "expenses", altype2 = "farming"),
  button(w/2/10+w/2, 200 , w/2/10*8, 25, text = "Ископаемые", altype2 = "mining", altype = "expenses"),
  button(w/2/10+w/2, 230 , w/2/10*8, 25, text = "Дерево", altype2 = "logging", altype = "expenses"),
  button(w/2/10+w/2, 260 , w/2/10*8, 25, text = "Индустрия", altype2 = "industry", altype = "expenses"),
  button(w/2/10+w/2, 290 , w/2/10*8, 25, text = "Еда", altype2 = "food", altype = "expenses"),
  button(w/2/10+w/2, 320 , w/2/10*8, 25, text = "Медицина", altype2 = "medicine", altype = "expenses"),
  button(w/2/10+w/2, 350 , w/2/10*8, 25, text = "Развлечения", altype2 = "fun", altype = "expenses"),
  button(w/2/10+w/2, 380 , w/2/10*8, 25, text = "резерв", altype2 = "rent", altype = "expenses"),
  button(w/2/10+w/2, 410 , w/2/10*8, 25, text = "", altype = "expenses", altype2 = "homerent"),
  button(w/2/10+w/2, 440 , w/2/10*8, 25, text = "Инфраструктура", altype = "expenses", altype2 = "struct" ),
  
  button(w/2/10+w/2, 470 , w/2/10*8, 25, text = "Всего", altype = "expenses" ),
  
  button(w/2/10+w/2, 500 , w/2/10*8, 25, text = "Всего", altype = "expenses" ),
  
  button(w/2/10+w/2, 530 , w/2/10*8, 25, text = "Всего", altype = "expenses" )
  
]

gmalhap = [
  button(w/2/10+w/2, 170 , w/2/10*8, 25, text = "Качество еды", altype = "happiness", altype2 = "food"),
  button(w/2/10+w/2, 200 , w/2/10*8, 25, text = "Качество жилья", altype2 = "home", altype = "happiness"),
  button(w/2/10+w/2, 230 , w/2/10*8, 25, text = "Развлечения", altype2 = "fun", altype = "happiness"),
  button(w/2/10+w/2, 260 , w/2/10*8, 25, text = "Медицина", altype2 = "health", altype = "happiness"),
  button(w/2/10+w/2, 290 , w/2/10*8, 25, text = "Работа", altype2 = "job", altype = "happiness"),
  button(w/2/10+w/2, 320 , w/2/10*8, 25, text = "Безопасность", altype2 = "safety", altype = "happiness"),
  button(w/2/10+w/2, 350 , w/2/10*8, 25, text = "Экология", altype2 = "beauty", altype = "happiness"),
  button(w/2/10+w/2, 380 , w/2/10*8, 25, text = "Свобода", altype2 = "freedom", altype = "happiness"),
  button(w/2/10+w/2, 410 , w/2/10*8, 25, text = "Уважение", altype2 = "respect", altype = "happiness"),
  button(w/2/10+w/2, 440 , w/2/10*8, 25, text = "Всего", altype = "happiness" )
  
]


gmalfrac = [
  button(w/2/10+w/2, 170 , w/2/10*8, 25, text = "Капиталисты", altype = "fractions", altype2 = "capitalists"),
  button(w/2/10+w/2, 200 , w/2/10*8, 25, text = "Коммунисты", altype = "fractions", altype2 = "communists"),
  button(w/2/10+w/2, 230 , w/2/10*8, 25, text = "Интеллегенты", altype2 = "intellectuals", altype = "fractions"),
  button(w/2/10+w/2, 260 , w/2/10*8, 25, text = "Милитаристы", altype2 = "militarists", altype = "fractions"),
  button(w/2/10+w/2, 260 , w/2/10*8, 25, text = "Религионеры", altype2 = "religion", altype = "fractions"),
  button(w/2/10+w/2, 290 , w/2/10*8, 25, text = "Зелёные", altype2 = "beauty", altype = "fractions"),
  button(w/2/10+w/2, 320 , w/2/10*8, 25, text = "Националисты", altype2 = "nationalists", altype = "fractions"),
  button(w/2/10+w/2, 350 , w/2/10*8, 25, text = "Лоялисты", altype2 = "loyalists", altype = "fractions"),
  button(w/2/10+w/2, 380 , w/2/10*8, 25, text = "Всего", altype2 = "main", altype = "fractions")
  
]

gmalgrowth = [
  button(w/2/10+w/2, 170 , w/2/10*8, 25, text = "Количество людей", altype = "growth", altype2 = "main"),
  button(w/2/10+w/2, 200 , w/2/10*8, 25, text = "Средняя ЗП", altype = "growth", altype2 = "avsalary"),
  button(w/2/10+w/2, 230 , w/2/10*8, 25, text = "Медианная ЗП", altype2 = "medsalary", altype = "growth"),
  button(w/2/10+w/2, 260 , w/2/10*8, 25, text = "Средний возраст", altype2 = "avage", altype = "growth"),
  button(w/2/10+w/2, 290 , w/2/10*8, 25, text = "Качество еды", altype2 = "food", altype = "happiness")
  
  
]

gmalsoutexpense = [
  button(w/2/10+w/2, 170 , w/2/10*8, 25, text = "За все время", altype = "outexpenses", altype2 = "main"),
  button(w/2/10+w/2, 200 , w/2/10*8, 25, text = "За год", altype = "outexpenses", altype2 = "main"),
  button(w/2/10+w/2, 230 , w/2/10*8, 25, text = "Фермерство", altype = "outexpenses", altype2 = "farming"),
  button(w/2/10+w/2, 260 , w/2/10*8, 25, text = "Ископаемые", altype = "outexpenses", altype2 = "mining"),
  button(w/2/10+w/2, 290 , w/2/10*8, 25, text = "Древесина", altype = "outexpenses", altype2 = "logging"),
  button(w/2/10+w/2, 320 , w/2/10*8, 25, text = "Промышленность", altype = "outexpenses", altype2 = "industry"),
  button(w/2/10+w/2, 350 , w/2/10*8, 25, text = "Аренда", altype = "outexpenses", altype2 = "rent"),
  button(w/2/10+w/2, 380 , w/2/10*8, 25, text = "Строительство", altype = "outexpenses", altype2 = "building"),
  
  button(w/2/10+w/2, 410 , w/2/10*8, 25, text = "Амортизация зданий", altype = "outexpenses", altype2 = "upkeep")
]

gmalsoutincome = [
  button(w/2/10+w/2, 170 , w/2/10*8, 25, text = "За все время", altype = "outincome", altype2 = "main"),
  button(w/2/10+w/2, 200 , w/2/10*8, 25, text = "За год", altype = "outincome", altype2 = "main"),
  button(w/2/10+w/2, 230 , w/2/10*8, 25, text = "Фермерство", altype = "outincome", altype2 = "farming"),
  button(w/2/10+w/2, 260 , w/2/10*8, 25, text = "Ископаемые", altype = "outincome", altype2 = "mining"),
  button(w/2/10+w/2, 290 , w/2/10*8, 25, text = "Древесина", altype = "outincome", altype2 = "logging"),
  button(w/2/10+w/2, 320 , w/2/10*8, 25, text = "Промышленность", altype = "outincome", altype2 = "industry"),
  button(w/2/10+w/2, 350 , w/2/10*8, 25, text = "Аренда", altype = "outincome", altype2 = "rent"),
  button(w/2/10+w/2, 380 , w/2/10*8, 25, text = "Строительство", altype = "outincome", altype2 = "building")
]

gmalmrot = [
  button(w/2/10+w/2, 170 , w/2/10*8, 25, text = "Средняя зарплата", altype = "growth", altype2 = "avsalary"),
  button(w/2/10+w/2, 200 , w/2/10*8, 25, text = "Всего", altype = "outincome", altype2 = "main"),
  button(w/2/10+w/2, 230 , w/2/10*8, 25, text = "Еда", altype = "outincome", altype2 = "eat"),
  button(w/2/10+w/2, 260 , w/2/10*8, 25, text = "Медицина", altype = "outincome", altype2 = "health"),
  button(w/2/10+w/2, 290 , w/2/10*8, 25, text = "Развлечения", altype = "outincome", altype2 = "fun"),
  button(w/2/10+w/2, 320 , w/2/10*8, 25, text = "Жильё", altype = "outincome", altype2 = "home")
]

gmalscapitalists = [
  button(w / 2 / 10 + w / 2, 170, w / 2 / 10 * 8, 25, text="Общее уважение капитал", altype="growth",
         altype2="avsalary"),
  button(w / 2 / 10 + w / 2, 200, w / 2 / 10 * 8, 25, text="Основные требования", altype="outincome", altype2="main"),
  button(w / 2 / 10 + w / 2, 230, w / 2 / 10 * 8, 25, text="Требование 1"),
  button(w / 2 / 10 + w / 2, 260, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 290, w / 2 / 10 * 8, 25, text="Требование 3"),
  button(w / 2 / 10 + w / 2, 320, w / 2 / 10 * 8, 25, text="Второстепенные требования"),
  button(w / 2 / 10 + w / 2, 350, w / 2 / 10 * 8, 25, text="требование 1"),
  button(w / 2 / 10 + w / 2, 380, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 410, w / 2 / 10 * 8, 25, text="требование 3"),
  button(w / 2 / 10 + w / 2, 440, w / 2 / 10 * 8, 25, text="требование 4"),
  button(w / 2 / 10 + w / 2, 470, w / 2 / 10 * 8, 25, text="требование 5")
]

gmalscommunists = [
  button(w / 2 / 10 + w / 2, 170, w / 2 / 10 * 8, 25, text="Общее уважение коммунистов", altype="growth",
         altype2="avsalary"),
  button(w / 2 / 10 + w / 2, 200, w / 2 / 10 * 8, 25, text="Основные требования", altype="outincome", altype2="main"),
  button(w / 2 / 10 + w / 2, 230, w / 2 / 10 * 8, 25, text="Требование 1"),
  button(w / 2 / 10 + w / 2, 260, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 290, w / 2 / 10 * 8, 25, text="Требование 3"),
  button(w / 2 / 10 + w / 2, 320, w / 2 / 10 * 8, 25, text="Второстепенные требования"),
  button(w / 2 / 10 + w / 2, 350, w / 2 / 10 * 8, 25, text="требование 1"),
  button(w / 2 / 10 + w / 2, 380, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 410, w / 2 / 10 * 8, 25, text="требование 3"),
  button(w / 2 / 10 + w / 2, 440, w / 2 / 10 * 8, 25, text="требование 4"),
  button(w / 2 / 10 + w / 2, 470, w / 2 / 10 * 8, 25, text="требование 5")

]

gmalsintellectuals = [
  button(w / 2 / 10 + w / 2, 170, w / 2 / 10 * 8, 25, text="Общее уважение intel", altype="growth", altype2="avsalary"),
  button(w / 2 / 10 + w / 2, 200, w / 2 / 10 * 8, 25, text="Основные требования", altype="outincome", altype2="main"),
  button(w / 2 / 10 + w / 2, 230, w / 2 / 10 * 8, 25, text="Требование 1"),
  button(w / 2 / 10 + w / 2, 260, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 290, w / 2 / 10 * 8, 25, text="Требование 3"),
  button(w / 2 / 10 + w / 2, 320, w / 2 / 10 * 8, 25, text="Второстепенные требования"),
  button(w / 2 / 10 + w / 2, 350, w / 2 / 10 * 8, 25, text="требование 1"),
  button(w / 2 / 10 + w / 2, 380, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 410, w / 2 / 10 * 8, 25, text="требование 3"),
  button(w / 2 / 10 + w / 2, 440, w / 2 / 10 * 8, 25, text="требование 4"),
  button(w / 2 / 10 + w / 2, 470, w / 2 / 10 * 8, 25, text="требование 5")

]

gmalsmilitarists = [
  button(w / 2 / 10 + w / 2, 170, w / 2 / 10 * 8, 25, text="Общее уважение mil", altype="growth", altype2="avsalary"),
  button(w / 2 / 10 + w / 2, 200, w / 2 / 10 * 8, 25, text="Основные требования", altype="outincome", altype2="main"),
  button(w / 2 / 10 + w / 2, 230, w / 2 / 10 * 8, 25, text="Требование 1"),
  button(w / 2 / 10 + w / 2, 260, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 290, w / 2 / 10 * 8, 25, text="Требование 3"),
  button(w / 2 / 10 + w / 2, 320, w / 2 / 10 * 8, 25, text="Второстепенные требования"),
  button(w / 2 / 10 + w / 2, 350, w / 2 / 10 * 8, 25, text="требование 1"),
  button(w / 2 / 10 + w / 2, 380, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 410, w / 2 / 10 * 8, 25, text="требование 3"),
  button(w / 2 / 10 + w / 2, 440, w / 2 / 10 * 8, 25, text="требование 4"),
  button(w / 2 / 10 + w / 2, 470, w / 2 / 10 * 8, 25, text="требование 5"),
button(w / 2 / 10 + w / 2, 500, w / 2 / 10 * 8, 25, text="требование 6"),
button(w / 2 / 10 + w / 2, 530, w / 2 / 10 * 8, 25, text="требование 7"),
button(w / 2 / 10 + w / 2, 560, w / 2 / 10 * 8, 25, text="требование 8"),

]
gmalsbeautyf = [
  button(w / 2 / 10 + w / 2, 170, w / 2 / 10 * 8, 25, text="Общее уважение green", altype="growth", altype2="avsalary"),
  button(w / 2 / 10 + w / 2, 200, w / 2 / 10 * 8, 25, text="Основные требования", altype="outincome", altype2="main"),
  button(w / 2 / 10 + w / 2, 230, w / 2 / 10 * 8, 25, text="Требование 1"),
  button(w / 2 / 10 + w / 2, 260, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 290, w / 2 / 10 * 8, 25, text="Требование 3"),
  button(w / 2 / 10 + w / 2, 320, w / 2 / 10 * 8, 25, text="Второстепенные требования"),
  button(w / 2 / 10 + w / 2, 350, w / 2 / 10 * 8, 25, text="требование 1"),
  button(w / 2 / 10 + w / 2, 380, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 410, w / 2 / 10 * 8, 25, text="требование 3"),
  button(w / 2 / 10 + w / 2, 440, w / 2 / 10 * 8, 25, text="требование 4"),
  button(w / 2 / 10 + w / 2, 470, w / 2 / 10 * 8, 25, text="требование 5")

]
gmalsnationalists = [
  button(w / 2 / 10 + w / 2, 170, w / 2 / 10 * 8, 25, text="Общее уважение nat", altype="growth", altype2="avsalary"),
  button(w / 2 / 10 + w / 2, 200, w / 2 / 10 * 8, 25, text="Основные требования", altype="outincome", altype2="main"),
  button(w / 2 / 10 + w / 2, 230, w / 2 / 10 * 8, 25, text="Требование 1"),
  button(w / 2 / 10 + w / 2, 260, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 290, w / 2 / 10 * 8, 25, text="Требование 3"),
  button(w / 2 / 10 + w / 2, 320, w / 2 / 10 * 8, 25, text="Второстепенные требования"),
  button(w / 2 / 10 + w / 2, 350, w / 2 / 10 * 8, 25, text="требование 1"),
  button(w / 2 / 10 + w / 2, 380, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 410, w / 2 / 10 * 8, 25, text="требование 3"),
  button(w / 2 / 10 + w / 2, 440, w / 2 / 10 * 8, 25, text="требование 4"),
  button(w / 2 / 10 + w / 2, 470, w / 2 / 10 * 8, 25, text="требование 5")

]
gmalsloyalists = [
  button(w / 2 / 10 + w / 2, 170, w / 2 / 10 * 8, 25, text="Общее уважение loya", altype="growth", altype2="avsalary"),
  button(w / 2 / 10 + w / 2, 200, w / 2 / 10 * 8, 25, text="Основные требования", altype="outincome", altype2="main"),
  button(w / 2 / 10 + w / 2, 230, w / 2 / 10 * 8, 25, text="Требование 1"),
  button(w / 2 / 10 + w / 2, 260, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 290, w / 2 / 10 * 8, 25, text="Требование 3"),
  button(w / 2 / 10 + w / 2, 320, w / 2 / 10 * 8, 25, text="Второстепенные требования"),
  button(w / 2 / 10 + w / 2, 350, w / 2 / 10 * 8, 25, text="требование 1"),
  button(w / 2 / 10 + w / 2, 380, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 410, w / 2 / 10 * 8, 25, text="требование 3"),
  button(w / 2 / 10 + w / 2, 440, w / 2 / 10 * 8, 25, text="требование 4"),
  button(w / 2 / 10 + w / 2, 470, w / 2 / 10 * 8, 25, text="требование 5")

]

gmalreligion = [
  button(w / 2 / 10 + w / 2, 170, w / 2 / 10 * 8, 25, text="Общее уважение loya", altype="growth", altype2="avsalary"),
  button(w / 2 / 10 + w / 2, 200, w / 2 / 10 * 8, 25, text="Основные требования", altype="outincome", altype2="main"),
  button(w / 2 / 10 + w / 2, 230, w / 2 / 10 * 8, 25, text="Требование 1"),
  button(w / 2 / 10 + w / 2, 260, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 290, w / 2 / 10 * 8, 25, text="Требование 3"),
  button(w / 2 / 10 + w / 2, 320, w / 2 / 10 * 8, 25, text="Второстепенные требования"),
  button(w / 2 / 10 + w / 2, 350, w / 2 / 10 * 8, 25, text="требование 1"),
  button(w / 2 / 10 + w / 2, 380, w / 2 / 10 * 8, 25, text="требование 2"),
  button(w / 2 / 10 + w / 2, 410, w / 2 / 10 * 8, 25, text="требование 3"),
  button(w / 2 / 10 + w / 2, 440, w / 2 / 10 * 8, 25, text="требование 4"),
  button(w / 2 / 10 + w / 2, 470, w / 2 / 10 * 8, 25, text="требование 5")

]

gmalbalance = [
  button(w/2/10+w/2, 170 , w/2/10*8, 25, text = "Всего", altype = "balance", altype2 = "main"),
  button(w/2/10+w/2, 200 , w/2/10*8, 25, text = "Фермерство", altype = "", altype2 = "farming"),
  button(w/2/10+w/2, 230 , w/2/10*8, 25, text = "Добыча", altype = "mining", altype2 = "mining"),
  button(w/2/10+w/2, 260 , w/2/10*8, 25, text = "Леса", altype = "balance", altype2 = "logging"),
  button(w/2/10+w/2, 290 , w/2/10*8, 25, text = "Развлечения", altype = "balance", altype2 = "fun"),
  button(w/2/10+w/2, 320 , w/2/10*8, 25, text = "Жильё", altype = "balance", altype2 = "rent")
]

for i in gmalmrot:
  if i != 0:
    i.altype = "mrot"
    
    
for i in gmalbalance:
  if i != 0:
    i.altype = "balance"





smb = [button(w/4 + w/16, 150, w/2 - w/8, 50),
button(w/4 + w/16, 250, w/2 - w/8, 50),
button(w/4 + w/8 + w/16, 600, w/2 - w/8, 50),
button(w/2-60+ 200, 170, 50, 50),
button(w/2+10+200, 170, 50, 50),
button(w/2-60+200, 270, 50, 50),
button(w/2+10+200, 270, 50, 50)]
smb[2].text = "Назад"
smb[3].text = " - "
smb[4].text = " + "
smb[5].text = " - "
smb[6].text = " + "

gme[0].text = ""
gme[1].text = "Продолжить"
gme[2].text = "Настройки"
gme[3].text = "Альманах"
gme[4].text = "Главное меню"
sb1[0].text = "Создать остров"
sb1[1].text = "Назад"


albutmain = {
  "overview":gmaloverview,
  "people":gmalpeople,
  "economy":gmaleco,
  "politics":gmalpolitics,
  "lists":gmallists,
  "other":[],
  
 
  
}
albutsec = {
  "income":gmalsincome,
  "outincome":gmalsoutincome,
  "expenses": gmalsexpense,
  "outexpenses":gmalsoutexpense,
  "happiness":gmalhap,
  "fractions":gmalfrac,
  "growth":gmalgrowth,
  "mrot":gmalmrot,
  "balance":gmalbalance,
"capitalists":gmalscapitalists,
  "communists":gmalscommunists,
  "intellectuals":gmalsintellectuals,
  "militarists":gmalsmilitarists,
  "beauty":gmalsbeautyf,
  "nationalists":gmalsnationalists,
  "loyalists":gmalsloyalists,
  "religion":gmalreligion
  
  
}
def setalmain(mode = None):
  
    for i in albutmain:
      for j in albutmain[i]:
        j.active = 0
    if mode != None:
      for j in albutmain[mode]:
        j.active = 1
        j.mtif = 30
def setalsec(mode = None):
  
    for i in albutsec:
      for j in albutsec[i]:
        j.active = 0
    if mode != None:
      for j in albutsec[mode]:
        j.active = 1
        j.mtif = 30
        
setalmain()
setalsec()

gmalbutall = gmalgrowth+gmalsoutincome+gmalsoutexpense+ gmalmrot + gmalbalance

questbuttons = [
  button(100, 100, w-200, h-150, text = ""),
  button(150, 110, w-300, 50, text = "имя фамилия", col = (0,0,0)),
  button(110, 170, w-220, h/3*2-190, text = "описание задания", col = (0,0,0), textscale = 20, wrap = 110),
  button(110, h/3*2-10-5, w-220, 30, text = "цель", col = (0,0,0)),
  button(110, h/3*2+20, w-220, 30, text = "награда", col = (0,0,0)),
  button(110, h/3*2+55, (w-220)/2, 30, text = "опция 1", col = (0,0,0)),
  button(110, h/3*2+90, (w-220)/2, 30, text = "опция 2", col = (0,0,0)),
  button(110, h/3*2+125, (w-220)/2, 30, text = "опция 3", col = (0,0,0)),
  button(110, h-110, 75, 50, text = "принять", col = (0,180,0)),
  button(w-110 -75, h-110, 75, 50, text = "закрыть", col = (0,180,0)),
  button(w-110 -75, h-170, 75, 50, text = "ещё", col = (0,180,0))
]
      