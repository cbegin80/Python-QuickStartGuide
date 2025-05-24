import distance

dist = distance.Distance(3)
print(f"3 kilometers is {dist.miles} miles.")
dist.miles = 3
print(f"3 miles is {dist.km} kilometers.")