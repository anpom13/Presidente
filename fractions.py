from family import *



def truefunc(di={}, di2={}):
    return True


def difun(a={}):
    return a


class reqcore():
    def __init__(self, che=truefunc, change=difun, val = 30):
        self.active = True

        self.name = "None"

        self.funcheck = che
        self.funinp = truefunc
        self.funchange = change
        self.stage = 0
        self.time = 0
        self.input = {}
        self.args = {
            "value": val,
            "chval": 30,
            "text": "требование описание"
        }
        self.value = 1
        self.text = "описание требования"
        self.state = True

    def check(self):
        self.args = self.funchange(self.args)

        return self.funcheck(self.input, self.args)

    def get_value(self):

        if self.check():
            self.state = True
            return -int(self.args["value"] / 2)
           # return 0

        else:

            self.state = False
            return int(self.args["value"]/2)


class mainfrac():
    def __init__(self, args={}, name=None):

        self.input = {
            "time": 0,
            "months": 0
        }

        self.args = {
            "baserate": 100,

        }

        self.changefunc = difun
        self.reschecks = []
        self.resmain = []
        self.ressec = []
        self.resadd = []
        self.actchecks = []  # все актуальные проверки
        self.actmainchecks = []  # главные проверки
        self.actsecchecks = []  # вторичные проверки
        self.actaddchecks = []  # проверки-модификаторы
        self.baserate = 50
        self.actualrate = 50
        self.name = name
        self.other = {}

    def addmain(self, lvar):
        self.actchecks.append(lvar)
        self.actmainchecks.append(lvar)

    def addsec(self, lvar):
        self.actchecks.append(lvar)
        self.actsecchecks.append(lvar)

    def addadd(self, lvar):
        self.actchecks.append(lvar)
        self.actaddchecks.append(lvar)

    def update(self):
        self.args = self.changefunc(self.input, self.args)

    def updrate(self):
        actualrate = self.baserate

        for i in self.actchecks:
            actualrate -= i.get_value()

        self.actualrate = actualrate

        for i in politrespect:
            alsecdi[i] = {"main": politrespect[i]}

    def get_rate(self):
        self.updrate()
        return min(max(self.actualrate, 0), 100)

    def set_rate(self):
        politrespect[self.name] = [self.get_rate()]
        if self.name not in albutsec:
            print("fraction not on list")
            print("fraction, self.name")
            print(albutsec)
        if self.name in albutsec:
            list = albutsec[self.name]
            ite = 2
            albutsec[self.name][0].text = "Уважение: " + str(self.actualrate)
            for i in range(1, 11):
                albutsec[self.name][i].text = ""
            albutsec[self.name][ite].text = "Основные требования:          "
            ite += 1
            for i in self.actmainchecks:
                albutsec[self.name][ite].text = i.args["text"] + " " + str(i.state)
                ite += 1
            if len(self.actsecchecks) > 0:
                albutsec[self.name][ite].text = "Вторичные требования:        "
                ite += 1
                for i in self.actsecchecks:
                    albutsec[self.name][ite].text = i.args["text"] + " " + str(i.state)
                    albutsec[self.name][ite].text0 = str(i.state)
                    ite += 1
            if len(self.actaddchecks) > 0:
                albutsec[self.name][ite].text = "Модификаторы"
                ite += 1
                for i in self.actaddchecks:
                    albutsec[self.name][ite].text = i.args["text"] + " " + str(i.state)
                    ite += 1


def chececomine(a={}, args={}):

    cnt = 0
    for i in buildings:
        if i.type == "mine" and i.bready > 0:
            cnt += 1
    if cnt == 0:
        return True
    else:
        return False


def lvarcheckbeauty(a={}, args={}):

    if allhap["beauty"][0] >= args["chval"]:
        return True
    else:
        return False


def lvarchangebeauty(args={}):
    if monthl[0] < 3:
        args["chval"] = 30
        args["text"] = "Уровень красоты выше 30"
        return args
    else:
        args["chval"] = 60
        args["text"] = "Уровень красоты выше 60"
        return args


def lvarchangeecomine(args={}):
    args["text"] = "На острове нет шахт"
    return args

def lv333(a={}, args={}):

    cnt = 0
    for i in buildings:
        if i.type == "svalka" and i.bready > 0:
            cnt += 1
    if cnt*200 >= len(humans):
        return True
    else:
        return False

def lv3333(args={}):
    args["text"] = "На достаточно свалок"
    return args

lvar2 = reqcore(lvarcheckbeauty, lvarchangebeauty)

lvar = mainfrac(name="beauty")  # защищенность капиталистов
lvar3 = reqcore(chececomine, lvarchangeecomine)
lvar4 = reqcore(lv333, lv3333)
lvar2.value = 30
lvar3.value = 30
lvar.addmain(lvar2)
lvar.addmain(lvar3)
lvar.addmain(lvar4)

