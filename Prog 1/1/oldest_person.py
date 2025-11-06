names = []
ages = []
names.append(input("Name 1\n"))
ages.append(int(input("Birthyear 1\n")))
names.append(input("Name 2\n"))
ages.append(int(input("Birthyear 2\n")))
names.append(input("Name 3\n"))
ages.append(int(input("Birthyear 3\n")))
oldest = min(ages)
oldest_index = ages.index(oldest)
print(names[oldest_index])
