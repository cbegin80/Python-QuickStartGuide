def passBeer(startingBeers = 99):
    beersOnWall = startingBeers
    while beersOnWall > 0:
        verse = []
        verse.append("\n" + ("*" * 20) + "\n")
        verse.append(f"{beersOnWall} bottles of beer on the wall\n")
        verse.append(f"{beersOnWall} bottles of beer!\n")
        verse.append("Take one down, pass it around:\n")
        beersOnWall -= 1
        verse.append(f"Now there's {beersOnWall} bottles of beer on the wall!\n")
        verse.append(("*" * 20) + "\n")
        yield "".join(verse)
    return True

stock = int(input("How many bottles of beer do you want to start with? "))

song = []
print("Preparing song...\n")

for verse in passBeer(stock):
    song.append(verse)

print("".join(song))