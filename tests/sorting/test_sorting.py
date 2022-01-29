from src.sorting import sort_by
import pytest

jobs = [
    {"date_posted": "2002-08-22", "max_salary": 3000, "min_salary": 5000},
    {"date_posted": "2003-09-23", "max_salary": 2000, "min_salary": 4000},
    {"date_posted": "2005-08-22", "max_salary": 1000, "min_salary": 2000},
]

max_salary = [
    {"date_posted": "2002-08-22", "max_salary": 3000, "min_salary": 5000},
    {"date_posted": "2003-09-23", "max_salary": 2000, "min_salary": 4000},
    {"date_posted": "2005-08-22", "max_salary": 1000, "min_salary": 2000},
]

min_salary = [
    {"date_posted": "2005-08-22", "max_salary": 1000, "min_salary": 2000},
    {"date_posted": "2003-09-23", "max_salary": 2000, "min_salary": 4000},
    {"date_posted": "2002-08-22", "max_salary": 3000, "min_salary": 5000},
]

date_posted = [
    {"date_posted": "2005-08-22", "max_salary": 1000, "min_salary": 2000},
    {"date_posted": "2003-09-23", "max_salary": 2000, "min_salary": 4000},
    {"date_posted": "2002-08-22", "max_salary": 3000, "min_salary": 5000},
]


def test_sort_by_criteria():
    sort_by(jobs, "max_salary")
    assert jobs == max_salary

    sort_by(jobs, "min_salary")
    assert jobs == min_salary

    sort_by(jobs, "date_posted")
    assert jobs == date_posted

    with pytest.raises(ValueError, match="invalid sorting criteria: date"):
        sort_by(jobs, "date")
