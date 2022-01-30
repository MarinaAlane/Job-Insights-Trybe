from src.sorting import sort_by
import pytest

jobs_list = [
     {"min_salary": 20, "max_salary": 40, "date_posted": "2022-03-01"},
     {"min_salary": 10, "max_salary": 60, "date_posted": "2022-01-01"},
     {"min_salary": 30, "max_salary": 50, "date_posted": "2022-02-01"},
]

ordered_by_min_salary = [
     {"min_salary": 10, "max_salary": 60, "date_posted": "2022-01-01"},
     {"min_salary": 20, "max_salary": 40, "date_posted": "2022-03-01"},
     {"min_salary": 30, "max_salary": 50, "date_posted": "2022-02-01"},
]

ordered_by_max_salary = [
     {"min_salary": 10, "max_salary": 60, "date_posted": "2022-01-01"},
     {"min_salary": 30, "max_salary": 50, "date_posted": "2022-02-01"},
     {"min_salary": 20, "max_salary": 40, "date_posted": "2022-03-01"},
]

ordered_by_date = [
     {"min_salary": 20, "max_salary": 40, "date_posted": "2022-03-01"},
     {"min_salary": 30, "max_salary": 50, "date_posted": "2022-02-01"},
     {"min_salary": 10, "max_salary": 60, "date_posted": "2022-01-01"},
]


def test_sort_by_criteria():
    sort_by(jobs_list, "min_salary")
    assert jobs_list == ordered_by_min_salary

    sort_by(jobs_list, "max_salary")
    assert jobs_list == ordered_by_max_salary

    sort_by(jobs_list, "date_posted")
    assert jobs_list == ordered_by_date

    with pytest.raises(ValueError):
        sort_by(jobs_list, "invalid_criteria")

# ref linha 40 a 42 :
# https://github.com/tryber/sd-011-project-job-insights/pull/106/files
