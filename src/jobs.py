from functools import lru_cache
import csv  # importo a livraria CSV pq o arquivo que quero ler é do tipo CSV


@lru_cache
def read(file_path):
    with open(file_path, 'r') as csv_file:
        jobs_csv = csv.DictReader(csv_file)
        jobs = []
        for row in jobs_csv:
            jobs.append(row)
        return jobs


# a função read deve abrir um arquivo CV e retornar dados em formato de list
# de dicionários

# o with serve para nao precisarmos ficar fechando o arquivo e
# e ficarmos ocupando mta memória. Então com with o arquivo abre
# faz o que necessita e fecha.

# o csv.DictReader serve para retonar dados em formato de lista
# de dicionários

# o for lê-se: para cada linha de jobs_csv, adiciono na variável jobs
# cada linha e retorno jobs para a função.
