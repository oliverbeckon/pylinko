


money = 0

def init(starterMoney = 100) -> None:
  global money
  money = starterMoney

def addMoney(value) -> None:
  global money
  money += value

def getMoney() -> int:
  global money
  return money
  
def isMore(value) -> True | False:
  global money
  return money >= value