lvar.set_rate()


fracmains["beauty"] = lvar


def lvarcheck(a={}, args={}):

    if allhap["safety"][0] >= args["chval"]:
        return True
    else:
        return False


def lvarchange(args={}):

    if monthl[0] < 3:
        args["chval"] = 30
        args["text"] = "Уровень безопасности выше 30"
        return args
    else:
        args["chval"] = 60
        args["text"] = "Уровень безопасности выше 60"

        return args

#outincomedi["industry"][max(-3, -len(outincomedi["industry"])):]
def lv1(a={}, args={}):

    if sum(outincomedi["industry"][max(-3, -len(outincomedi["industry"])):]) > 0:
        return True
    else:
        return False


def lv11(args={}):


        args["text"] = "Есть доход от промышленности"

        return args


def lv2(a={}, args={}):

    lvlv = 0
    for i in outincomedi:
        lvlv += sum(outincomedi[i][max(-3, -len(outincomedi[i])):])
    if lvlv >= 30000:
        return True
    else:
        return False


def lv22(args={}):
    args["text"] = "Доход за 3 года больше чем 30000"

    return args

def lv6(a={}, args={}):

    for i in buildings:
        if i.type == "freedom":
            if i.mode == "capitalists":
                return True
    return False

def lv66(args={}):
    args["text"] = "Есть капиталистическая газета"
    return args
lvar = mainfrac(name="capitalists")  # защищенность капиталистов
lvar2 = reqcore(lvarcheck, lvarchange)
lvar666= reqcore(lv6, lv66, 10)

lvar2.value = 30
lvar.addmain(lvar2)
lvar.addsec(lvar666)

lvar.set_rate()


fracmains["capitalists"] = lvar


# lvar2 = reqcore(lvarcheck)



def checcomhome(a={}, args={}):

    cnt = 0
    for i in humans:
        if i.homenumber == -1:
            cnt += 1
    if cnt <= 20:
        return True
    else:
        return False


def lvarchangehome(args={}):
    args["text"] = "меньше 20 бездомных"
    return args


def checcomfood(a={}, args={}):

    cnt = 0
    for i in humans:
        if i.hap_eat <= 0:
            cnt += 1
    if cnt <= 3:
        return True
    else:
        return False


def lvarchangefood(args={}):
    args["text"] = "меньше 3 голодающих"
    return args


lvar4 = reqcore(checcomfood, lvarchangefood)


def lvarcheckhealth(a={}, args={}):
    print("pдесь вероятна ошибка")
    print(allhap["health"])
    print(args)

    if allhap["health"][0] >= args["chval"]:
        return True
    else:
        return False


def lvarchangebeauty(args={}):
    if monthl[0] < 20:
        args["chval"] = 30
        args["text"] = "Уровень здравоохранения выше 30"
        return args
    elif monthl[0] < 40:
        args["chval"] = 45
        args["text"] = "Уровень здравоохранения выше 45"
        return args
    else:
        args["chval"] = 60
        args["text"] = "Уровень здравоохранения выше 60"
        return args

def lv6(a={}, args={}):

    for i in buildings:
        if i.type == "freedom":
            if i.mode == "communists":
                return True
    return False

def lv66(args={}):
    args["text"] = "Есть коммунистическая газета"
    return args

lvar2 = reqcore(checcomhome, lvarchangehome)

lvar = mainfrac(name="communists")  # защищенность капиталистов
lvar3 = reqcore(lvarcheckhealth, lvarchangebeauty)
lvar666 = reqcore(lv6, lv66, 10)
lvar2.value = 30
lvar3.value = 30
lvar.addmain(lvar2)
lvar.addmain(lvar3)
lvar.addmain(lvar4)
lvar.addsec(lvar666)

lvar.set_rate()


fracmains["communists"] = lvar


def checloyahome(a={}, args={}):

    cnt = 0
    for i in buildings:
        if i.type == "childhome" and i.bready > 0:
            cnt += 1
    if cnt > 0:
        return True
    else:
        return False

def checloyaelec(a={}, args={}):

    if gamevalues["last_elections"] == False or gamevalues["last_elections"] == None:
        return True
    else:
        return False

def lvarchangeloyaelec(args={}):
    args["text"] = "Выборы не проведены"
    return args


def lvarchangechildhome(args={}):
    args["text"] = "построен дом детства"
    return args


def checloyamania(a={}, args={}):

    if timelist[0] - gamevalues["last_mania_time"] < 58:
        return True
    else:
        return False

def lvarchecloyamania(args={}):
    args["text"] = "Указ мании величии < 5 лет"
    return args

