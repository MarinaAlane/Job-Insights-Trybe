import pytest
from src.sorting import sort_by


criteria_message = "invalid sorting criteria: invalid_criteria"
result_by_max_salary = [
    {"date_posted": "2021-01-30", "min_salary": 3000, "max_salary": 4000},
    {"date_posted": "2021-01-29", "min_salary": 2000, "max_salary": 3000},
    {"date_posted": "2021-01-28", "min_salary": 1000, "max_salary": 2000},
    {"date_posted": "2021-01-27", "min_salary": 0, "max_salary": 1000},
]
result_by_min_salary = [
    {"date_posted": "2021-01-27", "min_salary": 0, "max_salary": 1000},
    {"date_posted": "2021-01-28", "min_salary": 1000, "max_salary": 2000},
    {"date_posted": "2021-01-29", "min_salary": 2000, "max_salary": 3000},
    {"date_posted": "2021-01-30", "min_salary": 3000, "max_salary": 4000},
]
result_by_date = [
    {"date_posted": "2021-01-30", "min_salary": 3000, "max_salary": 4000},
    {"date_posted": "2021-01-29", "min_salary": 2000, "max_salary": 3000},
    {"date_posted": "2021-01-28", "min_salary": 1000, "max_salary": 2000},
    {"date_posted": "2021-01-27", "min_salary": 0, "max_salary": 1000},
]


@pytest.fixture
def jobs():
    return [
        {"date_posted": "2021-01-27", "min_salary": 0, "max_salary": 1000},
        {"date_posted": "2021-01-28", "min_salary": 1000, "max_salary": 2000},
        {"date_posted": "2021-01-29", "min_salary": 2000, "max_salary": 3000},
        {"date_posted": "2021-01-30", "min_salary": 3000, "max_salary": 4000},
    ]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "max_salary")
    assert jobs == result_by_max_salary
    sort_by(jobs, "min_salary")
    assert jobs == result_by_min_salary
    sort_by(jobs, "date_posted")
    assert jobs == result_by_date
    with pytest.raises(ValueError, match=criteria_message):
        sort_by(jobs, "invalid_criteria")
