import pytest
from src.sorting import sort_by

mock = [
    {"min_salary": 2500, "max_salary": 10000, "date_posted": "2021-03-04"},
    {"min_salary": 1000, "max_salary": 20000, "date_posted": "2022-01-01"},
    {"min_salary": 3100, "max_salary": 30000, "date_posted": "2020-02-01"},
]


min_salary_expect = [
    {"min_salary": 1000, "max_salary": 20000, "date_posted": "2022-01-01"},
    {"min_salary": 2500, "max_salary": 10000, "date_posted": "2021-03-04"},
    {"min_salary": 3100, "max_salary": 30000, "date_posted": "2020-02-01"},
]

max_salary_expect = [
    {"min_salary": 3100, "max_salary": 30000, "date_posted": "2020-02-01"},
    {"min_salary": 1000, "max_salary": 20000, "date_posted": "2022-01-01"},
    {"min_salary": 2500, "max_salary": 10000, "date_posted": "2021-03-04"},
]

date_posted_expect = [
    {"min_salary": 1000, "max_salary": 20000, "date_posted": "2022-01-01"},
    {"min_salary": 2500, "max_salary": 10000, "date_posted": "2021-03-04"},
    {"min_salary": 3100, "max_salary": 30000, "date_posted": "2020-02-01"},
]

# Codigo referencia: https://github.com/tryber/sd-011-project-job-insights
# /blob/guidpo0-job-insights/tests/sorting/test_sorting.py


def test_sort_by_criteria():
    sort_by(mock, "min_salary")
    assert mock == min_salary_expect

    sort_by(mock, "max_salary")
    assert mock == max_salary_expect

    sort_by(mock, "date_posted")
    assert mock == date_posted_expect
