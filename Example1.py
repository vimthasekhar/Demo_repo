class Sample:

  def add(self, a,b):
    print(a+b)

  def sub(self, a,b):
    print(a-b)

  @staticmethod
  def mul(a,b):
    print(a*b)

  @staticmethod
  def div(a,b):
    print(a/b)

if __name__=="__main__":
  s = Sample()
  s.add(10,25)
  s.sub(15,7)
  Sample.mul(10,20)
  Sample.div(100,25)
