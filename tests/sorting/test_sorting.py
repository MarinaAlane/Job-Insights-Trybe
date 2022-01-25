import pytest
from src.sorting import sort_by

job_data = [
    {'max_salary': 5000, 'min_salary': 800, 'date_posted': '2021-01-01'},
    {'max_salary': 2500, 'min_salary': 1200, 'date_posted': '2021-01-02'},
    {'max_salary': 3200, 'min_salary': 1800, 'date_posted': '2021-01-03'},
            ]


def test_sort_by_criteria():
    with pytest.raises(TypeError):
        sort_by(job_data, "invalid", "otherInvalid")

    sort_by(job_data, 'max_salary')

    assert job_data == [
        {'max_salary': 5000, 'min_salary': 800, 'date_posted': '2021-01-01'},
        {'max_salary': 3200, 'min_salary': 1800, 'date_posted': '2021-01-03'},
        {'max_salary': 2500, 'min_salary': 1200, 'date_posted': '2021-01-02'},
                    ]

    sort_by(job_data, 'min_salary')

    assert job_data == [
        {'max_salary': 5000, 'min_salary': 800, 'date_posted': '2021-01-01'},
        {'max_salary': 2500, 'min_salary': 1200, 'date_posted': '2021-01-02'},
        {'max_salary': 3200, 'min_salary': 1800, 'date_posted': '2021-01-03'},
                    ]
