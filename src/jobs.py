from functools import lru_cache
import csv


@lru_cache
def read(path):

    with open(path) as file:
        list_of_jobs = []
        jobs = csv.reader(file)

        # separa o cabeçalho do restante dos dados.
        header, *data = jobs

        # a cada nova linha vai ser criado um novo dicionário
        # que vai ser modificado a cada novo header e nova linha
        # e essa modificação vai ser incluída no dicionário antes vazio
        for row in data:
            jobs = dict()
            for index in range(len(header)):
                jobs[header[index]] = row[index]

            list_of_jobs.append(jobs)

    return list_of_jobs