def ll1(a={}, args={}):
    print(palaces)
    if len(palaces[0].workers) >= 4:
        return True
    else:
        return False

def ll11(args={}):
    args["text"] = "Дворец охраняют 4 человека"
    return args

def ll2(a={}, args={}):

    if palaces[0].salary >= 50:
        return True
    else:
        return False

def ll22(args={}):
    args["text"] = "Охрана дворца получает зарплату не ниже 50"
    return args

def ll3(a={}, args={}):
    self = palaces[0]
    for i in range(3):
        if self.modstates[i] != True:
            return False
    return True

def ll33(args={}):
    args["text"] = "Все улучшения дворца есть"
    return args

lvar3 = reqcore(checloyahome, lvarchangechildhome)
lvar4 = reqcore(checloyaelec, lvarchangeloyaelec)
lvar5 = reqcore(checloyamania, lvarchecloyamania)
lvar01 = reqcore(ll1, ll11, 10)
lvar02 = reqcore(ll2, ll22, 10)
lvar03 = reqcore(ll3, ll33, 10)
lvar = mainfrac(name="loyalists")
lvar.addmain(lvar3)
lvar.addmain(lvar4)
lvar.addmain(lvar5)
lvar.addsec(lvar01)
lvar.addsec(lvar02)
lvar.addsec(lvar03)
fracmains["loyalists"] = lvar

def checknatsal(a={}, args={}):

    if growthdi["avsalary"] >= gamevalues["carribean_salary"]:
        return True
    else:
        return False

def lvarchecknatsal(args={}):
    args["text"] = "Высокая зарплата (выше чем Карибская)"
    return args

def checknatsal(a={}, args={}):

    if gameparametrs["imigration office mode"] != "base"  or gameparametrs["imigration office 1"] == None:
        return True
    else:
        return False

def lvarchecknatsal(args={}):
    args["text"] = "Границы не открыты для всех подряд"
    return args

def checknatun(a={}, args={}):

    if gamevalues["first_union"] == None:
        return True
    else:
        return False

def lvarchecknatun(args={}):
    args["text"] = "Нет союза со сверхдержавой"
    return args

def lv6(a={}, args={}):

    for i in buildings:
        if i.type == "freedom":
            if i.mode == "nationalists":
                return True
    return False

def lv66(args={}):
    args["text"] = "Есть национальная газета"
    return args

lvar3 = reqcore(checknatsal, lvarchecknatsal)
lvar4 = reqcore(checknatsal, lvarchecknatsal)
lvar5 = reqcore(checknatun, lvarchecknatun)
lvar33 = reqcore(lv6, lv66, 10)
lvar = mainfrac(name="nationalists")
lvar.addmain(lvar3)
lvar.addmain(lvar4)
lvar.addmain(lvar5)
lvar.addsec(lvar33)
fracmains["nationalists"] = lvar

def lv1(a={}, args={}):

    if gamevalues["last_elections_fraud"] != True and gamevalues["last_elections"] != False:
        return True
    else:
        return False

def lv11(args={}):
    args["text"] = "Последние выборы были честными"
    return args

def lv2(a={}, args={}):

    a = False
    for i in buildings:
        if i.type == "schoщl":
            a = True
    return a


def lv22(args={}):
    args["text"] = "Есть средняя школа"
    return args

def lv3(a={}, args={}):
    a = False
    for i in buildings:
        if i.type == "univ":
            a = True
    return a

def lv33(args={}):
    args["text"] = "Есть Колледж"
    return args

def lv4(a={}, args={}):
    a = False
    if allhap["freedom"][0] >= 60:
        return True
    else:
        return False

def lv44(args={}):
    args["text"] = "Свобода больше 60"
    return args

lvar3 = reqcore(lv1, lv11)
lvar33 = reqcore(lv2, lv22)
lvar333 = reqcore(lv3, lv33)
lvar3333 = reqcore(lv4, lv44, 10)
lvar = mainfrac(name="intellectuals")
lvar.addmain(lvar3)
lvar.addmain(lvar33)
lvar.addmain(lvar333)
lvar.addsec(lvar3333)
fracmains["intellectuals"] = lvar

def lv1(a={}, args={}):

    cnt = 0
    for i in humans:
        if i.work_n >=0 and (buildings[i.work_n].type == "army1" or buildings[i.work_n].type == "army2" or buildings[i.work_n].type == "army3"):
            cnt += 1
    if cnt >= len(rebels):

        return True
    else:
        return False

def lv11(args={}):
    args["text"] = "Солдат больше чем повстанцев"
    return args


def lv2(a={}, args={}):

    cnt1 = 0
    cnt2 = 0
    for i in humans:
        if i.work_n >=0 and (buildings[i.work_n].type == "army1"):
            cnt1 += 1
    for i in humans:
        if i.work_n >=0 and (buildings[i.work_n].type == "army2"):
            cnt2 += 1
    if cnt2 * 3 >= cnt1:

        return True
    else:
        return False

