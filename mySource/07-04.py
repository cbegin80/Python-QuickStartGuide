class Furniture:
    def __init__(self, width, height, material):
        self.width = width
        self.height = height
        self.material = material

class Surface:
    def __init__(self, flat):
        self.flat = flat

class Table(Furniture, Surface):
    def __init__(self, width = 0, height = 0, material = "Wood", flat = True):
        Furniture.__init__(self, width, height, material)
        Surface.__init__(self, flat)
        self.legs = 4

# Two quiet, unassuming, regular tables. Nothing fancy here.
# We create them with no parameters and they receive defaults.
a = Table()
b = Table()

# And then there's a weird table named Fred. Poor Fred.
# He's not like the other tables a and b, he's not flat!
fred = Table(flat = False)

print(vars(a))
print(vars(b))
print(vars(fred))