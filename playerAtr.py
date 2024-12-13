from settings import *
import math

money = 0
ballValue = 0
ballValueIndex = 0
ballAmount = 0


  


playerBalls = []

class ballStats():
    def __init__(self, value, type = balls.Normal, isDuped = False) -> None:
      self.value = value
      self.type = type
      self.isDuped = isDuped

    def getValue(self):
      return self.value
    
    def getType(self):
      return self.type

    def getIsDuped(self):
      return self.isDuped


for i in range(STARTER_BALLAMOUNT):
  playerBalls.append(ballStats(STARTER_BALLVAL))


def getBalls() -> list:
  global playerBalls
  return playerBalls

def playerInit() -> None:
  global money, ballValue, ballValueIndex, ballAmount
  money = STARTER_MONEY
  ballValue = STARTER_BALLVAL
  ballValueIndex = 1
  ballAmount = STARTER_BALLAMOUNT

def addMoney(value) -> None:
  global money
  money += value

def getMoney() -> int:
  global money
  return money
  
def isMore(value) -> True | False:
  global money
  return money >= value

def increaseBallValue() -> None:
  global ballValue
  global ballValueIndex

  ballValueIndex += 1
  ballValue = chip_Value[ballValueIndex % 3] * math.pow(10, math.ceil(ballValueIndex / 3)) / 10

def decreaseBallValue() -> None:
  global ballValue
  global ballValueIndex

  ballValueIndex -= 1
  ballValue = chip_Value[ballValueIndex % 3] * math.pow(10, math.ceil(ballValueIndex / 3)) / 10

def getBallValue() -> int:
  global ballValue
  return ballValue


def getBallAmount() -> int:
  global ballAmount
  return ballAmount