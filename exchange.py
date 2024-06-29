
from semaphore import *
#министерство финансов устанавливает бюджетное правило. Его возможные параметры:
#1) часть доходов от экспорта (по умолчанию 50 процентов) может переводиться в рубли
#2) Если доход за месяц превышает заданную величину, то оставшаяся доходов может переводиться на счет цб/на счет минфина. по умолчанию не применяется
#3) Может просто переводить часть доходов на свой счет/ на счет цб. В случае применения правила 1 устанавливается часть доходов которая 
#4) Независимость от экспортных цен: если экспортная цена на товар выше установленного значения, то часть доход от экспорта по установленной цене отправляется в бюджет, остальная часть в минфин/в цб
# курс доллара dcourse[0] — сколько можно купить рублей за 1 доллар, 
# 1 доллар = dcourse[0] * 1 рубль
# 1 рубль = 1 доллар / dcourse[0]
def cmodul(a):
  if a>= 0:
    return a
  else:
    return -a

class minfin(object):
  def __init__(self):
    self.money = [0,0]
    self.exmode = "parttobudget" #половину экспорта переводит в рубли в бюджет
    self.exmode2 = "parttomb"
    self.part = 50 #процентов. эта часть прибыли от экспорта обменивается на рубли в цб
    self.part2 = 25#процентов. эта часть идет на счет в цб
    
  def extransact(self, val):
    part1 = 0
    if self.exmode == "parttobudget":
      part1 = max(0,min(self.part, 100))/100
      
      
      mainbanks[0].change("usdtorub", val*part1)
      money[0]+= val*part1*dcourse[0]
    p1 = part1*100
    part2 = max(0,min(self.part2, 100-p1))/100
    mainbanks[0].money[1] += val*part2
    part10 = 1 - part1 - part2
    money[1]+= val* part10
    
# цетральный банк устанавливает общие правила, по которым производится обмен валют
# по умолчанию все заявки на обмен автоматически адресуются бирже (плавающий курс)
# возможные режимы работы:
# плавающий курс — установлен по умолчанию 
# интервенции для манипуляции курсом, размер которых устанавливается вручную проводятся до тех пор пока на счете цб есть деньги (фиксированный размер в месяц)
# поддержка курса — цб определяет размер интервенций для поддержания текущего курса рубля. при наличии средств гарантирует, что курс не изменится польше чем на заданное количество процентов
# интервенции для достижения целевого значения курса — будут применяться для достижения и удержания целового курса
# ограничение импорта — если импорт (за рубли) выше задонного значения в месяц, импорт товаров (за исключением указов президента) запрещается
# фиксированный курс — цб не отправляет заявки на обмен на биржу, а вместо этого сам производит обмен валют по заданному Президентом курсу. В случае исчерпания бюджета цб, импорт для жителей острова ограничивается. Президенте может специальным указом осуществить импорт/экспорт товаров без операций обмена
class mainbank(object):
  def __init__(self):
    self.money = [0,0]
    self.buy = 0
    self.sell = 0
    self.mode1 = "support"
    self.mode2 = "support"
    self.target_rate = 1
    self.intervention = None
    self.targetrate = 1
    self.allprinted = 0
  def change(self, transaction = "rubtousd", val = 0):
   if self.mode1 != "imitation":
    if transaction == "rubtousd":
      self.sell += val
    if transaction == "usdtorub":
      self.buy += val*dcourse[0]
  def printmoney(self, val):
    money[0] += val
    self.allprinted += val
  def life(self):
    if self.mode1 == "free":
      if self.sell > 0:
        exchanges[0].sell += self.sell
        self.sell = 0
      if self.buy > 0:
        exchanges[0].buy += self.buy
        self.buy = 0
    if self.mode1 == "support":
      
      dx = self.sell - self.buy
      #print("dx = ",dx, " курс: ", dcourse[0])
      if dx > 0:
        #print("dx > 0")
        if self.money[1]*dcourse[0] < dx:
          #print("недостаточно денег, есть ", self.money[1], " долларов")
          if self.money[1]>0:
            self.buy += self.money[1]*dcourse[0]
            money[0] += money[1]*dcourse[0]
            self.money[1]=0
        else:
          #print("деньги есть ")
          self.buy = self.sell
          self.money[1] -= dx/dcourse[0]
          money[0] += dx
      if dx < 0:
        #print("dx < 0, печатаем рубли")
        money[0] += dx
        self.money[1] -= dx/dcourse[0]
        self.sell = self.buy
      if self.sell > 0:
        exchanges[0].sell += self.sell
        self.sell = 0
      if self.buy > 0:
        exchanges[0].buy += self.buy
        self.buy = 0
  
  
