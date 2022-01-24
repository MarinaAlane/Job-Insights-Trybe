import pytest
from src.sorting import sort_by

# dicionário mockado com as chaves min_salary, max_salary e date_posted.
jobs = [
    {"min_salary": 1000, "max_salary": 4000, "date_posted": "2022-01-24"},
    {"min_salary": 3000, "max_salary": 3000, "date_posted": "2022-03-24"},
    {"min_salary": 2000, "max_salary": 2000, "date_posted": "2022-02-24"},
]


def test_sort_by_criteria():
    # ordem cresente
    sort_by(jobs, "max_salary")
    assert jobs == [
        {"min_salary": 1000, "max_salary": 4000, "date_posted": "2022-01-24"},
        {"min_salary": 3000, "max_salary": 3000, "date_posted": "2022-03-24"},
        {"min_salary": 2000, "max_salary": 2000, "date_posted": "2022-02-24"},
    ]

    # ordem cresente
    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": 1000, "max_salary": 4000, "date_posted": "2022-01-24"},
        {"min_salary": 2000, "max_salary": 2000, "date_posted": "2022-02-24"},
        {"min_salary": 3000, "max_salary": 3000, "date_posted": "2022-03-24"},
    ]

    # ordem descresente
    sort_by(jobs, "date_posted")
    assert jobs == [
        {"min_salary": 3000, "max_salary": 3000, "date_posted": "2022-03-24"},
        {"min_salary": 2000, "max_salary": 2000, "date_posted": "2022-02-24"},
        {"min_salary": 1000, "max_salary": 4000, "date_posted": "2022-01-24"},
    ]

    # Se passar como parametro uma chave que não existe no dicionário...
    # ...ele lança um ValueError.
    with pytest.raises(ValueError):
        sort_by(jobs, "something")
