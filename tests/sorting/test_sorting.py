from src.sorting import sort_by
import pytest


@pytest.fixture
def jobs():
    return [
        {"min_salary": 1000, "max_salary": 2500, "date_posted": "2020-02-13"},
        {"min_salary": 3500, "max_salary": 7500, "date_posted": "2020-03-29"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2019-12-12"},
    ]


def test_sort_by_criteria(jobs):
    min_salary_sorting = [
        {"min_salary": 1000, "max_salary": 2500, "date_posted": "2020-02-13"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2019-12-12"},
        {"min_salary": 3500, "max_salary": 7500, "date_posted": "2020-03-29"},
    ]

    max_salary_sorting = [
        {"min_salary": 3500, "max_salary": 7500, "date_posted": "2020-03-29"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2019-12-12"},
        {"min_salary": 1000, "max_salary": 2500, "date_posted": "2020-02-13"},
    ]

    date_posted_sorting = [
        {"min_salary": 3500, "max_salary": 7500, "date_posted": "2020-03-29"},
        {"min_salary": 1000, "max_salary": 2500, "date_posted": "2020-02-13"},
        {"min_salary": 2000, "max_salary": 5000, "date_posted": "2019-12-12"},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == min_salary_sorting
    sort_by(jobs, "max_salary")
    assert jobs == max_salary_sorting
    sort_by(jobs, "date_posted")
    assert jobs == date_posted_sorting
