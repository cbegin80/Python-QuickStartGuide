# 99 Bottles of Beer
bottles = 99
while bottles > 0:
    print("*" * 20)
    print(f"{bottles} bottles of beer on the wall")
    print(f"{bottles} bottles of beer!")
    print("Take one down, pass it around:")
    bottles -= 1
    print(f"Now there's {bottles} bottles of beer on the wall!")
    print("*" * 20)