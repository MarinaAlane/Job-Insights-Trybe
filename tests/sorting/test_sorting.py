from src.sorting import sort_by
import pytest

data = [
    {"max_salary": 1000, "min_salary": 300, "date_posted": "2022-02-21"},
    {"max_salary": 900, "min_salary": 800, "date_posted": "2022-02-22"},
    {"max_salary": 1500, "min_salary": 1000, "date_posted": "2022-02-23"},
]

max_salary = [
    {"max_salary": 1500, "min_salary": 1000, "date_posted": "2022-02-23"},
    {"max_salary": 1000, "min_salary": 300, "date_posted": "2022-02-21"},
    {"max_salary": 900, "min_salary": 800, "date_posted": "2022-02-22"},
]

min_salary = [
    {"max_salary": 1500, "min_salary": 1000, "date_posted": "2022-02-23"},
    {"max_salary": 900, "min_salary": 800, "date_posted": "2022-02-22"},
    {"max_salary": 1000, "min_salary": 300, "date_posted": "2022-02-21"},
]

date_posted = [
    {"max_salary": 1500, "min_salary": 1000, "date_posted": "2022-02-23"},
    {"max_salary": 900, "min_salary": 800, "date_posted": "2022-02-22"},
    {"max_salary": 1000, "min_salary": 300, "date_posted": "2022-02-21"},
]


def test_sort_by_criteria():

    sort_by(data, "max_salary")
    assert data == max_salary

    sort_by(data, "min_salary")
    assert data == min_salary

    sort_by(data, "date_posted")
    assert data == date_posted

    invalid_criteria = [None, "wrong_criteria"]

    for invalid in invalid_criteria:
        with pytest.raises(ValueError):
            sort_by(data, invalid)
