imigrations = []
fracmains = {}
fracreqs = {}
cache = {}


humans = []
roadset = set()
semset = set()
buildings = []
factories = []
furs = []
ports = []
homes = []
clinics = []
farms = []
garages = []
resourses = []
cars = []
semaphores = []
trees = {}
markers = []
families = []
childrens = []
exchanges = []
minfins = []
mainbanks = []
metrolist = []
libertybuilds = []

undegrounds = []

gardens = []
elecbuildings = []
freedombuildings = []

rebels = []
activerebels = set()
activearmy = set()
mainfunc = {}
##test section
testllm = []
palaces = []

proadpair = []

monthl = [0]

gamevalues = {
    "last_elections": None,
    "last_elections_fraud" :None,
    "last_mania_time":-100,           #последний указ мании величия в месяцах
    "first_union": None,
    "now_union" : None,
    "carribean_salary": 8,
    "free_home":False,
    "free_food":False,
    "emission":0,
    "last_tax_reduction": -1000,
    "last_industry_reclaim": -1000,
    "bank_building":0,  #часть стоимости,которая не платится при строительстве зданий
    "bank_black":0, #количество денег в месяц которые идут на счет в швейцарском банке
    "likbez":False
}

def timeparametr(parametr, time):
    if gamevalues[parametr] + time >= monthl[0]:
        return True
    else:
        return False

decrees1 = []
decrees2 = []
decrees3 = []
decrees4 = []
decrees5 = []

decreedic = {
    "main": decrees1,
    "outside" : decrees2,
    "economic" : decrees3,
    "inside" : decrees4,
    "mania" : decrees5

}

def humancount():
    a = 0
    for i in humans:
        if i.life == 1:
            a+=1
    print(len(humans))
    return len(humans)