def lv22(args={}):
    args["text"] = "На каждых 3 солдат один генерал"
    return args


def lv3(a={}, args={}):

    cnt1 = 0

    for i in humans:
        if i.work_n >=0 and (buildings[i.work_n].type in soldierset):
            cnt1 += 1
    """for i in humans:
        if i.work_n  >=0 and (buildings[i.work_n].type == "army2"):
            cnt1 += 1

    for i in humans:
        if i.work_n  >=0 and (buildings[i.work_n].type == "army3"):
            cnt1 += 1"""

    lhum = len(humans) - cnt1


    if cnt1*30 >= lhum:

        return True
    else:
        return False

def lv33(args={}):
    args["text"] = "На каждых 30 солдат хотя бы 1 солдат"
    return args



def lv4(a={}, args={}):

    for i in buildings:
        if i.type == "weapon":
            return True
    return False

def lv44(args={}):
    args["text"] = "Построен оружейный завод"
    return args


def lv5(a={}, args={}):

    if allhap["safety"][0] > allhap["freedom"][0]:
            return True
    return False

def lv55(args={}):
    args["text"] = "Защищенность выше свободы"
    return args

def lv6(a={}, args={}):

    for i in buildings:
        if i.type == "freedom":
            if i.mode == "army":
                return True
    return False

def lv66(args={}):
    args["text"] = "Есть военная газета"
    return args


def lv7(a={}, args={}):
    cnt = 0
    for i in humans:
        if buildings[i.work_n].type in soldierset:
            cnt = 1
            if buildings[i.work_n].salary < 20:
                return False
    if cnt == 0:
        return False
    return True

def lv77(args={}):
    args["text"] = "жалование солдат больше 20"
    return args

def lv8(a={}, args={}):
    cnt = 0
    for i in humans:
        if buildings[i.work_n].type in soldierset:
            cnt += 1
    if cnt < 30:
        return False
    return True

def lv88(args={}):
    args["text"] = "В армии больше 30 людей"
    return args

def lv9(a={}, args={}):
    cnt = 0
    for i in buildings:
        if i.type == "army2":
            return True
    return False


def lv99(args={}):
    args["text"] = "Построен арсенал"
    return args


lvar3 = reqcore(lv1, lv11)
lvar33 = reqcore(lv2, lv22)
lvar333 = reqcore(lv3, lv33)
lvar3333 = reqcore(lv4, lv44, 10)
lvar33333 = reqcore(lv5, lv55, 10)
lvar333333 = reqcore(lv6, lv66, 10)
lvar3333333 = reqcore(lv7, lv77, 10)
lvar33333333 = reqcore(lv8, lv88, 10)
lvar333333333 = reqcore(lv9, lv99, 10)
lvar = mainfrac(name="militarists")
lvar.addmain(lvar3)
lvar.addmain(lvar33)
lvar.addmain(lvar333)
lvar.addsec(lvar3333)
lvar.addsec(lvar33333)
lvar.addsec(lvar333333)
lvar.addsec(lvar3333333)
lvar.addsec(lvar33333333)
lvar.addsec(lvar333333333)
fracmains["militarists"] = lvar


def lv1(a={}, args={}):

    for i in buildings:
        if i.type == "church":
            return True
    return False

def lv11(args={}):
    args["text"] = "Построена церковь"
    return args

def lv2(a={}, args={}):

    for i in buildings:
        if i.type == "sobor":
            return True
    return False

def lv22(args={}):
    args["text"] = "Построен собор"
    return args


def lv3(a={}, args={}):

    if allhap["religion"][0] >= args["chval"]:
        return True
    else:
        return False


def lv33(args={}):
    if monthl[0] < 48:
        args["chval"] = 40
        args["text"] = "Уровень красоты выше 30"
        return args
    else:
        args["chval"] = 60
        args["text"] = "Уровень красоты выше 60"
        return args

def lv4(a={}, args={}):

    for i in buildings:
        if i.type == "freedom":
            if i.mode == "religion":
              return True
    return False

def lv44(args={}):
    args["text"] = "Религиозная газета"
    return args


lvar3 = reqcore(lv1, lv11)
lvar33 = reqcore(lv2, lv22)
lvar333 = reqcore(lv3, lv33)
lvar3333 = reqcore(lv4, lv44)
lvar = mainfrac(name="religion")
lvar.addmain(lvar3)
lvar.addmain(lvar33)
lvar.addmain(lvar333)
lvar.addsec(lvar3333)
#if gameparametrs["religion"] == True:
fracmains["religion"] = lvar

