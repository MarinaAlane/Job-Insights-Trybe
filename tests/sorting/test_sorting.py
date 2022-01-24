from src.sorting import sort_by
import pytest


@pytest.fixture
def jobs_for_sort_by_criteria():
    return [
        {"date_posted": "2020-05-17", "max_salary": 15, "min_salary": 10},
        {"date_posted": "2020-12-02", "max_salary": 10000, "min_salary": 200},
        {"date_posted": "2020-09-25", "max_salary": 150, "min_salary": 100},
    ]


def test_sort_by_criteria(jobs_for_sort_by_criteria):
    pass
    sort_by(jobs_for_sort_by_criteria, "min_salary")
    assert jobs_for_sort_by_criteria == [
        {"date_posted": "2020-05-17", "max_salary": 15, "min_salary": 10},
        {"date_posted": "2020-09-25", "max_salary": 150, "min_salary": 100},
        {"date_posted": "2020-12-02", "max_salary": 10000, "min_salary": 200},
    ]

    sort_by(jobs_for_sort_by_criteria, "max_salary")
    assert jobs_for_sort_by_criteria == [
        {"date_posted": "2020-12-02", "max_salary": 10000, "min_salary": 200},
        {"date_posted": "2020-09-25", "max_salary": 150, "min_salary": 100},
        {"date_posted": "2020-05-17", "max_salary": 15, "min_salary": 10},
    ]

    sort_by(jobs_for_sort_by_criteria, "date_posted")
    assert jobs_for_sort_by_criteria == [
        {"date_posted": "2020-12-02", "max_salary": 10000, "min_salary": 200},
        {"date_posted": "2020-09-25", "max_salary": 150, "min_salary": 100},
        {"date_posted": "2020-05-17", "max_salary": 15, "min_salary": 10},
    ]