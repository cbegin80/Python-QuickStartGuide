for empties in range(99):
    bottles = 99 - empties
    print("*" * 20)
    print(f"{bottles} bottles of beer on the wall")
    print(f"{bottles} bottles of beer!")
    print("Take one down, pass it around:")
    print(f"Now there's {bottles - 1} bottles of beer on the wall!")
    print("*" * 20)