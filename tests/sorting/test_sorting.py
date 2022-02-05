import pytest
from src.sorting import sort_by

jobs = [
    {"max_salary": 4000, "min_salary": 2500, "date_posted": "02-05-2022"},
    {"max_salary": 6000, "min_salary": 4500, "date_posted": "02-06-2022"},
    {"max_salary": 8000, "min_salary": 6500, "date_posted": "02-07-2022"},
]

mock = {
    "max_salary": [jobs],
    "min_salary": [jobs],
    "date_posted": [jobs],
}


def test_sort_by_criteria():
    sort_by(jobs, 'max_salary')
    assert(jobs) == mock['max_salary']

    sort_by(jobs, 'min_salary')
    assert(jobs) == mock['min_salary']

    sort_by(jobs, 'date_posted')
    assert(jobs) == mock['date_posted']

    with pytest.raises(ValueError, 'invalid_criteria'):
        sort_by(jobs, 'invalid_criteria')
