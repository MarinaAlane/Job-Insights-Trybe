import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {"min_salary": 10, "max_salary": 100, "date_posted": "2020-05-08"},
        {"min_salary": 1, "max_salary": 60, "date_posted": "2020-09-18"},
        {"min_salary": 32, "max_salary": -1, "date_posted": "2020-05-04"},
    ]


def test_sort_by_criteria(jobs):
    assert sort_by(jobs, "min_salary") is None
