class ElementalBalance(dict):

  def __init__(self, _class=None):
    d = Dice()
    self["wood_base"] = d.rollBest3of6d6(4, 4, 250)
    self["fire_base"] = d.rollBest3of6d6(4, 4, 250)
    self["earth_base"] = d.rollBest3of6d6(4, 4, 250)
    self["metal_base"] = d.rollBest3of6d6(4, 4, 250)
    self["water_base"] = d.rollBest3of6d6(4, 4, 250)
    self.balance()

  def balance(self):
    # tweak the best stat by raising it half way to 1000
    # steal that much off the other four stats to make up for it.
    best = sorted(self.items(), key=lambda x: x[1], reverse=True)[0][0]
    self["best"] = best
    boost = int((1000 - self[best]) / 2)
    if best == "wood_base":
      self["wood"] = self["wood_base"] + boost
    else:
      self["wood"] = self["wood_base"] - int(boost / 4)

    if best == "fire_base":
      self["fire"] = self["fire_base"] + boost
    else:
      self["fire"] = self["fire_base"] - int(boost / 4)

    if best == "earth_base":
      self["earth"] = self["earth_base"] + boost
    else:
      self["earth"] = self["earth_base"] - int(boost / 4)

    if best == "metal_base":
      self["metal"] = self["metal_base"] + boost
    else:
      self["metal"] = self["metal_base"] - int(boost / 4)

    if best == "water_base":
      self["water"] = self["water_base"] + boost
    else:
      self["water"] = self["water_base"] - int(boost / 4)

    #print ourselves
    print(self)
    print()

  def __str__(self):
    return f'ElementalBalance(///{super().__str__()}///)'
