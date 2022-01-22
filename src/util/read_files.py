import csv


def read_file_csv(path):
    with open(path, "r", encoding="iso-8859-1") as arquivo:
        read_file = csv.DictReader(arquivo)
        result = list(read_file)
    return result
