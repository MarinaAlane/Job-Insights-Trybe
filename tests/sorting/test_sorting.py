from src.sorting import sort_by
import pytest


jobs = [
        {'min_salary': 6, 'max_salary': 35, 'date_posted': '2010-10-12'},
        {'min_salary': 10, 'max_salary': 30, 'date_posted': '2010-10-16'},
        {'min_salary': 55, 'max_salary': 120, 'date_posted': '2010-10-20'},
]


def test_sort_by_criteria():
    sort_by(jobs, 'min_salary')
    assert jobs == [
        {'min_salary': 6, 'max_salary': 35, 'date_posted': '2010-10-12'},
        {'min_salary': 10, 'max_salary': 30, 'date_posted': '2010-10-16'},
        {'min_salary': 55, 'max_salary': 120, 'date_posted': '2010-10-20'},
    ]

    sort_by(jobs, 'max_salary')
    assert jobs == [
        {'min_salary': 55, 'max_salary': 120, 'date_posted': '2010-10-20'},
        {'min_salary': 6, 'max_salary': 35, 'date_posted': '2010-10-12'},
        {'min_salary': 10, 'max_salary': 30, 'date_posted': '2010-10-16'},
    ]

    sort_by(jobs, 'date_posted')
    assert jobs == [
        {'min_salary': 55, 'max_salary': 120, 'date_posted': '2010-10-20'},
        {'min_salary': 10, 'max_salary': 30, 'date_posted': '2010-10-16'},
        {'min_salary': 6, 'max_salary': 35, 'date_posted': '2010-10-12'},
    ]

    with pytest.raises(ValueError):
        sort_by(jobs, "invalid_criteria")
