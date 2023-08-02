from ElementalBalance import ElementalBalance
from Dice import Dice
from Fight   import Fight


class Character(dict):

  # core races
  AVESFOLK = 100  # air
  DRACONIC = 101  # fire
  DWARF = 102  # earth
  ELF = 103  # wood
  HALFLING = 104  # small, rural
  HUMAN = 105  # neutral
  LIZARDFOLK = 106  # metal
  ORC = 107  # small, urban
  TROLL = 108  # large, solo

  WARRIOR = 1001  # con  
  BARD = 1002  # shr
  MAGE = 1003  # int
  CLERIC = 1004  # wis
  THIEF = 1005  # dex

  #def __str__(self):
  #  return f'Character(///{super().__str__()}///)'

  def restore(self):
    self["current hit points"] = self["hit points"]

  def __init__(self, _class=None, _race=HUMAN):
    d = Dice()

    #race
    self["race"] = _race  

    #core stats
    match self["race"]:
     case self.HALFLING : 
      self["strength"] = d.rollBest3of6d6(25, 10, 100)
      self["dexterity"] = d.rollBest3of6d6(30, 10, 100)
      self["wisdom"] = d.rollBest3of6d6(25, 10, 100)
      self["intelligence"] = d.rollBest3of6d6(10, 10, 100)
      self["charisma"] = d.rollBest3of6d6(25, 10, 100)
      self["constitution"] = d.rollBest3of6d6(25, 10, 100)
     case self.HUMAN : 
      self["strength"] = d.rollBest3of6d6(20, 10, 100)
      self["dexterity"] = d.rollBest3of6d6(20, 10, 100)
      self["wisdom"] = d.rollBest3of6d6(20, 10, 100)
      self["intelligence"] = d.rollBest3of6d6(20, 10, 100)
      self["charisma"] = d.rollBest3of6d6(20, 10, 100)
      self["constitution"] = d.rollBest3of6d6(20, 10, 100)
     case self.ORC : 
      self["strength"] = d.rollBest3of6d6(15, 10, 100)
      self["dexterity"] = d.rollBest3of6d6(20, 10, 100)
      self["wisdom"] = d.rollBest3of6d6(20, 10, 100)
      self["intelligence"] = d.rollBest3of6d6(30, 10, 100)
      self["charisma"] = d.rollBest3of6d6(25, 10, 100)
      self["constitution"] = d.rollBest3of6d6(10, 10, 100)
     case self.TROLL : 
      self["strength"] = d.rollBest3of6d6(30, 10, 100)
      self["dexterity"] = d.rollBest3of6d6(25, 10, 100)
      self["wisdom"] = d.rollBest3of6d6(30, 10, 100)
      self["intelligence"] = d.rollBest3of6d6(10, 10, 100)
      self["charisma"] = d.rollBest3of6d6(25, 10, 100)
      self["constitution"] = d.rollBest3of6d6(30, 10, 100)
     case _: 
      print("Error no race!\n")

    #core-derived stats
    self["hit points"] = d.rollBest3of6d6(10, 10, 100) + self["constitution"]
    self["current hit points"] = self["hit points"]

    #class
    if _class is None:
      self["class"] = self.WARRIOR
      if self["charisma"] >= 600:
        self["class"] = self.BARD
      if self["wisdom"] >= 600:
        self["class"] = self.CLERIC
      if self["dexterity"] >= 600:
        self["class"] = self.THIEF
      if self["intelligence"] >= 600:
        self["class"] = self.MAGE
    else:
      self["class"] = _class

    #self["inventory"] = {"weapon": "dagger", "pants": "civilian pants"}



# tests
e = ElementalBalance()

c0 = Character()
c1 = Character(c0.WARRIOR, c0.HUMAN)
c1["name"] = "first"
print(c1)
print()

c2 = Character()
c2["name"] = "second"
print(c2)
print()

f = Fight()
print(f.fight(c1, c2))
