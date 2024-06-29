from mainquest import *


def zerofunc13():
    return 0
class decree():
    def __init__(self, description = "", action = truefunc, type = "full", uslov = truefunc, name = "", price = zerofunc13):

        self.description = description #описание того что делает указ
        self.action = action #функция которая в игре указ осуществит (от изменения специфического параметра до прямых изменений игры
        self.type = type #Есть несколько типов 1) постоянное действие 2) единоразовый эффект 3) временный эффект
        self.uslov = uslov
        self.name = name
        self.price = zerofunc13





lvar = decree()

lvar.name = "free_home"
lvar.description = "бесплатное жилье для всех"
def lvardef():
    for i in buildings:
        if i.type == "home":
            i.rent = 0
    transact(0, "outside", 500)
    gamevalues["free_home"] = True
    #money[0] -= 500

lvar.action = lvardef

def lp():
    return 500

lvar.price = lp

testdecree = lvar

decrees5.append(testdecree)



decreestat = ["main", testdecree ]


lvar = decree()
lvar.name = "emission"
lvar.description = "Печать 20 000, инфляция 30 процентов"
def lvardef():

    money[0]+=20000
    gamevalues["emission"]+=1
    gameparametrs["pricemodifer"] = gameparametrs["pricemodifer"]*1.3



lvar.action = lvardef

def lvardef():
    if gamevalues["emission"] <= 4:
        return True
    else:
        return False

lvar.uslov = lvardef

def lp():
    return 0

lvar.price = lp

decrees5.append(lvar)


#"last_tax_reduction" gamevalues


lvar = decree()
lvar.name = "taxreduct"
lvar.description = "Снижаем налоги"
def lvardef():

    #money[0] -=
    for i in humans:
        if i.life == 1:
            transact("island", i, 100)

    print("сейчас месяц", monthl[0])
    gamevalues["last_tax_reduction"] = monthl[0]
    #gamevalues["emission"]+=1
    #gameparametrs["pricemodifer"] = gameparametrs["pricemodifer"]*1.3



lvar.action = lvardef

def lvardef():

        return True


lvar.uslov = lvardef

def lp():
    a = 0
    for i in humans:
        if i.life == 1:
            a+=1
    return a*100

lvar.price = lp

decrees3.append(lvar)


lvar = decree()
lvar.name = "early_elections"
lvar.description = "ранние выборы"


def lvardef():
    if mainquests[0].electionquest.stage < 99:
        mainquests[0].electionquest.beginstage(99)

lvar.action = lvardef


def lvardef():
    if mainquests[0].electionquest.stage < 99:
        return True
    else:
        return False


lvar.uslov = lvardef


def lp():
    return 2000

lvar.price = lp


decrees4.append(lvar)

lvar = decree()
lvar.name = "industry_reclaim"
lvar.description = "рекламная компания промышленности"


def lvardef():
    gamevalues["last_industry_reclaim"] = monthl[0]
    transact(0, "outside", 8000)

lvar.action = lvardef


def lvardef():
    #print(monthl)
    print("тестовый параметр: ", timeparametr("last_industry_reclaim", 36))
    if gamevalues["last_industry_reclaim"] + 36 <= monthl[0]:
        print("Указ не введен")
        print(monthl, gamevalues["last_industry_reclaim"])
        return True
    else:
        print("Указ введен")
        print(monthl, gamevalues["last_industry_reclaim"])
        return False


lvar.uslov = lvardef


def lp():
    return 8000

lvar.price = lp


decrees3.append(lvar)




lvar = decree()
lvar.name = "likbezedict"
lvar.description = "Ликвидация безграмотности"


def lvardef():
    if gamevalues["likbez"] == False:
        gamevalues["likbez"] = True
        transact(0, "outside", 3000)
    else:
        gamevalues["likbez"] = False

lvar.action = lvardef


def lvardef():
    return True


lvar.uslov = lvardef


def lp():
    if gamevalues["likbez"] == False:
        return 3000
    else:
        return 0

lvar.price = lp


decrees1.append(lvar)