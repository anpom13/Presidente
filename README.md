# Presidente
#Для запуска игры необходимо:
#Python с установленными pygame, random и sys модулями
#
#Для запуска на ios/ipad os достаточно Python3IDE.
#
#
#Для запуска последей версии запускайте файл main_pygame.py
#
#
#
#Эта игра -- градостроительный/экономический симулятор.
#в игре реализовано:
#люди, каждый из которых сам принимает решения на счет того, что ему делать
#Много видов зданий, каждое из которых тем или иным образом влияет на аспекты жизни островитян
#система астостоянок и дорог, простая система нахождения оптимального пути и система предварительной генерации оптимального пути 
#система строительства зданий, стоянок и дорог
#система отображения основной информации о каждом жителе и о каждом здании на острове, система настройки некоторых зданий, система квестов, фракций, валютная биржа, бюджетные правила и валютные интервенции, влияющие на курс национальной валюты (если включено, работает в тестовом режиме), политическая система (в тестовом режиме), сбор и отображение статистики каждого здания, жителя
#
#
#
#
#Для строительства зданий:
#Нажмите кнопку "строительство". Откроется режим строительства. Нажмите на то здание, которое хотите построить. Нажмите на то место на карте, в котором вы хотите его построить. Нажмите кнопку "строить". Для выхода из режима строительства нажмите кнопку "строительство". В зависимости от размера карты выход из режима строительства может занять продолжительное время, поскольку при выходе из этого режима заново генерируются некоторые пути. 
#
#Для получения информации о здании -- найдите его на картеи щелкните по нему. Откроется меню здания
#Для получения информации о жителе -- найдите здание, в котором он работает, откройте один из пунктов контекстного меню здания, щелкните по кнопке с именем жителя. Откроется меню жителя
#
#Виды зданий:
#1) Ферма, нужна для производства растительной пищи и ресурсов
#2) Ранчо -- для производства мяса и молока
#3) Клиника -- нужна для производства аспирина, им жители удовлетворяют потребность в здоровье (другого лечения на острове не найти!) 
#4) Экспортный центр (порт) -- экспортирует товары, произведенные на острове по экспортным ценам
#5) Офис грузоперевозок -- нужен для перемещения товаров между зданиями 
#6) Театр -- нужно для того, чтобы жители могли удовлетворять потребность в развлечениях
#7) Жилой дом -- нужен для того чтобы жители удовлетворяли потребность в отдыхе. Разные дома 
#8) Продуктовый магазин -- нужен для того чтобы продавать товары
#9) Имиграционное бюро -- привлекает на остров иммигрантов
#10) Ромовый завод -- производит ром из сахара. Для запуска процесса производство рома нужно построить фему, поставить её в режим производства сахара и подождать пока офис грузоперевозок не переместит сахар из фермы в ромовый завод
#11) Консервный завод -- производит консервы их ананасов, кофе или мяса
#12) Сырный завод -- производит сыр из молока
#13)Сигарная фабрика -- производит сигары из табака
#Множество других зданий
#
#Для того чтобы жители могли быстро перемещаться по острову, им нужны дорога и автостоянка. Постройте дорогу и постройте гараж в тех местах, где жители часто бывают и дальше жители сами решат, какой спрсоб передвижения займёт у них меньше времени. Но будьте осторожны -- большое количество машин на дорогах может привести к пробкам.
#
#В случае если обнаружите, что в том или ином здании нет или почти нет рабочих, увеличьте зарплату в этом здании. Жители каждый месяц пересматривают свой выбор места работы, и при выборе учитывают в том числе и зарплату
#
#Для изменения начального количества жителей измените nhumans в lists.py
#
#
#
#
