from savestate import *


texturedic = {
    'mansion':"textures/buildings/homes/condom.jpg",
    "condonium":"textures/buildings/homes/condom.jpg",
    'tenement':'textures/buildings/homes/tenement.jpg',
    'farm':'textures/buildings/farm.jpg',
    'barak':'textures/buildings/homes/barak.jpg',
    'shanty':"textures/buildings/homes/shanty.jpg",
    'clinic':'textures/buildings/clinic.jpg',
    'apartment':'textures/buildings/homes/apartment.jpg',
    "canns": "textures/buildings/factories/1.jpg",
    "cigar":"textures/buildings/factories/2.jpg",
    "cheese":"textures/buildings/factories/3.jpg",
    "rome":"textures/buildings/factories/4.jpg",
    "furniture":"textures/buildings/factories/5.jpg",
    "lumber":"textures/buildings/factories/6.jpg",
    "jewerly":"textures/buildings/factories/7.jpg",
}

def gettexture(name):
    if name in texturedic:
        return texturedic[name]

    else:
        print("texture_not_found")
        return 'grass'

"""
butdisstat[4].text = str(self.testp5)
        # price = str(infomod[0])
        butdisinfo[0].text = idinfo
        butdisinfo[1].text = idinfo2
        butdismode[0].text = mode1
        butdismode[1].text = mode2
        butdismode[2].text = mode3
        butdismode[3].text = mode4
        butdismode[4].text = mode5
        butdisother[0].text = other1
        butdisother[1].text = other2
        butdisother[2].text = other3
        butdisother[3].text = other4
        butdisother[4].text = other5
        butdisother[5].text = other6
        buttonsfarm[1].text = name  # везде
        butdisprice

"""


