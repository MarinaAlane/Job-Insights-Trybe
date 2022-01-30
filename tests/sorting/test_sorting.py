from src.sorting import sort_by
import pytest

# Amandha W. Barok
# - https://github.com/tryber/sd-011-project-job-insights/pull/106/commits/528696db686e61bd17a390a2cc58cae744ddf2bc

# mock
job = [
     {"min_salary": 20, "max_salary": 40, "date_posted": "2022-03-01"},
     {"min_salary": 10, "max_salary": 60, "date_posted": "2022-01-01"},
     {"min_salary": 30, "max_salary": 50, "date_posted": "2022-02-01"},
]
# listas com a ordenação correta para usar como base
min_salary = [
     {"min_salary": 10, "max_salary": 60, "date_posted": "2022-01-01"},
     {"min_salary": 20, "max_salary": 40, "date_posted": "2022-03-01"},
     {"min_salary": 30, "max_salary": 50, "date_posted": "2022-02-01"},
]

max_salary = [
     {"min_salary": 10, "max_salary": 60, "date_posted": "2022-01-01"},
     {"min_salary": 30, "max_salary": 50, "date_posted": "2022-02-01"},
     {"min_salary": 20, "max_salary": 40, "date_posted": "2022-03-01"},
]

date_posted = [
     {"min_salary": 20, "max_salary": 40, "date_posted": "2022-03-01"},
     {"min_salary": 30, "max_salary": 50, "date_posted": "2022-02-01"},
     {"min_salary": 10, "max_salary": 60, "date_posted": "2022-01-01"},
]


def test_sort_by_criteria():
    # verifica que se é ordenado corretamente por criterio
    sort_by(job, "min_salary")
    assert job == min_salary
    sort_by(job, "max_salary")
    assert job == max_salary
    sort_by(job, "date_posted")
    assert job == date_posted
    # verifica se falha quando um valor invalido é passado
    # como parametro para criteria
    with pytest.raises(ValueError):
        sort_by(job, "None")
    pass
