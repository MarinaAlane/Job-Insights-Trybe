import pytest
from src.sorting import sort_by

jobs = [
    {"min_salary": 1000, "max_salary": 4000, "date_posted": "2022-01-24"},
    {"min_salary": 3000, "max_salary": 3000, "date_posted": "2022-03-24"},
    {"min_salary": 2000, "max_salary": 2000, "date_posted": "2022-02-24"},
]  # Mock dos Dados para os testes


def test_sort_by_criteria():

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"min_salary": 1000, "max_salary": 4000, "date_posted": "2022-01-24"},
        {"min_salary": 3000, "max_salary": 3000, "date_posted": "2022-03-24"},
        {"min_salary": 2000, "max_salary": 2000, "date_posted": "2022-02-24"},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": 1000, "max_salary": 4000, "date_posted": "2022-01-24"},
        {"min_salary": 2000, "max_salary": 2000, "date_posted": "2022-02-24"},
        {"min_salary": 3000, "max_salary": 3000, "date_posted": "2022-03-24"},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"min_salary": 3000, "max_salary": 3000, "date_posted": "2022-03-24"},
        {"min_salary": 2000, "max_salary": 2000, "date_posted": "2022-02-24"},
        {"min_salary": 1000, "max_salary": 4000, "date_posted": "2022-01-24"},
    ]

    with pytest.raises(ValueError):
        sort_by(jobs, "something")  # pega erros
