from functools import lru_cache
import csv

# Requisito 1
# Com o DictReader não precisa manipular os índices...
# ...para acessar os dados das colunas.
# Uso o list() para transformar o conteudo em uma lista.


@lru_cache
def read(path):
    with open(path) as file:
        get_jobs = csv.DictReader(file, delimiter=",", quotechar='"')
        content = list(get_jobs)
    return content
