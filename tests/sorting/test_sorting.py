import pytest
from src.sorting import sort_by

# ..source: https://github.com/tryber/sd-011-project-job-insights/blob/
# .. tarcisio-menezes-job-insights/tests/sorting/test_sorting.py
# he helped me to understand the concept of the requisite


@pytest.fixture
def jobs():
    return [
        {"min_salary": 10, "max_salary": 100, "date_posted": "2020-05-08"},
        {"min_salary": 1, "max_salary": 60, "date_posted": "2020-09-18"},
        {"min_salary": 32, "max_salary": 3000, "date_posted": "2020-05-04"},
    ]


sort_by_min_salary = [
    {"min_salary": 1, "max_salary": 60, "date_posted": "2020-09-18"},
    {"min_salary": 10, "max_salary": 100, "date_posted": "2020-05-08"},
    {"min_salary": 32, "max_salary": 3000, "date_posted": "2020-05-04"},
]

sort_by_max_salary = [
    {"min_salary": 32, "max_salary": 3000, "date_posted": "2020-05-04"},
    {"min_salary": 10, "max_salary": 100, "date_posted": "2020-05-08"},
    {"min_salary": 1, "max_salary": 60, "date_posted": "2020-09-18"},
]

sort_by_mix_date_posted = [
    {"min_salary": 1, "max_salary": 60, "date_posted": "2020-09-18"},
    {"min_salary": 10, "max_salary": 100, "date_posted": "2020-05-08"},
    {"min_salary": 32, "max_salary": 3000, "date_posted": "2020-05-04"},
]


def test_sort_by_criteria(jobs):

    sort_by(jobs, "min_salary")
    assert jobs == sort_by_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == sort_by_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == sort_by_mix_date_posted

    with pytest.raises(ValueError):
        sort_by([], "try_error")
