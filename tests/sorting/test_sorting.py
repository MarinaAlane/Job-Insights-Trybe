import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {"max_salary": 1000, "min_salary": 500, "date_posted": "1992-08-10"},
        {"max_salary": 1500, "min_salary": 300, "date_posted": "1992-09-10"},
        {"max_salary": 900, "min_salary": 50, "date_posted": "1992-01-10"},
    ]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "max_salary")
    assert [
        {"max_salary": 1500, "min_salary": 300, "date_posted": "1992-09-10"},
        {"max_salary": 1000, "min_salary": 500, "date_posted": "1992-08-10"},
        {"max_salary": 900, "min_salary": 50, "date_posted": "1992-01-10"},
    ] == jobs
