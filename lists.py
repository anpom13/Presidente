import pygame
import math
import numpy as np
import mlists

from mlists import *
#from pysweepline import *

entlayers = []
maincnt = [0]
courseon = [False] ##если ли национальная валюта
laymod = ["None"]
#ursinalists
monthevt = [0]




ididict = {
    "school":"Школа",
    "beauty":"красота",
    "metro":"перевозит людей под землей",
    "tavern":"Одно из немногих местных развлечений",
    "rome":"делает ром из сахара",
    "cigar":"делает сигары из табака",
    "cheese":"делает сыр из молока",
    "canns":"делает консервы из мяса, кофе или ананасов",
    "rancho":"Производит молоко или мясо",
"farm": "Может производить кукурузу, кофе, ананасы, табак и сахар",
"clinic":"В этом здании врачи открывают колбы аспирина для островитян",
"home":"Здесь люди удовлетворяют нужду в отдыхе",
"fur":"Перевозит товары, которые произвели на ферме, ранчо и заводах",
"port":"Экспортирует товары, произведённые на острове",
"imig":"Привлекает иммигрантов на остров",
    "shop":"Перепродает товары людям",
'build':'строит здания на острове',
"palace":"Это ваша резиденция"
}



#если включено, то на острове используется своя валюта, и для трансакций с другими странами используется иностранная
# если выключено, то используется только иностранная валюта

editparametrs = {
  
}
gameparametrs = {
  "exportpricemodifer":1,
  "exportdic":{},
  "conflict":None,
"imigration office 1":0,
    "imigration office mode":"base",
    "religion":True,
    "pricemodifer":1,
    "no_think":False
}
timelist = [0]
walknodes = set()
walkroads = {}
walksvsets = [] #список связности графа
walksvdic = {} #словарь связности, каждой вершине сопоставляет номер компоненты связности
garagedic = {} #каждой целой точке на карте сопоставляет список ближайших гаражей
gatagediclist = {}
roadsetobj = []
walklistscache = {}
roaddic = {}# сопоставляет дороге из roadset дорогу из roadsetobj

pricedic = {
  "shanty":150,
  "barak":500,
  "county":1000,
  "house":2000,
  "mansion":4000,
  "tenement":4000,
  "apartment":5000,
  "condonium":6000,
  "farm":1500,
  "rancho":750,
  "fish":3000,
  "shop":500,
  "mine":3000,
  "oilwell":8000,
  "logging":1500,
  "lumber":5000,
  "cigar":10000,
  "rome":22000,
  "jewerly":13000,
  "furniture":17000,
  "canns":15000,
  "weapon":17000,
  "garage":2500,
  "road":20,
  "port":2000,
  #мусор
  "fur":2000,
  "elec":17000,
  "substation":2000,
  #ветряк
  "build":2000,
  
  
  "eatmatket":3000,
  "metro":25000
}

def get_build_price(type, subtype = None):
  price = 10

  if type != "home":
    if type in pricedic:
      price = pricedic[type]
    #else:
      #price = 10
  if type == "home":
    if subtype in pricedic:
      price = pricedic[subtype]
    #else:
      #price = 10
  if type == "metro":
    return pricedic["metro"]* (1+len(metrolist)/2)
  return price*gameparametrs["pricemodifer"]
def build_allow(type, subtype = None):
  pr = get_build_price(type, subtype)

  if money[0] - pr > -10000:
    type = type
  else:
    return False
  return True
def wnodesv(a,b):
  #связывает 2 вершины графа
  if a in walkroads:
    walkroads[a].add(b)
  else:
    walkroads[a] = {b}
  if b in walkroads:
    walkroads[b].add(a)
  else:
    walkroads[b] = {a}

def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

def do_edges_intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


def get_initial_main_edges(walkroads):
    initial_main_edges = []
    for node in walkroads:
        for neighbor in walkroads[node]:
            edge = tuple(sorted((node, neighbor)))  # Сортируем, чтобы избежать дубликатов
            if edge not in initial_main_edges:
                initial_main_edges.append(edge)
    return initial_main_edges

#initial_main_edges = get_initial_main_edges(walkroads)
def get_cell_coords(point, cell_size):
    return point[0] // cell_size, point[1] // cell_size


