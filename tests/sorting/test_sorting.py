import pytest
from src.sorting import sort_by


jobs = [
    {"max_salary": 6000, "min_salary": 3000, "date_posted": "2022-01-01"},
    {"max_salary": 5000, "min_salary": 2000, "date_posted": "2021-09-09"},
    {"max_salary": 4000, "min_salary": 1000, "date_posted": "2019-12-12"},
]


def test_sort_by_criteria():
    with pytest.raises(TypeError):
        sort_by(jobs, "invalid", "teste")

    sort_by(jobs, "max_salary")
    assert jobs == [
        {'max_salary': 6000, 'min_salary': 3000, 'date_posted': '2022-01-01'},
        {'max_salary': 5000, 'min_salary': 2000, 'date_posted': '2021-09-09'},
        {'max_salary': 4000, 'min_salary': 1000, 'date_posted': '2019-12-12'},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == [
        {'max_salary': 4000, 'min_salary': 1000, 'date_posted': '2019-12-12'},
        {'max_salary': 6000, 'min_salary': 3000, 'date_posted': '2022-01-01'},
        {'max_salary': 5000, 'min_salary': 2000, 'date_posted': '2021-09-09'},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {'max_salary': 6000, 'min_salary': 3000, 'date_posted': '2022-01-01'},
        {'max_salary': 5000, 'min_salary': 2000, 'date_posted': '2021-09-09'},
        {'max_salary': 4000, 'min_salary': 1000, 'date_posted': '2019-12-12'},
    ]