def infodisu(self, buttonsfarm, butdisinfo, butdismode, butdisprice, butdisstat, butdisother):

    if self.maintype == "human":

        self.dismod = 1

        if buttonsinfomen[0].press() == 1:
            infomod[0] = "info"
            priorl2 = butdisinfo
        if buttonsinfomen[1].press() == 1:
            infomod[0] = "mode"
            priorl2 = butdismode
        if buttonsinfomen[2].press() == 1:
            infomod[0] = "money"
            priorl2 = butdisprice
        if buttonsinfomen[3].press() == 1:
            infomod[0] = "stat"
            priorl2 = butdisstat
        if buttonsinfomen[4].press() == 1:
            infomod[0] = "other"
            priorl2 = butdisother
        stdi = {0: "идет в ", 1: "занят, ", 2: "думает"}
        ttdi = {0: "ест в ", 1: "лечится в ", 2: "отдыхает в ", 3: "работает в ", 4: "веселится в "}

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
            resourses = "статус: " + stdi[self.state] + res2
        else:
            resourses = ""
        age = "возраст: " + str(self.age)

        name = self.name
        workers = "деньги:              " + str(int(self.money))
        sal = "зарплата на момент найма: " + str(int(self.salary))
        # pygame.draw.rect(sc, (225,225,220), (0, h/2, w+250, h/2+50))
        if infomod[0] == "mode":
            priorl2 = butdismode
        if infomod[0] == "other":
            priorl2 = butdisother

            # pygame.draw.rect(sc, (0,0,0), (w/2, h/1.5 +20, self.hap_eat , 70))
        if infomod[0] == "money":
            priorl2 = butdisprice
        if infomod[0] == "stat":
            priorl2 = butdisstat
        if infomod[0] == "info":
            priorl2 = butdisinfo
        for i in priorl2:
            i.active = 1
        # for i in butdisprice:
        # i.text = ""
        for i in butdisinfo:
            i.text = ""
        for i in butdismode:
            i.text = ""
        for i in butdisother:
            i.text = ""
        for i in butdisstat:
            i.text = ""

        setbtext()
        buttonsfarm[7].text = name
        butdisinfo[0].text = age
        butdisinfo[1].text = workpl
        butdisprice[8].text = resourses
        butdisprice[9].text = workers
        butdisprice[10].text = sal
        butdisstat[20].text = "сытость: " + str(int(self.hap_eat))
        butdisstat[21].text = "здоровье: " + str(int(self.hap_health))
        butdisstat[22].text = "веселье: " + str(int(self.hap_fun))
        butdisstat[23].text = "отдых: " + str(int(self.rest))
        butdisstat[24].text = "работа: " + str(int(self.wotworkt))



        butdisstat[1].text = "работа: " + str(int(self.happiness["job"]))
        butdisstat[2].text = "коасота: " + str(int(self.happiness["beauty"]))
        butdisstat[3].text = "кдом: " + str(int(self.happiness["home"]))
        butdisstat[4].text = "свобода: " + str(int(self.happiness["freedom"]))
        butdisstat[0].text = "еда: " + str(int(self.happiness["food"]))
        butdisstat[5].text = "безопасность: " + str(int(self.happiness["safety"]))
        butdisstat[6].text = "развлечения: " + str(int(self.happiness["fun"]))
        butdisstat[7].text = "здоровье: " + str(int(self.happiness["health"]))
        butdisstat[8].text = "уважение: " + str(int(self.happiness["respect"]))
        butdisstat[9].text = "всего: " + str(int(self.happiness["main"]))
        butdisother[0].text = self.thinfo1
        butdisother[1].text = self.thinfo2
        butdisother[2].text = self.thinfo3
        butdisother[3].text = self.thinfo4
        butdisother[4].text = self.thinfo5

    if self.maintype == "building":
        # priorl2 = []
        #setbtext() #сбрасывает кнопки
        mode1 = ""
        mode2 = ""
        mode3 = ""
        mode4 = ""
        mode5 = ""
        other1 = ""
        other2 = ""
        other3 = ""
        other4 = ""
        other5 = ""
        other6 = ""
        if self.workallow == 1:
            other6 = "рабочие:"
        idinfo2 = ""
        """
        for i in buttonsinfomen:########################################################################b
            i.active = 1
        if buttonsinfomen[0].press() == 1:
            infomod[0] = "info"
            priorl2 = butdisinfo
        if buttonsinfomen[1].press() == 1:
            infomod[0] = "mode"
            priorl2 = butdismode
        
        if buttonsinfomen[2].press() == 1:
            infomod[0] = "money"
            priorl2 = butdisprice
        if buttonsinfomen[3].press() == 1:
            infomod[0] = "stat"
            priorl2 = butdisstat
        if buttonsinfomen[4].press() == 1:
            infomod[0] = "other"
            priorl2 = butdisother#############################################################################################E
        """
        resourses = "не доделано: " + str(int(self.outres["corn"]))
        name = "Здание"
        workers = "Работает: " + str(self.nwork) + " из " + str(self.maxnwork)
        sal = "Зарплата: " + str(int(self.salary))
        price = "Цена: " + str(int(self.price))
        if self.subtype != "":
            subtype = "режим работы: " + str(self.subtype)
        else:
            subtype = "у данного здания нет режимов работы"
        eatallow = ""
        idinfo = ""

        if self.eat_allow == 0 and self.type != "minfin":#######################################################################B
            eatallow = "здание не предоставляет пищу"
            #price = ""
           # butdisprice[2].active = 0
           # butdisprice[3].active = 0
        else:
            eatallow = "здание предоставляет пищу"
           # butdisprice[2].active = 1
          #  butdisprice[3].active = 1#################################################################################################

        if self.type == "palace":
            name = "Дворец"
            idinfo = "Ваш дворец"
        if self.type == "metro":
            name = "Метрополитен"
            idinfo = "Позволяет быстро перемещаться по острову"
        if self.type == "elec":
            name = "Электростанция"
            resourses = "Всего:" + str(int(electro[0])) + "Дост:" + str(int(electro[1]))
            price = str(electro[2]) + " " + str(electro[3])
        if self.type == "mine":
            name = "Шахта"
            resourses = "На складе:" + str(int(self.outres[self.subtype])) + " осталось:" + str(self.mineres.amount)
            idinfo = "Шахта позволяет добывать полезные ископаемые"
            price = self.power_switch
        if self.type == "tavern":
            name = "Театр"
            resourses = "Посетители: " + str(len(self.visiters))
            idinfo = "Одно из немногих местных развлечений"
            price = "Цена: " + str(int(self.price))
        if self.type == "rome":
            resourses = "Количество рома на складе: " + str(int(self.outres["rom"]))
            name = "Ромовый завод"
            other1 = "ром:  " + str(int(self.outres["rom"]))
            other2 = "сахар:" + str(int(self.inres["sugar"]))
            # other6 = str(int(self.pinres[ "sugar" ]))
            idinfo = "делает ром из сахара"
        if self.type == "cigar":
            resourses = "Количество сигар на складе: " + str(int(self.outres["cigar"]))
            name = "Сигаретная фабрика"
            other1 = "сигары:  " + str(int(self.outres["cigar"]))
            other2 = "табак:" + str(int(self.inres["tobacco"]))
            # other6 = str(int(self.pinres[ "sugar" ]))
            idinfo = "делает сигары из табака"
        if self.type == "cheese":
            resourses = "Количество сыра на складе: " + str(int(self.outres["cheese"]))
            name = "Сырный завод"
            other1 = "сыр:   " + str(int(self.outres["cheese"]))
            other2 = "молоко:" + str(int(self.inres["milk"]))
            # other6 = str(int(self.pinres[ "sugar" ]))
            idinfo = "делает сыр из молока"
        if self.type == "canns":
            resourses = "Количество товара на складе: " + str(int(self.outres["canns"]))
            name = "Консервный завод"
            other1 = "консервы: " + str(int(self.outres["canns"]))
            other2 = "ананасы:  " + str(int(self.inres["pineapple"]))
            other3 = "кофе:  " + str(int(self.inres["coffee"]))
            other4 = "мясо:  " + str(int(self.inres["meat"]))
            mode1 = "мясо"
            mode2 = "ананасы"
            mode3 = "кофе"
            # other6 = str(int(self.pinres[ "sugar" ]))
            idinfo = "делает консервы из мяса, кофе или ананасов"
        if self.type == "mainbank":
            name = "Центральный банк"
            # price = "процент в цб" + str(minfins[0].part2)
            idinfo = "Главный банк острова. Печатает деньги, поддерживает курс рубля"
            mode1 = "free"
            mode2 = "support"
            # resourses = "обмен" + str(minfins[0].part)
        if self.type == "minfin":
            name = "Министерство финансов"
            price = "процент в цб" + str(minfins[0].part2)
            idinfo = "Устанавливает бюджетное правило"
            mode1 = "ex->цб"
            resourses = "обмен" + str(minfins[0].part)

        if self.type == "rancho":
            resourses = "Количество еды: " + str(int(self.outres[self.subtype]))
            name = "Ферма"
            workers = "Работает: " + str(self.nwork) + " из " + str(self.maxnwork)
            sal = "Зарплата: " + str(int(self.salary))
            price = "Цена: " + str(int(self.price))
            mode1 = "мясо"
            mode2 = "молоко"
            # mode3 = "кофе"
            # mode4 = "табак"
            # mode5 = "сахар"
            other1 = "мяса:  " + str(int(self.outres["meat"]))
            other2 = "молока:" + str(int(self.outres["milk"]))
            # other3=  "кофе " + str(self.outres[ "coffee" ])
            # other4=  "табака: " + str(self.outres[ "tobacco" ])
            # other5=  "сахара: " + str(self.outres[ "sugar" ])
            idinfo = "Производит молоко или мясо"
        if self.type == "farm":
            resourses = "Количество еды: " + str(int(self.outres[self.subtype]))
            name = "Ферма"
            workers = "Работает: " + str(self.nwork) + " из " + str(self.maxnwork)
            sal = "Зарплата: " + str(int(self.salary))
            price = "Цена: " + str(int(self.price))
            mode1 = "кукуруза"
            mode2 = "ананасы"
            mode3 = "кофе"
            mode4 = "табак"
            mode5 = "сахар"
            other1 = "кукурузы:" + str(int(self.outres["corn"]))
            other2 = "ананасов:" + str(int(self.outres["pineapple"]))
            other3 = "кофе:     " + str(int(self.outres["coffee"]))
            other4 = "табака:   " + str(int(self.outres["tobacco"]))
            other5 = "сахара:   " + str(int(self.outres["sugar"]))
            # other6 = str(self.poutres["tobacco"])
            idinfo = "На ферме может производиться кукуруза, кофе, ананасы, табак и сахар"
        if self.type == "clinic":
            resourses = "Количество медикаментов: " + str(int(self.amount))
            name = "Клиника"
            workers = "Работает: " + str(self.nwork) + " из " + str(self.maxnwork)
            sal = "Зарплата: " + str(int(self.salary))
            price = "Цена: " + str(int(self.price))
            idinfo = "Недавно мы нашли на острове огромный склад аспирина. В этом здании врачи открывают колбы для островитян"
        if self.type == "home":
            resourses = "Качество жилья: " + str(int(self.quality))
            name = "Дом"
            workers = "Живёт: " + str(self.number) + " из " + str(self.max_number)
            sal = "Цена аренды: " + str(self.rent)
            # price = str(self.id)
            price = ""
            idinfo = "Здесь люди удовлетворяют нужду в отдыхе"
        if self.type == "fur":
            resourses = ""
            name = "Офис грузоперевозок"
            # mode1 = " Авто "
            # mode2 = "Ручной"
            price = ""
            idinfo = "Основное здание в экономике острова. Перевозит грузы из одних зданий в другие"
        if self.type == "shop":
            resourses = ""
            name = "Магазин"
            other1 = "кукурузы: " + str(int(self.outres["corn"]))
            other2 = "ананасов: " + str(int(self.outres["pineapple"]))
            other3 = "кофе:     " + str(int(self.outres["coffee"]))
            other4 = "табака:   " + str(int(self.outres["tobacco"]))
            other5 = "сахара:   " + str(int(self.outres["sugar"]))
            # price = ""
            idinfo = "Перепродаёт товары которые люди произвели на ферме, ранчо и заводах"
        if self.type == "port":
            resourses = ""
            name = "Порт"
            price = ""
            idinfo = "Экспортирует товары, произведённые на острове"
            cnt = 0
            lrlist = []
            for i in self.inres:
                cnt += self.inres[i]
                lrlist.append((self.inres[i], i + ": "))
            lrlist.sort(reverse=True)
            idinfo2 = "на складе: " + str(int(cnt))

            other1 = lrlist[0][1] + str(int(lrlist[0][0]))
            other2 = lrlist[1][1] + str(int(lrlist[1][0]))
            other3 = lrlist[2][1] + str(int(lrlist[2][0]))
            other4 = lrlist[3][1] + str(int(lrlist[3][0]))
            other5 = lrlist[4][1] + str(int(lrlist[4][0]))
            other6 = lrlist[5][1] + str(int(lrlist[5][0]))
            other7 = lrlist[6][1] + str(int(lrlist[6][0]))
            other8 = lrlist[7][1] + str(int(lrlist[7][0]))
            other9 = lrlist[8][1] + str(int(lrlist[8][0]))
            other10 = lrlist[9][1] + str(int(lrlist[9][0]))
        if self.type == "imigration":
            resourses = ""
            name = "Бюро иммиграции"
            price = ""
            idinfo = "Привлекает иммигрантов на остров"
        """
        # pygame.draw.rect(sc, (225,225,220), (0, h/2, w+250, h/2+50))###################################################
        buttonsfarm[0].active = 1
        buttonsfarm[1].active = 1
#########################################################################################################################
"""
        if infomod[0] == "mode":
            priorl2 = butdismode
        if infomod[0] == "other":
            priorl2 = butdisother
        if infomod[0] == "money":
            priorl2 = butdisprice
        if infomod[0] == "stat":
            priorl2 = butdisstat
        if infomod[0] == "info":
            priorl2 = butdisinfo
        """
        for i in priorl2:#####################################################################################################B
            i.active = 1

        s = self.type
        if self.eat_allow == 0:
            if s != "clinic" and s != "tavern" and s != "minfin" and s != "mainbank":
                butdisprice[2].active = 0
                butdisprice[3].active = 0
        elif infomod[0] == "price":
            butdisprice[2].active = 1
            butdisprice[3].active = 1
        if self.workallow == 0 and self.type != "minfin" and self.type != "mainbank":
            butdisprice[0].active = 0
            butdisprice[1].active = 0

            butdisprice[2].active = 0
            butdisprice[3].active = 0
        elif infomod[0] == "price":
            butdisprice[2].active = 1
            butdisprice[3].active = 1
        if infomod[0] == "price" and (self.type == "minfin" or self.type == "mainbank"):
            butdisprice[2].active = 1
            butdisprice[3].active = 1
            butdisprice[0].active = 1
            butdisprice[1].active = 1
#################################################################################################################################
"""
        butdisstat[0].text = str(self.testp1)
        butdisstat[1].text = str(self.testp2)
        butdisstat[2].text = str(self.testp3)
        butdisstat[3].text = str(self.testp4)
        butdisstat[4].text = str(self.testp5)
        # price = str(infomod[0])
        butdisinfo[0].text = idinfo
        butdisinfo[1].text = idinfo2
        #butdismode[0].text = mode1
        #butdismode[1].text = mode2
        #butdismode[2].text = mode3
       # butdismode[3].text = mode4
        #butdismode[4].text = mode5
        butdisother[0].text = other1
        butdisother[1].text = other2
        butdisother[2].text = other3
        butdisother[3].text = other4
        butdisother[4].text = other5
        butdisother[5].text = other6
        buttonsfarm[7].text = name  # везде
        butdisprice[8].text = resourses  # в главную информацию
        butdisprice[9].text = workers  # в price
        butdisprice[10].text = sal  # в price
        butdisprice[11].text = price  # тоже в price
        butdisstat[1].text = "Экспорт"
        butdisstat[11].text = str(int(sumlist(self.monthstat["export"])))

        butdisstat[21].text = str(int(self.allstat["export"]))
        butdisstat[2].text = "местное потребл."
        butdisstat[12].text = str(int(sumlist(self.monthstat["this"])))
        butdisstat[22].text = str(int(self.allstat["this"]))
        butdisstat[3].text = "Зарплата"
        butdisstat[13].text = str(int(sumlist(self.monthstat["salary"])))
        butdisstat[23].text = str(int(self.allstat["salary"]))
        butdisstat[4].text = "Содержание"
        butdisstat[14].text = str(int(sumlist(self.monthstat["upkeep"])))
        butdisstat[24].text = str(int(self.allstat["upkeep"]))
        butdisstat[5].text = "Баланс"
        butdisstat[15].text = str(int(sumlist(self.monthstat["balance"])))
        butdisstat[25].text = str(int(self.allstat["balance"]))
        butdisstat[6].text = "Производство"
        butdisstat[16].text = str(int(sumlist(self.monthstat["prodused"])))
        butdisstat[26].text = str(int(self.allstat["prodused"]))
        butdisstat[7].text = "готовая продукция"
        butdisstat[17].text = str(int(sumdic(self.outres)))
        butdisstat[8].text = "На складе ресурсов"
        butdisstat[18].text = str(int(sumdic(self.inres)))

        butdisstat[10].text = "за 12 мес."
        butdisstat[20].text = "за все время"
        intersale = 1 / fps * 4
        interprice = 1 / fps * 4
        if self.salary > 10:
            intersale = (3 + self.salary) / fps
        if self.price > 10:
            interprice = (3 + self.price) / fps
        """
        if butdisprice[0].press() == 1:
            self.salary += intersale
        if butdisprice[1].press() == 1:
            if self.salary - intersale > 0:
                self.salary -= intersale
            else:
                self.salary = 0

        if butdisprice[8].press() == 1:
            for i in buildings:
                if i.type == self.type:
                    i.salary = self.salary
        if butdisprice[9].press() == 1:
            for i in buildings:
                if i.type == self.type:
                    i.price = self.price
                    if self.type != "minfin":
                        i.prices = self.prices.copy()
        if butdisprice[2].press() == 1:
            self.price += interprice
            if self.type == "farm" or self.type == "rancho":
                for i in eat:
                    self.prices[i] = self.price
        if butdisprice[3].press() == 1:
            self.price -= interprice
            if self.type == "farm" or self.type == "rancho":
                for i in eat:
                    self.prices[i] = self.price
                    
        if self.type == "minfin":
            minfins[0].part = self.salary
            minfins[0].part2 = self.price
        if self.type == "mainbank":
            if butdismode[0].press() == 1:
                self.subtype = "free"
                mainbanks[0].mode1 = "free"
            if butdismode[1].press() == 1:
                self.subtype = "support"
                mainbanks[0].mode1 = "support"
        if self.type == "farm":
            if butdismode[0].press() == 1:
                self.subtype = "corn"
            if butdismode[1].press() == 1:
                self.subtype = "pineapple"
            if butdismode[2].press() == 1:
                self.subtype = "coffee"
            if butdismode[3].press() == 1:
                self.subtype = "tobacco"
            if butdismode[4].press() == 1:
                self.subtype = "sugar"
        if self.type == "fur":
            if butdismode[0].press() == 1:
                self.mode = "auto"
            if butdismode[1].press() == 1:
                self.mode = "manual"
        if self.type == "canns":
            if butdismode[0].press() == 1:
                self.subtype = "meat"
                self.alinres = reszero.copy()
                self.alinres[self.subtype] = 1
            if butdismode[1].press() == 1:
                self.subtype = "pineapple"
                self.alinres = reszero.copy()
                self.alinres[self.subtype] = 1
            if butdismode[2].press() == 1:
                self.subtype = "coffee"
                self.alinres = reszero.copy()
                self.alinres[self.subtype] = 1
        """
        #butdismode[5].text = str(self.f_eat_allow())  # self.subtype -- для тестов
        #butdismode[5].text = self.subtype


        """        if self.type == "rancho":
            if butdismode[0].press() == 1:
            self.subtype = "meat"
            if butdismode[1].press() == 1:
            self.subtype = "milk"
        """
        butdismode[9].text = eatallow  # self.subtype -- для тестов
        #butdismode[8].text = subtype


        """if self.type == "palace":
            butdismode[12].text = 'Вазочки'
            butdismode[13].text = 'Статуи'
            butdismode[14].text = "Охрана"
            butdismode[19].text = "Делать"
            if self.modc == 1:
                butdismode[10].text = "улучшает красоту"
                butdismode[11].text = "5000"
            if self.modc == 2:
                butdismode[10].text = "Легче работать стражам"
                butdismode[11].text = "7000"
            if self.modc == 3:
                butdismode[10].text = "Статуи президентэ"
                butdismode[11].text = "10000" """
        for i in range(len(self.mods)):
            f = self.mods[i]
            butdismode[12+i].text = f.text0
            if self.modc == i+1:
                butdismode[10].text = f.text
                butdismode[11].text = str(f.price)
        print(self.type)
        if len(self.modes) > 0:
            print("Режимы есть")
            if self.activemode == None:
                self.activemode = self.modes[0]
                self.nmode = 0
            butdismode[8].text = self.activemode.text0
            butdismode[9].text = self.activemode.text




# f1 = pygame.font.SysFont('arial', 40)
# text1 = f1.render(name, True,(0, 0, 0))
##text2 = f1.render(resourses, True,(0, 0, 0))
# text3 = f1.render(workers, True,(0, 0, 0))
# text4 = f1.render(sal, True,(0, 0, 0))
# sc.blit(text1, (0, h/2))
# sc.blit(text2, (0, h/2 + 40))
# sc.blit(text3, (0, h/2 + 80))
# sc.blit(text4, (0, h/2 + 120))
        j = 0
        """
if infomod[0] == "price" and self.type == "minfin":
    for i in butdisprice:
        i.active = 1
if infomod[0] == "other":
    for i in self.workers:
        buttonshuman[i].x = w / 3 * 2
        buttonshuman[i].y = h / 3 * 2 + 30 + 20 * j
        buttonshuman[i].active = 1
        j += 1

        """