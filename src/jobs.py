import csv

path = str(input("FILE NAME"))

with open(path, encoding="utf8") as file:
    info = csv.reader(file, delimiter=",", quotechar='"')
    header, *data = info

print(header)
file.close()