from src.sorting import sort_by
import pytest
from mocks import (
  jobs,
  sort_date,
  sort_max_salary,
  sort_min_salary,
)


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
