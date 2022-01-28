import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {"max_salary": 98, "min_salary": 10, "date_posted": "2021-09-27"},
        {"max_salary": 99, "min_salary": 50, "date_posted": "2022-01-17"},
        {"max_salary": 100, "min_salary": 9, "date_posted": "2021-05-17"},
        {"max_salary": 95, "min_salary": 11, "date_posted": "2020-05-19"},
        {"max_salary": 101, "min_salary": 13},
    ]


@pytest.fixture
def criteria():
    return ["min_salary", "max_salary", "date_posted"]


def test_sort_by_criteria(jobs, criteria):
    sort_by(jobs, criteria[0])
    assert jobs == ([
        {"max_salary": 100, "min_salary": 9, "date_posted": "2021-05-17"},
        {"max_salary": 98, "min_salary": 10, "date_posted": "2021-09-27"},
        {"max_salary": 95, "min_salary": 11, "date_posted": "2020-05-19"},
        {"max_salary": 101, "min_salary": 13},
        {"max_salary": 99, "min_salary": 50, "date_posted": "2022-01-17"},
    ])
    sort_by(jobs, criteria[1])
    assert jobs == ([
       {"max_salary": 101, "min_salary": 13},
       {"max_salary": 100, "min_salary": 9, "date_posted": "2021-05-17"},
       {"max_salary": 99, "min_salary": 50, "date_posted": "2022-01-17"},
       {"max_salary": 98, "min_salary": 10, "date_posted": "2021-09-27"},
       {"max_salary": 95, "min_salary": 11, "date_posted": "2020-05-19"},
    ])
    sort_by(jobs, criteria[2])
    assert jobs == ([
        {"max_salary": 99, "min_salary": 50, "date_posted": "2022-01-17"},
        {"max_salary": 98, "min_salary": 10, "date_posted": "2021-09-27"},
        {"max_salary": 100, "min_salary": 9, "date_posted": "2021-05-17"},
        {"max_salary": 95, "min_salary": 11, "date_posted": "2020-05-19"},
        {"max_salary": 101, "min_salary": 13},
    ])
    with pytest.raises(ValueError, match="invalid criteria"):
        sort_by(jobs, "invalid criteria")
