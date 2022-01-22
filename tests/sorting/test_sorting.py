import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {"min_salary": 100, "max_salary": 4500, "date_posted": "2021-12-05"},
        {"min_salary": 300, "max_salary": 2800, "date_posted": "2019-01-06"},
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2020-11-11"}
    ]


sort_date_posted = [
        {"min_salary": 100, "max_salary": 4500, "date_posted": "2021-12-05"},
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2020-11-11"},
        {"min_salary": 300, "max_salary": 2800, "date_posted": "2019-01-06"}
    ]

sort_max_salary = [
        {"min_salary": 100, "max_salary": 4500, "date_posted": "2021-12-05"},
        {"min_salary": 300, "max_salary": 2800, "date_posted": "2019-01-06"},
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2020-11-11"}
    ]

sort_min_salary = [
        {"min_salary": 100, "max_salary": 4500, "date_posted": "2021-12-05"},
        {"min_salary": 300, "max_salary": 2800, "date_posted": "2019-01-06"},
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2020-11-11"}
    ]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "date_posted")
    assert jobs == sort_date_posted

    sort_by(jobs, "max_salary")
    assert jobs == sort_max_salary

    sort_by(jobs, "min_salary")
    assert jobs == sort_min_salary

    with pytest.raises(ValueError):
        sort_by(jobs, "invalid_criteria")