class exchange(object):
  def __init__(self):
    self.buy = 0 #биржа покупает рубли
    self.sell = 0 #биржа продает рубли
    
  def adjust_exchange_rate(self, current_rate, buy_orders, sell_orders, adjustment_factor=0.01):
    demand_supply_difference = buy_orders - sell_orders
    lv1 = cmodul(demand_supply_difference)/(buy_orders+ sell_orders+0.000001)
    lv1 = lv1*lv1*200
    # Если спрос превышает предложение, увеличиваем курс
    if demand_supply_difference > 0:
        new_rate = current_rate / (1 + adjustment_factor*lv1)
    # Если предложение превышает спрос, снижаем курс
    elif demand_supply_difference < 0:
        new_rate = current_rate * (1 + adjustment_factor*lv1)
    # Если спрос и предложение равны, курс остается неизменным
    else:
        new_rate = current_rate

    return new_rate
  def update(self, adj = 0.01):
    #print("старый курс ", dcourse[0])
    #print("заявок на покупку", self.buy)
    #print("заявок на продажу", self.sell)
    dcourse[0] = self.adjust_exchange_rate(dcourse[0], self.buy, self.sell, adj)
    #print("новый курс ", dcourse[0])
    #столько иностранные инвесторы вкладывают в месяц
    pm = mainbanks[0].allprinted
    realcourse = dcourse[0]/math.sqrt((25000 + pm)/25000)
    self.buy = 1000*dcourse[0] * realcourse#биржа покупает рубли #
    self.sell = 1000*dcourse[0] /  realcourse#биржа продает рубли
    
    
class exchange2(object):
  def __init__(self):
    self.buy = 0 #биржа покупает вымышленную валюту
    self.sell = 0 #биржа продает вымышленную валюту
    
  def adjust_exchange_rate(self, current_rate, buy_orders, sell_orders, adjustment_factor=0.01):
    demand_supply_difference = buy_orders - sell_orders
    lv1 = cmodul(demand_supply_difference)/(buy_orders+ sell_orders+0.000001)
    lv1 = lv1*lv1*15
    # Если спрос превышает предложение, увеличиваем курс
    if demand_supply_difference > 0:
        new_rate = current_rate / (1 + adjustment_factor*lv1)
    # Если предложение превышает спрос, снижаем курс
    elif demand_supply_difference < 0:
        new_rate = current_rate * (1 + adjustment_factor*lv1)
    # Если спрос и предложение равны, курс остается неизменным
    else:
        new_rate = current_rate

    return new_rate
  def update(self, adj = 0.01):
    #print("старый курс ", dcourse[0])
    #print("заявок на покупку", self.buy)
    #print("заявок на продажу", self.sell)
    dcourse[0] = self.adjust_exchange_rate(dcourse[0], self.buy, self.sell, adj)
    #print("новый курс ", dcourse[0])
    
    self.buy = 0 #биржа покупает рубли
    self.sell = 0 #биржа продает рубли

exchanges = [exchange()]
mainbanks = [mainbank()]
minfins = [minfin()]

#roadexch

hapexchdic = {
  "food": exchange2(),
  "health": exchange2(),
  
}
# Пример использования функции:
#current_rate = 10  # текущий курс обмена
#buy_orders = 100   # количество заявок на покупку
#sell_orders = 0   # количество заявок на продажу

#new_rate = adjust_exchange_rate(current_rate, buy_orders, sell_orders)
#print("Новый курс обмена:", new_rate)