import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {
            "min_salary": 3000,
            "max_salary": 4000,
            "date_posted": "2022-01-28",
        },
        {
            "min_salary": 2000,
            "max_salary": 3000,
            "date_posted": "2022-01-28",
        },
        {
            "min_salary": 1000,
            "max_salary": 1500,
            "date_posted": "2022-01-28",
        },
        {
            "min_salary": 500,
            "max_salary": 1000,
            "date_posted": "2022-01-28",
        },
    ]


def test_sort_by_criteria(jobs):

    sort_by(jobs, "min_salary")
    min_salary = []
    for job in jobs:
        min_salary.append(job["min_salary"])
    assert min_salary == [500, 800, 1000, 2000]
