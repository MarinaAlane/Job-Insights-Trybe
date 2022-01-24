from src.sorting import sort_by
import pytest

jobs = [
    {"min_salary": 2500, "max_salary": 5000, "date_posted": "2021-12-07"},
    {"min_salary": 2000, "max_salary": 5500, "date_posted": "2021-12-06"},
    {"min_salary": 3000, "max_salary": 6000, "date_posted": "2021-12-08"},
]
jobs_sorted_by_min_salary = [
    jobs[1],
    jobs[0],
    jobs[2],
]
jobs_sorted_by_max_salary = [
    jobs[2],
    jobs[1],
    jobs[0],
]
jobs_sorted_by_date_posted = [
    jobs[2],
    jobs[0],
    jobs[1],
]

criteria = [
    "min_salary",
    "max_salary",
    "date_posted",
]


def test_sort_by_criteria():
    sort_by(jobs, criteria[0])
    assert jobs == jobs_sorted_by_min_salary
    sort_by(jobs, criteria[1])
    assert jobs == jobs_sorted_by_max_salary
    sort_by(jobs, criteria[2])
    assert jobs == jobs_sorted_by_date_posted

    with pytest.raises(ValueError, match="invalid sorting criteria: no"):
        sort_by(jobs, "no")
