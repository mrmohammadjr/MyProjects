class pay:
  def __init__(self, hours, rate):
    self.hours = hours
    self.rate = rate

  def myfunc(self):
    if hours < 40:
      money = rate * hours
    else:
      overtime = hours - 40
      money = (rate * 40.0) + (1.5 * rate * overtime)
    print('pay : ',money)

inth = input("enter hours : ")
intr = input("enter rate : ")
hours = int(inth)
rate = int(intr)
pays = pay(hours, rate)
pays.myfunc()