def get_vertices_in_cells(vertices, cell_size):
    cell_dict = {}
    for vertex in vertices:
        cell_coords = get_cell_coords(vertex, cell_size)
        if cell_coords in cell_dict:
            cell_dict[cell_coords].append(vertex)
        else:
            cell_dict[cell_coords] = [vertex]
    return cell_dict

def add_additional_edges(cell_dict = get_vertices_in_cells(walknodes, 10),cell_size = 10):
    def is_edge_crossing_initial_main_edges(edge_candidate, initial_main_edges):
        A, B = edge_candidate
        for main_edge in initial_main_edges:
            if do_edges_intersect(A, B, main_edge[0], main_edge[1]):
                return True
        return False

    initial_main_edges = [(node, neighbor) for node, neighbors in walkroads.items() for neighbor in neighbors if node < neighbor]

    for cell_coords, vertices in cell_dict.items():
        for node1 in vertices:
            for neighbor_offset in [(0,0),(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                neighbor_coords = (cell_coords[0] + neighbor_offset[0], cell_coords[1] + neighbor_offset[1])
                if neighbor_coords in cell_dict:
                    neighbor_vertices = cell_dict[neighbor_coords]
                    for node2 in neighbor_vertices:
                        if node1 != node2 and node2 not in walkroads[node1]:
                            edge_candidate = (node1, node2)
                            if not is_edge_crossing_initial_main_edges(edge_candidate, initial_main_edges):
                                wnodesv(node1, node2)
mdownevent = [0]
pausel = [0]
questwindow = {
  "turn":False,
  "name":"Абрахам Цвайнштайн",
  "description": "это простое задание для новичков. просто выполни цель и отвали, ахахахахаахахахаахахахаахаахахахахахахаахахаххахаахахахахахахахахахаахахахах",
  "target":"это описание цели",
  "reward":"ты получишь такую награду",
  "option1":"есть такая опция",
  "option2":False,
  "option3":False,
  "accept":True,
  "close":True,
  "output":None
  
}


wpdict = {"farm": "ферма", "clinic":"клиника", "port":"порт", "fur": "офис грузоперевозо", "immigration": "иммиграционное бюро", "shop": "магазин", "tavern" :"театр ", "ranch": "ранчо" ,"rome" :"ромовый завод", "cheese":"сырный завод","canns":"консервный завод" ,"cigar":"сигарный завод", 'build':"Строительная контора",
          "shanty": "лачуга",
          "barak": "барак",
          "country":"Фазенда",
          "house":"Дом",
          "mansion":"Особняк",
          "tenement":"Хрущевка",
          "apartment":"Апартаменты",
          "condonium":"Коттедж"}

def getbuiname(str, sub):
    if str != "home":
        if str in wpdict:
            return wpdict[str]
        else:
            return "None"
    else:
        if sub in wpdict:
            return wpdict[sub]
        else:
            return "Жилье"


exportprices = { "coffee":800,"cheese":1500,"corn":400, "pineapple":600, "sugar":800, "tobacco":900, "meat":3000, "milk":500, "fish":700, "aspirin": 1200, "rom":7000, "cigar":5000, "canns":1500, "bouxit" : 2500, "oil":1500,  "gold":4800, "iron":2000, "coal":1000, "loggs":1000, "lumber": 1000, "furniture": 1000, "jewerly":1000, "weapon":1000}
reszero = {"coffee":0, "cheese":0,"corn":0, "pineapple":0, "sugar":0, "tobacco":0, "meat":0, "milk":0, "fish":0, "aspirin": 0, "rom":0, "cigar":0, "canns":0, "":0}

reslist = {}
for i in exportprices:
  reslist[i] = [0]
  gameparametrs["exportdic"][i]= 1

resone = {"coffee":1 ,"cheese":1,"corn":1, "pineapple":1, "sugar":1, "tobacco":1, "meat":1, "milk":1, "fish":1, "aspirin": 1, "rom":1, "cigar":1, "canns":1, "":0}
eat = {"cheese", "corn","pineapple","meat","milk","fish","canns"}
names ={0: "Никита", 1:"Андрей", 2: "Пётр", 3: "Александр", 4: "Александра", 5:"Василий", 6:"Элина" , 7: "Диана", 8:"Алёна", 9: "Мария", 10: "Эльвира", 11: "Олеся", 12: "Тимофей", 13: "Яна", 14: "Артемий"}
surnames = {0: "Померанцес", 1: "Яковенко", 2: "Верлянко", 3: "Савченко", 4: "Калиниченко", 5: "Дюма", 6: "Шапиро", 7:"Никитенко", 8:"Живаго", 9:"Черных", 10: "Романенко", 11: "Паганини", 12: "Заика", 13: "Шарандак", 14:"Цыбулько"}

def getexportprise(res):
    if res in exportprices:
        if gamevalues["last_industry_reclaim"] + 36 >= monthl[0]:
            #print("рекламная компания промышленности действует")
            return exportprices[res]*gameparametrs["exportpricemodifer"]*gameparametrs["exportdic"][res]*1.2

        else:
            #print("рекламная компания промышленности НЕ действует")
            return exportprices[res]*gameparametrs["exportpricemodifer"]*gameparametrs["exportdic"][res]


    else:
        return 0
def setresmodifer(res, val):
  gameparametrs["exportdic"][res] = val
  
def scaleresmodifer(res, val):
  gameparametrs["exportdic"][res] = gameparametrs["exportdic"][res]*val
  
  
for i in exportprices:
  reszero[i] = 0
for i in exportprices:
  resone[i] = 1
electro = [0,0,0,0]

nhumans = 70
brot = 0
xxtest = 2
yytest = 1
pxxtest = 1
pyytest = 1
nopt= 1

pauseg = 0

x = 0
y = 0
n = 51
m = 51
starthumans = 0
year = 2023
month = 0
time = 0# 2 минуты -- игровой месяц
ids = [0]
infomod = ["info"]
game_run = 1
proad = [0,0]

monthevent = 0
typi = -1  # для табло с информацией (245,245,220)
numbi = -1
money = [250000, 25000] #рубль в бюджете, доллар в бюджете
dcourse = [0]
cbcash = [10000,10000]

xtest = 0
ytest = 0

#global FPS
FPSl = [30]

#FPS = 30
nds = 0.0
sp = None
medc = 10
tapped = 0
zagl = [] 
contmod=[0,0,0,0]
#FPS = 20
fps = 60
WIN_WIDTH = 1300
w = 1300
WIN_HEIGHT = 800
h = 800
WHITE = (255, 255, 255)
GG=(255,0,0)
ORANGE = (255, 150, 100)
WM = ORANGE
 
test = [0]

sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

dcour = ["None"]


rm = [[0 for j in range(0,m)] for i in range (0,n)]
carchanks = [[[] for j in range(0,m//2+1)] for i in range (0,n//2+1)]
actchanks = set()
vecmap = rm.copy()
rm = np.array(rm, dtype=int)
arzero = rm.copy()

eleclay = rm.copy()
beautylay = rm.copy()
freedomlay = rm.copy()
oillay = rm.copy()
ironlay = rm.copy()
coallay = rm.copy()
goldlay = rm.copy()
heightmap = rm.copy()
treemap = rm.copy()
safelay = rm.copy()

lays = {
  "beauty":beautylay,
  "freedom":freedomlay,
  "safe":safelay
}


almod = {
  "main":"overview",
  "second":"income"
}
politrespect = {
  "capitalists":[50],
  "communists":[50],
  "intellectuals":[50],
  "militarists":[50],
  "beauty":[50],
  "nationalists":[50],
  "loyalists":[50],
    "religion":[50],
  "main":[50]
}
allhapmon = {
          "main":[50,50,50,50,50,50,50],
        "food":[50], #доступность еды умножитьна нормированный к разнообразия
        "safety":[50],
        "home":[50],#=качество жилья
        "beauty":[50],#красота около дома и работы
        "freedom":[50],#свобода около дома и работы
        "fun":[50],#доступность развлечений * качество
        "job":[50],#качество работы * коэф частоты смены работы#хрень. Сколько он может купить на зарплату, нормированно и сколько может потратить за границей 
        "health":[50],#качество медицины * доступность
        "religion":[50],
        "respect":[50]
        }

allhap = { 
        "main":[50],
        "food":[50], #доступность еды умножитьна нормированный к разнообразия
        "safety":[50],
        "home":[50],#=качество жилья
        "beauty":[50],#красота около дома и работы
        "freedom":[50],#свобода около дома и работы
        "fun":[50],#доступность развлечений * качество
        "job":[50],#качество работы * коэф частоты смены работы#хрень. Сколько он может купить на зарплату, нормированно и сколько может потратить за границей 
        "health":[50],#качество медицины * доступность
        "respect":[50],
        "religion":[50]
        }
        
incomedi = {
  "main":[0],
  "farming":[0],
  "mining":[0],
  "logging":[0],
  "industry":[0],
  "food":[0],
  "medicine":[0],
  "fun":[0],
  "rent":[0],
  "homerent":[0],
  "other":[0]
}



outincomedi = {
  "main":[0],
  "all":[0],
  "farming":[0],
  "mining":[0],
  "logging":[0],
  "industry":[0],
  "rent":[0],
  "building":[0],
  "other":[0]
}
expendi = {
  "main":[0],
  "farming":[0],
  "mining":[0],
  "logging":[0],
  "industry":[0],
  "food":[0],
  "medicine":[0],
  "fun":[0],
  "rent":[0],
  "homerent":[100],
  
  "struct":[0], #инфраструктура
  "education":[0],
  
  "other":[0]
}

outexpendi = {
  "main":[0],
  "all":[0],
  "farming":[0],
  "mining":[0],
  "logging":[0],
  "industry":[0],
  "rent":[0],
  "building":[0],
  "upkeep":[0],
  "other":[0]
}

growthdi = {
  "main":[len(humans)],
  "avsalary":[0],
  "medsalary":[0],
  "avage":[0]
  }
inecondi = {
  
  }
allmrot = {
  "main":[0],
  "eat":[0],
  "health":[0],
  "fun":[0],
  "home":[0],
  "dollar":[0],
  "avsalary":[0]
}


balancestat = {
    "main":[0],

  "mining":[0],
  "logging":[0],
  
  "food":[0],


  "rent":[0],
  "homerent":[100],
  "building":[0],
  "upkeep":[0],
  "other":[0],
  
  "struct":[0], #инфраструктура
  "education":[0],
  "industry":[0],
  "fun":[0],
  "farming":[0],
  "medicine":[0]
}

maindizat = {
  "main":[-1313]
}

alsecdi = {
  "income":incomedi,
  "outincome":outincomedi,
  "expenses":expendi,
  "outexpenses":outexpendi,
  "happiness":allhap,
  "fractions":politrespect,
  "growth":growthdi,
  "mrot":allmrot,
  "balance":balancestat,
"capitalists":{"main":politrespect["capitalists"]},
"communists":maindizat,
  "intellectuals":maindizat,
  "militarists":maindizat,
  "beauty":maindizat,
  "nationalists":maindizat,
  "loyalists":maindizat
}




def getindustry(name):
  dic = {
    "school":"education",
    "beauty":"struct",
    "metro":"struct",
    "tavern":"fun",
    "rome":"industry",
    "cigar":"industry",
    "cheese":"industry",
    "canns":"industry",
    "rancho":"farming",
"farm": "farming",
"clinic":"medicine",
"home":"struct",
"fur":"struct",
"port":"struct",
"imig":"struct",
    "shop":"struct",
'build':'struct'
}
  if name in dic:
    return dic[name]
  else:
    return "other"

humans = []
buildings = []

mmenu = ["menu","main", "game", "menu"]

xytestdic = {
    1: [2,2],
    2: [2,2]
}

for i in range(100):
    xytestdic[i] = [2,2]
xytestdic[10] = [1,1]
xytestdic[1] = [1,1]
xytestdic[2] = [1,1]
xytestdic[3] = [3,3]
xytestdic[46] = [1,1]
xytestdic[47] = [1,2]
xytestdic[48] = [1,2]
xytestdic[49] = [2,2]
xytestdic[50] = [3,2]
xytestdic[51] = [4,3]
xytestdic[52] = [4,3]
xytestdic[53] = [4,2]

soldierset = {
    'army1', 'army2', 'army3'
}





