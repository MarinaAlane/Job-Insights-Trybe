from src.sorting import sort_by
import pytest

jobs = [
    {"min_salary": "1", "max_salary": "2", "date_posted": "2020-01-03"},
    {"min_salary": "2", "max_salary": "3", "date_posted": "2020-01-02"},
    {"min_salary": "3", "max_salary": "4", "date_posted": "2020-01-01"},
]


def test_sort_by_criteria():
    pass
    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": "1", "max_salary": "2", "date_posted": "2020-01-03"},
        {"min_salary": "2", "max_salary": "3", "date_posted": "2020-01-02"},
        {"min_salary": "3", "max_salary": "4", "date_posted": "2020-01-01"},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"min_salary": "3", "max_salary": "4", "date_posted": "2020-01-01"},
        {"min_salary": "2", "max_salary": "3", "date_posted": "2020-01-02"},
        {"min_salary": "1", "max_salary": "2", "date_posted": "2020-01-03"},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"min_salary": "1", "max_salary": "2", "date_posted": "2020-01-03"},
        {"min_salary": "2", "max_salary": "3", "date_posted": "2020-01-02"},
        {"min_salary": "3", "max_salary": "4", "date_posted": "2020-01-01"},
    ]


with pytest.raises(ValueError):
    sort_by(jobs, "invalid_criteria")
