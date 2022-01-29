import pytest
from src.sorting import sort_by


@pytest.fixture  # ajuda a pensar pré condições
def jobs():
    return [
        {"min_salary": 100, "max_salary": 5000, "date_posted": "2020-01-01"},
        {"min_salary": 5000, "max_salary": 20000, "date_posted": "2021-01-01"},
        {"min_salary": 9000, "max_salary": 40000, "date_posted": "2022-01-01"},
    ]


sort_by_min_salary = [
    {"min_salary": 100, "max_salary": 5000, "date_posted": "2020-01-01"},
    {"min_salary": 5000, "max_salary": 20000, "date_posted": "2021-01-01"},
    {"min_salary": 9000, "max_salary": 40000, "date_posted": "2022-01-01"},
]
sort_by_max_salary = [
    {"min_salary": 9000, "max_salary": 40000, "date_posted": "2022-01-01"},
    {"min_salary": 5000, "max_salary": 20000, "date_posted": "2021-01-01"},
    {"min_salary": 100, "max_salary": 5000, "date_posted": "2020-01-01"},

]
sort_by_date_posted = [
    {"min_salary": 9000, "max_salary": 40000, "date_posted": "2022-01-01"},
    {"min_salary": 5000, "max_salary": 20000, "date_posted": "2021-01-01"},
    {"min_salary": 100, "max_salary": 5000, "date_posted": "2020-01-01"},
]


def test_sort_by_criteria(jobs):  # passa fixture
    # arrange/act
    sort_by(jobs, "min_salary")
    # assert - expectativa de retorno
    assert jobs == sort_by_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == sort_by_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == sort_by_date_posted
