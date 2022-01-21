import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {
            "max_salary": 100001,
            "min_salary": 50000,
            "title": "Software Engineer",
            "date_posted": "2020-01-01"
        },
        {
            "max_salary": 100000,
            "min_salary": 40099,
            "title": "Software Engineer",
            "date_posted": "2021-01-01"
        },
        {
            "max_salary": 100003,
            "min_salary": 40098,
            "title": "Software Engineer",
            "date_posted": "2022-01-01"
        }
    ]


ordered_max_salary = [
    {
        "max_salary": 100003,
        "min_salary": 40098,
        "title": "Software Engineer",
        "date_posted": "2022-01-01"
    },
    {
        "max_salary": 100001,
        "min_salary": 50000,
        "title": "Software Engineer",
        "date_posted": "2020-01-01"
    },
    {
        "max_salary": 100000,
        "min_salary": 40099,
        "title": "Software Engineer",
        "date_posted": "2021-01-01"
    }
]

ordered_min_salary = [
    {
        "max_salary": 100003,
        "min_salary": 40098,
        "title": "Software Engineer",
        "date_posted": "2022-01-01"
    },
    {
        "max_salary": 100000,
        "min_salary": 40099,
        "title": "Software Engineer",
        "date_posted": "2021-01-01"
    },
    {
        "max_salary": 100001,
        "min_salary": 50000,
        "title": "Software Engineer",
        "date_posted": "2020-01-01"
    }
]

ordered_date_posted = [
    {
        "max_salary": 100003,
        "min_salary": 40098,
        "title": "Software Engineer",
        "date_posted": "2022-01-01"
    },
    {
        "max_salary": 100000,
        "min_salary": 40099,
        "title": "Software Engineer",
        "date_posted": "2021-01-01"
    },
    {
        "max_salary": 100001,
        "min_salary": 50000,
        "title": "Software Engineer",
        "date_posted": "2020-01-01"
    }
]


def test_sort_by_criteria(jobs):
    sort_by(jobs, "max_salary")
    assert jobs == ordered_max_salary
    sort_by(jobs, "min_salary")
    assert jobs == ordered_min_salary
    sort_by(jobs, "date_posted")
    assert jobs == ordered_date_posted

