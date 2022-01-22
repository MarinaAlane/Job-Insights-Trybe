import pprint

import pytest
from src.sorting import sort_by

from mocked_jobs import (
    job_sorted_by_date_posted,
    job_sorted_by_max_salary,
    job_sorted_by_min_salary,
)

pp = pprint.PrettyPrinter(indent=4)


def test_sort_by_criteria():
    pass
    sort_by(job_sorted_by_min_salary[0], "min_salary")
    assert job_sorted_by_min_salary[0] == job_sorted_by_min_salary[1]

    sort_by(job_sorted_by_max_salary[0], "max_salary")
    assert job_sorted_by_max_salary[0] == job_sorted_by_max_salary[1]

    sort_by(job_sorted_by_date_posted[0], "date_posted")
    assert job_sorted_by_date_posted[0] == job_sorted_by_date_posted[1]

    with pytest.raises(ValueError):
        sort_by(job_sorted_by_min_salary[0], "incorrect_criteria")
