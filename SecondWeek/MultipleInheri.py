class Fly:
  def fly(self):
    return "I can fly"


class Swim:
  def swim(self):
    return "i can swim"


class Swan(Fly,Swim):
  pass

swan=Swan()
print(swan.fly()
)
print(swan.swim())
