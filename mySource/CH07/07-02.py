class Furniture:
    def __init__(self, width = 0, height = 0, material = "Wood"):
        self.width = width
        self.height = height
        self.material = material

class Chair(Furniture):
    def __init__(self, material, width = 0, height = 0, arms = True, back = True):
        super().__init__(width, height, material)
        self.arms = arms
        self.back = back

    def fold(self):
        self.folded = True
        print("The chair is now folded and ready for transport.")

    def unfold(self):
        self.folded = False
        print("The chair is now unfolded and ready for use.")

class Bench(Chair):
    pass

sofa = Bench("Metal")
print(vars(sofa))
