books = ["ULYSSES", "ANIMAL FARM", "BRAVE NEW WORLD", "ENDER'S GAME"]
bookdict = {}
for name in books:
  lenght = len(name)
  unique = len(list(set(name)))
  comb = (lenght, unique)
  bookdict[name] = comb
print(bookdict)
