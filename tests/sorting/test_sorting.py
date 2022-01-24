import pytest
from src.sorting import sort_by


MIN_SALARY_INFO = [
    {"date_posted": "2020-01-20", "max_salary": 100000, "min_salary": 52000},
    {"date_posted": "2020-01-19", "max_salary": 100095, "min_salary": 57000},
    {"date_posted": "2020-01-15", "max_salary": 100230, "min_salary": 58000},
    {"date_posted": "2020-01-01", "max_salary": 102038, "min_salary": 70000},
]

MAX_SALARY_INFO = [
    {"date_posted": "2020-01-01", "max_salary": 102038, "min_salary": 70000},
    {"date_posted": "2020-01-15", "max_salary": 100230, "min_salary": 58000},
    {"date_posted": "2020-01-19", "max_salary": 100095, "min_salary": 57000},
    {"date_posted": "2020-01-20", "max_salary": 100000, "min_salary": 52000},
]

DATE_POSTED_INFO = [
    {"date_posted": "2020-01-20", "max_salary": 100000, "min_salary": 52000},
    {"date_posted": "2020-01-19", "max_salary": 100095, "min_salary": 57000},
    {"date_posted": "2020-01-15", "max_salary": 100230, "min_salary": 58000},
    {"date_posted": "2020-01-01", "max_salary": 102038, "min_salary": 70000},
]


@pytest.fixture()
def jobs():
    return [
        {
            "date_posted": "2020-01-20",
            "max_salary": 100000,
            "min_salary": 52000,
        },
        {
            "date_posted": "2020-01-19",
            "max_salary": 100095,
            "min_salary": 57000,
        },
        {
            "date_posted": "2020-01-15",
            "max_salary": 100230,
            "min_salary": 58000,
        },
        {
            "date_posted": "2020-01-01",
            "max_salary": 102038,
            "min_salary": 70000,
        },
    ]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "min_salary")
    assert jobs == MIN_SALARY_INFO

    sort_by(jobs, "max_salary")
    assert jobs == MAX_SALARY_INFO

    sort_by(jobs, "date_posted")
    assert jobs == DATE_POSTED_INFO

    with pytest.raises(ValueError):
        sort_by(jobs, "criteria_criteria")
