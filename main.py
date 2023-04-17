from ElementalBalance import ElementalBalance
from Dice import Dice


class Fight():

  def fight(self, char1, char2):
    if char1["current hit points"] <= 0:
      if char2["current hit points"] <= 0:
        r = random.randrange(2)
        if r == 0:
          print("drawn fight, going with " + char1["name"])
          return char1
        else:
          print("drawn fight, going with " + char2["name"])
          return char2
      return char2
    if char2["current hit points"] <= 0:
      return char1

    char2["current hit points"] = char2["current hit points"] - len(
      char1["inventory"]["weapon"])
    char1["current hit points"] = char1["current hit points"] - len(
      char2["inventory"]["weapon"])

    return self.fight(char1, char2)


class Character(dict):

  #def __str__(self):
  #  return f'Character(///{super().__str__()}///)'

  def restore(self):
    self["current hit points"] = self["hit points"]

  def __init__(self, _class=None):
    d = Dice()

    self["race"] = "human"

    self["strength"] = d.rollBest3of6d6(10, 10, 100)
    self["dexterity"] = d.rollBest3of6d6(10, 10, 100)
    self["wisdom"] = d.rollBest3of6d6(10, 10, 100)
    self["intelligence"] = d.rollBest3of6d6(10, 10, 100)
    self["charisma"] = d.rollBest3of6d6(10, 10, 100)
    self["constitution"] = d.rollBest3of6d6(10, 10, 100)

    self["inventory"] = {"weapon": "dagger", "pants": "civilian pants"}

    if _class is None:
      self["class"] = "warrior"
      if self["charisma"] >= 600:
        self["class"] = "bard"
        self["inventory"]["weapon"] = "dagger"
      if self["wisdom"] >= 600:
        self["class"] = "cleric"
        self["inventory"]["weapon"] = "mace"
      if self["dexterity"] >= 600:
        self["class"] = "thief"
        self["inventory"]["weapon"] = "dagger"
      if self["intelligence"] >= 600:
        self["class"] = "mage"
        self["inventory"]["weapon"] = "staff"
      if self["class"] == "warrior":
        self["inventory"]["weapon"] = "two handed sword"

    self["hit points"] = d.rollBest3of6d6(10, 10, 100) + self["constitution"]
    self["current hit points"] = self["hit points"]


# tests
e = ElementalBalance()

c1 = Character()
c1["name"] = "first"
print(c1)
print()

c2 = Character()
c2["name"] = "second"
print(c2)
print()

f = Fight()
print(f.fight(c1, c2))
