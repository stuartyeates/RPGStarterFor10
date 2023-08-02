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

    char2["current hit points"] = char2["current hit points"] - 10
    char1["current hit points"] = char1["current hit points"] - 10

    return self.fight(char1, char2)
