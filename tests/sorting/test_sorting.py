from src.sorting import sort_by
import pytest


jobs = [
    {"min_salary": 4000, "max_salary": 8000, "date_posted": "2022-01-01"},
    {"min_salary": 9000, "max_salary": 10000, "date_posted": "2022-01-02"},
    {"min_salary": 5000, "max_salary": 14000, "date_posted": "2022-01-03"},
]


def test_sort_by_criteria():
    order_by_min_salary = [
        {"min_salary": 4000, "max_salary": 8000, "date_posted": "2022-01-01"},
        {"min_salary": 5000, "max_salary": 14000, "date_posted": "2022-01-03"},
        {"min_salary": 9000, "max_salary": 10000, "date_posted": "2022-01-02"},
    ]
    order_by_max_salary = [
        {"min_salary": 5000, "max_salary": 14000, "date_posted": "2022-01-03"},
        {"min_salary": 9000, "max_salary": 10000, "date_posted": "2022-01-02"},
        {"min_salary": 4000, "max_salary": 8000, "date_posted": "2022-01-01"},
    ]
    order_by_date_posted = [
        {"min_salary": 5000, "max_salary": 14000, "date_posted": "2022-01-03"},
        {"min_salary": 9000, "max_salary": 10000, "date_posted": "2022-01-02"},
        {"min_salary": 4000, "max_salary": 8000, "date_posted": "2022-01-01"},
    ]

    with pytest.raises(TypeError):
        sort_by(jobs, "salary", "remote")

    sort_by(jobs, "min_salary")
    assert jobs == order_by_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == order_by_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == order_by_date_posted
