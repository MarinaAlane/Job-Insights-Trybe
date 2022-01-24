from nis import match
from src.sorting import sort_by

import pytest

values = [
    {"date_posted": "2020-01-01", "max_salary": 10000, "min_salary": 200},
    {"date_posted": "2021-01-01", "max_salary": 1500, "min_salary": 0},
]

min_salary = [
    {"date_posted": "2021-01-01", "max_salary": 1500, "min_salary": 0},
    {"date_posted": "2020-01-01", "max_salary": 10000, "min_salary": 200},
]

date_posted = [
    {"date_posted": "2021-01-01", "max_salary": 1500, "min_salary": 0},
    {"date_posted": "2020-01-01", "max_salary": 10000, "min_salary": 200},
]


def test_sort_by_criteria():
    data = values.copy()
    with pytest.raises(
        TypeError, match="takes 2 positional arguments but 3 were given"
    ):
        sort_by(data, "teste", "teste2")

    data = values.copy()
    sort_by(data, "max_salary")
    assert data == [
        {"date_posted": "2020-01-01", "max_salary": 10000, "min_salary": 200},
        {"date_posted": "2021-01-01", "max_salary": 1500, "min_salary": 0},
    ]

    data = values.copy()
    sort_by(data, "min_salary")
    assert data == min_salary

    data = values.copy()
    sort_by(data, "date_posted")
    assert data == date_posted
