import pytest

from src.sorting import sort_by


jobs = [
    {"min_salary": 1500, "max_salary": 3000, "date_posted": "2021-02-01"},
    {"min_salary": 3680, "max_salary": 5000, "date_posted": "2022-01-01"},
    {"min_salary": 2740, "max_salary": 4000, "date_posted": "2019-03-03"},
]


def test_sort_by_criteria():
    with pytest.raises(TypeError):
        sort_by(jobs, "invalid", "invalid2")

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"min_salary": 3680, "max_salary": 5000, "date_posted": "2022-01-01"},
        {"min_salary": 2740, "max_salary": 4000, "date_posted": "2019-03-03"},
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2021-02-01"},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2021-02-01"},
        {"min_salary": 2740, "max_salary": 4000, "date_posted": "2019-03-03"},
        {"min_salary": 3680, "max_salary": 5000, "date_posted": "2022-01-01"},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"min_salary": 3680, "max_salary": 5000, "date_posted": "2022-01-01"},
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2021-02-01"},
        {"min_salary": 2740, "max_salary": 4000, "date_posted": "2019-03-03"},
    ]
