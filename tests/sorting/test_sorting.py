from src.sorting import sort_by
import pytest

jobs_max_salary = [
    {
        "max_salary": 200000,
        "min_salary": 150000,
        "date_posted": "2020-03-01",
    },
    {
        "max_salary": 150000,
        "min_salary": 100000,
        "date_posted": "2020-02-01",
    },
    {
        "max_salary": 100000,
        "min_salary": 50000,
        "date_posted": "2019-01-01",
    },
]


jobs_min_salary = [
    {
        "max_salary": 100000,
        "min_salary": 50000,
        "date_posted": "2019-01-01",
    },
    {
        "max_salary": 150000,
        "min_salary": 100000,
        "date_posted": "2020-02-01",
    },
    {
        "max_salary": 200000,
        "min_salary": 150000,
        "date_posted": "2020-03-01",
    },
]


@pytest.fixture
def jobs():

    return [
        {
            "max_salary": 100000,
            "min_salary": 50000,
            "date_posted": "2019-01-01",
        },
        {
            "max_salary": 150000,
            "min_salary": 100000,
            "date_posted": "2020-02-01",
        },
        {
            "max_salary": 200000,
            "min_salary": 150000,
            "date_posted": "2020-03-01",
        },
    ]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "max_salary")
    assert jobs == jobs_max_salary
    sort_by(jobs, "min_salary")
    assert jobs == jobs_min_salary
    sort_by(jobs, "date_posted")
    assert jobs == jobs
    with pytest.raises(ValueError):
        sort_by(jobs, "unknown_criteria")
