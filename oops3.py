class Father:
    def gardening(self):
        print("Gardening")

class Mother:
    def cooking(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.gardening()
c.cooking()