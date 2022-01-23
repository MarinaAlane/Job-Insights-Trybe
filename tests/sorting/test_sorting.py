from src.sorting import sort_by
import pytest
from mocks import (
  sort_date,
  sort_max_salary,
  sort_min_salary,
)

jobs = [
    {"min_salary": 10, "max_salary": 1000, "date_posted": "2021-01-24"},
    {"min_salary": 1000, "max_salary": 10000, "date_posted": "2020-01-24"},
    {"min_salary": '', "max_salary": '', "date_posted": ''},
]


def test_sort_by_criteria():
    sort_by(jobs, 'date_posted')
    assert jobs == sort_date

    sort_by(jobs, 'max_salary')
    assert jobs == sort_max_salary

    sort_by(jobs, 'min_salary')
    assert jobs == sort_min_salary

    invalid = ["last_salary", "first_salary"]
    for inv in invalid:
        with pytest.raises(
          ValueError, match=f"invalid sorting criteria: {inv}"):
            sort_by(jobs, inv)
