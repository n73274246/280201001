books = ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
bookdict = {}
for name in books:
  lenght = len(name)
  unique = len(list(set(name)))
  average = (lenght + unique) / 2
  comb = (lenght, unique, average)
  bookdict[name] = comb
print(bookdict)