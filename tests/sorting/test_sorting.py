from src.sorting import sort_by
import pytest


@pytest.fixture
def jobs():
    return [
        {
            "date_posted": "2022-03-24",
            "max_salary": 30000,
            "min_salary": 10000,
        },
        {
            "date_posted": "2020-10-28",
            "max_salary": 75000,
            "min_salary": 48000,
        },
        {
            "date_posted": "2019-03-25",
            "max_salary": 70000,
            "min_salary": 45000,
        },
        {
            "date_posted": "2018-05-07",
            "max_salary": 80000,
            "min_salary": 30000,
        },
    ]


sorted_by_date_posted = [
    {"date_posted": "2022-03-24", "max_salary": 30000, "min_salary": 10000},
    {"date_posted": "2020-10-28", "max_salary": 75000, "min_salary": 48000},
    {"date_posted": "2019-03-25", "max_salary": 70000, "min_salary": 45000},
    {"date_posted": "2018-05-07", "max_salary": 80000, "min_salary": 30000},
]

sorted_by_min_salary = [
    {"date_posted": "2022-03-24", "max_salary": 30000, "min_salary": 10000},
    {"date_posted": "2018-05-07", "max_salary": 80000, "min_salary": 30000},
    {"date_posted": "2019-03-25", "max_salary": 70000, "min_salary": 45000},
    {"date_posted": "2020-10-28", "max_salary": 75000, "min_salary": 48000},
]

sorted_by_max_salary = [
    {"date_posted": "2018-05-07", "max_salary": 80000, "min_salary": 30000},
    {"date_posted": "2020-10-28", "max_salary": 75000, "min_salary": 48000},
    {"date_posted": "2019-03-25", "max_salary": 70000, "min_salary": 45000},
    {"date_posted": "2022-03-24", "max_salary": 30000, "min_salary": 10000},
]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "min_salary")
    assert jobs == sorted_by_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == sorted_by_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == sorted_by_date_posted

    with pytest.raises(ValueError):
        sort_by(jobs, "criteria_criteria")
