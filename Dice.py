import random


class Dice:

  def rolldice(self, n=6):
    return random.randrange(n) + 1

  def rollBest3of6d6(self, rollcount=10, rollpick=10, dicetype=100):
    rolls = []

    for x in range(0, rollcount):
      rolls.append(self.rolldice(dicetype))

    rolls.sort()
    _sum = sum(rolls[-rollpick:])
    return _sum
