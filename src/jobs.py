from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, "r") as file:
        jobs_reader = csv.DictReader(file, delimiter=",", quotechar='"')

        result = []  # objeto não tem atributo append
        for row in jobs_reader:
            result.append(row)
    return result


if __name__ == "__main__":  # identifica o arquivo que est sendo executado
    print(read("src/jobs.csv"))

# DictReader - leitor (pode ser escritor) baseado em dicionários.
# não é preciso manipular os índices para acessar os dados das colunas.
# https://docs.python.org/pt-br/3.6/library/csv.html
