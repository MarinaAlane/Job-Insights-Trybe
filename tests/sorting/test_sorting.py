import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 100, "max_salary": 4500, "date_posted": "2021-01-01"},
        {"min_salary": 300, "max_salary": 2800, "date_posted": "2019-01-01"},
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2020-01-01"},
        {"min_salary": '', "max_salary": '', "date_posted": ''}
    ]

    sort_date_posted = [
        {"min_salary": 100, "max_salary": 4500, "date_posted": "2021-01-01"},
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2020-01-01"},
        {"min_salary": 300, "max_salary": 2800, "date_posted": "2019-01-01"},
        {"min_salary": '', "max_salary": '', "date_posted": ''}
    ]

    sort_max_salary = [
        {"min_salary": 100, "max_salary": 4500, "date_posted": "2021-12-01"},
        {"min_salary": 300, "max_salary": 2800, "date_posted": "2019-01-01"},
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2020-11-01"},
        {"min_salary": '', "max_salary": '', "date_posted": ''}
    ]

    sort_min_salary = [
        {"min_salary": 100, "max_salary": 4500, "date_posted": "2021-01-01"},
        {"min_salary": 300, "max_salary": 2800, "date_posted": "2019-01-01"},
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2020-01-01"},
        {"min_salary": '', "max_salary": '', "date_posted": ''},
    ]

    sort_by(jobs, 'min_salary')
    assert jobs == sort_min_salary

    sort_by(jobs, 'max_salary')
    assert jobs == sort_max_salary

    sort_by(jobs, 'date_posted')
    assert jobs == sort_date_posted

    invalid_criterias = ["job_type", "title"]
    for invalid_criteria in invalid_criterias:
        with pytest.raises(
            ValueError, match=f"invalid sorting criteria: {invalid_criteria}"
        ):
            sort_by(jobs, invalid_criteria)
