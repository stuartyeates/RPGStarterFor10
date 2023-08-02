def test_0(self):
  # Enter code here

  d = Dice()
  r = d.rollBest3of6d6(1, 1, 1)
  assert r > 0
  assert r < 2
  assert int(r)

  r = d.rolldice(1)
  assert r > 0
  assert r < 2
  assert int(r)


def test_1(self):
  # Enter code here

  c1 = Character()
  assert c1 != 0

  c1["name"] = "stuart"
  assert c1["name"] == "stuart"

  c2 = Character()
  c2["name"] = "yeates"
  assert c1 != c2


def test_2(self):
  # Enter code here
  d = Dice()
  r = d.rollBest3of6d6(1, 1, 6)
  assert r > 0
  assert r < 7
  assert int(r)

  r = d.rolldice(6)
  assert r > 0
  assert r < 7
  assert int(r)


def test_all(self):

  test_0()
  test_1()
  test_2()
  test_0()
