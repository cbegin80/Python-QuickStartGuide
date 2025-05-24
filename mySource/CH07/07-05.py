class Furniture:
    def __init__(self, width, height, material):
        self.width = width
        self.height = height
        self.material = material

class Chair(Furniture):
    def __init__(self, width, height, material):
        super().__init__( width, height, material)

        def fold(self):
            self.folded = True
            print("The chair is now folded and ready for transport.")

        def unfold(self):
            self.folded = False
            print("The chair is now unfolded and ready for use.")

class Stool(Chair):
    def __init__(self, width = 0, height = 0, material = "Wood", number = 0):
        super().__init__(width, height, material)
        self.number = number

# Create and empty list named bar
bar = []

# Add 8 stools to the bar
for i in range(8):
    bar.append(Stool(number = i))

for stool in bar:
    print(vars(stool))

