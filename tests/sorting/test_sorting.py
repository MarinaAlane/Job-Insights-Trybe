import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs():
    return [
        {'min_salary': 2000, 'max_salary': 2000, 'date_posted': '2021-12-01'},
        {'min_salary': 3000, 'max_salary': 8000, 'date_posted': '2020-03-10'},
        {'min_salary': 1000, 'max_salary': 6000, 'date_posted': '2019-10-10'},
    ]


def test_sort_by_criteria(jobs):
    sorted_by_min_salary = [
        {'min_salary': 1000, 'max_salary': 6000, 'date_posted': '2019-10-10'},
        {'min_salary': 2000, 'max_salary': 2000, 'date_posted': '2021-12-01'},
        {'min_salary': 3000, 'max_salary': 8000, 'date_posted': '2020-03-10'},
    ]

    sorted_by_max_salary = [
        {'min_salary': 3000, 'max_salary': 8000, 'date_posted': '2020-03-10'},
        {'min_salary': 1000, 'max_salary': 6000, 'date_posted': '2019-10-10'},
        {'min_salary': 2000, 'max_salary': 2000, 'date_posted': '2021-12-01'},
    ]

    sorted_by_date = [
        {'min_salary': 2000, 'max_salary': 2000, 'date_posted': '2021-12-01'},
        {'min_salary': 3000, 'max_salary': 8000, 'date_posted': '2020-03-10'},
        {'min_salary': 1000, 'max_salary': 6000, 'date_posted': '2019-10-10'},
    ]

    sort_by(jobs, 'min_salary')
    assert jobs == sorted_by_min_salary

    sort_by(jobs, 'max_salary')
    assert jobs == sorted_by_max_salary

    sort_by(jobs, 'date_posted')
    assert jobs == sorted_by_date

    with pytest.raises(ValueError):
        sort_by(jobs, 'wrong_criteria')
