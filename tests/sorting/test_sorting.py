from src.sorting import sort_by
from mocks import (
  sort_date,
  sort_max_salary,
  sort_min_salary,
)

jobs = [
    {"min_salary": 10, "max_salary": 1000, "date_posted": "2021-01-24"},
    {"min_salary": 1000, "max_salary": 10000, "date_posted": "2020-03-02"},
    {"min_salary": 100, "max_salary": 200, "date_posted": "2019-04-14"},
    {"min_salary": -50, "max_salary": 25, "date_posted": "2019-03-14"},
    {"min_salary": '', "max_salary": '', "date_posted": ''},
]


def test_sort_by_criteria():
    sort_by(jobs, 'date_posted')
    assert jobs == sort_date

    sort_by(jobs, 'max_salary')
    assert jobs == sort_max_salary

    sort_by(jobs, 'min_salary')
    assert jobs == sort_min_salary
