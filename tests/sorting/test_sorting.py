from src.sorting import sort_by
import pytest


mock = [
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2020-01-01"},
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2021-01-01"},
    {"min_salary": 3000, "max_salary": 5000, "date_posted": "2022-01-01"},
]

expect_min_salary = [
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2020-01-01"},
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2021-01-01"},
    {"min_salary": 3000, "max_salary": 5000, "date_posted": "2022-01-01"},
]

expect_max_salary = [
    {"min_salary": 3000, "max_salary": 5000, "date_posted": "2022-01-01"},
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2021-01-01"},
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2020-01-01"},
]

expect_date_posted = [
    {"min_salary": 3000, "max_salary": 5000, "date_posted": "2022-01-01"},
    {"min_salary": 2000, "max_salary": 4000, "date_posted": "2021-01-01"},
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2020-01-01"},
]


def test_sort_by_criteria():
    sort_by(mock, "min_salary")
    assert mock == expect_min_salary

    sort_by(mock, "max_salary")
    assert mock == expect_max_salary

    sort_by(mock, "date_posted")
    assert mock == expect_date_posted

    with pytest.raises(ValueError):
        sort_by(mock, "inválido")
