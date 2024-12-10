from settings import *


money = 0
ballValue = 0


def playerInit() -> None:
  global money, ballValue
  money = STARTER_MONEY
  ballValue = STARTER_BALLVAL

def addMoney(value) -> None:
  global money
  money += value

def getMoney() -> int:
  global money
  return money
  
def isMore(value) -> True | False:
  global money
  return money >= value

def setBallValue(value) -> None:
  global ballValue
  ballValue = value

def getBallValue() -> int:
  global ballValue
  return ballValue
